"""Greedy: start the ready task with the longest remaining path in its fastest feasible mode; no training or search.

Usage, from the repository root (the same options for every method):
    python -m planner.methods.greedy.greedy_run [--instances all|S|L|ID ...] [--seeds N ...] [--parallel K] [--output results]
Results go to results/runs/<instance>/greedy/seed<seed>/; see planner/runner.py.
"""

from pathlib import Path

from planner.methods.greedy.player import GreedyPlayer
from planner.runner import main, run_method


def contract(group, seed, settings):
    """The method settings frozen with a run: greedy has none."""
    return dict(training=None, evaluation_search=None, ppo=None)


def prepare(project, scenario, group, seed, folder, settings, identity):
    """Greedy needs no training or solving."""
    return None


def make_player(mdp, prepared):
    return GreedyPlayer(mdp)


def run(instances=('all',), seeds=None, parallel=1, output='results'):
    """Run greedy on the test instances (all, S, L or IDs) and seeds (default: the paper's), and evaluate it."""
    run_method('greedy', instances, seeds, parallel, Path(output))


if __name__ == '__main__':
    main('greedy', __doc__)
