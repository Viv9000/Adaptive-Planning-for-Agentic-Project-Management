"""Scheduling features, the inputs of the default network: per-mode duration summaries (duration_tables), and
per-task, per-mode, per-worker, and global features computed from the state encoding (SchedulingFeatures).

Durations are rounded time units, scaled by the deadline.
"""

from __future__ import annotations

import math

import torch
from torch import Tensor, nn

from planner.core.mdp import MDP
from planner.core.project import longest_paths

# Dedication comparisons allow the same rounding slack as the MDP's capacity check.
CAPACITY_TOLERANCE = 1e-9

def _longest_duration_days(distribution) -> int:
    """Return the longest rounded duration: the table's longest day, or the PERT maximum rounded up."""
    if distribution.family == 'tabular':
        return max(distribution.probabilities)
    return math.ceil(distribution.parameters['c'])


def duration_tables(project, layout, time_scale=None):
    """Build original and conditional lower/upper/mean summaries from known distributions.

    Condition active observations through the shared MDP remaining-duration CDF.
    Unreachable elapsed observations remain zero and cannot appear in validated states.
    """
    mdp = MDP(project)
    deadline = project.deadline.delta
    scale = deadline if time_scale is None else time_scale
    maximum_elapsed = max(deadline, *map(_longest_duration_days, project.distributions.values()))
    original = torch.zeros(layout.n_tasks, layout.max_modes, 3)
    conditional = torch.zeros(layout.n_tasks, layout.max_modes, maximum_elapsed + 1, 3)
    dedication = torch.zeros(layout.n_tasks, layout.max_modes, layout.n_workers)
    exists = torch.zeros(layout.n_tasks, layout.max_modes, dtype=torch.bool)
    for task_index, task in enumerate(project.tasks):
        for mode_index, mode in enumerate(task.modes):
            # Summarize the rounded duration: shortest, longest, and mean days
            distribution = project.distributions[mode.distribution_hash]
            maximum = _longest_duration_days(distribution)
            days = torch.arange(maximum + 1, dtype=torch.float64)
            cdf = torch.tensor([distribution.evaluate_cdf(int(day)) for day in days], dtype=torch.float64)
            probabilities = torch.diff(cdf, prepend=torch.zeros(1, dtype=torch.float64))
            support = days[probabilities > 0]
            if not len(support):
                raise ValueError('Rounded duration distribution has no positive-probability support')
            original[task_index, mode_index] = torch.tensor([
                support[0], support[-1], (days * probabilities).sum(),
            ]) / scale

            # Summarize the remaining duration for every age the task can still be running at
            for elapsed in range(int(support[-1])):
                remaining_days = torch.arange(maximum - elapsed + 1, dtype=torch.float64)
                remaining_cdf = torch.tensor([
                    mdp.remaining_duration_cdf(task.id, mode.id, elapsed, int(day))
                    for day in remaining_days
                ], dtype=torch.float64)
                mass = torch.diff(remaining_cdf, prepend=torch.zeros(1, dtype=torch.float64))
                remaining_support = remaining_days[mass > 0]
                conditional[task_index, mode_index, elapsed] = torch.tensor([
                    remaining_support[0], remaining_support[-1], (remaining_days * mass).sum(),
                ]) / scale

            # Record the mode's dedication per worker
            for worker_id, amount in mode.dedication.items():
                dedication[task_index, mode_index, layout.worker_index[worker_id]] = amount
            exists[task_index, mode_index] = True
    return original, conditional, dedication, exists


def duration_quantiles(project, layout, levels, time_scale=None):
    """Return [tasks, modes, len(levels)]: the smallest rounded duration whose CDF reaches each level, in deadline units."""
    scale = project.deadline.delta if time_scale is None else time_scale
    table = torch.zeros(layout.n_tasks, layout.max_modes, len(levels))
    for task_index, task in enumerate(project.tasks):
        for mode_index, mode in enumerate(task.modes):
            distribution = project.distributions[mode.distribution_hash]
            maximum = _longest_duration_days(distribution)
            cdf = [distribution.evaluate_cdf(day) for day in range(maximum + 1)]
            for level_index, level in enumerate(levels):
                day = next((d for d, value in enumerate(cdf) if value >= level - 1e-12), maximum)
                table[task_index, mode_index, level_index] = day / scale
    return table


# Scheduling features --------------------------------------------------------------------------------------

class SchedulingFeatures(nn.Module):
    """Compute per-task, per-mode, per-worker, and global scheduling features from the standard state encoding.

    Durations are in deadline units, like the state encoding's time and ages.
    The critical path of a task is its remaining duration plus the longest chain of successors after it,
    each successor taking its shortest mean duration over modes; slack is the time left after that path.
    """

    def __init__(self, project, layout) -> None:
        super().__init__()
        self.layout = layout
        self.deadline = project.deadline.delta
        self._last = None  # (inputs, features) of the last call without gradients; see forward
        original, conditional, dedication, exists = duration_tables(project, layout)
        for name, table in (('original', original), ('conditional', conditional),
                            ('dedication', dedication), ('exists', exists)):
            self.register_buffer(name, table)

        # Direct precedence: predecessors[j, i] = 1 when task i must finish before task j starts
        n = layout.n_tasks
        predecessors = torch.zeros(n, n)
        for before, after in project.tpg_edges:
            predecessors[layout.task_index[after], layout.task_index[before]] = 1
        successors = predecessors.T.contiguous()
        self.register_buffer('predecessors', predecessors)
        self.register_buffer('successors', successors)

        # Each mode's 90th and 99th percentile of the rounded duration, in deadline units (risk inputs)
        self.register_buffer('risk', duration_quantiles(project, layout, (0.9, 0.99)))

        # Each task's shortest mean duration over its modes
        means = original[..., 2].masked_fill(~exists, torch.inf)
        shortest = means.min(dim=1).values
        self.register_buffer('shortest', shortest)

        # Longest chain after each task: the longest path of any successor, 0 after the last tasks
        paths = longest_paths(project, {task_id: shortest[i] for i, task_id in enumerate(layout.task_ids)},
                              zero=torch.tensor(0.0))
        tail = torch.stack([max((paths[layout.task_ids[j]] for j in successors[i].nonzero().flatten().tolist()),
                                default=torch.tensor(0.0)) for i in range(n)])
        self.register_buffer('tail', tail)

        # Share of all tasks that come after each task, directly or not
        reachable = successors.bool()
        for _ in range(n):
            reachable = reachable | ((reachable.float() @ successors) > 0)
        self.register_buffer('descendants', reachable.float())
        self.register_buffer('successor_share', reachable.float().sum(dim=1) / n)

    def forward(self, time: Tensor, task_features: Tensor, free: Tensor) -> dict[str, Tensor]:
        """Return a dict of feature tensors for a batch of encoded states (see network/encoding.py).

        Without gradients, the last result is reused for the same input tensors: the policy and value networks
        can share one SchedulingFeatures (it has no weights), so a search leaf computes its features once.
        """
        if not torch.is_grad_enabled() and self._last is not None and all(map(
                lambda a, b: a is b, self._last[0], (time, task_features, free))):
            return self._last[1]
        features = self._compute(time, task_features, free)
        self._last = ((time, task_features, free), features) if not torch.is_grad_enabled() else None
        return features

    def _compute(self, time: Tensor, task_features: Tensor, free: Tensor) -> dict[str, Tensor]:
        """Compute the feature tensors; see forward."""
        layout = self.layout
        unstarted, active, completed = task_features[:, :, 0], task_features[:, :, 1], task_features[:, :, 2]
        selected = task_features[:, :, 3:3 + layout.max_modes]
        pending = task_features[:, :, -1]
        elapsed = (task_features[:, :, -2] * self.deadline).round().long().clamp(0, self.conditional.shape[2] - 1)

        # Remaining-duration summary per mode: conditioned on age for a running task's observed selected mode,
        # the original summary otherwise, and zero for completed tasks and unselected modes of active tasks
        batch = task_features.shape[0]
        task_indices = torch.arange(layout.n_tasks, device=task_features.device)[None, :, None]
        mode_indices = torch.arange(layout.max_modes, device=task_features.device)[None, None, :]
        conditional = self.conditional[task_indices, mode_indices, elapsed[:, :, None]]
        observed = (active * (1 - pending))[:, :, None] * selected
        remaining = torch.where(observed.bool()[..., None], conditional, self.original.expand(batch, -1, -1, -1))
        unavailable = completed[:, :, None].bool() | (active[:, :, None].bool() & ~selected.bool())
        remaining = remaining.masked_fill(unavailable[..., None], 0)

        # Each task's own remaining duration: the selected mode's mean if active, the shortest mean if unstarted
        own = active * (remaining[..., 2] * selected).sum(dim=2) + unstarted * self.shortest
        critical = (own + self.tail) * (1 - completed)
        slack = (1 - time - critical) * (1 - completed)

        # A task is ready when it is unstarted and every predecessor is completed; a mode fits in the free dedication
        unfinished_predecessors = torch.einsum('ij,bj->bi', self.predecessors, 1 - completed)
        ready = unstarted * (unfinished_predecessors == 0).float()
        within = (self.dedication[None] <= free[:, None, None, :] + CAPACITY_TOLERANCE).all(dim=-1)
        fits = (self.exists[None] & within & ready[:, :, None].bool()).float()

        # Project level: the longest critical path among tasks that are running or could start now
        candidates = ((active + ready) > 0).float()
        project_remaining = (critical * candidates).max(dim=1, keepdim=True).values
        return {
            'own': own, 'free': free,
            'unstarted': unstarted, 'active': active, 'completed': completed, 'selected': selected,
            'elapsed': task_features[:, :, -2], 'pending': pending, 'remaining': remaining,
            'critical': critical, 'slack': slack, 'ready': ready, 'fits': fits,
            'project_remaining': project_remaining, 'project_slack': 1 - time - project_remaining,
        }

    def task_inputs(self, features: dict[str, Tensor]) -> Tensor:
        """Return per-task inputs [B, N, 11]: status, age, pending, ready, any fitting mode, critical path, slack, and size."""
        batch = features['ready'].shape[0]
        constant = lambda table: table[None].expand(batch, -1)
        return torch.stack((
            features['unstarted'], features['active'], features['completed'], features['elapsed'], features['pending'],
            features['ready'], features['fits'].amax(dim=2), features['critical'], features['slack'],
            constant(self.successor_share), constant(self.shortest),
        ), dim=-1)

    def mode_inputs(self, features: dict[str, Tensor]) -> Tensor:
        """Return per-mode inputs [B, N, K, 10]: exists, fits, selected, original and remaining summaries, total dedication."""
        batch = features['ready'].shape[0]
        constant = lambda table: table[None].expand(batch, *table.shape)
        return torch.cat((
            constant(self.exists.float())[..., None], features['fits'][..., None], features['selected'][..., None],
            constant(self.original), features['remaining'], constant(self.dedication.sum(dim=-1))[..., None],
        ), dim=-1)

    def risk_mode_inputs(self, features: dict[str, Tensor]) -> Tensor:
        """Return each mode's duration risk [B, N, K, 2]: its p90 and p99."""
        return self.risk[None].expand(features['ready'].shape[0], -1, -1, -1)

    def worker_inputs(self, features: dict[str, Tensor], free: Tensor) -> Tensor:
        """Return per-worker inputs [B, W, 2]: free dedication and the dedication the fitting modes ask for."""
        demand = torch.einsum('bnk,nkw->bw', features['fits'], self.dedication) / self.layout.max_modes
        return torch.stack((free, demand), dim=-1)

    def global_inputs(self, time: Tensor, features: dict[str, Tensor]) -> Tensor:
        """Return global inputs [B, 5]: time, project critical path and slack, and the shares completed and active."""
        return torch.cat((time, features['project_remaining'], features['project_slack'],
                          features['completed'].mean(dim=1, keepdim=True), features['active'].mean(dim=1, keepdim=True)), dim=1)
