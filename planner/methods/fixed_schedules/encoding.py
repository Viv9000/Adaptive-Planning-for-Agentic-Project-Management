"""The schedule encoding that GA and SA search: a task order and a mode per task, decoded on the mean durations by a
serial schedule generation scheme that books partial dedications.
"""

from dataclasses import dataclass

from planner.methods.cpsat.solver import ModeSchedule, mean_durations


@dataclass(frozen=True, slots=True)
class Chromosome:
    """A schedule's encoding: a task order (task indices) and each task's mode index."""

    order: tuple[int, ...]
    modes: tuple[int, ...]


def repair_order(order, predecessors):
    """Stable topological repair, retaining priorities whenever precedence permits."""
    remaining = list(order)
    result = []
    completed = 0  # Bit mask of the tasks placed so far
    while remaining:
        # Take the first remaining task whose predecessors are all placed
        task = next((t for t in remaining if predecessors[t] & completed == predecessors[t]), None)
        if task is None:
            raise ValueError('Activity order is not a permutation of an acyclic project')
        remaining.remove(task)
        result.append(task)
        completed |= 1 << task
    return tuple(result)


def move_list(values: tuple[int, ...], move: int, first: int, second: int) -> tuple[int, ...]:
    """Swap (0), insert the first entry at the second index (1), or reverse inclusively (2)."""
    result = list(values)
    if move == 0:
        result[first], result[second] = result[second], result[first]
    elif move == 1:
        result.insert(second, result.pop(first))
    elif move == 2:
        low, high = sorted((first, second))
        result[low:high + 1] = reversed(result[low:high + 1])
    else:
        raise ValueError('Move must be swap (0), insertion (1), or reversal (2)')
    return tuple(result)


def change_mode(modes, data, rng):
    """Give a random task a different random mode, in place, if it has more than one."""
    task = int(rng.integers(len(data.tasks)))
    count = len(data.tasks[task].modes)
    if count > 1:
        # Shift by 1 to count - 1 places, so the new mode always differs
        modes[task] = (modes[task] + int(rng.integers(1, count))) % count


@dataclass
class ModeData:
    """A project prepared for decoding: tasks by index, predecessor bit masks and mean durations."""

    project: object

    def __post_init__(self):
        self.tasks = tuple(self.project.tasks)
        indices = {task.id: i for i, task in enumerate(self.tasks)}
        masks = [0] * len(self.tasks)
        for before, after in self.project.tpg_edges:
            masks[indices[after]] |= 1 << indices[before]
        self.predecessor_masks = tuple(masks)  # Bit j of entry i: task j precedes task i.
        self.durations = mean_durations(self.project)
        # Replace skill count by mean catalogue dedication in the crossover requirement heuristic.
        self.weighted_requirements = tuple(
            sum(self.durations[task.id, mode.id] * sum(mode.dedication.values()) for mode in task.modes)
            / len(task.modes) for task in self.tasks)

    def random(self, rng):
        """A random precedence-feasible order with a random mode per task."""
        order = repair_order(tuple(map(int, rng.permutation(len(self.tasks)))), self.predecessor_masks)
        return Chromosome(order, tuple(int(rng.integers(len(task.modes))) for task in self.tasks))

    def decode(self, candidate, backward=False):
        """Serial insertion SGS; jump between booking boundaries, preserving partial capacities.

        Each task, in order, starts at the earliest time after its predecessors at which its mode's workers have the
        dedication free for its whole duration. backward schedules the reversed order on the reversed precedences and
        mirrors the result (used by GA's forward-backward improvement).
        """
        masks = self.predecessor_masks
        order = candidate.order
        if backward:
            # Reverse the precedences: bit j of entry i now means task j succeeds task i
            masks = tuple(sum(1 << j for j, mask in enumerate(masks) if mask & (1 << i))
                          for i in range(len(self.tasks)))
            order = tuple(reversed(order))
        starts, finishes, bookings = {}, {}, []  # bookings: (start, end, dedication) of every placed task
        for index in order:
            task = self.tasks[index]
            mode = task.modes[candidate.modes[index]]
            duration = self.durations[task.id, mode.id]
            # Earliest start: when the last predecessor finishes
            release = max((finishes[j] for j in finishes if masks[index] & (1 << j)), default=0)
            day = release
            while duration > 0:
                # Bookings that overlap [day, day + duration); the load can only rise at day or at their starts
                overlaps = [(start, end, dedication) for start, end, dedication in bookings
                            if start < day + duration and end > day]
                boundaries = sorted({day} | {start for start, _, _ in overlaps if day < start < day + duration})
                violation = None
                for boundary in boundaries:
                    load = dict(mode.dedication)
                    for start, end, dedication in overlaps:
                        if start <= boundary < end:
                            for worker, amount in dedication.items():
                                load[worker] = load.get(worker, 0) + amount
                    if any(amount > 1 + 1e-9 for amount in load.values()):
                        violation = boundary
                        break
                if violation is None:
                    break
                # Over capacity at violation: try again from the earliest end of a booking running then
                day = min(end for start, end, _ in overlaps if start <= violation < end)
            starts[index], finishes[index] = day, day + duration
            if duration:
                bookings.append((day, day + duration, mode.dedication))
        completion = max(finishes.values(), default=0)
        if backward:
            # Mirror the backward schedule so it runs forward from day 0
            starts = {i: completion - finishes[i] for i in starts}
        plan = ModeSchedule(completion, {task.id: dict(day=starts[i], mode=task.modes[candidate.modes[i]].id)
                                         for i, task in enumerate(self.tasks)})
        return plan

    def chronological(self, plan):
        """The tasks in order of their start in plan (ties by index), repaired for precedence."""
        order = sorted(range(len(self.tasks)), key=lambda i: (plan.starts[self.tasks[i].id]['day'], i))
        return repair_order(order, self.predecessor_masks)
