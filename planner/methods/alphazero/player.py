"""Play an episode's moves with MCTS: one search per decision, exploring for training or greedy for evaluation."""

from __future__ import annotations

from numpy.random import Generator

from planner.core.state import Action, State
from planner.methods.alphazero.mcts import MCTS
from planner.methods.alphazero.mcts.metrics import select_action_with_stats
from planner.core.players import Player


class MCTSPlayer(Player):
    """Choose each move of an episode by a search from the current state; the only caller of MCTS.select_action.

    explore=True samples the move from the visit distribution (training self-play); explore=False plays the
    most-visited move (evaluation). Call start_episode(rng) before each episode: it clears the tree and makes the planner
    use that episode's generator, so each episode's draws depend only on its own generator.
    After act, pi is that search's visit distribution; stats sums the search statistics and decisions counts the
    searches since the player was made.
    """

    def __init__(self, planner: MCTS, explore: bool) -> None:
        self.planner = planner
        self.explore = explore
        self.pi: dict[Action, float] = {}
        self.stats: dict[str, float] = {}
        self.decisions = 0

    def start_episode(self, rng: Generator) -> None:
        """Start a new episode: forget the previous search tree and use rng from now on."""
        self.planner.reset_tree()
        self.planner.rng = rng

    def act(self, state: State, rng: Generator) -> Action:
        """Search from state and return the move."""
        # Search, and add its statistics to the totals
        action, self.pi, stats = select_action_with_stats(self.planner, state)
        for name, number in stats.items():
            self.stats[name] = self.stats.get(name, 0) + number
        self.decisions += 1

        # Training samples the move in proportion to its visits; evaluation keeps the most-visited one
        if self.explore:
            actions = list(self.pi)
            action = actions[int(rng.choice(len(actions), p=[self.pi[a] for a in actions]))]
        return action
