"""Single-attempt API generation with durable reservations and no automatic retries.

Each job (model, prompt, replicate) is one API request. Before sending it, its worst-case charge is reserved in
ledger.json, and nothing is sent if the reservations would pass the dollar cap. A request that ends without a saved
result is marked 'uncertain' and stops generation, so it is never sent twice by accident.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import ast
import fcntl
import json
import os
from pathlib import Path
import threading
import time
from urllib.request import Request, urlopen

from planner.core.artifacts import frozen, read, write_json
from planner.methods.llm.settings import MODELS, canonical, digest


# The only modules a generated program may import
ALLOWED_IMPORTS = {'__future__', 'math', 'cmath', 'statistics', 'random', 'time', 'collections',
                   'itertools', 'functools', 'heapq', 'bisect', 'operator', 'copy', 'typing',
                   'dataclasses', 'enum', 'fractions', 'decimal', 'numpy', 'scipy'}


def validate_source(source):
    """Check a generated program before it runs: a build_policy function, allowed imports only, and no code at the
    module's top level apart from definitions and literal constants. Raises ValueError otherwise."""
    tree = ast.parse(source)
    if not any(isinstance(node, ast.FunctionDef) and node.name == 'build_policy' for node in tree.body):
        raise ValueError('Missing build_policy function')
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules = [name.name.split('.')[0] for name in node.names]
        elif isinstance(node, ast.ImportFrom):
            modules = [(node.module or '').split('.')[0]]
            if node.level:
                raise ValueError('Relative imports are not available')
        else:
            continue
        if any(module not in ALLOWED_IMPORTS for module in modules):
            raise ValueError('Imports allowed: ' + ', '.join(sorted(ALLOWED_IMPORTS)))
    # Keep project preprocessing inside the timed build rather than module execution.
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
            continue
        value = node.value if isinstance(node, (ast.Assign, ast.AnnAssign, ast.Expr)) else None
        try:
            ast.literal_eval(value)
        except (ValueError, TypeError):
            raise ValueError('Module top level may contain only imports, definitions, and literal constants') from None
    return tree


# The reply must be JSON with exactly one field: the program's source
SOURCE_SCHEMA = dict(type='object', properties={'source': {'type': 'string'}},
                     required=['source'], additionalProperties=False)


def payload(job, prompt):
    """The API request: OpenAI's Responses API with medium reasoning, or Bedrock's Converse API."""
    config = MODELS[job['model']]
    if config['provider'] == 'bedrock':
        inference = dict(maxTokens=job['max_output_tokens'])
        if config.get('temperature') is not None:
            inference['temperature'] = config['temperature']
        return dict(modelId=config['model'], messages=[dict(role='user', content=[{'text': prompt}])],
                    inferenceConfig=inference)
    return dict(model=config['model'], input=prompt, store=False,
                service_tier='default', reasoning={'effort': 'medium'},
                max_output_tokens=job['max_output_tokens'],
                text={'format': dict(type='json_schema', name='scheduler',
                                     schema=SOURCE_SCHEMA, strict=True)})


def invoke(job, request, timeout, profile=None, region=None):
    """Send one request; return (raw response, text, input tokens, output tokens, complete)."""
    if MODELS[job['model']]['provider'] == 'bedrock':
        return invoke_bedrock(request, timeout, profile, region)
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise RuntimeError('OPENAI_API_KEY must be set in the environment')
    call = Request('https://api.openai.com/v1/responses', data=canonical(request).encode(),
                   headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
    with urlopen(call, timeout=timeout) as response:
        result = json.load(response)
    usage = result['usage']
    text = ''.join(part.get('text', '') for item in result.get('output', [])
                   if item.get('type') == 'message' for part in item.get('content', [])
                   if part.get('type') == 'output_text')
    complete = result.get('status') == 'completed'
    return result, text, usage['input_tokens'], usage['output_tokens'], complete


def invoke_bedrock(request, timeout, profile, region):
    """Send one Converse request to Amazon Bedrock (boto3 is needed only for Bedrock models)."""
    import boto3
    from botocore.config import Config
    client = boto3.Session(profile_name=profile, region_name=region).client(
        'bedrock-runtime', config=Config(retries={'total_max_attempts': 1}, connect_timeout=20, read_timeout=timeout))
    result = client.converse(**request)
    # Keep a JSON-serializable response without botocore's metadata.
    result.pop('ResponseMetadata', None)
    text = ''.join(block.get('text', '') for block in result.get('output', {}).get('message', {}).get('content', []))
    usage = result['usage']
    return result, text, usage['inputTokens'], usage['outputTokens'], result.get('stopReason') == 'end_turn'


def source_from_text(text):
    """The program in a reply, checked with validate_source; raises if the reply is not {"source": "..."}."""
    # A single optional fence is formatting normalization, not a corrective model call.
    text = text.strip()
    if text.startswith('```') and text.endswith('```'):
        parts = text.split('\n', 1)
        if len(parts) < 2:
            raise ValueError('Fenced reply without content')
        text = parts[1].rsplit('```', 1)[0].strip()
    parsed = json.loads(text)
    if set(parsed) != {'source'} or type(parsed['source']) is not str:
        raise ValueError('Expected exactly one source string')
    validate_source(parsed['source'])
    return parsed['source']


def generate(root, jobs, *, parallel, api_cap, max_hours, profile=None, region=None):
    """Send every job's request once (parallel at once) and save each program to programs/<job>/policy.py.

    A pending request is never reissued automatically, including after process death. Stops at the dollar cap
    (api_cap) or after max_hours from the first call.
    """
    if any(MODELS[j['model']]['provider'] == 'openai' for j in jobs) and not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('Set OPENAI_API_KEY before generation; no requests were dispatched')
    if any(MODELS[j['model']]['provider'] == 'bedrock' for j in jobs):
        import boto3
        if boto3.Session(profile_name=profile, region_name=region).get_credentials() is None:
            raise RuntimeError('AWS credentials for Bedrock are unavailable; no requests were dispatched')
    # One generation process at a time; refuse to continue while a request's outcome is unknown
    root = Path(root)
    ledger_path = root / 'ledger.json'
    frozen(root / 'generation_budget.json', dict(api_cap_usd=api_cap, max_hours=max_hours, region=region, profile=profile))
    with (root / '.generation.lock').open('a') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        records = read(ledger_path) if ledger_path.exists() else {}
        if any(row['status'] in ('reserved', 'uncertain') for row in records.values()):
            raise RuntimeError('Unresolved API request: reconcile the saved ledger before continuing')
        start_path = root / 'generation_clock.json'
        if not start_path.exists():
            write_json(start_path, {'stop_at': time.time() + 3600 * max_hours})
        stop_at = read(start_path)['stop_at']
        lock = threading.Lock()
        halted = threading.Event()

        def one(job):
            # The first error of any job stops every job that has not started yet (jobs already sending finish)
            try:
                return reserve_and_send(job)
            except BaseException:
                halted.set()
                raise

        def reserve_and_send(job):
            # Reserve the job's worst-case charge, send its request, save the response and the program
            key = job['id']
            prompt = (root / job['prompt_path']).read_text()
            if digest(prompt) != job['prompt_hash']:
                raise ValueError(f'Prompt changed: {key}')
            request = payload(job, prompt)
            signature = digest(request)
            with lock:
                if key in records:
                    if records[key]['request_hash'] != signature:
                        raise ValueError('Saved API payload differs')
                    return
                if halted.is_set() or time.time() >= stop_at:
                    raise RuntimeError('Generation stopped at its persistent time limit')
                if not job['context_certified']:
                    raise RuntimeError(f'Context not certified for {key}; inspect prompt_audit.json')
                config = MODELS[job['model']]
                # UTF-8 bytes bound text tokens; extra overhead covers provider message/schema framing.
                bound = ((len(prompt.encode()) + 4096) * config['reserve_input_rate']
                         + job['max_output_tokens'] * config['output_rate']) / 1e6
                if sum(r['charge_bound_usd'] for r in records.values()) + bound > api_cap:
                    halted.set()
                    raise RuntimeError('API reservation would exceed the spending cap')
                records[key] = dict(status='reserved', request_hash=signature, payload=request,
                                    charge_bound_usd=bound, dispatched_at=time.time())
                write_json(ledger_path, records)
            # Send the request; the reservation becomes the actual charge once usage is known
            started = time.monotonic()
            try:
                raw, output, inputs, outputs, complete = invoke(
                    job, request, max(1, min(600, stop_at - time.time())), profile, region)
                # Save the provider response before parsing generated code.
                write_json(root / 'responses' / (key + '.json'), raw)
                if inputs > len(prompt.encode()) + 4096 or outputs > job['max_output_tokens']:
                    raise RuntimeError('Provider usage exceeded reservation assumptions')
                status = dict(status='invalid_source', reason='incomplete_response')
                if complete:
                    try:
                        source = source_from_text(output)
                        target = root / 'programs' / key / 'policy.py'
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_text(source)
                        status = dict(status='ready', source_hash=digest(source))
                    except (ValueError, TypeError, SyntaxError, KeyError) as error:
                        status = dict(status='invalid_source', reason=type(error).__name__ + ':' + str(error)[:400])
                write_json(root / 'programs' / key / 'generation.json', status)
                with lock:
                    row = records[key]
                    row.update(status='complete', input_tokens=inputs, output_tokens=outputs,
                               seconds=time.monotonic() - started, generation=status)
                    row['charge_bound_usd'] = (inputs * config['reserve_input_rate']
                                               + outputs * config['output_rate']) / 1e6
                    write_json(ledger_path, records)
                print(key, status['status'], flush=True)
            except BaseException as error:
                halted.set()
                with lock:
                    records[key].update(status='uncertain', error_type=type(error).__name__)
                    write_json(ledger_path, records)
                # Provider exceptions can contain request details; persist only their type.
                raise RuntimeError(f'{key}: {type(error).__name__}; inspect saved response/ledger') from None

        with ThreadPoolExecutor(max_workers=parallel) as pool:
            futures = [pool.submit(one, job) for job in jobs]
            for future in as_completed(futures):
                future.result()
