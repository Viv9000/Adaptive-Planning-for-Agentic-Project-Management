"""Replay buffer holding the decisions of the most recent episodes."""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Sequence

from numpy.random import Generator

from planner.core.state import ActiveTask, State, action_from_record, action_record
from planner.methods.alphazero.training.self_play import TrainingSample


class ReplayBuffer:
    """Training samples from the last max_episodes episodes, each stored with its episode's outcome.

    The outcome (completion day, finished flag) lets relabeling curricula recompute value targets.
    """

    def __init__(self, max_episodes: int) -> None:
        self.max_episodes = max_episodes
        self.samples: deque[TrainingSample] = deque()
        self.outcomes: deque[tuple[int, bool]] = deque()
        self.episode_lengths: deque[int] = deque()  # Decisions per stored episode, oldest first.

    def __len__(self) -> int:
        return len(self.samples)

    def add_episode(self, samples: Sequence[TrainingSample], completion_day: int, finished: bool) -> None:
        """Add an episode's samples, then drop the oldest episodes beyond max_episodes."""
        self.samples.extend(samples)
        self.outcomes.extend([(completion_day, finished)] * len(samples))
        self.episode_lengths.append(len(samples))

        # Drop the oldest episodes until at most max_episodes remain
        while len(self.episode_lengths) > self.max_episodes:
            for _ in range(self.episode_lengths.popleft()):
                self.samples.popleft()
                self.outcomes.popleft()

    def clear(self) -> None:
        """Remove all episodes."""
        self.samples.clear()
        self.outcomes.clear()
        self.episode_lengths.clear()

    def sample_with_outcomes(
        self, batch_size: int, rng: Generator, value_target: Callable[[int, bool], float] | None = None,
    ) -> tuple[list[TrainingSample], list[tuple[int, bool]]]:
        """Return a batch drawn without replacement, with each sample's episode outcome (completion day, finished).

        value_target(day, finished) relabels the value targets from the outcomes.
        """
        indices = [int(i) for i in rng.choice(len(self.samples), batch_size, replace=False)]
        outcomes = [self.outcomes[i] for i in indices]
        if value_target is None:
            return [self.samples[i] for i in indices], outcomes

        # Replace each stored value target with one computed from its episode's outcome
        return [(self.samples[i][0], self.samples[i][1], value_target(*self.outcomes[i])) for i in indices], outcomes

    def state_dict(self) -> dict:
        """Return the buffer as primitive data (states as tuples) for weights-only checkpoints."""
        records = []
        for state, target, outcome in self.samples:
            active = [(task.task_id, task.mode_id, task.start_day, task.pending) for task in state.active]
            if isinstance(target, dict):
                target = {'sparse': [[action_record(action), probability] for action, probability in target.items()]}
            records.append((sorted(state.completed), active, state.day, target, outcome))
        return {'samples': records, 'outcomes': list(self.outcomes), 'episode_lengths': list(self.episode_lengths)}

    def load_state_dict(self, saved: dict) -> None:
        """Replace the buffer's contents with those of state_dict()."""
        # Rebuild the states from their tuples
        self.clear()
        for completed, active, day, target, outcome in saved['samples']:
            state = State(frozenset(completed), tuple(ActiveTask(*task) for task in active), day)
            if isinstance(target, dict):
                target = {action_from_record(action): probability for action, probability in target['sparse']}
            self.samples.append((state, target, outcome))

        # Restore the outcomes and episode lengths that go with them
        self.outcomes.extend(tuple(outcome) for outcome in saved['outcomes'])
        self.episode_lengths.extend(saved['episode_lengths'])
