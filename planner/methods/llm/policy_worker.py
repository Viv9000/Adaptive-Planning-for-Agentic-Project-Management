"""The worker process that runs one generated policy (started by policy_process.py).

Reads one request per line from stdin and answers one JSON line on stdout: 'build' runs the generated program and
calls its build_policy(project, static_features, limits); 'reset' calls the policy's start_episode(policy_seed);
'select' calls the policy on an observation and returns its action ID.
"""

import contextlib
import io
import json
import resource
import sys
import time
import types

# One numerical thread is set by the parent before Python or BLAS starts.
# Limits: 4 GiB of memory, 1 MiB per written file, no core dumps. numpy and scipy load before the policy's build time.
resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
resource.setrlimit(resource.RLIMIT_FSIZE, (1024**2, 1024**2))
resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
import numpy  # noqa: E402
import scipy.optimize  # noqa: E402
import scipy.stats  # noqa: E402


def canonical(value):
    return json.dumps(value, sort_keys=True, allow_nan=False)


selector = None
build_inputs = None
build_snapshot = None
print('{"ready":true}', flush=True)
for line in sys.stdin:
    try:
        request = json.loads(line)
        original = canonical(request)
        started = time.monotonic()
        # Generated diagnostics cannot corrupt the host protocol or fill a stderr pipe.
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            if request['command'] == 'build':
                module = types.ModuleType('generated_scheduler')
                sys.modules[module.__name__] = module
                namespace = module.__dict__
                exec(compile(request['source'], '<generated_scheduler>', 'exec'), namespace)
                build_inputs = [request['project'], request['static_features'], request['limits']]
                build_snapshot = canonical(build_inputs)
                selector = namespace['build_policy'](request['project'], request['static_features'], request['limits'])
                if not callable(selector):
                    raise TypeError('build_policy must return a callable')
                value = None
            elif request['command'] == 'reset':
                reset = getattr(selector, 'start_episode', None)
                if not callable(reset):
                    raise TypeError('Missing callable start_episode(policy_seed)')
                reset(request['policy_seed'])
                value = None
            elif request['command'] == 'select':
                value = selector(request['observation'])
                if type(value) is not int:
                    raise TypeError('select_action must return a built-in int action_id')
            else:
                raise ValueError('unknown command')
        # The policy must not change its inputs (they are reused for later decisions)
        if canonical(request) != original:
            raise ValueError('input_mutation')
        if build_inputs is not None and canonical(build_inputs) != build_snapshot:
            raise ValueError('build_input_mutation')
        result = dict(ok=True, value=value, selector_seconds=time.monotonic() - started)
    except BaseException as error:
        result = dict(ok=False, error=type(error).__name__ + ':' + str(error)[:600])
    print(json.dumps(result, allow_nan=False), flush=True)
