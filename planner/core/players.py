"""Players: choose the move to play in a state, for an episode run by run_episode (planner/core/simulator.py).

Every player subclasses Player: act(state, rng) returns the move, and start_episode(rng) is called before each
episode (a no-op unless the player keeps state across moves, like MCTSPlayer). Here: RandomPlayer (it sets the
ranked reward's first bar).
The methods' players are in planner/methods (e.g. GreedyPlayer, MCTSPlayer, FixedSchedulePlayer).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from numpy.random import Generator

from planner.core.state import STOP, Action, State

if TYPE_CHECKING:
    from planner.core.mdp import MDP


class Player(ABC):
    """Chooses one move per call; an episode calls start_episode once, then act at every decision."""

    def start_episode(self, rng: Generator) -> None:
        """Prepare for a new episode played with rng; players without state across moves need nothing."""

    @abstractmethod
    def act(self, state: State, rng: Generator) -> Action:
        """Return the move to play in state."""


class RandomPlayer(Player):
    """Take a uniformly random legal START(task, mode); STOP only when none is legal."""

    def __init__(self, mdp: MDP) -> None:
        self.mdp = mdp

    def act(self, state: State, rng: Generator) -> Action:
        # Take a random legal start if any; otherwise wait for a completion
        starts = [action for action in self.mdp.legal_actions(state) if action != STOP]
        if starts:
            return starts[int(rng.integers(len(starts)))]
        return STOP
