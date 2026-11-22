"""The greedy player: start the ready task with the longest remaining path in its fastest feasible mode."""

from planner.core.distributions import expected_duration
from planner.core.mdp import MDP
from planner.core.project import longest_paths
from numpy.random import Generator

from planner.core.state import STOP, Action, Start, State
from planner.core.players import Player


class GreedyPlayer(Player):
    """Prioritize longest remaining precedence paths, then fastest feasible modes, with stored-order ties.

    Path weights use shortest expected rounded mode durations and ignore resource competition along the path.
    Start whenever feasible, STOP otherwise, and never inspect private sampled finish days.
    """

    def __init__(self, mdp: MDP) -> None:
        self.mdp = mdp
        project = mdp.project
        durations = {key: expected_duration(distribution) for key, distribution in project.distributions.items()}

        # Record each mode's expected duration and stored position, and each task's fastest mode
        shortest = {}
        self.mode_duration = {}
        self.stored_order = {}
        for task_index, task in enumerate(project.tasks):
            for mode_index, mode in enumerate(task.modes):
                action = Start(task.id, mode.id)
                self.mode_duration[action] = durations[mode.distribution_hash]
                self.stored_order[action] = (task_index, mode_index)
            shortest[task.id] = min(durations[mode.distribution_hash] for mode in task.modes)

        # Each task's longest remaining path, in shortest expected durations
        self.remaining_path = longest_paths(project, shortest)

    def act(self, state: State, rng: Generator) -> Action:
        # Start the task with the longest remaining path in its fastest mode; otherwise wait for a completion
        starts = [action for action in self.mdp.legal_actions(state) if isinstance(action, Start)]
        if starts:
            # Mode speed must not change which tied task wins
            return min(starts, key=lambda action: (
                -self.remaining_path[action.task_id], self.stored_order[action][0],
                self.mode_duration[action], self.stored_order[action][1],
            ))
        return STOP

