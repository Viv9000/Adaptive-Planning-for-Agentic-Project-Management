"""The ranked reward that both learning methods, the AlphaZero-based method and PPO, train with. Evaluation always uses
the final deadline and binary success.

Each episode earns 1 for beating ranked_percentile of the last ranked_window completion days, 0.5 for matching the bar
and 0 otherwise, run to completion; the bar never falls below the deadline (half a day after it), so once the policy
meets the deadline the reward is the binary deadline reward. Random rollouts' completion days set the first bar.
value_target lets the AlphaZero-based method relabel its replay buffer against the current bar.
"""

import numpy as np
from numpy.random import default_rng

from planner.core.mdp import MDP
from planner.core.simulator import run_episode
from planner.config import DEFAULT_TRAINING_CONFIG
from planner.core.players import RandomPlayer


class TrainingMDP(MDP):
    """The scheduling MDP with a cutoff day and, for the ranked curriculum, a reward bar on the completion day."""

    def __init__(self, project, cutoff, threshold=None):
        super().__init__(project)
        self.cutoff = cutoff
        self.threshold = threshold  # Ranked reward bar on the completion day; None means binary deadline reward.

    @property
    def stop_day(self):
        """Return the cutoff day; None runs episodes to completion (for calibration and the ranked reward)."""
        return self.cutoff

    def terminal_return(self, state):
        """Return the ranked reward with a bar, else 1 for finishing by the deadline; unfinished episodes earn 0."""
        if not self.is_complete(state):
            return 0.0
        if self.threshold is not None:
            return ranked_reward(state.day, self.threshold)
        return float(state.day <= self.project.deadline.delta)


def ranked_reward(day, threshold):
    """Return 1 for finishing before the bar, 0.5 for finishing exactly on it, and 0 after it."""
    if day < threshold:
        return 1.0
    return 0.5 if day == threshold else 0.0


def validate_curriculum(config):
    """Check a positive integer curriculum_rollouts and the ranked settings."""
    config = dict(DEFAULT_TRAINING_CONFIG, **config)
    count = config['curriculum_rollouts']
    if type(count) is not int or count < 1:
        raise ValueError('curriculum_rollouts must be a positive integer')
    if not 0 < config['ranked_percentile'] < 1:
        raise ValueError('ranked_percentile must be in (0, 1)')
    if type(config['ranked_window']) is not int or config['ranked_window'] < 1:
        raise ValueError('ranked_window must be a positive integer')


def random_completion_days(project, count, seed):
    """Return the completion days of count random-player episodes run to completion; they set the first ranked bar."""
    mdp = TrainingMDP(project, cutoff=None)
    rng = default_rng(seed)
    player = RandomPlayer(mdp)
    return [run_episode(mdp, mdp.reset(), lambda state: player.act(state, rng), rng).day for _ in range(count)]


class Curriculum:
    """Sets each episode's ranked bar; its state dict is saved in checkpoints."""

    def __init__(self, project, config, saved=None):
        config = dict(DEFAULT_TRAINING_CONFIG, **config)
        self.project = project
        self.ranked_percentile = config['ranked_percentile']
        self.ranked_window = config['ranked_window']
        # Continue a saved curriculum
        if saved is not None:
            self.state = saved
            return

        # Random rollouts' completion days set the first ranked bar
        days = random_completion_days(project, config['curriculum_rollouts'], config['seed'])
        self.state = dict(context=None, calibration_days=days, recent_days=days[-self.ranked_window:])

    def ranked_threshold(self):
        """Return the bar: the completion day that a share ranked_percentile of recent episodes did not beat.

        The bar never falls below the deadline: it is at least half a day after it, so finishing on the deadline still
        earns the full reward.
        """
        bar = float(np.quantile(self.state['recent_days'], 1 - self.ranked_percentile))
        return max(bar, self.project.deadline.delta + 0.5)

    def value_target(self, completion_day, completed):
        """Return the value target for a stored episode outcome under the current bar."""
        if not completed:
            return 0.0
        return ranked_reward(completion_day, self.state['context']['threshold'])

    def record_completion(self, completion_day, completed):
        """Add a finished episode's completion day to the ranked window."""
        if completed:
            days = self.state['recent_days']
            days.append(completion_day)
            del days[:-self.ranked_window]

    def episode_context(self, episode):
        """Return the context of a one-based episode number: the final deadline and the ranked bar."""
        return dict(deadline=self.project.deadline.delta, threshold=self.ranked_threshold())

    def training_mdp(self, context):
        """Return a TrainingMDP for a context; see context_mdp."""
        return context_mdp(self.project, context)


def context_mdp(project, context):
    """Return the TrainingMDP of a context: episodes run to completion and earn the ranked reward against its bar."""
    return TrainingMDP(project, None, threshold=context['threshold'])
