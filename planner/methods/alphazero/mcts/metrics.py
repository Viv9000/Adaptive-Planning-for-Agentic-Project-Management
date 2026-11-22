"""Search statistics, measured around MCTS.select_action; the search itself records nothing."""

from __future__ import annotations

import math
from time import perf_counter

from planner.core.state import Action, State
from planner.methods.alphazero.mcts.search import DecisionNode, MCTS

# Statistics that are summed over an episode's decisions and reported as their mean per decision
PER_DECISION_MEANS = ('root_action_coverage', 'root_prior_entropy', 'root_visit_entropy', 'root_value')


def select_action_with_stats(planner: MCTS, state: State) -> tuple[Action | None, dict[Action, float], dict[str, float]]:
    """Run planner.select_action and return (action, visit distribution, statistics of that search)."""
    started = perf_counter()
    hits_before = planner.transposition_hits
    action, pi = planner.select_action(state)
    stats = compute_tree_stats(planner.last_root)
    stats['transposition_hits'] = planner.transposition_hits - hits_before
    stats['search_seconds'] = perf_counter() - started
    return action, pi, stats


def compute_tree_stats(root: DecisionNode) -> dict[str, float]:
    """Return the root's visits, the share of legal root actions visited, and the number of decision nodes."""
    # Count the decision nodes in the graph, each shared node once
    nodes = 0
    seen = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if id(node) in seen:
            continue
        seen.add(id(node))
        nodes += 1
        stack.extend(child for edge in node.edges.values() for child in edge.outcomes.values())

    # Measure root coverage; a forced move is not searched, so its one action counts as covered
    coverage = 1.0
    if root.edges:
        coverage = sum(edge.visit_count > 0 for edge in root.edges.values()) / len(root.edges)

    # Signs of a collapsing search: the entropy (nats) of the root's priors (with any root noise) and of its visits,
    # and the root's mean backed-up value; a forced move counts as zero entropy and its parent's value is unknown, 0
    priors = [edge.prior for edge in root.edges.values() if edge.prior > 0]
    total = sum(edge.visit_count for edge in root.edges.values())
    visits = [edge.visit_count / total for edge in root.edges.values() if edge.visit_count > 0] if total else []
    entropy = lambda probabilities: -sum(p * math.log(p) for p in probabilities)
    return {'root_visits': root.visit_count, 'root_action_coverage': coverage, 'nodes': nodes,
            'root_prior_entropy': entropy(priors), 'root_visit_entropy': entropy(visits),
            'root_value': root.value_sum / root.visit_count if root.visit_count else 0.0}
