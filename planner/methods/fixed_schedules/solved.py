"""Solve a fixed schedule once per run and keep it in the run folder's solve.json."""

from dataclasses import asdict
from time import perf_counter

from planner.core.artifacts import read, write_json
from planner.methods.cpsat.solver import ModeSchedule, check_schedule, mean_durations


def solved_schedule(folder, project, solve):
    """Return the run's checked plan; solve() -> (plan, statistics) runs only if solve.json does not exist yet."""
    path = folder / 'solve.json'
    # Solve, check and save, unless an earlier run of this folder already did
    if not path.exists():
        started = perf_counter()
        plan, statistics = solve()
        check_schedule(project, mean_durations(project), plan, dedication='partial')
        write_json(path, dict(plan=asdict(plan), statistics=statistics, seconds=perf_counter() - started))
    # Always load the saved schedule, so a fresh and a resumed run play the same one
    plan = ModeSchedule(**read(path)['plan'])
    check_schedule(project, mean_durations(project), plan, dedication='partial')
    return plan
