"""Stochastic, neural MCTS inspired by AlphaZero with chance nodes, searching a graph of shared decision nodes.

Used as an online planner to make one decision.
Initialization input: the current state, the MDP, the policy and value networks.
Input per decision (select_action): the current state (state).
Output per decision: the most visited root action and the root visit distribution, (action, pi).
Attributes set by each call:
  - last_root: the finished search tree; the next call reuses its subtree, and search statistics read it (planner/methods/alphazero/mcts/metrics.py).

Hyperparameters (default values in: planner/config.py, DEFAULT_SEARCH_CONFIG):
- c_puct: weight of the exploration bonus in PUCT; higher explores more, 0 is greedy on Q.
- search_budget: simulations at the first searched decision of each day.
- top_up_visits: the day's later searched decisions only top their reused root up to this many visits.
- root_noise_fraction (optional, off by default; training turns it on): how much noise, the share f in
  (1 - f) * P + f * noise at the root; 0 keeps the network's priors.
- root_noise_concentration (used only with root noise): what the noise looks like, Dirichlet alpha = concentration / legal actions;
  small alpha puts the noise on a few random actions, large alpha spreads it evenly;
  dividing by the legal actions keeps it equally spiky whatever their number.
An untried (s, a) has Q = 0, i.e. it counts as a failure until visited.

The search is a graph, not a tree: a state reached by several paths (e.g. two orders of the same assignments) has
one decision node, shared by every chance node that leads to it, so its visits and expansion are shared too.
Each chance node keeps its own N(s, a) and W(s, a), and a simulation backs up only along the path it took
(not Czech et al.'s graph backup). Each search keeps only the nodes reachable from its root.

The graph alternates two kinds of node:
- Decision node (s): a state; its children are the chance nodes (s, a), one per legal action a.
- Chance node (s, a): action a taken in state s; its children are the successor decision nodes s'.
  Durations are random, so one (s, a) can lead to several s', each its own decision node.
  Visit counts and values are kept on both: N(s) and W(s) on s, N(s, a) and W(s, a) on (s, a);
  the prior P(s, a) is kept on (s, a) only.

Per decision (one select_action call), before returning (action, pi):
1. Root: reuse the reached state's subtree (its visits are kept), else start a new graph.
2. Root noise: if root_noise_fraction is on, mix noise into the priors P(s0, a) of the root's chance nodes only.
3. Run the simulations: search_budget at the day's first search, else a top-up to top_up_visits; see below.

Per simulation (one pass from the root down to a leaf and back):
Input: the graph so far, rooted at the observed current state.
Every node in it holds its visit count N and value sum W from earlier simulations,
and every chance node (s, a) also holds its prior P(s, a), fixed when s was expanded.
The simulation grows the graph by at most one leaf and updates N and W along one path.
1. Selection:
   a) Start at the root decision node s.
      The simulator draws fresh hidden durations from the root state at the start of every simulation.
   b) Pick the chance node (s, a) with the highest PUCT score,
      PUCT(s, a) = Q(s, a) + c_puct * P(s, a) * sqrt(1 + N(s)) / (1 + N(s, a)),
      where Q(s, a) = W(s, a) / N(s, a) is the mean backed-up value of (s, a)
      and P(s, a) the policy network's prior for a in s; ties are broken at random.
      Q of an unvisited (s, a) is 0.
   c) Step the simulator with a to get the successor s', i.e. the outcome of (s, a).
   d) Move to the decision node s' under (s, a): the one already in the graph for state s', or a new one.
   e) Repeat b) to d) until reaching a decision node that has not been expanded yet (a leaf)
      or the episode ends.
2. Expansion & Evaluation:
   a) If the episode ended during selection, use the terminal reward; nothing is expanded.
   b) Otherwise give the leaf s one chance node (s, a) per legal action a, set each prior P(s, a) from the policy
      network, normalized over the legal actions, and score the leaf with the value network V(s).
3. Backup:
   a) Add one visit and that same value (undiscounted) to every s and (s, a) on the path.

Structure follows MCTSPlanner from the TDDE78 lab 4 notebook: selection, expansion, evaluation, backup.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
import math
from numbers import Integral
from typing import TypeAlias

from numpy.random import Generator

from planner.core.mdp import MDP
from planner.core.project import Config
from planner.core.simulator import RolloutSimulator
from planner.core.state import Action, State
from planner.config import DEFAULT_SEARCH_CONFIG


PriorFunction: TypeAlias = Callable[[State, Sequence[Action]], dict[Action, float]]
ValueFunction: TypeAlias = Callable[[State], float]


@dataclass(slots=True)
class DecisionNode:
    """A state in the search graph: its chance nodes by action, visit count N(s) and value sum."""

    state: State
    edges: dict[Action, ChanceNode] = field(default_factory=dict)
    expanded: bool = False
    visit_count: int = 0
    value_sum: float = 0.0

    def is_leaf(self) -> bool:
        return not self.expanded


@dataclass(slots=True)
class ChanceNode:
    """An action (s, a): its prior P(s, a), visit count N(s, a), value sum W(s, a), and the decision nodes of the
    states it led to, one per sampled outcome."""

    action: Action
    prior: float
    visit_count: int = 0
    value_sum: float = 0.0
    outcomes: dict[State, DecisionNode] = field(default_factory=dict)

    @property
    def q_value(self) -> float:
        """Mean backed-up value W / N, or 0 before any visit."""
        return self.value_sum / self.visit_count if self.visit_count else 0.0


class MCTS:
    """Choose actions by tree search from the current state.

    last_root is the root of the latest search, kept for tree reuse and for statistics;
    call reset_tree() between episodes.
    """

    def __init__(self, mdp: MDP, prior_fn: PriorFunction, value_fn: ValueFunction, config: Config, rng: Generator) -> None:
        """Store the MDP, network callbacks, search settings, and the RNG used for noise and tie-breaking."""
        self.mdp = mdp
        self.prior_fn = prior_fn
        self.value_fn = value_fn
        self.rng = rng
        self.config = dict(DEFAULT_SEARCH_CONFIG, **config)
        _validate_search_config(self.config)
        self.last_root: DecisionNode | None = None
        self.nodes_by_state: dict[State, DecisionNode] = {}  # Every decision node reachable from the current root.
        self.transposition_hits = 0  # Successors found in the graph under another path, over the planner's lifetime.
        self.search_day: int | None = None  # Day of the latest full search.

    def reset_tree(self) -> None:
        """Forget the previous search graph, e.g. at the start of an episode."""
        self.last_root = None
        self.nodes_by_state.clear()
        self.search_day = None

    def select_action(self, state: State) -> tuple[Action | None, dict[Action, float]]:
        """Search from state and return (most-visited action, root visit distribution).

        Terminal states return (None, {}); a forced move returns its only action without search.
        """
        # Reuse the subtree for this state if there is one, otherwise start a new graph
        root = self._find_or_create_root(state)
        self.last_root = root

        # Check if the state is terminal
        if self.mdp.is_terminal(state):
            return None, {}

        # Check if the move is forced
        actions = self.mdp.legal_actions(state)
        if len(actions) == 1:
            return actions[0], {actions[0]: 1.0}

        # Expand the root and add exploration noise to its priors
        if not root.expanded:
            self.expand(root)
        self.add_root_noise(root)

        # Run the simulations
        for _ in range(self.simulation_budget()):
            self._run_simulation(root)

        # Turn the root visit counts into the search policy
        total = sum(edge.visit_count for edge in root.edges.values())
        pi = {action: edge.visit_count / total for action, edge in root.edges.items()}

        # Pick the most visited action; on equal visits, the one the policy network prefers
        best = max(root.edges.values(), key=lambda edge: (edge.visit_count, edge.prior))
        return best.action, pi

    def _find_or_create_root(self, state: State) -> DecisionNode:
        """Return the previous graph's node for state when the state was reached, else a new node."""
        # Look for the state among the outcomes of the previous root's actions
        # A reused root keeps its earlier visits and gets the full budget on top
        root = None
        if self.last_root is not None:
            for edge in self.last_root.edges.values():
                if state in edge.outcomes:
                    root = edge.outcomes[state]
                    break

        # Not found: start a new graph
        if root is None:
            root = DecisionNode(state)

        # Keep only the nodes reachable from the root, so states left behind are not reused
        reachable = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node.state in reachable:
                continue
            reachable[node.state] = node
            stack.extend(child for edge in node.edges.values() for child in edge.outcomes.values())
        self.nodes_by_state = reachable
        return root

    def _run_simulation(self, root: DecisionNode) -> None:
        """Run one simulation: select down the graph, expand the leaf, evaluate it, and back up the value."""
        # Each simulation samples fresh hidden durations from the observed root state
        simulator = RolloutSimulator(self.mdp, root.state, self.rng)
        node = root
        nodes = [root]
        edges = []
        done = False

        # 1. Selection: PUCT picks the action; at its chance node the simulator picks the outcome
        while not node.is_leaf():
            edge = self._select_action_by_puct(node)
            successor, reward, done = simulator.step(edge.action)
            edges.append(edge)
            if done:
                break
            node = self._successor_node(edge, successor)
            nodes.append(node)

        # 2. Expansion and 3. evaluation; a terminal step uses its reward instead of the network
        if done:
            value = reward
        else:
            self.expand(node)
            value = self.value_fn(node.state)

        # 4. Backup
        self.backpropagate(nodes, edges, value)

    def _successor_node(self, edge: ChanceNode, state: State) -> DecisionNode:
        """Return the decision node for state under edge, sharing the graph's node for state if there is one."""
        if state not in edge.outcomes:
            node = self.nodes_by_state.get(state)
            if node is None:
                node = self.nodes_by_state[state] = DecisionNode(state)
            else:
                self.transposition_hits += 1
            edge.outcomes[state] = node
        return edge.outcomes[state]

    def _select_action_by_puct(self, node: DecisionNode) -> ChanceNode:
        """Return the edge of the action with the highest PUCT score, breaking ties at random."""
        edges = list(node.edges.values())
        scores = [self.puct_score(node, edge) for edge in edges]
        best = max(scores)
        candidates = [edge for edge, score in zip(edges, scores) if score == best]
        return candidates[int(self.rng.integers(len(candidates)))]

    def puct_score(self, node: DecisionNode, edge: ChanceNode) -> float:
        """Return Q + c_puct * P * sqrt(1 + N_parent) / (1 + N_edge); an untried action has Q = 0."""
        exploration_bonus = self.config['c_puct'] * edge.prior * math.sqrt(1 + node.visit_count) / (1 + edge.visit_count)
        q_value = edge.q_value if edge.visit_count else 0.0
        return q_value + exploration_bonus

    def expand(self, node: DecisionNode) -> None:
        """Add an edge for every legal action, with the policy network's priors normalized over them."""
        actions = self.mdp.legal_actions(node.state)
        priors = self.prior_fn(node.state, actions)
        total = sum(priors[action] for action in actions)
        node.edges = {action: ChanceNode(action, priors[action] / total) for action in actions}
        node.expanded = True

    def add_root_noise(self, root: DecisionNode) -> None:
        """Mix root priors with Dirichlet noise: (1 - f) * P + f * noise, alpha = concentration / k."""
        # Skip when noise is off or there is nothing to choose between
        fraction = self.config['root_noise_fraction']
        action_count = len(root.edges)
        if fraction == 0 or action_count <= 1:
            return

        # Draw the noise and mix it into the priors
        alpha = self.config['root_noise_concentration'] / action_count
        noise = self.rng.dirichlet([alpha] * action_count)
        for edge, probability in zip(root.edges.values(), noise):
            edge.prior = (1 - fraction) * edge.prior + fraction * float(probability)

    def simulation_budget(self) -> int:
        """Return the number of simulations for the current root (last_root).

        A day's first search runs search_budget simulations; its later searches only top the root up to top_up_visits.
        """
        root = self.last_root
        # A forced move runs no search, so the day's first search can come after one
        if self.search_day == root.state.day:
            return max(0, self.config['top_up_visits'] - root.visit_count)
        self.search_day = root.state.day
        return self.config['search_budget']

    def backpropagate(self, nodes: Sequence[DecisionNode], edges: Sequence[ChanceNode], value: float) -> None:
        """Add one visit and the same undiscounted value to every node and edge on the path."""
        for item in (*nodes, *edges):
            item.visit_count += 1
            item.value_sum += value


def _validate_search_config(config: Config) -> None:
    """Check a positive integer budget, c_puct >= 0, a noise fraction in [0, 1], positive concentration, and the top-up."""
    # Check the budget
    budget = config['search_budget']
    if not isinstance(budget, Integral) or budget < 1:
        raise ValueError('search_budget must be a positive integer')

    # Check the exploration settings
    if not math.isfinite(config['c_puct']) or config['c_puct'] < 0:
        raise ValueError('c_puct must be finite and nonnegative')
    fraction = config['root_noise_fraction']
    concentration = config['root_noise_concentration']
    if not math.isfinite(fraction) or not 0 <= fraction <= 1:
        raise ValueError('root_noise_fraction must be finite and in [0,1]')
    if not math.isfinite(concentration) or concentration <= 0:
        raise ValueError('root_noise_concentration must be finite and positive')

    # Check the top-up of a day's later searches
    top_up = config['top_up_visits']
    if not isinstance(top_up, Integral) or isinstance(top_up, bool) or top_up < 0:
        raise ValueError('top_up_visits must be a nonnegative integer')
