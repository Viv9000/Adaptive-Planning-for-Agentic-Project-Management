"""LLM-generated policies: generate them through a model API, then run them on the test instances.

Two policy types: general (one per instance set, S or L) and instance-specific. Stages, each run separately:
    prepare   prompts and generation jobs in results/llm (no API calls)
    generate  call the model APIs up to a dollar cap, three policies per prompt: OpenAI (set OPENAI_API_KEY) for
              Sol, Luna and Astra; Amazon Bedrock (AWS credentials, --profile, --region) for DeepSeek V3.2 and Kimi K3.1
    evaluate  run every policy in its own process on its instances and the 500 shared futures
    report    count the generations and evaluations

Usage, from the repository root:
    python -m planner.methods.llm.llm_run --stage prepare [--instances all|S|L|ID ...]
    python -m planner.methods.llm.llm_run --stage generate --models sol --execute-paid --api-cap 100 --max-hours 4
    python -m planner.methods.llm.llm_run --stage evaluate --models sol [--instances ...] [--seeds 0 1 2] --parallel 8
New generations give new policies, so their results differ from the paper's.
"""

from pathlib import Path

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import json
import os

import torch

from planner.core.artifacts import frozen, read, write_json
from planner.methods.llm.settings import HERE, LIMITS, MODELS, OUTPUT, ROOT, canonical, digest, file_hash, implementation_hash
from planner.methods.llm.generation import generate
from planner.methods.llm.observation import project_data
from planner.core.scenario_file import load_project
from planner.evaluate.paired import evaluate
from planner.methods.llm.player import LLMPlayer


def inventory(selection=('all',)):
    """The selected test instances: all, S, L, or instance IDs."""
    number = lambda folder: int(folder.name.rsplit('_', 1)[1])
    chosen = [dict(group=group, instance=folder.name) for group in ('S', 'L')
              for folder in sorted((ROOT / 'dataset' / 'test_instances' / group).iterdir(), key=number)]
    selection = list(selection)
    if selection not in (['all'], ['S'], ['L']):
        unknown = set(selection) - {item['instance'] for item in chosen}
        if unknown:
            raise SystemExit(f'Unknown test instances: {sorted(unknown)}')
    return [item for item in chosen if selection == ['all'] or selection == [item['group']] or item['instance'] in selection]


def token_audit(prompt, model, max_output):
    """Check that a prompt plus the longest reply fits the model's context, bounding tokens by the prompt's UTF-8
    bytes plus 4096; a prompt that may not fit is not sent."""
    byte_bound = len(prompt.encode()) + 4096
    result = dict(utf8_bytes=len(prompt.encode()), input_upper_bound=byte_bound,
                  context_limit=MODELS[model]['context'], max_output_tokens=max_output,
                  method='UTF-8 byte bound plus 4096 framing tokens')
    try:
        import tiktoken
        result['approx_o200k_tokens'] = len(tiktoken.get_encoding('o200k_base').encode(prompt))
    except Exception:
        result['approx_o200k_tokens'] = None
    result['context_certified'] = result['input_upper_bound'] + max_output <= result['context_limit']
    return result


def prepare(args):
    """Write the prompts, the jobs (model x prompt x replicate) and the copied scenarios to --output; no API calls.

    Prompts: shared.txt plus general.txt for each set, or plus individual.txt with the project's tables for each
    instance. The contract is frozen once generation or evaluation has started.
    """
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    shared = (HERE / 'prompts' / 'shared.txt').read_text()
    selected = inventory(args.instances)
    if args.instances == ['all'] and len({r['instance'] for r in selected}) != 120:
        raise ValueError('Expected the frozen 60 S + 60 L test instances')
    contract = dict(
        schema=1, implementation_hash=implementation_hash(), models=MODELS, limits=LIMITS,
        instances=selected, generation_replicates=[0, 1, 2], samples=500,
        openai_reasoning='medium',
        corrective_generations=0, fallback='existing GreedyPlayer for each failed nonforced selection',
        general_examples='synthetic schema example only; no test project in generation prompt')
    # Draft preparation can be refreshed until any execution artifact exists.
    executing = (root / 'ledger.json').exists() or (root / 'evaluation').exists()
    if executing:
        frozen(root / 'contract.json', contract)
    else:
        write_json(root / 'contract.json', contract)
    records, missing = [], []
    for item in selected:
        path = args.final_root / item['group'] / item['instance'] / 'instance.json'
        if not path.exists():
            missing.append(item['instance'])
            continue
        record = read(path)
        if record['group'] != item['group'] or record['instance'] != item['instance']:
            raise ValueError(f'Unexpected dataset identity: {path}')
        scenario = Path(record['scenario'])
        if not scenario.exists():
            scenario = path.parent / scenario.name
        if not scenario.exists() or file_hash(scenario) != record['scenario_sha256']:
            raise ValueError(f'Missing or changed final scenario: {path}')
        relative_scenario = f'scenarios/{item["instance"]}.md'
        target = root / relative_scenario
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and target.read_bytes() != scenario.read_bytes():
            raise ValueError('Saved scenario differs; choose a new output directory')
        target.write_bytes(scenario.read_bytes())
        records.append(record | {'scenario': relative_scenario})
    record_map = {record['instance']: record for record in records}
    project_cache = {}
    jobs, audits = [], []
    scopes = [('general', group, group) for group in ('S', 'L')]
    scopes += [('individual', item['instance'], item['group']) for item in selected]
    for arm, scope, group in scopes:
        if arm == 'general':
            prompt = shared + '\n' + (HERE / 'prompts' / 'general.txt').read_text().format(group=group)
        elif scope in record_map:
            record = record_map[scope]
            project_cache[scope] = project_data(load_project(root / record['scenario']))
            prompt = shared + '\n' + (HERE / 'prompts' / 'individual.txt').read_text().replace(
                '{project}', canonical(project_cache[scope]))
        else:
            prompt = None
        relative = f'prompts/{arm}/{scope}.txt'
        if prompt is not None:
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and destination.read_text() != prompt:
                raise ValueError('Existing prompt differs; choose a new output directory')
            destination.write_text(prompt)
        for model in MODELS:
            max_output = MODELS[model]['max_output_tokens']
            audit = token_audit(prompt, model, max_output) if prompt else {
                'context_certified': False, 'reason': 'final scenario has not been materialized'}
            audits.append(dict(arm=arm, scope=scope, model=model, **audit))
            for replicate in range(3):
                job = dict(id=f'{model}/{arm}/{scope}/rep{replicate}', model=model, arm=arm,
                           scope=scope, group=group, replicate=replicate,
                           max_output_tokens=max_output, prompt_path=relative,
                           prompt_hash=digest(prompt) if prompt else None,
                           context_certified=audit['context_certified'])
                jobs.append(job)
    for name, value in [('projects.json', records), ('jobs.json', jobs)]:
        if executing:
            frozen(root / name, value)
        else:
            write_json(root / name, value)
    write_json(root / 'prompt_audit.json', audits)
    write_json(root / 'readiness.json', dict(jobs=len(jobs), ready=sum(j['context_certified'] for j in jobs),
                                       missing_final_scenarios=missing, api_calls_made=0,
                                       generation_api_cap='required explicitly at paid launch'))
    print(json.dumps(read(root / 'readiness.json'), indent=2))


def evaluate_policy(arguments, samples=500):
    """Evaluate one generated policy (job) on one instance (record) on the shared futures; return the result folder.

    Writes <root>/evaluation/<job>/<instance>/: contract.json (frozen), evaluation.json (each episode, with its
    fallbacks) and summary.json (on-time rate, fallback rate over the non-forced decisions, decision counters).
    """
    root, job, record = Path(arguments[0]), arguments[1], arguments[2]
    # One CPU thread per evaluation, as for every method (the observation features use torch)
    torch.set_num_threads(1)
    scenario = root / record['scenario']
    if file_hash(scenario) != record['scenario_sha256']:
        raise ValueError('Scenario differs from its frozen final-evaluation record')
    # The generated program, unless generation failed (then every decision falls back to greedy)
    program = root / 'programs' / job['id']
    generation = read(program / 'generation.json')
    source = None
    if generation['status'] == 'ready':
        source = (program / 'policy.py').read_text()
        if digest(source) != generation['source_hash']:
            raise ValueError('Generated source changed')
    # Freeze what this evaluation depends on, including the code (implementation_hash)
    directory = root / 'evaluation' / job['id'] / record['instance']
    frozen(directory / 'contract.json', dict(job=job, scenario_sha256=record['scenario_sha256'], generation=generation,
                                             implementation_hash=implementation_hash(), limits=LIMITS, samples=samples))
    if (directory / 'summary.json').exists():
        return str(directory)
    evaluate(load_project(scenario), lambda mdp: LLMPlayer(mdp, source), directory / 'evaluation.json', samples,
             f"{job['id']}/{record['instance']}")
    # Summarize: on-time rate, and fallback rate over the non-forced decisions
    rows = read(directory / 'evaluation.json')['episodes']
    totals = Counter()
    for row in rows:
        totals.update(row['counters'])
    write_json(directory / 'summary.json', dict(
        episodes=len(rows), on_time=sum(row['success'] for row in rows) / len(rows),
        mean_completion=sum(row['completion'] for row in rows) / len(rows),
        episodes_with_fallback=sum(bool(row['failures']) for row in rows), counters=dict(totals),
        fallback_rate=totals['fallbacks'] / max(1, totals['nonforced']),
        build_attempts=sum(len(row['builds']) for row in rows), generation_status=generation['status']))
    return str(directory)


def main(description=None):
    parser = argparse.ArgumentParser(description=description or __doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--stage', choices=('inventory', 'prepare', 'generate', 'evaluate', 'report'), default='inventory')
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--final-root', type=Path, default=ROOT / 'dataset' / 'test_instances', help='The frozen test instances')
    parser.add_argument('--instances', nargs='+', default=['all'], help='all, S, L, or test instance IDs')
    parser.add_argument('--seeds', nargs='+', type=int, default=[0, 1, 2], help='Generation replicates (0-2)')
    parser.add_argument('--models', nargs='+', choices=MODELS, default=list(MODELS))
    parser.add_argument('--arms', nargs='+', choices=('general', 'individual'), default=['general', 'individual'])
    parser.add_argument('--parallel', type=int, default=1, help='Requests or evaluations at once')
    parser.add_argument('--profile', help='AWS profile for the Bedrock models (default: the standard credentials)')
    parser.add_argument('--region', default='ap-southeast-2', help="AWS region of the Bedrock models (the paper's)")
    parser.add_argument('--api-cap', type=float, help='Explicit approved USD generation reservation ceiling')
    parser.add_argument('--max-hours', type=float, help='Time limit of the generate stage')
    parser.add_argument('--execute-paid', action='store_true', help='Explicitly authorize the generate stage')
    args = parser.parse_args()
    if args.parallel < 1:
        parser.error('--parallel must be positive')
    if args.stage == 'inventory':
        instances = inventory(args.instances)
        print(json.dumps(dict(instances=instances, models=MODELS, limits=LIMITS,
                              generation_jobs=(len(instances) + 2) * len(MODELS) * 3,
                              evaluation_episodes=len(instances) * 2 * len(MODELS) * 3 * 500,
                              status='preparation only; no APIs, no scenario generation'), indent=2))
        return
    if args.stage == 'prepare':
        prepare(args)
        return
    if args.stage == 'report':
        ledger = read(args.output / 'ledger.json') if (args.output / 'ledger.json').exists() else {}
        summaries = list((args.output / 'evaluation').rglob('summary.json'))
        print(json.dumps(dict(api_requests=len(ledger),
                              api_charge_upper_bound_usd=sum(r['charge_bound_usd'] for r in ledger.values()),
                              completed_policy_project_evaluations=len(summaries)), indent=2))
        return
    # generate and evaluate: refuse to run if the code changed since prepare
    jobs = [j for j in read(args.output / 'jobs.json')
            if j['model'] in args.models and j['arm'] in args.arms and j['replicate'] in args.seeds]
    if read(args.output / 'contract.json')['implementation_hash'] != implementation_hash():
        parser.error('Implementation changed since preparation; refresh the draft or choose a new output directory')
    if args.stage == 'generate':
        if args.max_hours is None or args.max_hours <= 0:
            parser.error('A positive --max-hours is required')
        if not args.execute_paid or args.api_cap is None or args.api_cap <= 0:
            parser.error('Paid generation requires --execute-paid and an explicit positive --api-cap')
        if any(not j['context_certified'] for j in jobs):
            parser.error('Selected batch contains blocked prompts; inspect prompt_audit.json')
        generate(args.output, jobs, parallel=args.parallel, api_cap=args.api_cap,
                 max_hours=args.max_hours, profile=args.profile, region=args.region)
    else:
        selected = {item['instance'] for item in inventory(args.instances)}
        records = [record for record in read(args.output / 'projects.json') if record['instance'] in selected]
        if not records:
            parser.error('None of the selected instances was prepared')
        # A general policy runs on every instance of its set, an instance-specific one on its instance
        tasks = [(str(args.output.resolve()), job, record) for job in jobs for record in records
                 if (job['arm'] == 'general' and job['group'] == record['group'])
                 or (job['arm'] == 'individual' and job['scope'] == record['instance'])]
        if any(not (args.output / 'programs' / job['id'] / 'generation.json').exists()
               for _, job, _ in tasks):
            parser.error('Missing completed generation; unresolved API requests are not heuristic failures')
        # Numerical libraries must use one thread inside every evaluation process.
        for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
            os.environ[name] = '1'
        with ProcessPoolExecutor(max_workers=args.parallel) as pool:
            for directory in pool.map(evaluate_policy, tasks):
                print(directory, flush=True)


if __name__ == '__main__':
    main()
