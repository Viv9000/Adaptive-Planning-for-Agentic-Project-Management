"""Self-play episodes that produce training samples."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TypeAlias

from numpy.random import Generator
from torch import Tensor

from planner.core.mdp import MDP
from planner.core.simulator import run_episode
from planner.core.state import Action, State
from planner.methods.alphazero.mcts import MCTS
from planner.network.encoding import NeuralLayout, policy_to_tensor
from planner.methods.alphazero.player import MCTSPlayer

# (state, policy target over the action catalogue, episode return)
TrainingSample: TypeAlias = tuple[State, Tensor, float]


def play_episode(
    mdp: MDP, choose: Callable[[State], tuple[Action, Mapping[Action, float]]], layout: NeuralLayout, rng: Generator,
) -> tuple[list[TrainingSample], State]:
    """Play one episode from the start and return its samples and terminal state.

    choose(state) returns (action, policy target); every sample's value target is the episode's terminal return.
    """
    # Play until the episode ends, storing each state with its policy target
    trajectory = []

    def act(state):
        action, pi = choose(state)
        # Convert the policy to a tensor once here rather than every time the replay buffer draws it; states stay raw for the update's legal masks.
        trajectory.append((state, policy_to_tensor(pi, layout)))
        return action

    terminal = run_episode(mdp, mdp.reset(), act, rng)

    # Give every sample the episode's terminal return as its value target
    outcome = mdp.terminal_return(terminal)
    return [(state, target, outcome) for state, target in trajectory], terminal


def generate_episode(
    mdp: MDP, planner: MCTS, layout: NeuralLayout, rng: Generator,
) -> tuple[list[TrainingSample], State, dict[str, float]]:
    """Play one self-play episode, sampling each action from the MCTS visit distribution.

    Returns the samples, the terminal state, and the search metrics summed over the episode's decisions.
    """
    player = MCTSPlayer(planner, explore=True)
    player.start_episode(rng)

    def choose(state):
        # Search, then sample the move from the root visit distribution, which is also the policy target
        action = player.act(state, rng)
        return action, player.pi

    samples, terminal = play_episode(mdp, choose, layout, rng)
    return samples, terminal, player.stats
