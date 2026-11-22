"""CP-SAT: solve the makespan problem on the mean durations with partial dedication, then follow the plan.

Usage, from the repository root (the same options for every method):
    python -m planner.methods.cpsat.cpsat_run [--instances all|S|L|ID ...] [--seeds N ...] [--parallel K] [--output results]
Results go to results/runs/<instance>/cpsat/seed<seed>/; see planner/runner.py.
"""

from pathlib import Path

from dataclasses import asdict

from planner.methods.cpsat.solver import mean_durations, solve_makespan
from planner.methods.fixed_schedules.player import FixedSchedulePlayer
from planner.methods.fixed_schedules.solved import solved_schedule
from planner.runner import main, run_method


def contract(group, seed, settings):
    """The method settings frozen with a run; CP-SAT's time and threads are in the run settings."""
    return dict(training=None, evaluation_search=None, ppo=None)


def prepare(project, scenario, group, seed, folder, settings, identity):
    """Solve once (settings: cpsat_seconds, cpsat_threads) and return the plan."""
    def solve():
        result = solve_makespan(project, mean_durations(project), settings['cpsat_seconds'],
                                seed=seed, threads=settings['cpsat_threads'], dedication='partial')
        if result.plan is None:
            raise RuntimeError(f'{identity}: CP-SAT has no feasible plan ({result.status})')
        return result.plan, asdict(result)
    return solved_schedule(folder, project, solve)


def make_player(mdp, plan):
    return FixedSchedulePlayer(mdp, plan)


def run(instances=('all',), seeds=None, parallel=1, output='results'):
    """Run CP-SAT on the test instances (all, S, L or IDs) and seeds (default: the paper's), and evaluate it."""
    run_method('cpsat', instances, seeds, parallel, Path(output))


if __name__ == '__main__':
    main('cpsat', __doc__)
