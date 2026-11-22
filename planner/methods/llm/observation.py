"""What a generated policy sees: the project as plain tables, and per decision the state, the legal actions and the
same features the AlphaZero-based method's and PPO's networks get."""

import torch

from planner.core.state import STOP
from planner.network.encoding import build_layout, encode_state
from planner.network.features import SchedulingFeatures


# Names of the feature columns, in order, as the prompt describes them
TASK_FIELDS = ['unstarted', 'active', 'completed', 'elapsed', 'pending', 'ready', 'any_fitting_mode',
               'critical_path', 'slack', 'successor_share', 'shortest_mean_duration']
MODE_FIELDS = ['exists', 'fits', 'selected', 'original_lower', 'original_upper', 'original_mean',
               'remaining_lower', 'remaining_upper', 'remaining_mean', 'total_dedication', 'p90', 'p99']
GLOBAL_FIELDS = ['time', 'project_remaining', 'project_slack', 'completed_share', 'active_share']


def project_data(project):
    """The project as JSON tables, given to build_policy.

    deadline; workers (their number); predecessors of each task (by index); teams: each distinct team as four lists
    of worker indices, by dedication 0.25, 0.5, 0.75 and 1; modes: per task, per mode [a, b, c, team index], the PERT
    minimum, most likely value and maximum (zero for the milestones).
    """
    layout = build_layout(project)
    ti, wi = layout.task_index, layout.worker_index
    predecessors = [[] for _ in layout.task_ids]
    for before, after in project.tpg_edges:
        predecessors[ti[after]].append(ti[before])
    tasks = {t.id: t for t in project.tasks}
    teams, team_index, modes = [], {}, []
    for task_id, mode_ids in zip(layout.task_ids, layout.mode_ids):
        lookup = {m.id: m for m in tasks[task_id].modes}
        rows = []
        for mode_id in mode_ids:
            mode = lookup[mode_id]
            groups = [[] for _ in range(4)]
            for worker, dedication in sorted(mode.dedication.items()):
                quarters = round(4 * dedication)
                if quarters not in (1, 2, 3, 4) or quarters / 4 != dedication:
                    raise ValueError('This interface requires quarter-unit dedication')
                groups[quarters - 1].append(wi[worker])
            key = tuple(tuple(sorted(group)) for group in groups)
            if key not in team_index:
                team_index[key] = len(teams)
                teams.append([list(group) for group in key])
            distribution = project.distributions[mode.distribution_hash]
            if distribution.family == 'pert':
                abc = [distribution.parameters[k] for k in ('a', 'b', 'c')]
            elif distribution.family == 'tabular' and dict(distribution.probabilities) == {0: 1.0}:
                abc = [0, 0, 0]
            else:
                raise ValueError('Only PERT and deterministic-zero milestones are supported')
            rows.append(abc + [team_index[key]])
        modes.append(rows)
    return dict(deadline=project.deadline.delta, workers=layout.n_workers,
                predecessors=[sorted(p) for p in predecessors], teams=teams, modes=modes)


class Observation:
    """Turns a state into the observation passed to the policy at a decision."""

    def __init__(self, mdp):
        self.mdp = mdp
        self.layout = build_layout(mdp.project)
        self.project = project_data(mdp.project)
        self.features = SchedulingFeatures(mdp.project, self.layout).eval()
        self.action_ids = {action: i for i, action in enumerate(self.layout.actions)}

    def __call__(self, state):
        """The day, completed and active tasks (index, mode index, start day, pending), the network features, and the
        legal actions as [action ID, [task index, mode index] or None for STOP]."""
        layout = self.layout
        with torch.inference_mode():
            time, tasks, free = encode_state(state, self.mdp, layout)
            features = self.features(time, tasks, free)
            mode_inputs = torch.cat((self.features.mode_inputs(features),
                                     self.features.risk_mode_inputs(features)), dim=-1)[0]
            network = dict(
                tasks=self.features.task_inputs(features)[0].tolist(),
                modes=[mode_inputs[i, :len(ids)].tolist() for i, ids in enumerate(layout.mode_ids)],
                workers=self.features.worker_inputs(features, free)[0].tolist(),
                global_inputs=self.features.global_inputs(time, features)[0].tolist(),
                free_dedication=free[0].tolist(), max_modes=layout.max_modes)
        legal = []
        for action in self.mdp.legal_actions(state):
            pair = None if action == STOP else [layout.task_index[action.task_id],
                                               layout.mode_index[layout.task_index[action.task_id]][action.mode_id]]
            legal.append([self.action_ids[action], pair])
        return dict(time=state.day, completed=sorted(layout.task_index[t] for t in state.completed),
                    active=[[layout.task_index[a.task_id], layout.mode_index[layout.task_index[a.task_id]][a.mode_id],
                             a.start_day, int(a.pending)] for a in state.active],
                    features=network, legal_actions=legal)
