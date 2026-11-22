"""The genetic algorithm over task orders and modes: a population of 75, tournament selection, the two-point
crossover, mutation, forward-backward improvement of every schedule, and a scan of modes on the ten best.
"""

from dataclasses import replace

from planner.methods.fixed_schedules.budget import search
from planner.methods.fixed_schedules.encoding import Chromosome, change_mode, move_list, repair_order

POPULATION = 75


def low_requirement_cuts(data, order, rng):
    """Two cut points in the order, in the middle of its two longest stretches of below-average requirement.

    With fewer than two such stretches, two random cut points.
    """
    average = sum(data.weighted_requirements) / len(order)
    ranges = []
    start = None
    for position in range(len(order) + 1):
        below = position < len(order) and data.weighted_requirements[order[position]] < average
        if below and start is None:
            start = position
        elif not below and start is not None:
            ranges.append((start, position))
            start = None
    ranges.sort(key=lambda interval: (-(interval[1] - interval[0]), interval[0]))
    if len(ranges) < 2:
        return tuple(sorted(map(int, rng.choice(len(order) + 1, size=2, replace=False))))
    return tuple(sorted((start + end + 1) // 2 for start, end in ranges[:2]))


def crossover(data, first, second, rng):
    """Two children, one from each parent: the tasks between two cuts of the order (placed around low-requirement
    stretches) keep their positions but take the other parent's order, and a random stretch of modes is swapped."""
    children = []
    # The stretch of modes to swap, the same for both children
    pl_low, pl_high = sorted(map(int, rng.choice(len(first.modes) + 1, size=2, replace=False)))
    for left, right in ((first, second), (second, first)):
        # The tasks between the cuts keep their positions but follow the other parent's order
        low, high = low_requirement_cuts(data, left.order, rng)
        members = set(left.order[low:high])
        middle = tuple(task for task in right.order if task in members)
        order = left.order[:low] + middle + left.order[high:]
        modes = left.modes[:pl_low] + right.modes[pl_low:pl_high] + left.modes[pl_high:]
        children.append(Chromosome(repair_order(order, data.predecessor_masks), modes))
    return tuple(children)


def mutate(data, candidate, rng):
    """Swap two tasks in the order, and change one task's mode, each with probability 0.2."""
    if rng.random() < 0.2 and len(data.tasks) > 1:
        first, second = map(int, rng.choice(len(data.tasks), 2, replace=False))
        order = move_list(candidate.order, 0, first, second)
        candidate = replace(candidate, order=repair_order(order, data.predecessor_masks))
    if rng.random() < 0.2:
        # Different tasks have different mode counts, so swapping mode-index genes is invalid.
        modes = list(candidate.modes)
        change_mode(modes, data, rng)
        candidate = replace(candidate, modes=tuple(modes))
    return candidate


def fresh():
    """The initial GA state: an empty population, to be filled in the 'initial' phase."""
    return dict(population=[], phase='initial', index=0, child=0, children=None, evaluated=[], elites=[],
                local_indices=[], local_position=0, mode_task=0, mode_index=0)


def keep_elites(state, candidate, plan):
    """The two best schedules seen, which replace the two worst after each generation."""
    state['elites'] = sorted(state['elites'] + [(candidate, plan)], key=lambda pair: pair[1].completion)[:2]


def step(data, state, rng, assess):
    """Assess one schedule. Phases: initial population, children, forward-backward improvement (right, then left),
    and the mode scan on the ten best."""
    completion = lambda pair: pair[1].completion
    if state['phase'] == 'initial':
        # Fill the population with random schedules
        state['population'].append(assess(data.random(rng)))
        if len(state['population']) == POPULATION:
            state.update(phase='children', index=0, generation=1)
    elif state['phase'] == 'children':
        # Each member is a first parent; a binary tournament picks the second; crossover with probability 0.8.
        # The better of the two mutated children replaces the member.
        if state['children'] is None:
            contenders = rng.choice(POPULATION, 2, replace=False)
            second = min((state['population'][int(i)] for i in contenders), key=completion)
            parents = (state['population'][state['index']][0], second[0])
            state['children'] = crossover(data, *parents, rng) if rng.random() < 0.8 else parents
        candidate = mutate(data, state['children'][state['child']], rng)
        state['evaluated'].append(assess(candidate))
        state['child'] += 1
        if state['child'] == 2:
            state['population'][state['index']] = min(state['evaluated'], key=completion)
            state.update(children=None, evaluated=[], child=0, index=state['index'] + 1)
            if state['index'] == POPULATION:
                state.update(phase='right', index=0)
    elif state['phase'] == 'right':
        # Forward-backward improvement: schedule each member backward (right-justified) ...
        candidate, _ = state['population'][state['index']]
        state['right'] = assess(candidate, backward=True)
        state['phase'] = 'left'
    elif state['phase'] == 'left':
        # ... then forward again in the order of the backward schedule's starts; repeat while it improves
        original = state['population'][state['index']]
        candidate = replace(state['right'][0], order=data.chronological(state['right'][1]))
        changed = assess(candidate)
        if changed[1].completion < original[1].completion:
            state['population'][state['index']] = changed
            state['phase'] = 'right'
        else:
            state.update(phase='right', index=state['index'] + 1)
            if state['index'] == POPULATION:
                state.update(phase='modes', local_indices=sorted(range(POPULATION),
                             key=lambda i: state['population'][i][1].completion)[:10],
                             local_position=0, mode_task=0, mode_index=0)
    else:
        # Mode scan: try every mode of every task on the ten best members, keeping improvements;
        # then the two elites replace the two worst members and the next generation starts
        index = state['local_indices'][state['local_position']]
        candidate, _ = state['population'][index]
        task = state['mode_task']
        modes = list(candidate.modes)
        modes[task] = state['mode_index']
        changed = assess(replace(candidate, modes=tuple(modes)))
        if changed[1].completion < state['population'][index][1].completion:
            state['population'][index] = changed
        state['mode_index'] += 1
        if state['mode_index'] == len(data.tasks[task].modes):
            state.update(mode_index=0, mode_task=task + 1)
            if state['mode_task'] == len(data.tasks):
                state.update(mode_task=0, local_position=state['local_position'] + 1)
                if state['local_position'] == len(state['local_indices']):
                    worst = sorted(range(POPULATION), key=lambda i: state['population'][i][1].completion,
                                   reverse=True)[:2]
                    for slot, elite in zip(worst, state['elites']):
                        state['population'][slot] = elite
                    state.update(phase='children', index=0, generation=state['generation'] + 1)


def solve(data, evaluations, seed, checkpoint, progress=None):
    """Search with `evaluations` assessed schedules, resumable from `checkpoint`; return the best plan and statistics."""
    return search(data, 'ga', evaluations, seed, checkpoint, fresh, step, keep=keep_elites, progress=progress)
