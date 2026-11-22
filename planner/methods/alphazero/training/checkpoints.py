"""Save and load model checkpoints, and restore training state to resume a run.

Checkpoints hold only primitive data, so they load with PyTorch's weights-only loader.
"""

from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile

import torch
from torch import nn

from planner.core.project import Config, PathLike, Project, project_key
from planner.network.encoding import NeuralLayout, build_layout
from planner.network.policy import build_networks
from planner.methods.alphazero.training.replay_buffer import ReplayBuffer

# Settings that older checkpoints store, with the switched-off values loading accepts: greedy demonstrations
REMOVED_SETTINGS = {
    'greedy_replay_episodes': 0, 'greedy_replay_fraction': 0.0, 'greedy_replay_epsilon': 0.0,
    # and team formulations and networks, at their defaults
    'formulation': 'modes', 'network_architecture': 'baseline_features_risk', 'replay_capacity': None,
    'learning_rate_schedule': [],
    'decoder_entropy_weight': 0.0, 'transformer_width': 128, 'transformer_ff': 256, 'transformer_layers': 2,
    'transformer_heads': 4, 'transformer_attention': 'full', 'transformer_relation_bias': True,
    'transformer_zero_init': False, 'transformer_skip': False, 'proposal_teams': 2, 'proposal_widening': 0.5,
    'proposal_list_below': 0, 'proposal_heuristic': False, 'proposal_explore_temperature': 0.0,
    'proposal_diversity': 0.0, 'proposal_priors': 'network',
}


def save_checkpoint(
    path: PathLike, policy: nn.Module, value: nn.Module, project: Project, layout: NeuralLayout,
    config: Config, *, training_state: dict | None = None,
) -> None:
    """Atomically save weights, network sizes, settings, layout, and project key (plus optional training state)."""
    # Collect everything needed to rebuild the networks for this project
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    saved = {
        'project_key': project_key(project), 'layout': layout_record(layout), 'config': dict(config),
        'policy_dimensions': _dimensions(policy), 'value_dimensions': _dimensions(value),
        'policy': policy.state_dict(), 'value': value.state_dict(),
    }
    if training_state is not None:
        saved['training_state'] = training_state

    # Write to a temporary file and rename, so a failed save keeps the previous checkpoint
    with NamedTemporaryFile(dir=path.parent, prefix=path.name + '.', suffix='.tmp', delete=False) as temporary:
        temporary_path = Path(temporary.name)
    try:
        torch.save(saved, temporary_path)
        temporary_path.replace(path)
    finally:
        temporary_path.unlink(missing_ok=True)


def load_checkpoint(path: PathLike, project: Project) -> tuple[nn.Module, nn.Module, NeuralLayout, Config]:
    """Load models in evaluation mode, after checking they belong to this project."""
    # Check that the checkpoint belongs to this project
    saved = torch.load(path, map_location='cpu', weights_only=True)
    layout = build_layout(project)
    if saved['project_key'] != project_key(project) or saved['layout'] != layout_record(layout):
        raise ValueError('Checkpoint project or layout does not match')

    # Rebuild the networks and load their weights
    policy, value = build_networks(project, layout, saved['config'],
                                   policy_dimensions=saved['policy_dimensions'],
                                   value_dimensions=saved['value_dimensions'])
    policy.load_state_dict(saved['policy'])
    value.load_state_dict(saved['value'])
    policy.eval()
    value.eval()
    return policy, value, layout, saved['config']


def load_resumable_checkpoint(path: PathLike) -> dict:
    """Load a latest.pt checkpoint, which holds the training state needed to resume."""
    saved = torch.load(path, map_location='cpu', weights_only=True)
    if 'training_state' not in saved:
        raise ValueError('Checkpoint has no training state; weights-only checkpoints are evaluation-only')
    return saved


def restore_training(saved, project, layout, config, policy, value, optimizers, replay: ReplayBuffer, rng, device):
    """Restore weights, optimizers, replay buffer, random states, and metrics from a resumable checkpoint.

    Only episodes and device may differ from the saved settings.
    Returns (completed episodes, completed updates, metrics, inference metrics).
    """
    # Check that the checkpoint matches this project and these settings
    if saved['project_key'] != project_key(project) or saved['layout'] != layout_record(layout):
        raise ValueError('Checkpoint project or layout does not match')
    ignored = ('episodes', 'device')
    saved_config = dict(saved['config'])
    for key, off in REMOVED_SETTINGS.items():
        # Checkpoints that store such a setting resume only if it was switched off
        if saved_config.pop(key, off) != off:
            raise ValueError(f'Checkpoint uses {key}, which this code does not support')
    if ({key: value for key, value in saved_config.items() if key not in ignored}
            != {key: value for key, value in config.items() if key not in ignored}):
        raise ValueError('Resume settings must match the checkpoint except episodes and device')
    state = saved['training_state']
    if state['completed_episodes'] > config['episodes']:
        raise ValueError('Target episodes must be at least the completed checkpoint episode count')

    # Restore the weights, optimizers, and replay buffer
    policy.load_state_dict(saved['policy'])
    value.load_state_dict(saved['value'])
    for optimizer, optimizer_state in zip(optimizers, state['optimizers']):
        optimizer.load_state_dict(optimizer_state)
    replay.load_state_dict(state['replay'])

    # Restore the random states last: building the models already consumed random draws
    rng.bit_generator.state = state['numpy_rng']
    torch.set_rng_state(state['torch_rng'])
    if device.type == 'cuda' and state['cuda_rng'] is not None:
        torch.cuda.set_rng_state(state['cuda_rng'], device)
    return state['completed_episodes'], state['completed_updates'], state['metrics'], state['inference_metrics']


def _dimensions(network) -> tuple[int, int] | None:
    """Return (embedding_dim, hidden_dim) for networks sized by the config, or None for fixed-size ones."""
    if hasattr(network, 'embedding_dim') and hasattr(network, 'hidden_dim'):
        return (network.embedding_dim, network.hidden_dim)
    return None


def layout_record(layout: NeuralLayout) -> dict:
    """Return the task, mode, and worker IDs that fix the network input and output layout."""
    return {'task_ids': layout.task_ids, 'mode_ids': layout.mode_ids, 'worker_ids': layout.worker_ids}
