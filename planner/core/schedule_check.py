"""Check that a played schedule is valid, independently of the MDP.

Every task runs once, without preemption, for a duration its mode can take, after all its predecessors have finished,
and no worker's total dedication exceeds one on any day.
Durations here are the realized ones of a stochastic episode, rounded up to whole days, D = ceil(max(0, X)).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import math

from planner.core.project import CAPACITY_TOLERANCE, Project, task_distribution_hash
from planner.core.state import State


@dataclass(frozen=True)
class ScheduledTask:
    """One activity of a played schedule: start day, finish day (inf if still running) and dedication per worker."""

    task_id: str
    start: int
    finish: float
    dedication: dict[str, float]
    mode_id: int | None


def schedule_from_states(project: Project, states: Sequence[State]) -> dict[str, ScheduledTask]:
    """Return the schedule of an episode from its states in order (the last one terminal).

    A task's start is its record's start day; it finishes on the day of the first state where it is completed.
    Tasks still running at the end get finish = inf. Each task's workers and dedications come from its mode.
    """
    tasks = {task.id: task for task in project.tasks}
    records = {}
    finishes: dict[str, float] = {}
    for state in states:
        for record in state.active:
            records.setdefault(record.task_id, record)
        for task_id in state.completed:
            finishes.setdefault(task_id, state.day)
    schedule = {}
    for task_id, record in records.items():
        mode = next((mode for mode in tasks[task_id].modes if mode.id == record.mode_id), None)
        dedication = dict(mode.dedication) if mode is not None else {}
        schedule[task_id] = ScheduledTask(task_id, record.start_day, finishes.get(task_id, math.inf), dedication,
                                          record.mode_id)
    return schedule


def schedule_violations(project: Project, schedule: dict[str, ScheduledTask], complete: bool) -> list[str]:
    """Return every rule the schedule breaks (an empty list for a valid schedule).

    complete: the episode finished every task, so every task must be scheduled and finished.
    """
    violations = []
    tasks = {task.id: task for task in project.tasks}

    # Every task once (when complete), with a possible duration
    if complete and set(schedule) != set(tasks):
        violations.append(f'Tasks not scheduled: {sorted(set(tasks) - set(schedule))}')
    for item in schedule.values():
        if item.start < 0 or item.finish < item.start:
            violations.append(f'{item.task_id}: start {item.start}, finish {item.finish}')
        elif math.isfinite(item.finish) and not _possible_duration(project, tasks[item.task_id], item, item.finish - item.start):
            violations.append(f'{item.task_id}: duration {item.finish - item.start} is impossible')

    # Precedence: a task starts only after all its predecessors finished
    for before, after in project.tpg_edges:
        if after in schedule and (before not in schedule or schedule[before].finish > schedule[after].start):
            violations.append(f'Precedence {before} -> {after} broken')

    # No worker over capacity on any day
    events = sorted({item.start for item in schedule.values()})
    for day in events:
        load: dict[str, float] = {}
        for item in schedule.values():
            if item.start <= day < item.finish:
                for worker, amount in item.dedication.items():
                    load[worker] = load.get(worker, 0.0) + amount
        for worker, amount in load.items():
            if amount > 1 + CAPACITY_TOLERANCE:
                violations.append(f'Worker {worker} is over capacity ({amount}) on day {day}')
    return violations


def check_episode(project: Project, states: Sequence[State], complete: bool) -> None:
    """Raise ValueError if the episode's schedule breaks any rule of schedule_violations."""
    violations = schedule_violations(project, schedule_from_states(project, states), complete)
    if violations:
        raise ValueError('Invalid schedule: ' + '; '.join(violations[:5]))


def _possible_duration(project: Project, task, item: ScheduledTask, days: float) -> bool:
    """Return whether a rounded duration of this many days has positive probability for the task (or its mode)."""
    key = next((mode.distribution_hash for mode in task.modes if mode.id == item.mode_id), None)
    distribution = project.distributions[key if key is not None else task_distribution_hash(task)]
    days = int(days)
    probability = distribution.evaluate_cdf(days) - (distribution.evaluate_cdf(days - 1) if days > 0 else 0.0)
    return probability > 0
