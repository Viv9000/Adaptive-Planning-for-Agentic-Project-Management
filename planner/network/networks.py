"""The paper's policy and value networks: an MLP over scheduling features (planner/network/features.py).

Each task's input holds its scheduling features (readiness, critical path, slack, ...) and, for each of its modes, a
summary of the mode (duration, dedication, whether it fits now) and the mode's duration risk (p90 and p99). A shared
task encoder embeds every task; a two-layer ReLU trunk reads the embeddings with the time, the workers' free
dedication and the project's remaining critical path and slack. The policy has a task head (tasks + STOP) and a mode
head; the value network has its own body and a sigmoid head.
"""

from __future__ import annotations

import torch
from torch import Tensor, nn

from planner.network.features import SchedulingFeatures


class MLPBody(nn.Module):
    """The task encoder and trunk on the scheduling features."""

    def __init__(self, project, layout, embedding_dim: int, hidden_dim: int,
                 features: SchedulingFeatures | None = None) -> None:
        super().__init__()
        self.features = features or SchedulingFeatures(project, layout)
        # Per mode: 10 summary inputs and 2 risk inputs; per task: 11 scheduling inputs
        task_width = 11 + 12 * layout.max_modes
        global_width = 1 + layout.n_workers + 2
        self.task_encoder = nn.Sequential(nn.Linear(task_width, embedding_dim), nn.ReLU())
        width = global_width + layout.n_tasks * embedding_dim
        self.trunk = nn.Sequential(nn.Linear(width, hidden_dim), nn.ReLU(), nn.Linear(hidden_dim, hidden_dim), nn.ReLU())

    def forward(self, time: Tensor, task_features: Tensor, free: Tensor) -> Tensor:
        # Per task: scheduling features and every mode's summary and risk; globally: time, free dedication, project slack
        features = self.features(time, task_features, free)
        modes = torch.cat((self.features.mode_inputs(features), self.features.risk_mode_inputs(features)), dim=-1)
        tasks = torch.cat((self.features.task_inputs(features), modes.flatten(start_dim=2)), dim=-1)
        embeddings = self.task_encoder(tasks).flatten(start_dim=1)
        context = (time, free, features['project_remaining'], features['project_slack'])
        return self.trunk(torch.cat((*context, embeddings), dim=1))


class MLPPolicy(nn.Module):
    """Task and mode heads on an MLP body; outputs are logits, which masked_joint_policy turns into probabilities."""

    def __init__(self, layout, body: nn.Module, embedding_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.layout = layout
        self.body = body
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.task_head = nn.Linear(hidden_dim, layout.n_tasks + 1)  # STOP is the last entry.
        self.mode_head = nn.Linear(hidden_dim, layout.n_tasks * layout.max_modes)  # Padded modes are masked later.

    def forward(self, time: Tensor, task_features: Tensor, free: Tensor) -> tuple[Tensor, Tensor]:
        hidden = self.body(time, task_features, free)
        return self.task_head(hidden), self.mode_head(hidden).reshape(-1, self.layout.n_tasks, self.layout.max_modes)


class MLPValue(nn.Module):
    """Sigmoid success head on its own MLP body: the probability of on-time completion."""

    def __init__(self, body: nn.Module, embedding_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.body = body
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.head = nn.Linear(hidden_dim, 1)

    def forward(self, time: Tensor, task_features: Tensor, free: Tensor) -> Tensor:
        return torch.sigmoid(self.head(self.body(time, task_features, free)))


def build(project, layout, config, policy_dimensions=None, value_dimensions=None):
    """Return the (policy, value) pair; both share one features module, which has no weights."""
    dimensions = (config.get('embedding_dim', 16), config.get('hidden_dim', 128))
    policy_sizes, value_sizes = policy_dimensions or dimensions, value_dimensions or dimensions
    features = SchedulingFeatures(project, layout)
    return (MLPPolicy(layout, MLPBody(project, layout, *policy_sizes, features=features), *policy_sizes),
            MLPValue(MLPBody(project, layout, *value_sizes, features=features), *value_sizes))
