"""Updating the policy and value networks: the losses, one gradient step from a replay buffer batch, and the learning-rate schedule."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeAlias

import torch
from torch import nn
from torch.optim import Optimizer

from planner.core.mdp import MDP
from planner.network.encoding import NeuralLayout, encode_batch
from planner.network.policy import masked_joint_policy
from planner.methods.alphazero.training.self_play import TrainingSample

LossMetrics: TypeAlias = dict[str, float]

def update_networks(
    batch: Sequence[TrainingSample], mdp: MDP, layout: NeuralLayout,
    policy: nn.Module, value: nn.Module, optimizers: tuple[Optimizer, Optimizer],
) -> LossMetrics:
    """Update both networks on one batch of (state, visit distribution, value target) and return the losses.

    optimizers is (policy optimizer, value optimizer).
    """
    # Encode the batch's states
    states, visit_targets, value_targets = zip(*batch)
    policy.train()
    value.train()
    device = next(policy.parameters()).device
    inputs = encode_batch(states, mdp, layout, device)

    # Policy loss: cross-entropy between the masked policy and the visit targets
    legal_actions = [mdp.legal_actions(state) for state in states]
    _, log_probabilities = masked_joint_policy(policy, *inputs, layout, legal_actions)
    policy_loss = visit_cross_entropy(torch.stack(visit_targets).to(device), log_probabilities)

    # Value loss: binary cross-entropy against the value targets
    value_targets = torch.tensor(value_targets, dtype=torch.float32, device=device).unsqueeze(1)
    value_loss = torch.nn.functional.binary_cross_entropy(value(*inputs), value_targets)
    losses = {'policy_loss': float(policy_loss.detach()), 'value_loss': float(value_loss.detach())}

    # Take one optimizer step for each network
    for optimizer in optimizers:
        optimizer.zero_grad()
    policy_loss.backward()
    value_loss.backward()
    for optimizer in optimizers:
        optimizer.step()
    return losses


def update_from_replay(replay, curriculum, mdp: MDP, layout: NeuralLayout, policy: nn.Module, value: nn.Module,
                  optimizers: tuple[Optimizer, Optimizer], batch_size: int, rng) -> LossMetrics:
    """Run one update on a batch from the replay buffer, scoring the stored outcomes against the current ranked bar."""
    batch, _ = replay.sample_with_outcomes(batch_size, rng, curriculum.value_target)
    return update_networks(batch, mdp, layout, policy, value, optimizers)


def visit_cross_entropy(visit_targets, log_probabilities):
    """Return the mean over the batch of -sum(visits · log policy)."""
    # Only actions with visits contribute; illegal actions have log probability -inf, and 0 · -inf would be NaN.
    visited = visit_targets > 0
    return -(visit_targets[visited] * log_probabilities[visited]).sum() / len(visit_targets)
