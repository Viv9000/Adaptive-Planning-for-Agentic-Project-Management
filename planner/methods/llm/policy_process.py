"""Run a generated policy in its own Python process (policy_worker.py), so every call can be timed out.

The two processes talk by one JSON line per request and reply: build the policy for a project, reset it for an
episode, select an action. The process is not a sandbox: the generated code runs with your user's permissions.
"""

import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

from planner.methods.llm.settings import PolicyFailure, canonical


# The worker and its numerical libraries use one thread
ENVIRONMENT = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                   PYTHONDONTWRITEBYTECODE='1')


class PolicyProcess:
    """A worker process holding one policy; every call has a wall-clock deadline (PolicyFailure if missed)."""

    def __init__(self):
        command = [sys.executable, str(Path(__file__).with_name('policy_worker.py'))]
        self.process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=ENVIRONMENT,
                                        stderr=subprocess.DEVNULL, start_new_session=True, bufsize=0)
        self.buffer = b''
        try:
            if self.read(time.time() + 30) != {'ready': True}:
                raise RuntimeError('Unexpected isolation handshake')
        except BaseException:
            self.close()
            raise

    def read(self, deadline):
        """Read one JSON line from the worker before the deadline; kill the worker if it is late."""
        import json
        with selectors.DefaultSelector() as selector:
            selector.register(self.process.stdout, selectors.EVENT_READ)
            while b'\n' not in self.buffer:
                remaining = deadline - time.time()
                if remaining <= 0 or not selector.select(remaining):
                    self.close()
                    raise PolicyFailure('local_time_limit')
                block = os.read(self.process.stdout.fileno(), 65536)
                if not block:
                    raise PolicyFailure('policy_worker_exited')
                self.buffer += block
                if len(self.buffer) > 1024 * 1024:
                    raise PolicyFailure('oversized_policy_response')
        line, self.buffer = self.buffer.split(b'\n', 1)
        return json.loads(line)

    def call(self, request, deadline):
        """Send one request and return the worker's reply; any failure becomes a PolicyFailure."""
        try:
            data = (canonical(request) + '\n').encode()
            # A busy or failed worker must not hold the host in a blocking pipe write.
            os.set_blocking(self.process.stdin.fileno(), False)
            with selectors.DefaultSelector() as selector:
                selector.register(self.process.stdin, selectors.EVENT_WRITE)
                while data:
                    remaining = deadline - time.time()
                    if remaining <= 0 or not selector.select(remaining):
                        raise PolicyFailure('local_time_limit')
                    try:
                        data = data[os.write(self.process.stdin.fileno(), data):]
                    except BlockingIOError:
                        continue
            result = self.read(deadline)
            if not result.get('ok'):
                raise PolicyFailure(result.get('error', 'policy_worker_error'))
            return result
        except (BrokenPipeError, OSError, ValueError) as error:
            raise PolicyFailure('policy_worker_io:' + type(error).__name__) from None

    def build(self, source, project, static, limits, deadline):
        return self.call(dict(command='build', source=source, project=project, static_features=static, limits=limits), deadline)

    def reset(self, seed, deadline):
        return self.call(dict(command='reset', policy_seed=seed), deadline)

    def select(self, observation, deadline):
        return self.call(dict(command='select', observation=observation), deadline)

    def close(self):
        """Kill the worker's process group if it still runs, and close its pipes."""
        if self.process.poll() is None:
            try:
                os.killpg(self.process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        self.process.wait()
        for stream in (self.process.stdin, self.process.stdout):
            stream.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
