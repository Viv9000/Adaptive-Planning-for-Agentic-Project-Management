"""The schedule budget shared by the GA and SA searches: count every assessed schedule, keep the best, and save the
search state every 1000 schedules so that an interrupted search resumes exactly.
"""

import os
from pathlib import Path
import pickle

import numpy as np


def save_state(path, state):
    """Atomically save this runner's trusted local search state."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    with temporary.open('wb') as stream:
        pickle.dump(state, stream)
    os.replace(temporary, path)


def search(data, method, evaluations, seed, checkpoint, fresh, step, keep=None, progress=None):
    """Call step(data, state, rng, assess), which assesses one schedule, until `evaluations` schedules are assessed.

    fresh() gives the method's initial state; keep(state, candidate, plan) sees every forward schedule after the best
    is updated. Resumes from `checkpoint` if it exists. Returns the best plan and dict(evaluations, generations,
    restarts).
    """
    if evaluations < 1:
        raise ValueError('Expected a positive evaluation budget')
    checkpoint = Path(checkpoint)
    rng = np.random.default_rng(seed)
    # Resume a saved search, including its random generator, or start a new one
    if checkpoint.exists():
        with checkpoint.open('rb') as stream:
            state = pickle.load(stream)
        if state['method'] != method or state['seed'] != seed or state['limit'] != evaluations:
            raise ValueError('Search checkpoint settings differ')
        rng.bit_generator.state = state['rng']
    else:
        state = dict(method=method, seed=seed, limit=evaluations, count=0, best=None, best_schedule=None, generation=0,
                     restarts=0, **fresh())
        # A random schedule that is never assessed, as in line 6 of the published SA. GA draws it too, so that both
        # random streams are the paper's.
        data.random(rng)

    def persist():
        # Save the state and report progress
        state['rng'] = rng.bit_generator.state
        save_state(checkpoint, state)
        if progress:
            progress(state['count'], state['best_schedule'].completion if state['best_schedule'] else None)

    def assess(candidate, backward=False):
        # Decode one schedule, count it against the budget, and keep it if it is the best forward schedule so far
        plan = data.decode(candidate, backward)
        state['count'] += 1
        if not backward:
            if state['best_schedule'] is None or plan.completion < state['best_schedule'].completion:
                state['best'], state['best_schedule'] = candidate, plan
            if keep:
                keep(state, candidate, plan)
        return candidate, plan

    # Run the method one assessed schedule at a time, saving every 1000 schedules
    while state['count'] < evaluations:
        step(data, state, rng, assess)
        if state['count'] % 1000 == 0:
            persist()
    persist()
    return state['best_schedule'], dict(evaluations=state['count'], generations=state['generation'],
                                    restarts=state['restarts'])
