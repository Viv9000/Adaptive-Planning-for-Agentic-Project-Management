"""Run a method on a set of instances and evaluate it on the shared futures.

Every method module (planner/methods/<method>/<method>_run.py) has run(), runnable as
python -m planner.methods.<method>.<method>_run, and the same three functions:
- contract(group, seed, settings): the method settings frozen with a run;
- prepare(project, scenario, group, seed, folder, settings, identity): train or solve, resuming saved state;
- make_player(mdp, prepared): the player that executes a project.
Each (instance, seed) writes <output>/runs/<instance>/<method>/seed<seed>/: the frozen settings (contract.json), the
training or solve record, the evaluation on the shared futures (evaluation.json) and the compute record.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
import hashlib
import importlib
from pathlib import Path

import torch

from planner.config import CPSAT_SECONDS, CPSAT_THREADS, EVALUATION_FUTURES, SCHEDULE_EVALUATIONS, SEEDS
from planner.core.artifacts import frozen, read
from planner.core.scenario_file import load_project
from planner.evaluate.compute import measure_search
from planner.evaluate.paired import evaluate

METHODS = ('alphazero', 'ppo', 'ga', 'sa', 'cpsat', 'greedy')
DATA = Path(__file__).resolve().parents[1] / 'dataset' / 'test_instances'
SCHEMA = 1


def method_module(method):
    """Return planner.methods.<method>.<method>_run."""
    return importlib.import_module(f'planner.methods.{method}.{method}_run')


def settings():
    """The paper's run settings: evaluation futures, GA and SA budget, CP-SAT time and threads."""
    return dict(futures=len(EVALUATION_FUTURES), schedule_evaluations=SCHEDULE_EVALUATIONS,
                cpsat_seconds=CPSAT_SECONDS, cpsat_threads=CPSAT_THREADS)


def instances(selection):
    """Return (group, instance) for the selected frozen test instances: all, S, L, or instance IDs."""
    chosen = [(path.parent.name, path.name) for path in sorted(DATA.glob('*/*')) if path.is_dir()]
    if selection not in (['all'], ['S'], ['L']):
        unknown = set(selection) - {instance for _, instance in chosen}
        if unknown:
            raise SystemExit(f'Unknown test instances: {sorted(unknown)}')
    return [(group, instance) for group, instance in chosen
            if selection == ['all'] or selection == [group] or instance in selection]


def run(job):
    """Prepare one method on one instance and seed, then evaluate it; a finished run is read back, not rerun."""
    method, group, instance, seed, output, run_settings = job
    torch.set_num_threads(1)
    # Load the frozen instance, refusing a scenario file that changed
    folder = DATA / group / instance
    record = read(folder / 'instance.json')
    scenario = folder / record['scenario']
    if hashlib.sha256(scenario.read_bytes()).hexdigest() != record['scenario_sha256']:
        raise ValueError(f'{instance}: the frozen scenario changed')
    project = load_project(scenario)
    root = Path(output) / 'runs' / instance / method / f'seed{seed}'
    root.mkdir(parents=True, exist_ok=True)
    module = method_module(method)
    identity = f'{instance}/{method}/seed{seed}'
    # Freeze the run's settings: a rerun into the same folder with other settings is refused
    frozen(root / 'contract.json', dict(schema=SCHEMA, instance=instance, group=group, method=method, seed=seed,
                                      scenario_sha256=record['scenario_sha256'], settings=run_settings,
                                      **module.contract(group, seed, run_settings)))
    if (root / 'evaluation.json').exists():
        # Finished earlier: read the result back
        return identity, read(root / 'evaluation.json')['summary']
    # Train or solve, then evaluate on the shared futures, recording the time of this session
    with measure_search(root / 'compute_sessions.jsonl') as compute:
        prepared = module.prepare(project, scenario, group, seed, root, run_settings, identity)
        compute['phase'] = 'evaluation'
        summary = evaluate(project, lambda mdp: module.make_player(mdp, prepared), root / 'evaluation.json',
                           run_settings['futures'], identity)
    return identity, summary


def run_method(method, selection=('all',), seeds=None, parallel=1, output=Path('results')):
    """Run a method on the selected instances and seeds (default: the paper's), parallel runs at once."""
    run_settings = settings()
    # Start the larger instances first, so the last runs to finish are short ones.
    chosen = sorted(instances(list(selection)), key=lambda item: (item[0] != 'L', item[1]))
    jobs = [(method, group, instance, seed, str(output), run_settings)
            for group, instance in chosen for seed in (seeds or SEEDS[method])]
    with ProcessPoolExecutor(max_workers=parallel) as pool:
        for identity, summary in pool.map(run, jobs):
            print(identity, f"on time {summary['on_time']:.3f}", flush=True)


def main(method, description=None):
    """The command line of every method module (python -m planner.methods.<method>.<method>_run)."""
    parser = argparse.ArgumentParser(description=description or __doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--instances', nargs='+', default=['all'], help='all, S, L, or test instance IDs')
    parser.add_argument('--seeds', nargs='+', type=int, help="Default: the paper's seeds of the method")
    parser.add_argument('--parallel', type=int, default=1,
                        help='Runs at once; each uses one CPU thread, a CP-SAT run eight')
    parser.add_argument('--output', type=Path, default=Path('results'))
    args = parser.parse_args()
    if args.parallel < 1:
        parser.error('--parallel must be positive')
    run_method(method, args.instances, args.seeds, args.parallel, args.output)
