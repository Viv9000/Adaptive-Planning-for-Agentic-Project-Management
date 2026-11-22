"""CP-SAT over explicit modes: a fixed schedule of (start, mode) per task that minimises the makespan.

Durations are fixed per mode: the expected rounded duration E[ceil(X)] (mean_durations).
With dedication='partial' (the CP-SAT method) a worker may run several tasks at once while their dedications sum to at
most one; with 'full' (the deadline reference of dataset/generator) every worker of a mode is busy for the whole task.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from ortools.sat.python import cp_model

from planner.core.distributions import expected_duration
from planner.core.project import Project

# Fixed duration of each (task, mode), in time units
Durations = dict[tuple[str, int], int]


@dataclass(frozen=True)
class ModeSchedule:
    """Planned start and mode per task, and the planned completion."""

    completion: int
    starts: dict[str, dict]  # task -> {'day': start, 'mode': mode id}


@dataclass(frozen=True)
class ModeSolveResult:
    """What a CP-SAT solve returns."""

    plan: ModeSchedule | None  # None if CP-SAT found no schedule in time
    status: str  # CP-SAT's status name, e.g. OPTIMAL or FEASIBLE
    bound: float | None  # CP-SAT's lower bound on the makespan
    seconds: float


def mean_durations(project: Project) -> Durations:
    """Each mode's expected rounded duration E[ceil(X)], rounded to the nearest whole time unit."""
    return {(task.id, mode.id): round(expected_duration(project.distributions[mode.distribution_hash]))
            for task in project.tasks for mode in task.modes}


def solve_makespan(project: Project, durations: Durations, time_limit: float, seed: int = 0, threads: int = 8,
                   dedication: str = 'full') -> ModeSolveResult:
    """Minimise the makespan with fixed durations."""
    if dedication not in ('full', 'partial'):
        raise ValueError("dedication must be 'full' or 'partial'")
    started = perf_counter()
    # No schedule needs longer than all tasks in a row
    horizon = serial_horizon(project, durations)
    model = cp_model.CpModel()
    starts, ends, chosen = {}, {}, {}
    worker_intervals: dict[str, list] = {worker.id: [] for worker in project.workers}
    worker_demands: dict[str, list] = {worker.id: [] for worker in project.workers}
    # Dedications become integers: a share of 0.25 with 4 levels is a demand of 1 out of a capacity of 4
    levels = project.n_dedication_levels

    # Each task has a start, an end, and one optional interval per mode, of which exactly one is chosen
    for task in project.tasks:
        shortest = min(durations[task.id, mode.id] for mode in task.modes)
        if shortest > horizon:
            return ModeSolveResult(None, 'INFEASIBLE', None, perf_counter() - started)
        start = model.new_int_var(0, horizon - shortest, f's_{task.id}')
        end = model.new_int_var(shortest, horizon, f'e_{task.id}')
        starts[task.id], ends[task.id] = start, end
        presences = []
        for mode in task.modes:
            present = model.new_bool_var(f'x_{task.id}_{mode.id}')
            chosen[task.id, mode.id] = present
            presences.append(present)
            interval = model.new_optional_interval_var(start, durations[task.id, mode.id], end, present,
                                                       f'i_{task.id}_{mode.id}')
            # The interval occupies every worker of the mode, by the mode's dedication
            for worker_id, amount in mode.dedication.items():
                worker_intervals[worker_id].append(interval)
                worker_demands[worker_id].append(round(amount * levels))
        model.add_exactly_one(presences)

    # Precedence: a task starts after its predecessors end
    for before, after in project.tpg_edges:
        model.add(ends[before] <= starts[after])

    # Worker capacity: one task at a time (full), or dedications summing to at most one (partial)
    for worker_id, intervals in worker_intervals.items():
        if not intervals:
            continue
        if dedication == 'full':
            model.add_no_overlap(intervals)
        else:
            model.add_cumulative(intervals, worker_demands[worker_id], levels)

    # Objective: the latest end
    makespan = model.new_int_var(0, horizon, 'makespan')
    model.add_max_equality(makespan, list(ends.values()))
    model.minimize(makespan)

    # Solve within the time limit, with the given seed and search threads
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = threads
    solver.parameters.random_seed = seed
    status = solver.solve(model)
    if status == cp_model.MODEL_INVALID:
        raise ValueError(f'Invalid CP-SAT model: {model.validate()}')

    # Read the start and chosen mode of every task, and check the schedule independently of the model
    plan = None
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        plan_starts = {}
        for task in project.tasks:
            mode_id = next(mode.id for mode in task.modes if solver.value(chosen[task.id, mode.id]))
            plan_starts[task.id] = dict(day=solver.value(starts[task.id]), mode=mode_id)
        plan = ModeSchedule(solver.value(makespan), plan_starts)
        check_schedule(project, durations, plan, dedication)
    bound = float(solver.best_objective_bound) if plan is not None else None
    return ModeSolveResult(plan, solver.status_name(status), bound, perf_counter() - started)


def serial_horizon(project: Project, durations: Durations) -> int:
    """Every task one after another in its longest mode: no schedule needs longer."""
    return max(1, sum(max(durations[task.id, mode.id] for mode in task.modes) for task in project.tasks))


def check_schedule(project: Project, durations: Durations, plan: ModeSchedule, dedication: str = 'full') -> None:
    """Check precedence, worker capacity at every start, and the stated completion, independently of the model."""
    modes = {(task.id, mode.id): mode for task in project.tasks for mode in task.modes}

    # Every task has a valid start and mode; compute its finish
    finish = {}
    for task_id, item in plan.starts.items():
        if item['day'] < 0 or (task_id, item['mode']) not in modes:
            raise ValueError(f'{task_id}: invalid start or mode')
        finish[task_id] = item['day'] + durations[task_id, item['mode']]

    # Precedence, and the completion is the latest finish
    for before, after in project.tpg_edges:
        if finish[before] > plan.starts[after]['day']:
            raise ValueError(f'{after} starts before {before} finishes')
    if max(finish.values()) != plan.completion:
        raise ValueError('stated completion differs from the latest finish')

    # Capacity only changes at starts, so check the load at every start
    for task_id, item in plan.starts.items():
        day = item['day']
        load: dict[str, float] = {}
        # Sum the dedication of every task running at that start (zero-duration tasks never run)
        for other, other_item in plan.starts.items():
            if other_item['day'] <= day < finish[other] and finish[other] > other_item['day']:
                for worker_id, amount in modes[other, other_item['mode']].dedication.items():
                    load[worker_id] = load.get(worker_id, 0) + (1 if dedication == 'full' else amount)
        if any(value > 1 + 1e-9 for value in load.values()):
            raise ValueError(f'worker over capacity at {day}')
