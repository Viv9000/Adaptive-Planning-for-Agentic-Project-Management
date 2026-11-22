"""The LLM-based method's player: a generated policy in its own process, with the greedy method deciding wherever the
policy fails.

A forced decision (one legal action) is taken directly. Any other decision is asked of the policy, which falls back
to the greedy method if the policy fails to build, raises, returns an illegal action, or takes longer than
LIMITS['move_seconds']; each fallback is counted. A policy that fails to build is not asked again on that instance.
"""

from collections import Counter
import time

from planner.core.players import Player
from planner.methods.greedy.player import GreedyPlayer
from planner.methods.llm.observation import Observation
from planner.methods.llm.policy_process import PolicyProcess
from planner.methods.llm.settings import LIMITS


def failure_kind(error):
    """Classify a policy failure: timeout, input_mutation, invalid_action or exception."""
    message = str(error)
    if 'time_limit' in message:
        return 'timeout'
    if 'mutation' in message:
        return 'input_mutation'
    if 'invalid_action' in message or 'return a built-in int' in message:
        return 'invalid_action'
    return 'exception'


class LLMPlayer(Player):
    """Play a generated program (source, or None if generation failed) on mdp's project.

    episode_record() returns the episode's decision counters, fallbacks and build attempts, which the evaluation
    (planner/evaluate/paired.py) adds to the episode's row.
    """

    def __init__(self, mdp, source):
        self.mdp = mdp
        self.source = source
        self.observation = Observation(mdp)
        self.greedy = GreedyPlayer(mdp)
        self.worker = None
        self.disabled = 'generation_failure' if source is None else None
        self.seed = 0
        self.reset_problem = None
        self.counters, self.failures, self.builds = Counter(), [], []

    # The policy process: built on first use, rebuilt after a failure

    def build(self):
        """Start a worker process and build the policy (LIMITS['build_seconds']); False if it fails."""
        if self.disabled:
            return False
        started = time.monotonic()
        try:
            self.worker = PolicyProcess()
            static = self.observation(self.mdp.reset())['features']
            self.worker.build(self.source, self.observation.project, static, LIMITS,
                              time.time() + LIMITS['build_seconds'])
            self.builds.append(dict(status='ready', seconds=time.monotonic() - started))
            return True
        except Exception as error:
            self.builds.append(dict(status='failed', reason=failure_kind(error),
                                    detail=str(error)[:400], seconds=time.monotonic() - started))
            self.disabled = 'build_failure'
            self.close()
            return False

    def close(self):
        if self.worker is not None:
            self.worker.close()
            self.worker = None

    def ask(self, observation):
        """Ask the policy for an action ID: (action ID or None, failure reason or None, seconds)."""
        if self.disabled:
            return None, self.disabled, 0.0
        if self.reset_problem:
            reason, self.reset_problem = 'reset_' + self.reset_problem, None
            return None, reason, 0.0
        # After a failure the worker was closed: start a new one and reset it for this episode
        if not self.worker:
            if not self.build():
                return None, self.disabled, 0.0
            try:
                self.worker.reset(self.seed, time.time() + 1.0)
            except Exception as error:
                self.close()
                return None, 'reset_' + failure_kind(error), 0.0
        # The action must arrive within the time per decision and be one of the legal action IDs
        started = time.monotonic()
        deadline = time.time() + LIMITS['move_seconds']
        try:
            action_id = self.worker.select(observation, deadline)['value']
            if type(action_id) is not int or action_id not in {row[0] for row in observation['legal_actions']}:
                raise ValueError('invalid_action')
            if time.time() > deadline:
                raise TimeoutError('local_time_limit')
            return action_id, None, time.monotonic() - started
        except Exception as error:
            self.close()
            return None, failure_kind(error), time.monotonic() - started

    # The player interface

    def start_episode(self, rng):
        """Give the policy this episode's seed, drawn from the episode's policy stream; reset the counters."""
        # Build attempts belong to the episode in which they happen (the first build is in the first episode)
        self.counters, self.failures, self.builds = Counter(), [], []
        self.seed, self.reset_problem = int(rng.integers(0, 2**63)), None
        if self.worker:
            try:
                self.worker.reset(self.seed, time.time() + 1.0)
            except Exception as error:
                self.reset_problem = failure_kind(error)
                self.close()

    def act(self, state, rng):
        legal = self.mdp.legal_actions(state)
        counters = self.counters
        counters['decisions'] += 1
        if len(legal) == 1:
            counters['forced'] += 1
            return legal[0]
        counters['nonforced'] += 1
        started = time.monotonic()
        observation = self.observation(state)
        counters['feature_seconds'] += time.monotonic() - started
        action_id, reason, seconds = self.ask(observation)
        counters['selection_seconds'] += seconds
        if reason:
            counters['fallbacks'] += 1
            counters['fallback_' + reason] += 1
            self.failures.append(dict(step=counters['decisions'] - 1, reason=reason, seconds=seconds))
            return self.greedy.act(state, rng)
        counters['valid_selections'] += 1
        return self.observation.layout.actions[action_id]

    def episode_record(self):
        """The episode's counters, fallbacks and build attempts, added to its row of the evaluation."""
        return dict(counters=dict(self.counters), failures=self.failures, builds=self.builds)
