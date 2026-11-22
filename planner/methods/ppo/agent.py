"""PPO: an actor-critic trained on its own episodes, which acts without search.

It uses the policy and value networks of planner/network/, which it shares with the AlphaZero-based method.
"""

from dataclasses import dataclass

import numpy as np
import torch

from planner.core.simulator import run_episode
from planner.core.schedule_check import check_episode
from planner.network.encoding import build_layout, encode_batch, encode_state
from planner.network.policy import build_networks, masked_joint_policy
from planner.core.players import Player


@dataclass(frozen=True)
class PPOSettings:
    """The paper's PPO settings."""

    episodes_per_batch: int = 16  # Episodes collected per update
    epochs: int = 4  # Passes over each batch
    minibatch_size: int = 32
    learning_rate: float = 0.001
    gamma: float = 1.0  # No discounting: the only reward comes at the end
    gae_lambda: float = 0.95
    clip_epsilon: float = 0.2  # How far the policy ratio may move from 1 in the surrogate
    value_weight: float = 0.5
    entropy_weight: float = 0.01

    def __post_init__(self):
        for name in ('episodes_per_batch', 'epochs', 'minibatch_size'):
            if type(getattr(self, name)) is not int or getattr(self, name) < 1:
                raise ValueError(f'{name} must be a positive integer')
        for name in ('gamma', 'gae_lambda'):
            if not 0 <= getattr(self, name) <= 1:
                raise ValueError(f'{name} must be in [0, 1]')
        if not np.isfinite(self.learning_rate) or self.learning_rate <= 0:
            raise ValueError('learning_rate must be positive and finite')
        if not 0 < self.clip_epsilon < 1:
            raise ValueError('clip_epsilon must be in (0, 1)')
        for name in ('value_weight', 'entropy_weight'):
            if not np.isfinite(getattr(self, name)) or getattr(self, name) < 0:
                raise ValueError(f'{name} must be nonnegative and finite')


@dataclass
class Trajectory:
    """Observed states and frozen collection statistics for one complete rollout."""

    states: list
    legal_actions: list
    actions: torch.Tensor
    old_log_probabilities: torch.Tensor
    old_values: torch.Tensor
    reward: float
    terminal: object


def generalized_advantages(values, terminal_reward, gamma=1.0, gae_lambda=0.95):
    """Return GAE and lambda-return targets, with zero bootstrap at episode termination."""
    advantages = torch.zeros_like(values)
    following_value = values.new_tensor(0.0)
    following_advantage = values.new_tensor(0.0)
    # Walk back from the last decision; the only reward is the terminal one
    for index in reversed(range(len(values))):
        reward = terminal_reward if index == len(values) - 1 else 0.0
        # One-step temporal-difference error, then its lambda-weighted sum over the following decisions
        delta = reward + gamma * following_value - values[index]
        following_advantage = delta + gamma * gae_lambda * following_advantage
        advantages[index] = following_advantage
        following_value = values[index]
    return advantages, advantages + values


def ppo_loss(log_probabilities, old_log_probabilities, advantages, values, targets, entropy, settings):
    """Clipped policy surrogate plus half squared value error and an entropy bonus."""
    ratio = (log_probabilities - old_log_probabilities).exp()
    clipped = ratio.clamp(1 - settings.clip_epsilon, 1 + settings.clip_epsilon)
    policy_loss = -torch.minimum(ratio * advantages, clipped * advantages).mean()
    value_loss = 0.5 * (values - targets).square().mean()
    return policy_loss + settings.value_weight * value_loss - settings.entropy_weight * entropy.mean()


class PPOPlayer(Player):
    """Choose the most probable legal action, without search or hidden simulator state."""

    def __init__(self, mdp, policy, layout=None):
        self.mdp, self.policy = mdp, policy
        self.layout = layout or build_layout(mdp.project)

    def act(self, state, rng):
        # The most probable legal action under the trained policy
        self.policy.eval()
        with torch.no_grad():
            probabilities, _ = masked_joint_policy(
                self.policy, *encode_state(state, self.mdp, self.layout), self.layout,
                [self.mdp.legal_actions(state)])
        return self.layout.actions[int(probabilities[0].argmax())]


class PPO:
    """CPU actor-critic with one joint Adam optimizer and no replay or search."""

    def __init__(self, project, config, settings=None):
        """config: the training config (network sizes and seed); settings: the PPO settings."""
        self.settings = settings or PPOSettings()
        # The policy and value networks (planner/network/), initialized from this run's seed without moving torch's
        # global random stream
        self.layout = build_layout(project)
        with torch.random.fork_rng(devices=[]):
            torch.manual_seed(config['seed'])
            self.policy, self.value = build_networks(project, self.layout, config)
        # The networks share only feature buffers; deduplication also protects shared parameters.
        self.parameters = list(dict.fromkeys([*self.policy.parameters(), *self.value.parameters()]))
        self.optimizer = torch.optim.Adam(self.parameters, lr=self.settings.learning_rate)
        self.rng = np.random.default_rng(config['seed'])
        self.environment_steps = 0
        self.optimizer_steps = 0

    def collect(self, mdp, seed, *, check_schedule=False):
        """Sample one trajectory through run_episode, keeping duration and policy streams separate."""
        duration_rng = np.random.default_rng(seed)
        policy_rng = np.random.default_rng(np.random.SeedSequence([seed, 1]))
        states, legal, actions, logs, values = [], [], [], [], []
        self.policy.eval()
        self.value.eval()

        def act(state):
            # Sample an action from the policy over the legal actions, and record what the update needs
            choices = mdp.legal_actions(state)
            with torch.no_grad():
                inputs = encode_state(state, mdp, self.layout)
                probabilities, log_probabilities = masked_joint_policy(self.policy, *inputs, self.layout, [choices])
                weights = probabilities[0].double().numpy()
                index = int(policy_rng.choice(len(weights), p=weights / weights.sum()))
                values.append(float(self.value(*inputs).item()))
                logs.append(float(log_probabilities[0, index]))
            states.append(state)
            legal.append(choices)
            actions.append(index)
            return self.layout.actions[index]

        # Play the episode; durations come from their own random stream
        terminal = run_episode(mdp, mdp.reset(), act, duration_rng)
        self.environment_steps += len(states)
        if check_schedule:
            check_episode(mdp.project, states + [terminal], mdp.is_complete(terminal))
        return Trajectory(states, legal, torch.tensor(actions, dtype=torch.long), torch.tensor(logs),
                          torch.tensor(values), mdp.terminal_return(terminal), terminal)

    def reevaluate(self, inputs, legal_actions, actions):
        """Differentiable taken-action log probabilities, values and masked joint entropy."""
        probabilities, logs = masked_joint_policy(self.policy, *inputs, self.layout, legal_actions)
        # Replace illegal log probabilities before multiplying, avoiding zero times minus infinity.
        entropy = -(probabilities * logs.masked_fill(~torch.isfinite(logs), 0)).sum(dim=1)
        return logs.gather(1, actions[:, None]).squeeze(1), self.value(*inputs).flatten(), entropy

    def update(self, mdp, trajectories):
        """Normalize advantages once over the on-policy batch, then shuffle minibatches each epoch."""
        if not trajectories or not all(trajectory.states for trajectory in trajectories):
            raise ValueError('PPO update needs nonempty trajectories')
        # Flatten the batch's decisions, and compute advantages and value targets from the collection-time values
        inputs = encode_batch([state for row in trajectories for state in row.states], mdp, self.layout, 'cpu')
        legal = [actions for row in trajectories for actions in row.legal_actions]
        actions = torch.cat([row.actions for row in trajectories])
        old_logs = torch.cat([row.old_log_probabilities for row in trajectories])
        estimates = [generalized_advantages(row.old_values, row.reward, self.settings.gamma,
                                           self.settings.gae_lambda) for row in trajectories]
        advantages, targets = (torch.cat(parts).detach() for parts in zip(*estimates))
        advantages = (advantages - advantages.mean()) / advantages.std(unbiased=False).clamp_min(1e-8)
        # Several epochs of shuffled minibatches, one Adam step each
        self.policy.train()
        self.value.train()
        losses = []
        for _ in range(self.settings.epochs):
            order = self.rng.permutation(len(actions))
            for start in range(0, len(actions), self.settings.minibatch_size):
                indices = order[start:start + self.settings.minibatch_size]
                logs, values, entropy = self.reevaluate(tuple(part[indices] for part in inputs),
                                                       [legal[index] for index in indices], actions[indices])
                loss = ppo_loss(logs, old_logs[indices], advantages[indices], values,
                                targets[indices], entropy, self.settings)
                if not torch.isfinite(loss):
                    raise FloatingPointError('Nonfinite PPO loss')
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                self.optimizer_steps += 1
                losses.append(float(loss.detach()))
        return dict(loss=float(np.mean(losses)), batch_steps=len(actions),
                    environment_steps=self.environment_steps, optimizer_steps=self.optimizer_steps)
