"""Fixed action layout for one project, state features, and training targets."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

import torch
from torch import Tensor

from planner.core.mdp import MDP
from planner.core.project import Project
from planner.core.state import STOP, Action, Start, State


@dataclass(frozen=True, slots=True)
class NeuralLayout:
    """Fixed tensor indices for one project's tasks, modes, workers, and actions.

    The action catalogue is every START(task, mode) in project order, then STOP; mode indices are per task.
    """

    task_ids: tuple[str, ...]
    mode_ids: tuple[tuple[int, ...], ...]
    worker_ids: tuple[str, ...]
    task_index: dict[str, int]
    mode_index: tuple[dict[int, int], ...]
    worker_index: dict[str, int]
    actions: tuple[Action, ...]
    action_index: dict[Action, int]
    n_tasks: int
    n_workers: int
    max_modes: int
    n_actions: int


def build_layout(project: Project) -> NeuralLayout:
    """Build the layout from the project's stored order."""
    task_ids = tuple(task.id for task in project.tasks)
    mode_ids = tuple(tuple(mode.id for mode in task.modes) for task in project.tasks)
    worker_ids = tuple(worker.id for worker in project.workers)
    actions = tuple(Start(task.id, mode.id) for task in project.tasks for mode in task.modes) + (STOP,)
    return NeuralLayout(
        task_ids=task_ids,
        mode_ids=mode_ids,
        worker_ids=worker_ids,
        task_index={task_id: index for index, task_id in enumerate(task_ids)},
        mode_index=tuple({mode_id: index for index, mode_id in enumerate(ids)} for ids in mode_ids),
        worker_index={worker_id: index for index, worker_id in enumerate(worker_ids)},
        actions=actions,
        action_index={action: index for index, action in enumerate(actions)},
        n_tasks=len(task_ids),
        n_workers=len(worker_ids),
        max_modes=max(map(len, mode_ids), default=0),
        n_actions=len(actions),
    )


def encode_state(state: State, mdp: MDP, layout: NeuralLayout) -> tuple[Tensor, Tensor, Tensor]:
    """Return (time [1, 1], task features [1, N, K + 5], free dedication [1, W]).

    Task feature columns: status one-hot (unstarted, active, completed), selected mode one-hot (K),
    days since start / deadline, and the pending flag. Time is day / deadline.
    """
    deadline = mdp.project.deadline.delta
    time = torch.tensor([[state.day / deadline]], dtype=torch.float32)

    # Mark every task unstarted, then overwrite the completed and active ones
    features = torch.zeros((1, layout.n_tasks, layout.max_modes + 5), dtype=torch.float32)
    features[0, :, 0] = 1
    for task_id in state.completed:
        index = layout.task_index[task_id]
        features[0, index, 0] = 0
        features[0, index, 2] = 1

    # Active tasks also get their mode, their age, and the pending flag
    for record in state.active:
        index = layout.task_index[record.task_id]
        features[0, index, 0] = 0
        features[0, index, 1] = 1
        features[0, index, 3 + layout.mode_index[index][record.mode_id]] = 1
        features[0, index, -2] = (state.day - record.start_day) / deadline
        features[0, index, -1] = record.pending

    # Free dedication per worker, in layout order
    remaining = mdp.remaining_dedication(state)
    dedication = torch.tensor([[remaining[key] for key in layout.worker_ids]], dtype=torch.float32)
    return time, features, dedication


def encode_batch(states, mdp: MDP, layout: NeuralLayout, device) -> tuple[Tensor, Tensor, Tensor]:
    """Encode several states and stack them into batched (time, task features, free dedication) tensors."""
    encoded = [encode_state(state, mdp, layout) for state in states]
    return tuple(torch.cat(parts).to(device) for parts in zip(*encoded))


def policy_to_tensor(pi: Mapping[Action, float], layout: NeuralLayout) -> Tensor:
    """Return a policy over actions as a vector over the action catalogue (zero for missing actions)."""
    vector = torch.zeros(layout.n_actions, dtype=torch.float32)
    for action, probability in pi.items():
        vector[layout.action_index[action]] = probability
    return vector
