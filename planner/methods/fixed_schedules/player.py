"""Non-anticipative replay of a fixed (start, mode) schedule, preserving its order on shared workers."""

import re

from numpy.random import Generator

from planner.core.mdp import MDP
from planner.core.state import STOP, Action, State
from planner.core.players import Player


class FixedSchedulePlayer(Player):
    """Follow a fixed (start, mode) schedule preserving its order on shared workers.

    Starts the first scheduled task, in scheduled start order, whose earlier tasks sharing a worker have all started and
    whose scheduled mode is legal now; otherwise waits (STOP). The scheduled start days are not kept: durations differ
    from the ones the schedule was computed with, so tasks start as soon as the order and the workers allow.
    """

    def __init__(self, mdp: MDP, plan) -> None:
        if set(plan.starts) != {task.id for task in mdp.project.tasks}:
            raise ValueError('A fixed schedule must contain every task exactly once')
        from planner.core.state import Start
        self.mdp = mdp
        # The scheduled START action of each task, and the workers of its mode
        self.actions = {task: Start(task, item['mode']) for task, item in plan.starts.items()}
        members = {task: set(mdp.mode(task, item['mode']).dedication) for task, item in plan.starts.items()}
        # Tasks by scheduled start day, ties broken by task number
        self.order = sorted(plan.starts, key=lambda task: (plan.starts[task]['day'],
                                                           int(re.search(r'\d+$', task).group())))
        # For each task, the earlier tasks that share a worker with it: they must start first
        self.previous = {task: frozenset(other for other in self.order[:index] if members[task] & members[other])
                         for index, task in enumerate(self.order)}

    def act(self, state: State, rng: Generator) -> Action:
        started = state.completed.union(record.task_id for record in state.active)
        legal = None
        # Start the first task in order whose turn it is and whose scheduled mode is legal now
        for task in self.order:
            if task in started or not self.previous[task] <= started:
                continue
            if legal is None:
                legal = set(self.mdp.legal_actions(state))
            if self.actions[task] in legal:
                return self.actions[task]
        # Nothing can start: advance to the next day
        return STOP
