"""Simulated annealing over task orders and modes: the acceptance, cooling and restart rules of the published SA
(Algorithm 1), with a neighbour that moves a task in the order or changes one task's mode.
"""

from dataclasses import replace
import math

from planner.methods.fixed_schedules.budget import search
from planner.methods.fixed_schedules.encoding import change_mode, move_list, repair_order


def neighbour(data, candidate, rng):
    """Move a task in the order (swap, insertion or reversal) or change one task's mode, each half the time."""
    if rng.integers(2) == 0 and len(data.tasks) > 1:
        first, second = map(int, rng.choice(len(data.tasks), 2, replace=False))
        order = move_list(candidate.order, int(rng.integers(3)), first, second)
        return replace(candidate, order=repair_order(order, data.predecessor_masks))
    modes = list(candidate.modes)
    change_mode(modes, data, rng)
    return replace(candidate, modes=tuple(modes))


def fresh():
    """The initial annealing state: temperature 100; the first iteration restarts, which sets the restart limit to 100."""
    return dict(temperature=100.0, restart_limit=100 / math.sqrt(2), last_improvement=-100 / math.sqrt(2),
                current=None, current_fitness=math.inf)


def step(data, state, rng, assess):
    """One SA iteration: propose a schedule, assess it, accept it or not, and cool down."""
    iteration = state['count']
    # Restart from a random schedule when nothing improved for restart_limit schedules; the limit grows by sqrt(2)
    if iteration - state['last_improvement'] >= state['restart_limit']:
        state['temperature'] = 100.0
        state['restart_limit'] *= math.sqrt(2)
        state['last_improvement'] = iteration
        state['current_fitness'] = math.inf
        candidate = data.random(rng)
        state['restarts'] += 1
    else:
        candidate = neighbour(data, state['current'], rng)
    _, plan = assess(candidate)
    # Accept a schedule that is no worse, or a worse one with probability exp(-delta / temperature)
    delta = plan.completion - state['current_fitness']
    accepted = delta <= 0 or rng.random() < math.exp(-delta / state['temperature'])
    if accepted:
        state['current'], state['current_fitness'] = candidate, plan.completion
        # A new best schedule resets the time since the last improvement
        if state['best'] == candidate and state['best_schedule'] is plan:
            state['last_improvement'] = iteration
    # Cool so that the temperature falls from 100 to 1 over restart_limit schedules
    state['temperature'] *= (1 / 100) ** (1 / state['restart_limit'])


def solve(data, evaluations, seed, checkpoint, progress=None):
    """Search with `evaluations` assessed schedules, resumable from `checkpoint`; return the best plan and statistics."""
    return search(data, 'sa', evaluations, seed, checkpoint, fresh, step, progress=progress)
