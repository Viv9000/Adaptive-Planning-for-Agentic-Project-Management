"""Scheduling rules: legal actions, state updates, outcome probabilities, and rewards.

The solver, MCTS, and simulator all use these rules.
"""

from __future__ import annotations

from collections import OrderedDict
from collections.abc import Callable, Iterable, Iterator
from dataclasses import replace
from itertools import product
import math
from numbers import Integral

from numpy.random import Generator

from planner.core.project import CAPACITY_TOLERANCE, Mode, Project
from planner.core.state import STOP, Action, ActiveTask, Progress, Start, State
from planner.core.validation import validate_project


class MDP:
    """The scheduling MDP for one fixed project.

    Success means every task completes by the deadline; the episode fails once the day passes it.
    """

    project: Project
    debug_validation: bool

    def __init__(self, project: Project, debug_validation: bool = False, *, legal_action_cache_size: int = 4096) -> None:
        """Validate the project and index its tasks, modes, distributions, and predecessors.

        debug_validation also checks every state passed in; legal_action_cache_size = 0 disables the cache.
        """
        # Check the project
        report = validate_project(project)
        if not report.is_correct:
            raise ValueError("Incorrect project: " + "; ".join(report.errors))
        self.project = project
        self.debug_validation = debug_validation
        self._legal_action_cache_size = legal_action_cache_size
        self._legal_action_cache: OrderedDict[tuple, tuple[Action, ...]] = OrderedDict()

        # Index tasks, modes, distributions, and predecessors by ID
        self._tasks = {task.id: task for task in project.tasks}
        self._modes = {(task.id, mode.id): mode for task in project.tasks for mode in task.modes}
        self._distributions = {key: project.distributions[mode.distribution_hash] for key, mode in self._modes.items()}
        self._predecessors: dict[str, set[str]] = {task.id: set() for task in project.tasks}
        for predecessor, successor in project.tpg_edges:
            self._predecessors[successor].add(predecessor)
        if any(not task.modes for task in project.tasks):
            raise ValueError('Every task needs at least one mode')

    def predecessors(self, task_id: str) -> set[str]:
        """Return the task's direct predecessors."""
        return self._predecessors[task_id]

    def mode(self, task_id: str, mode_id: int) -> Mode | None:
        """Return a stored mode, or None if the task has no such mode."""
        return self._modes.get((task_id, mode_id))

    def reset(self) -> State:
        """Return the start of the project: day zero, nothing started."""
        return State(frozenset(), (), 0)

    @property
    def stop_day(self) -> int | None:
        """Day the episode fails (deadline + 1); training curricula may override it."""
        return self.project.deadline.delta + 1

    def is_complete(self, state: State) -> bool:
        """Return whether every task is completed."""
        return state.completed == self._tasks.keys()

    def is_terminal(self, state: State) -> bool:
        """Return whether all tasks are complete or the cutoff day is reached."""
        return self.is_complete(state) or (self.stop_day is not None and state.day >= self.stop_day)

    def success_indicator(self, state: State) -> int:
        """Return 1 if all tasks completed by the deadline, otherwise 0."""
        return int(self.is_complete(state) and state.day <= self.project.deadline.delta)

    def reward(self, state: State, next_state: State) -> float:
        """Return the terminal return on the step that ends the episode, otherwise 0."""
        if not self.is_terminal(state) and self.is_terminal(next_state):
            return self.terminal_return(next_state)
        return 0.0

    def terminal_return(self, state: State) -> float:
        """Return 1.0 for on-time completion; training curricula override this."""
        return float(self.success_indicator(state))

    # Legal actions

    def legal_actions(self, state: State) -> list[Action]:
        """Return legal STARTs in project order, then STOP if any task is active.

        START needs an unstarted task, completed predecessors, and enough free dedication for its mode.
        Results are cached by (completed tasks, active task/mode pairs).
        """
        if self.debug_validation:
            self.validate_state(state)
        if self.is_terminal(state):
            return []

        # Return the cached actions if this combination of tasks was seen before
        cache_key = (state.completed, tuple((record.task_id, record.mode_id) for record in state.active))
        if self._legal_action_cache_size > 0:
            cached = self._legal_action_cache.get(cache_key)
            if cached is not None:
                self._legal_action_cache.move_to_end(cache_key)
                return list(cached)

        # The modes of ready tasks that fit in the workers' free dedication, then STOP once something is running
        started = state.completed.union(record.task_id for record in state.active)
        remaining = self.remaining_dedication(state)
        actions: list[Action] = []
        for task in self.project.tasks:
            if task.id in started or not self._predecessors[task.id].issubset(state.completed):
                continue
            for mode in task.modes:
                if all(dedication <= remaining[worker_id] + CAPACITY_TOLERANCE
                       for worker_id, dedication in mode.dedication.items()):
                    actions.append(Start(task.id, mode.id))
        if state.active:
            actions.append(STOP)

        # Cache the result, dropping the least recently used entry when full
        if self._legal_action_cache_size > 0:
            self._legal_action_cache[cache_key] = tuple(actions)
            if len(self._legal_action_cache) > self._legal_action_cache_size:
                self._legal_action_cache.popitem(last=False)
        return actions

    def is_legal(self, state: State, action: Action) -> bool:
        """Return whether an action is legal in a state."""
        return action in self.legal_actions(state)

    def remaining_dedication(self, state: State) -> dict[str, float]:
        """Return each worker's free dedication: 1 minus what active tasks reserve."""
        reserved = {worker.id: math.fsum(self.mode(record.task_id, record.mode_id).dedication.get(worker.id, 0)
                                         for record in state.active) for worker in self.project.workers}
        remaining = {}
        for worker in self.project.workers:
            available = 1 - reserved[worker.id]
            # Clip rounding noise to zero; larger negatives are left for validation to report.
            if -CAPACITY_TOLERANCE <= available < 0:
                available = 0.0
            remaining[worker.id] = available
        return remaining

    # State updates

    def apply_outcome(self, state: State, action: Action, finished_tasks: Iterable[str], elapsed_days: int = 0) -> State:
        """Return the next state for an action and a given outcome; nothing is sampled here.

        START adds the task as pending on the same day, keeping the active tasks in task-ID order.
        STOP advances elapsed_days, completes finished_tasks, and marks the rest as seen running.
        The caller supplies a legal action and a possible outcome.
        """
        if action != STOP:
            record = ActiveTask(action.task_id, action.mode_id, state.day, pending=True)
            index = next((i for i, other in enumerate(state.active) if other.task_id > record.task_id),
                         len(state.active))
            next_state = State(state.completed, state.active[:index] + (record,) + state.active[index:], state.day)
        else:
            # Advance the day, complete the finished tasks, and mark the rest as seen running
            completed = state.completed.union(finished_tasks)
            survivors = tuple(replace(record, pending=False) for record in state.active if record.task_id not in completed)
            next_state = State(completed, survivors, state.day + elapsed_days)
        if self.debug_validation:
            self.validate_state(next_state)
        return next_state

    # Durations

    def remaining_duration_cdf(self, task_id: str, mode_id: int, elapsed_days: int, u: int, pending: bool = False) -> float:
        """Return Pr(the task finishes within u more days), given it has run elapsed_days.

        For a task seen running this is 1 - S(e + u) / S(e) with S(t) = Pr(D > t), computed in log space.
        """
        distribution = self._distributions[(task_id, mode_id)]
        if u < 0:
            return 0.0

        # A pending task has not run yet, so its plain CDF applies
        if pending:
            return distribution.evaluate_cdf(u)

        # A running task is conditioned on having lasted elapsed_days
        log_survival = distribution.log_survival(elapsed_days)
        return -math.expm1(distribution.log_survival(elapsed_days + u) - log_survival)

    def sample_remaining_duration(
        self, task_id: str, mode_id: int, elapsed_days: int, rng: Generator, pending: bool = False,
    ) -> int:
        """Sample the remaining days; a task seen running takes at least one more day."""
        distribution = self._distributions[(task_id, mode_id)]
        if pending:
            return math.ceil(max(0, distribution.sample(rng)))
        return math.ceil(distribution.sample_above(elapsed_days, rng)) - elapsed_days

    # Exact outcomes (used by the exact solver and transition tests)

    def transition_outcomes(
        self, state: State, action: Action, check_budget: Callable[[], None] | None = None,
    ) -> Iterator[tuple[float, State]]:
        """Yield (probability, next_state) for every possible outcome of an action.

        For STOP, each delay up to the cutoff and each subset of active tasks finishing then is one outcome.
        check_budget is called regularly so the solver can stop at its time limit.
        """
        check = check_budget if check_budget is not None else lambda: None
        check()

        # Every action but STOP is deterministic
        if action != STOP:
            yield 1.0, self.apply_outcome(state, action, ())
            return

        # STOP: enumerate every delay up to the cutoff
        if self.stop_day is None:
            raise ValueError('Exact outcomes require a finite cutoff')
        horizon = self.stop_day - state.day
        for delay in range(horizon + 1):
            check()
            probabilities = [self._finish_and_survival_probabilities(record, state.day, delay) for record in state.active]

            # Each active task either finishes at this delay or survives past it
            for finishes in product((False, True), repeat=len(state.active)):
                check()
                # Nothing finishing is only possible at the cutoff
                if not any(finishes) and delay != horizon:
                    continue
                probability = math.prod(
                    mass if finished else survival for finished, (mass, survival) in zip(finishes, probabilities)
                )
                if probability > 0:
                    completed = [record.task_id for record, finished in zip(state.active, finishes) if finished]
                    yield probability, self.apply_outcome(state, action, completed, delay)

    def _finish_and_survival_probabilities(self, record: ActiveTask, day: int, delay: int) -> tuple[float, float]:
        """Return Pr(finish exactly at delay) and Pr(still running after delay), given the task's age."""
        # Condition on the task's age: pending tasks have not run, running ones have lasted age days
        distribution = self._distributions[(record.task_id, record.mode_id)]
        age = day - record.start_day
        denominator = 0.0 if record.pending else distribution.log_survival(age)

        # Probability of still running after the delay
        upper = age + delay
        log_after = distribution.log_survival(upper)
        survival = math.exp(log_after - denominator)

        # Probability of finishing exactly at the delay
        if delay == 0:
            mass = distribution.evaluate_cdf(0) if record.pending else 0.0
        elif distribution.family == "tabular":
            mass = distribution.probabilities.get(upper, 0) / math.exp(denominator)
        else:
            lower = upper - 1
            # CDF differences are accurate below the median; survival ratios above it.
            if distribution.evaluate_cdf(upper) <= 0.5:
                mass = (distribution.evaluate_cdf(upper) - distribution.evaluate_cdf(lower)) / math.exp(denominator)
            else:
                log_before = distribution.log_survival(lower)
                if log_before == -math.inf:
                    mass = 0.0
                else:
                    mass = math.exp(log_before - denominator) * -math.expm1(log_after - log_before)
        return mass, survival

    # Progress input and validation

    def state_from_progress(self, progress: Progress) -> State:
        """Build and validate a State from an observed progress record."""
        # Read the record, rejecting duplicate tasks
        try:
            completed = progress["completed"]
            active = tuple(
                ActiveTask(record["task"], record["mode"], record["start_day"], record.get("pending", False))
                for record in progress["active"]
            )
            if len(set(completed)) != len(completed):
                raise ValueError("Impossible progress: duplicate completed task")
            active_ids = [record.task_id for record in active]
            if len(set(active_ids)) != len(active_ids):
                raise ValueError("Impossible progress: duplicate active task")
            state = State(frozenset(completed), tuple(sorted(active, key=lambda record: record.task_id)), progress["day"])
        except (KeyError, TypeError, AttributeError) as error:
            raise ValueError(f"Invalid progress record: {error}") from error

        # Check the state against the project
        self.validate_state(state)
        return state

    def validate_state(self, state: State) -> None:
        """Raise ValueError if a state is inconsistent with the project.

        Checks: valid types and day, known and unique tasks in task-ID order, no task both completed and active,
        completed predecessors, known modes, start days within [0, day], pending tasks started today,
        running tasks able to last longer than their age, and no worker over capacity.
        """
        # Check the types and the day
        if not isinstance(state.day, Integral) or state.day < 0:
            raise ValueError(f"Impossible progress: day {state.day!r} must be a nonnegative integer")
        if not isinstance(state.completed, frozenset) or not isinstance(state.active, tuple):
            raise ValueError("State requires a frozenset of completed tasks and a tuple of active records")

        # Check that tasks are known, unique, in order, and not both completed and active
        active_ids = []
        for record in state.active:
            if not isinstance(record, ActiveTask):
                raise ValueError("State active entries must be ActiveTask records")
            active_ids.append(record.task_id)
        for task_id in (*state.completed, *active_ids):
            if not isinstance(task_id, str) or task_id not in self._tasks:
                raise ValueError(f"Impossible progress: unknown task {task_id!r}")
        if len(set(active_ids)) != len(active_ids):
            raise ValueError("Impossible progress: duplicate active task")
        if active_ids != sorted(active_ids):
            raise ValueError("Active records must be in canonical task-ID order")
        overlap = state.completed.intersection(active_ids)
        if overlap:
            raise ValueError(f"Impossible progress: tasks both completed and active: {sorted(overlap)}")

        # Check that every started task has its predecessors completed
        for task_id in (*state.completed, *active_ids):
            unfinished = self._predecessors[task_id] - state.completed
            if unfinished:
                status = "completed" if task_id in state.completed else "active"
                raise ValueError(
                    f"Impossible progress: task {task_id} is {status} but predecessor {sorted(unfinished)[0]} is unfinished"
                )

        # Check each active task's mode, then the workers' capacity
        for record in state.active:
            if not isinstance(record.mode_id, int) or self.mode(record.task_id, record.mode_id) is None:
                raise ValueError(f'Impossible progress: task {record.task_id} has unknown mode {record.mode_id!r}')
        for record in state.active:
            self._validate_active(record, state.day)
        for worker_id, remaining in self.remaining_dedication(state).items():
            if remaining < 0:
                raise ValueError(f"Impossible progress: worker {worker_id} exceeds unit capacity by {-remaining}")

    def _validate_active(self, record: ActiveTask, day: int) -> None:
        """Raise ValueError if an active task has an unknown mode, an impossible start day, or cannot still be running."""
        context = f"Impossible progress: task {record.task_id}"
        key = (record.task_id, record.mode_id)
        if key not in self._distributions or not isinstance(record.mode_id, Integral):
            raise ValueError(f"{context} has unknown mode {record.mode_id!r}")
        if not isinstance(record.start_day, Integral) or not 0 <= record.start_day <= day:
            raise ValueError(f"{context} start_day {record.start_day!r} must be an integer in [0, {day}]")
        if not isinstance(record.pending, bool):
            raise ValueError(f"{context} pending must be true or false")
        if record.pending:
            if record.start_day != day:
                raise ValueError(f"{context} is pending but did not start on day {day}")
        else:
            elapsed = day - record.start_day
            # Log survival keeps tiny but possible tails from rounding to zero.
            if self._distributions[key].log_survival(elapsed) == -math.inf:
                raise ValueError(f"{context} cannot survive to elapsed day {elapsed}")
