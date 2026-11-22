"""MDP state and action types, and the progress format for ongoing projects."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias, TypedDict


@dataclass(frozen=True, slots=True)
class ActiveTask:
    """A started task holding its mode's worker dedication.

    pending=True: started on the current day and not yet checked by STOP (even zero-duration tasks).
    pending=False: a STOP has seen the task still running.
    """

    task_id: str
    mode_id: int
    start_day: int
    pending: bool = False


@dataclass(frozen=True, slots=True)
class State:
    """Completed tasks, active tasks (sorted by task ID), and the current day.

    Sampled finish days live only in the simulator, so decisions cannot see the future.
    """

    completed: frozenset[str]
    active: tuple[ActiveTask, ...]
    day: int


@dataclass(frozen=True, slots=True)
class Start:
    """Start a task in a mode; reserves its workers without advancing time."""

    task_id: str
    mode_id: int


@dataclass(frozen=True, slots=True)
class Stop:
    """Advance time to the next task completion, or to the day after the deadline."""


Action: TypeAlias = Start | Stop
STOP = Stop()


def action_record(action: Action) -> list:
    """Return an action as primitive data: ['start', task, mode] or ['stop']."""
    if isinstance(action, Start):
        return ['start', action.task_id, action.mode_id]
    return ['stop']


def action_from_record(record: list) -> Action:
    """Return the action of action_record's data."""
    kind = record[0]
    if kind == 'start':
        return Start(record[1], record[2])
    if kind == 'stop':
        return STOP
    raise ValueError(f'Unknown action record {record!r}')


class _OptionalActiveProgress(TypedDict, total=False):
    # A separate base class keeps the other keys required on Python 3.10.
    pending: bool


class ActiveProgress(_OptionalActiveProgress):
    """One active task in a progress record; pending defaults to False."""

    task: str
    mode: int
    start_day: int


class Progress(TypedDict):
    """Observed progress of an ongoing project; unlisted tasks are unstarted."""

    day: int
    completed: list[str]
    active: list[ActiveProgress]
