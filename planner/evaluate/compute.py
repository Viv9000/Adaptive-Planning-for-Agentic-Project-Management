"""Measure the search compute of one run: simulation calls per phase and elapsed time."""

from contextlib import contextmanager
from datetime import datetime, timezone
import json
from time import perf_counter

from planner.methods.alphazero.mcts import MCTS


@contextmanager
def measure_search(path):
    """Record actual simulation calls and elapsed time, including interrupted attempts.

    Counts every MCTS simulation while the block runs, split into preparation ('optimization') and evaluation by the
    'phase' the caller sets, and appends one line per session to path.
    """
    previous = MCTS._run_simulation
    counts = {'phase': 'optimization', 'optimization_simulations': 0, 'evaluation_simulations': 0}
    started = perf_counter()

    # Count calls by wrapping MCTS._run_simulation for the duration of the block
    def measured(self, root):
        counts[counts['phase'] + '_simulations'] += 1
        return previous(self, root)

    MCTS._run_simulation = measured
    try:
        yield counts
    finally:
        MCTS._run_simulation = previous
        record = dict(counts, elapsed_seconds=perf_counter() - started,
                      timestamp=datetime.now(timezone.utc).isoformat())
        with path.open('a') as stream:
            stream.write(json.dumps(record) + '\n')
