"""SA: search task orders and modes with simulated annealing on the mean durations, then follow the best plan.

The search is in planner/methods/sa/search.py, over the schedule encoding in planner/methods/fixed_schedules/encoding.py.

Usage, from the repository root (the same options for every method):
    python -m planner.methods.sa.sa_run [--instances all|S|L|ID ...] [--seeds N ...] [--parallel K] [--output results]
Results go to results/runs/<instance>/sa/seed<seed>/; see planner/runner.py.
"""

from pathlib import Path

from planner.methods.fixed_schedules.encoding import ModeData
from planner.methods.sa.search import solve as search
from planner.methods.fixed_schedules.player import FixedSchedulePlayer
from planner.methods.fixed_schedules.solved import solved_schedule
from planner.runner import main, run_method


def contract(group, seed, settings):
    """The method settings frozen with a run; the schedule budget is in the run settings."""
    return dict(training=None, evaluation_search=None, ppo=None)


def prepare(project, scenario, group, seed, folder, settings, identity):
    """Search with settings['schedule_evaluations'] assessed schedules, resumable from search.pkl; return the plan."""
    def progress(count, best):
        print(f'SEARCH {identity} {count}/{settings["schedule_evaluations"]} best={best}', flush=True)

    def solve():
        return search(ModeData(project), settings['schedule_evaluations'], seed, folder / 'search.pkl', progress)
    return solved_schedule(folder, project, solve)


def make_player(mdp, plan):
    return FixedSchedulePlayer(mdp, plan)


def run(instances=('all',), seeds=None, parallel=1, output='results'):
    """Run SA on the test instances (all, S, L or IDs) and seeds (default: the paper's), and evaluate it."""
    run_method('sa', instances, seeds, parallel, Path(output))


if __name__ == '__main__':
    main('sa', __doc__)
