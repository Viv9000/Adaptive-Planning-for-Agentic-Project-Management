"""Evaluate a policy on the shared stochastic futures: each future seed fixes the realized duration of every task and mode,
so every method meets the same durations."""

from contextlib import contextmanager
import hashlib
import json
from time import perf_counter

import numpy as np

from planner.core.artifacts import write_json
from planner.core.schedule_check import check_episode
from planner.core.simulator import RolloutSimulator
from planner.core.state import STOP
from planner.core.mdp import MDP


class CompletionMDP(MDP):
    """The evaluation MDP: the deadline success criterion, but late episodes run to completion."""

    @property
    def stop_day(self) -> None:
        return None


class PairedSimulator(RolloutSimulator):
    """The simulator of an evaluation episode: each started (task, mode) draws its duration from its own seed.

    The seed is a hash of (future seed, task, mode), so a task in a mode gets the same duration in a future whatever
    the method and whenever it starts. Searches inside a policy (MCTS) use their own simulators and never see it.
    """

    def __init__(self, mdp, seed):
        self.future_seed = seed
        super().__init__(mdp, mdp.reset(), np.random.default_rng(seed))

    def step(self, action):
        # Before a START, reseed the duration draw for that task and mode
        if action != STOP:
            key = f'{self.future_seed}:{action.task_id}:{action.mode_id}'.encode()
            seed = int.from_bytes(hashlib.sha256(key).digest()[:16], 'little')
            self.rng = np.random.default_rng(seed)
        return super().step(action)


@contextmanager
def _closing(player):
    """Close the player at the end, if it holds a resource (the LLM-based method's policy process)."""
    try:
        yield
    finally:
        if hasattr(player, 'close'):
            player.close()


def evaluate(project, make_player, path, samples, identity):
    """Play make_player's policy on futures 10000, 10001, ... (samples in all) and save the episodes to path.

    Each finished episode is appended to path's .jsonl journal, so an interrupted evaluation resumes; the policy gets
    its own random generator per future. A player with episode_record() adds its fields to each episode's row (the
    LLM-based method's fallback counts); a player with close() is closed at the end. Returns the summary: on-time
    rate, mean completion and seconds.
    """
    mdp = CompletionMDP(project)
    player = make_player(mdp)
    # Read the episodes already played
    journal = path.with_suffix('.jsonl')
    rows = []
    if journal.exists():
        # A killed process may leave one incomplete final JSON line.
        lines = journal.read_text().splitlines()
        for index, line in enumerate(lines):
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                if index != len(lines) - 1:
                    raise
        journal.write_text(''.join(json.dumps(row) + '\n' for row in rows))
    if [row['seed'] for row in rows] != list(range(10000, 10000 + len(rows))) or len(rows) > samples:
        raise ValueError('Evaluation journal does not match the frozen future seeds')
    # Play the remaining futures; every 50th episode's schedule is checked independently of the MDP
    with journal.open('a', buffering=1) as stream, _closing(player):
        for seed in range(10000 + len(rows), 10000 + samples):
            started = perf_counter()
            policy_rng = np.random.default_rng(np.random.SeedSequence([seed, 1]))
            player.start_episode(policy_rng)
            simulator = PairedSimulator(mdp, seed)
            decisions = 0
            states = []
            while not mdp.is_terminal(simulator.state):
                if (seed - 10000) % 50 == 0:
                    states.append(simulator.state)
                action = player.act(simulator.state, policy_rng)
                if not mdp.is_legal(simulator.state, action):
                    raise ValueError(f'Illegal action {action} at seed {seed}')
                simulator.step(action)
                decisions += 1
            if states:
                check_episode(project, states + [simulator.state], True)
            row = dict(seed=seed, success=bool(mdp.success_indicator(simulator.state)),
                       completion=simulator.state.day, seconds=perf_counter() - started, decisions=decisions)
            if hasattr(player, 'episode_record'):
                row.update(player.episode_record())
            stream.write(json.dumps(row) + '\n')
            rows.append(row)
            if len(rows) % 25 == 0:
                print(f'EVAL {identity} {len(rows)}/{samples}', flush=True)
    # Summarize and save all episodes
    summary = dict(on_time=sum(row['success'] for row in rows) / samples,
                   mean_completion=float(np.mean([row['completion'] for row in rows])), samples=samples,
                   evaluation_seconds=sum(row['seconds'] for row in rows))
    write_json(path, dict(identity=identity, episodes=rows, summary=summary,
                         coupling='sha256(future_seed:task_id:mode_id), separate policy/search RNG'))
    return summary
