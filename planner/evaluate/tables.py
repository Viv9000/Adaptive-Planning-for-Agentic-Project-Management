"""Rebuild the paper's two result tables from the per-run result files.

Usage: python -m planner.evaluate.tables --results DIR [DIR ...] [--llm DIR ...]

--results folders hold runs/<instance>/<method>/seed<seed>/ as written by planner.runner; --llm folders hold the LLM
method's ledger.json (generation) and evaluation/ (evaluation) as written by planner.methods.llm.llm_run. When a run
appears in several folders, the last folder given wins.

Each number is averaged over a method's seeds (or generated policies) per instance, then over the instances of a set (S or L):
- on time: the share of the 500 shared futures finished by the deadline;
- preparation: the CPU hours of one optimization or training run (wall time times threads): CP-SAT's solve times its
  threads, GA's and SA's solve, the AlphaZero-based method's training episodes and updates, PPO's training, and for
  the LLM the wall time of the API call that generated a policy; greedy needs none;
- decision: the wall time to execute one project, summed over its decisions;
- failure (LLM): the share of non-forced decisions whose policy returned no legal action in time (greedy fallback);
- cost (LLM): the US dollars of one generation at list prices.
"""

import argparse
from collections import defaultdict
import json
from pathlib import Path
import statistics

from planner.config import CPSAT_THREADS

DATA = Path(__file__).resolve().parents[2] / 'dataset' / 'test_instances'
GROUP = {path.name: path.parent.name for path in DATA.glob('*/*') if path.is_dir()}
METHODS = {'cpsat': 'CP-SAT', 'ga': 'GA', 'sa': 'SA', 'greedy': 'Greedy', 'llm': 'LLM (Sol)', 'ppo': 'PPO',
           'alphazero': 'AlphaZero-based'}
# The paper's raw result files name the AlphaZero-based method asap_current.
ALIASES = {'asap_current': 'alphazero'}
MODELS = {'sol': 'Sol', 'luna': 'Luna', 'astra': 'Astra', 'kimik31': 'Kimi K3.1', 'deepseek': 'DeepSeek V3.2'}
# List prices in US dollars per million input and output tokens (November 2026); other models use the ledger's charge.
LIST_PRICES = {'sol': (2.0, 10.0), 'luna': (0.1, 0.5), 'deepseek': (0.6386, 1.9055), 'kimik31': (3.3, 16.5)}


def read(path):
    return json.loads(Path(path).read_text())


def run_numbers(method, folder):
    """Return (on time, preparation hours, decision seconds) of one run folder."""
    evaluation = read(folder / 'evaluation.json')
    episodes = evaluation['episodes']
    decision = statistics.mean(row['seconds'] for row in episodes)
    if method in ('cpsat', 'ga', 'sa'):
        settings = read(folder / 'contract.json').get('settings', {})
        threads = settings.get('cpsat_threads', settings.get('solver_threads', CPSAT_THREADS)) if method == 'cpsat' else 1
        preparation = read(folder / 'solve.json')['seconds'] * threads
    elif method == 'alphazero':
        metrics = read(folder / 'metrics.json')
        preparation = sum(metrics['episode_seconds']) + sum(metrics['update_seconds'])
    elif method == 'ppo':
        lines = (folder / 'checkpoints' / 'progress.jsonl').read_text().splitlines()
        preparation = json.loads(lines[-1])['training_seconds']
    else:
        preparation = 0.0
    return evaluation['summary']['on_time'], preparation / 3600, decision


def group_means(values):
    """{(key, instance): [numbers]} -> {(key, group): mean over instances of the per-instance mean}."""
    by_group = defaultdict(list)
    for (key, instance), numbers in values.items():
        by_group[(key, GROUP[instance])].append(statistics.mean(numbers))
    return {key: statistics.mean(numbers) for key, numbers in by_group.items()}


def method_rows(folders):
    """Per (method, group): on time, preparation hours and decision seconds of the method runs."""
    runs = {}
    for folder in folders:
        for path in sorted(Path(folder).glob('runs/*/*/seed*/evaluation.json')):
            method = ALIASES.get(path.parent.parent.name, path.parent.parent.name)
            if method in METHODS and path.parent.parent.parent.name in GROUP:
                runs[(path.parent.parent.parent.name, method, path.parent.name)] = (method, path.parent)
    numbers = [defaultdict(list) for _ in range(3)]
    for (instance, _, _), (method, folder) in runs.items():
        for table, value in zip(numbers, run_numbers(method, folder)):
            table[(method, instance)].append(value)
    return [group_means(table) for table in numbers]


def llm_data(folders):
    """Return the evaluation summaries {(model, arm, rep, project): summary} and the generation ledger rows."""
    summaries, ledger = {}, {}
    for folder in folders:
        for path in sorted(Path(folder).glob('evaluation/*/*/*/rep*/*/summary.json')):
            model, arm, _, rep, project = path.parts[-6:-1]
            summaries[(model, arm, rep, project)] = read(path)
        if (Path(folder) / 'ledger.json').exists():
            ledger.update(read(Path(folder) / 'ledger.json'))
    return summaries, ledger


def llm_rows(summaries, ledger):
    """Per (model, arm, group): on time, failure, decision seconds; per (model, arm): cost; per (model, group): hours."""
    on_time, failure, decision = defaultdict(list), defaultdict(list), defaultdict(list)
    for (model, arm, _, project), summary in summaries.items():
        on_time[((model, arm), project)].append(summary['on_time'])
        failure[((model, arm), project)].append(summary['fallback_rate'])
        counters = summary['counters']
        decision[((model, arm), project)].append((counters['selection_seconds'] + counters['feature_seconds'])
                                                 / summary['episodes'])
    cost, hours = defaultdict(list), defaultdict(list)
    for key, row in ledger.items():
        model, arm, scope, _ = key.split('/')
        if model in LIST_PRICES:
            prices = LIST_PRICES[model]
            cost[(model, arm)].append((row['input_tokens'] * prices[0] + row['output_tokens'] * prices[1]) / 1e6)
        else:
            cost[(model, arm)].append(row['charge_bound_usd'])
        if arm == 'individual' and scope in GROUP:
            hours[(model, GROUP[scope])].append(row['seconds'] / 3600)
    return (group_means(on_time), group_means(failure), group_means(decision),
            {key: statistics.mean(values) for key, values in cost.items()},
            {key: statistics.mean(values) for key, values in hours.items()})


def number(value, digits=3):
    """Format with three significant digits, keeping whole numbers whole."""
    return '–' if value is None else f'{value:.{digits}g}' if abs(value) < 10 ** digits else f'{value:.0f}'


def tables(results, llm, llm_model='sol'):
    """Return the two tables as Markdown: the methods (with the LLM row for llm_model) and the LLM models."""
    on_time, preparation, decision = method_rows(results)
    lines = ['| Method | On time S (%) | On time L (%) | Preparation S (h) | Preparation L (h) | Decision S (s) | Decision L (s) |',
             '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    llm_tables = llm_rows(*llm_data(llm)) if llm else None
    for method, name in METHODS.items():
        if method == 'llm':
            if not llm_tables:
                continue
            on, failure, seconds, cost, hours = llm_tables
            key = (llm_model, 'individual')
            values = [on.get((key, g)) for g in 'SL'], [hours.get((llm_model, g)) for g in 'SL'], \
                [seconds.get((key, g)) for g in 'SL']
        elif any((method, g) in on_time for g in 'SL'):
            values = [[table.get((method, g)) for g in 'SL'] for table in (on_time, preparation, decision)]
        else:
            continue
        cells = [f'{100 * v:.2f}' if v is not None else '–' for v in values[0]]
        cells += [number(v) for v in values[1]] + [number(v) for v in values[2]]
        lines.append(f'| {name} | ' + ' | '.join(cells) + ' |')
    output = ['On-time rate (%), preparation time (h) and decision time (s).', '', *lines]
    if llm_tables:
        on, failure, _, cost, _ = llm_tables
        output += ['', 'LLM-generated policies: on-time rate (%), failure rate (%) and cost per policy ($).', '',
                   '| Model | Instance-specific S | L | Failure | Cost | General S | L | Failure | Cost |',
                   '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
        for model, name in MODELS.items():
            cells = []
            for arm in ('individual', 'general'):
                key = (model, arm)
                if (key, 'S') not in on:
                    cells += ['–'] * 4
                    continue
                cells += [f'{100 * on[(key, g)]:.2f}' for g in 'SL']
                cells += [f'{100 * statistics.mean(failure[(key, g)] for g in "SL"):.1f}', f'{cost[key]:.3f}']
            if any(cell != '–' for cell in cells):
                output.append(f'| {name} | ' + ' | '.join(cells) + ' |')
    return '\n'.join(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--results', nargs='+', type=Path, default=[Path('results')])
    parser.add_argument('--llm', nargs='*', type=Path, default=[], help='LLM generation and evaluation folders')
    parser.add_argument('--llm-model', default='sol', help="The LLM row of the main table: this model's instance-specific policies")
    args = parser.parse_args()
    print(tables(args.results, args.llm, args.llm_model))


if __name__ == '__main__':
    main()
