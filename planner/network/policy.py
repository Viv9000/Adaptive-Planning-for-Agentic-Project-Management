"""Policy and value networks, and the masked policy over legal actions."""

from __future__ import annotations

from collections.abc import Sequence

import torch
from torch import Tensor, nn

from planner.core.state import STOP, Action
from planner.network.encoding import NeuralLayout


def build_networks(project, layout, config, *, policy_dimensions=None, value_dimensions=None):
    """Build the policy and value networks (planner/network/networks.py); checkpoints pass their saved sizes."""
    from planner.network.networks import build
    return build(project, layout, config, policy_dimensions, value_dimensions)


def masked_joint_policy(
    policy: nn.Module, time: Tensor, task_features: Tensor, remaining_dedication: Tensor,
    layout: NeuralLayout, legal_actions: Sequence[Sequence[Action]],
) -> tuple[Tensor, Tensor]:
    """Return probabilities and log probabilities [B, A] over the action catalogue.

    P(START(task, mode)) = P(task) * P(mode | task) and P(STOP) = P(STOP), each softmax over legal choices only.
    Illegal actions get probability 0 (log -inf).
    """
    task_logits, mode_logits = policy(time, task_features, remaining_dedication)
    catalogue = _catalogue(layout, task_logits.device)
    legal = _legal_mask(layout, legal_actions, task_logits.device)

    # A task (or STOP) is legal when any of its actions is; a mode slot when its START is
    batch, n_tasks, n_modes = mode_logits.shape
    task_mask = torch.zeros((batch, n_tasks + 1), device=legal.device).index_add_(1, catalogue['task'], legal.float()) > 0
    mode_mask = torch.zeros((batch, n_tasks * n_modes + 1), dtype=torch.bool, device=legal.device)
    mode_mask[:, catalogue['slot']] = legal
    mode_mask = mode_mask[:, :-1].reshape(batch, n_tasks, n_modes)

    # Softmax over the legal tasks, then over each task's legal modes; a task with no legal mode gets finite
    # placeholder logits instead of all -inf, whose softmax would be NaN (its actions are masked below anyway)
    task_log = torch.log_softmax(task_logits.masked_fill(~task_mask, -torch.inf), dim=1)
    has_mode = mode_mask.any(dim=2, keepdim=True)
    mode_inputs = torch.where(mode_mask, mode_logits, torch.where(has_mode, -torch.inf, 0.0))
    mode_log = torch.log_softmax(mode_inputs, dim=2).flatten(start_dim=1)

    # Combine per action: log P(task) + log P(mode | task), with STOP's mode term 0, and -inf for illegal actions
    mode_log = torch.cat((mode_log, mode_log.new_zeros((batch, 1))), dim=1)
    log_probabilities = (task_log[:, catalogue['task']] + mode_log[:, catalogue['slot']]).masked_fill(~legal, -torch.inf)
    return log_probabilities.exp(), log_probabilities


_CATALOGUES: dict[tuple, dict[str, Tensor]] = {}


def _catalogue(layout: NeuralLayout, device) -> dict[str, Tensor]:
    """Return, per catalogue action, its task index (STOP: n_tasks) and flat mode slot (STOP: n_tasks * max_modes).

    Cached per layout and device, since a project's catalogue never changes. Built outside inference mode, since the
    first call is usually in a search and the same tensors are later used in training updates.
    """
    key = (layout.actions, layout.n_tasks, layout.max_modes, str(device))
    if key not in _CATALOGUES:
        task, slot = [], []
        for action in layout.actions:
            if action == STOP:
                task.append(layout.n_tasks)
                slot.append(layout.n_tasks * layout.max_modes)
            else:
                index = layout.task_index[action.task_id]
                task.append(index)
                slot.append(index * layout.max_modes + layout.mode_index[index][action.mode_id])
        with torch.inference_mode(False):
            _CATALOGUES[key] = {'task': torch.tensor(task, device=device), 'slot': torch.tensor(slot, device=device)}
    return _CATALOGUES[key]


def _legal_mask(layout: NeuralLayout, legal_actions: Sequence[Sequence[Action]], device) -> Tensor:
    """Return a [B, A] mask of the legal actions in catalogue order."""
    rows = [index for row, actions in enumerate(legal_actions) for index in [row] * len(actions)]
    columns = [layout.action_index[action] for actions in legal_actions for action in actions]
    mask = torch.zeros((len(legal_actions), layout.n_actions), dtype=torch.bool)
    mask[rows, columns] = True
    return mask.to(device)
