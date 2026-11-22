"""Settings, frozen contracts and atomic records of the LLM-generated policies (general and instance-specific)."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUTPUT = Path('results') / 'llm'
# Per policy: 60 s to build, 1 s per decision, 4 GiB of memory, one thread
LIMITS = dict(build_seconds=60.0, move_seconds=1.0, memory_bytes=4 * 1024**3, threads=1)
# The paper's models. Rates are US dollars per million tokens; the generation cap reserves input at
# reserve_input_rate and output at output_rate. temperature None keeps the provider's default.
MODELS = {
    'luna': dict(provider='openai', model='gpt-6-luna', context=272000, max_output_tokens=32768,
                 input_rate=0.1, output_rate=0.5, reserve_input_rate=0.25),
    'sol': dict(provider='openai', model='gpt-6.1-sol', context=272000, max_output_tokens=32768,
                input_rate=2.0, output_rate=10.0, reserve_input_rate=5.0),
    # Astra's list input price is not known here; its reserve rate also stands in for it. Context assumed as Sol's.
    'astra': dict(provider='openai', model='gpt-6-astra', context=272000, max_output_tokens=32768,
                  input_rate=12.5, output_rate=50.0, reserve_input_rate=12.5),
    'deepseek': dict(provider='bedrock', model='deepseek.v3.2', context=163840, max_output_tokens=32768,
                     temperature=1.0, input_rate=0.6386, output_rate=1.9055, reserve_input_rate=0.6386),
    # Kimi K3.1's context length is an assumption; it only bounds the prompt-size check.
    'kimik31': dict(provider='bedrock', model='global.moonshotai.kimi-k3.1', context=262144, max_output_tokens=49152,
                    temperature=None, input_rate=3.3, output_rate=16.5, reserve_input_rate=3.3),
}


class PolicyFailure(Exception):
    """Generated code failed its runtime or action contract."""


def canonical(value):
    """Compact JSON with sorted keys: the same value always gives the same text (and digest)."""
    return json.dumps(value, separators=(',', ':'), sort_keys=True, allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def implementation_hash():
    paths = sorted(HERE.glob('*.py')) + sorted(HERE.glob('prompts/*.txt'))
    paths += sorted((ROOT / 'planner').rglob('*.py'))
    return digest([(str(p.relative_to(ROOT)), file_hash(p)) for p in paths])
