"""Generate test instances from MSLIB instance files: generator.py turns each into a project with explicit modes and
PERT durations, and its deadline is 1.25 times the makespan of a CP-SAT schedule on the mean durations (five minutes,
eight threads, full dedication).

Usage, from the repository root:
    python -m dataset.generator.generate MSLIB_FILE [MSLIB_FILE ...] --output DIR [--parallel N]
Writes DIR/<MSLIB instance>/: the scenario file and instance.json (deadline, reference schedule, settings).
The CP-SAT search is not deterministic across machines, so deadlines can differ from the frozen instances'; reproduce
the paper's results with dataset/test_instances.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict
import hashlib
from pathlib import Path

from dataset.generator.generator import GeneratorSettings, generate, with_deadline
from dataset.generator.mslib import parse_msrcp
from planner.core.artifacts import write_json
from planner.core.scenario_file import write_scenario
from planner.methods.cpsat.solver import mean_durations, solve_makespan

# The paper's settings: the generator with doubled duration uncertainty, and the deadline reference.
GENERATOR = GeneratorSettings(uncertainty=2.0)
DEADLINE_FACTOR = 1.25
REFERENCE = dict(deadline_reference='full', reference_seconds=300, solver_threads=8)


def generate_instance(source, output):
    """Generate one instance from an MSLIB file into output/<MSLIB instance>/ and return its instance.json path."""
    instance = parse_msrcp(source)
    root = Path(output) / instance.instance_id
    if (root / 'instance.json').exists():
        return root / 'instance.json'
    root.mkdir(parents=True, exist_ok=True)
    generated = generate(instance, GENERATOR)
    reference = solve_makespan(generated.project, mean_durations(generated.project), REFERENCE['reference_seconds'],
                               seed=2026, threads=REFERENCE['solver_threads'], dedication=REFERENCE['deadline_reference'])
    if reference.plan is None:
        raise RuntimeError(f'{instance.instance_id}: no deadline-reference plan: {reference.status}')
    project = with_deadline(generated.project, DEADLINE_FACTOR, reference.plan.completion)
    scenario = write_scenario(project, root, generation_config=generated.configuration() | dict(
        deadline_factor=DEADLINE_FACTOR, reference_makespan=reference.plan.completion,
        deadline_reference_dedication=REFERENCE['deadline_reference']))
    write_json(root / 'instance.json', dict(
        instance=instance.instance_id, scenario=scenario.name,
        scenario_sha256=hashlib.sha256(scenario.read_bytes()).hexdigest(), deadline=project.deadline.delta,
        reference=asdict(reference), settings=dict(REFERENCE, generator=asdict(GENERATOR))))
    return root / 'instance.json'


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('sources', nargs='+', type=Path, help='MSLIB instance files (.msrcp)')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--parallel', type=int, default=1, help='Instances at once, eight CP-SAT threads each')
    args = parser.parse_args()
    with ProcessPoolExecutor(max_workers=args.parallel) as pool:
        for path in pool.map(generate_instance, args.sources, [args.output] * len(args.sources)):
            print(path, flush=True)


if __name__ == '__main__':
    main()
