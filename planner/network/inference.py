"""Network callbacks for MCTS: priors over legal actions and state values as plain Python numbers."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from time import perf_counter

import torch
from torch import device as TorchDevice, nn

from planner.core.mdp import MDP
from planner.core.state import Action, State
from planner.network.encoding import NeuralLayout, encode_state
from planner.network.policy import masked_joint_policy


def make_inference_callbacks(
    mdp: MDP, layout: NeuralLayout, policy: nn.Module, value: nn.Module,
    device: str | TorchDevice = "cpu", metrics: dict[str, float] | None = None,
) -> tuple[Callable[[State, Sequence[Action]], dict[Action, float]], Callable[[State], float]]:
    """Return prior_fn(state, legal_actions) and value_fn(state) for MCTS.

    If metrics is given, encoding and inference call counts and seconds are added to it.
    """
    policy.to(device)
    value.to(device)
    policy.eval()
    value.eval()

    def record(name, elapsed):
        # Add one call and its seconds to the metrics, if they are collected
        if metrics is not None:
            metrics[name + '_seconds'] = metrics.get(name + '_seconds', 0) + elapsed
            metrics[name + '_calls'] = metrics.get(name + '_calls', 0) + 1

    # MCTS asks for a leaf's priors and then its value, so the last encoding is kept for the second call
    last = {'state': None, 'inputs': None}

    def features(state):
        if state == last['state']:
            return last['inputs']
        started = perf_counter()
        result = tuple(tensor.to(device) for tensor in encode_state(state, mdp, layout))
        record('encoding', perf_counter() - started)
        last.update(state=state, inputs=result)
        return result

    def prior_fn(state, actions):
        # Return the masked policy's probability of each legal action
        if policy.training:
            policy.eval()
        with torch.inference_mode():
            inputs = features(state)
            started = perf_counter()
            probabilities, _ = masked_joint_policy(policy, *inputs, layout, [actions])
            result = {action: float(probabilities[0, layout.action_index[action]]) for action in actions}
            record('inference', perf_counter() - started)
            return result

    def value_fn(state):
        # Return the value network's success probability for a nonterminal state
        if value.training:
            value.eval()
        with torch.inference_mode():
            inputs = features(state)
            started = perf_counter()
            result = float(value(*inputs).item())
            record('inference', perf_counter() - started)
            return result

    return prior_fn, value_fn
