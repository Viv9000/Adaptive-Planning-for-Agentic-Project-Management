"""Episode simulation with hidden sampled finish days."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING

from numpy.random import Generator

from planner.core.state import STOP, Action, State

if TYPE_CHECKING:
    from planner.core.mdp import MDP


class RolloutSimulator:
    """Simulate one episode; finish days are sampled at START and kept private until STOP reveals them.

    Every MCTS simulation creates a new simulator from the observed state, resampling active tasks.
    The state must be valid; callers validate states that come from outside.
    """

    def __init__(self, mdp: MDP, state: State, rng: Generator) -> None:
        """Sample finish days for the active tasks, conditioned on how long they have run."""
        self.mdp = mdp
        self.state = state
        self.rng = rng
        self._finish_days: dict[str, int] = {}
        if not mdp.is_terminal(state):
            for record in state.active:
                remaining = mdp.sample_remaining_duration(
                    record.task_id, record.mode_id, state.day - record.start_day, rng, record.pending,
                )
                self._finish_days[record.task_id] = state.day + remaining

    def step(self, action: Action) -> tuple[State, float, bool]:
        """Apply a legal action and return (next_state, reward, done).

        STOP advances to the earliest finish day (or the cutoff) and completes every task finishing then.
        """
        if action != STOP:
            # Sample a finish day for every task the action started
            next_state = self.mdp.apply_outcome(self.state, action, ())
            for record in next_state.active:
                if record.task_id not in self._finish_days:
                    duration = self.mdp.sample_remaining_duration(record.task_id, record.mode_id, 0, self.rng, True)
                    self._finish_days[record.task_id] = self.state.day + duration
        else:
            # Jump to the earliest finish day, but not past the cutoff
            next_day = min(self._finish_days.values())
            if self.mdp.stop_day is not None:
                next_day = min(next_day, self.mdp.stop_day)

            # Complete every task that finishes on that day
            finished = [task for task, day in self._finish_days.items() if day == next_day]
            next_state = self.mdp.apply_outcome(self.state, action, finished, next_day - self.state.day)
            for task in finished:
                del self._finish_days[task]

        reward = self.mdp.reward(self.state, next_state)
        self.state = next_state
        return next_state, reward, self.mdp.is_terminal(next_state)


def run_episode(mdp: MDP, state: State, act: Callable[[State], Action], rng: Generator) -> State:
    """Play from state until the episode ends, taking act(current state) at every step; return the terminal state.

    The episode loop of training (planner/methods/alphazero/training/self_play.py) and of the calibration rollouts;
    each wraps act to choose its own way and to record what it needs.
    """
    simulator = RolloutSimulator(mdp, state, rng)
    while not mdp.is_terminal(simulator.state):
        simulator.step(act(simulator.state))
    return simulator.state
