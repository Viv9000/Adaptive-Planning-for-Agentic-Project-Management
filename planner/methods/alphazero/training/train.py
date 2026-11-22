"""Sequential training: one process plays self-play episodes on one project and updates the networks after each.

Used by the evaluation runners to train one network on one project.

Input: a scenario file and the training settings (defaults in planner/config.py, DEFAULT_TRAINING_CONFIG).
Output: the trained policy and value networks, per-episode metrics, and the checkpoints described below.

Setup:
- Build the policy and value networks , one Adam optimizer each, an empty replay
  buffer (planner/methods/alphazero/training/replay_buffer.py), and the curriculum (planner/network/ranked_reward.py).

Training loop, repeated once per episode until config['episodes'] episodes are done:
1. Context: the curriculum sets the episode's ranked bar (planner/network/ranked_reward.py).
2. Self-play: play one episode from day 0 with the MCTS player, sampling each move from the visit distribution
   (planner/methods/alphazero/training/self_play.py); every decision gives a sample (state, visit distribution, episode return).
3. Store: add the episode's samples and outcome (completion day, finished) to the replay buffer, dropping the oldest episodes,
   and give the curriculum the completion day (it moves the ranked bar).
4. Update the networks: once the replay buffer holds a batch, run updates_per_episode updates (planner/methods/alphazero/training/network_update.py);
   each draws a random batch from the replay buffer (value targets relabeled under the current
   reward), and takes one gradient step on the policy loss (cross-entropy to the visit distribution) and the value
   loss (binary cross-entropy to the return).
5. Save: latest.pt (weights, optimizers, replay buffer, curriculum, random states) for resuming, and every checkpoint_every
   episodes a weights-only checkpoint for learning curves.

At the end: the final checkpoint.
Metrics, one value per episode: success by the final deadline (whatever the curriculum), completion day, return,
decisions, search statistics, replay buffer size, the ranked bar, losses and learning rate per update, and timings.
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime
import math
from pathlib import Path
from time import perf_counter
import resource
from typing import TypeAlias

from numpy.random import default_rng
import torch
from torch import nn

from planner.core.project import Config, PathLike
from planner.core.scenario_file import load_project
from planner.config import DEFAULT_TRAINING_CONFIG
from planner.methods.alphazero.mcts import MCTS
from planner.methods.alphazero.mcts.metrics import PER_DECISION_MEANS
from planner.network.encoding import build_layout
from planner.network.inference import make_inference_callbacks
from planner.network.policy import build_networks
from planner.methods.alphazero.training.checkpoints import load_resumable_checkpoint, restore_training, save_checkpoint
from planner.network.ranked_reward import Curriculum, TrainingMDP, validate_curriculum
from planner.methods.alphazero.training.self_play import generate_episode
from planner.methods.alphazero.training.replay_buffer import ReplayBuffer
from planner.methods.alphazero.training.network_update import update_from_replay

TrainingMetrics: TypeAlias = dict[str, list[float]]


def train_sequential(
    scenario_path: PathLike, config: Config, *,
    checkpoint_path: PathLike | None = None,
    progress_callback: Callable[[int, dict], None] | None = None,
    resume_from: PathLike | None = None,
) -> tuple[nn.Module, nn.Module, TrainingMetrics]:
    """Train policy and value networks on one scenario and return them with per-episode metrics.

    Each episode: play one self-play game, add it to the replay buffer, then run updates once the replay buffer holds a batch.
    latest.pt is saved after every episode for resuming; resume_from continues up to config['episodes'] in total.
    The success metric always uses the project's final deadline, whatever the curriculum.
    """
    # Check the settings and choose the checkpoint paths
    config = dict(DEFAULT_TRAINING_CONFIG, **config)
    _validate_config(config)
    checkpoint = _final_checkpoint_path(scenario_path, config, checkpoint_path)
    latest_checkpoint = checkpoint.with_name('latest.pt')
    if latest_checkpoint == checkpoint:
        raise ValueError('checkpoint_path must differ from the resumable latest.pt path')

    # Seed the random generators and load the project
    torch.manual_seed(config['seed'])
    rng = default_rng(config['seed'])
    project = load_project(scenario_path)
    saved = None if resume_from is None else load_resumable_checkpoint(resume_from)
    curriculum = Curriculum(project, config, None if saved is None else saved['training_state']['curriculum'])

    # Build the networks, optimizers, and replay buffer
    layout = build_layout(project)
    policy, value = build_networks(project, layout, config)
    policy.to(config['device'])
    value.to(config['device'])
    optimizers = (torch.optim.Adam(policy.parameters(), lr=config['learning_rate']),
                  torch.optim.Adam(value.parameters(), lr=config['learning_rate']))
    device = next(policy.parameters()).device
    replay = ReplayBuffer(config['replay_episodes'])
    metrics = {}
    inference_metrics = {}
    completed = completed_updates = 0

    # Continue from the checkpoint when resuming
    if saved is not None:
        completed, completed_updates, metrics, inference_metrics = restore_training(
            saved, project, layout, config, policy, value, optimizers, replay, rng, device,
        )
        del saved

    def record(name, number):
        metrics.setdefault(name, []).append(float(number))

    def evaluation_config():
        """Return the settings saved with weights-only checkpoints."""
        return config

    def save_latest_checkpoint(episode):
        training_state = {
            'completed_episodes': episode,
            'completed_updates': completed_updates,
            'optimizers': [optimizer.state_dict() for optimizer in optimizers],
            'replay': replay.state_dict(),
            'numpy_rng': rng.bit_generator.state,
            'torch_rng': torch.get_rng_state(),
            'cuda_rng': torch.cuda.get_rng_state(device) if device.type == 'cuda' else None,
            'metrics': metrics,
            'inference_metrics': inference_metrics,
            'curriculum': curriculum.state,
        }
        save_checkpoint(latest_checkpoint, policy, value, project, layout, config, training_state=training_state)

    for episode in range(completed, config['episodes']):
        # Choose this episode's ranked bar
        started = perf_counter()
        context = curriculum.episode_context(episode + 1)
        # The MDP and planner are built once; each episode only moves the bar, and the replay buffer is relabeled
        if episode == completed:
            mdp = curriculum.training_mdp(context)
            prior_fn, value_fn = make_inference_callbacks(mdp, layout, policy, value, config['device'], inference_metrics)
            planner = MCTS(mdp, prior_fn, value_fn, config, rng)
            # Updates use the same rules without a cutoff: the replay buffer may hold states past the current cutoff.
            update_mdp = TrainingMDP(mdp.project, None)
        mdp.threshold = context['threshold']
        record('ranked_threshold', context['threshold'])
        curriculum.state['context'] = context
        record('training_deadline', context['deadline'])

        # Play one self-play episode and record its outcome and search statistics
        policy.eval()
        value.eval()
        samples, terminal, search = generate_episode(mdp, planner, layout, rng)
        finished = mdp.is_complete(terminal)
        success = int(finished and terminal.day <= project.deadline.delta)
        record('episode_seconds', perf_counter() - started)
        record('decisions', len(samples))
        record('success', success)
        for name, number in search.items():
            record(name, number / len(samples) if name in PER_DECISION_MEANS else number)
        record('search_seconds_per_decision', search['search_seconds'] / len(samples))
        record('completion_day', terminal.day)
        record('episode_completed', finished)
        record('training_return', mdp.terminal_return(terminal))
        curriculum.record_completion(terminal.day, finished)

        # Add the episode to the replay buffer
        replay.add_episode(samples, terminal.day, finished)
        record('replay_size', len(replay))

        # Update the networks once the replay buffer holds a full batch
        started = perf_counter()
        if len(replay) >= config['batch_size']:
            for _ in range(config['updates_per_episode']):
                losses = update_from_replay(replay, curriculum, update_mdp, layout, policy, value, optimizers,
                                       config['batch_size'], rng)
                completed_updates += 1
                record('learning_rate', config['learning_rate'])
                for name, number in losses.items():
                    record(name, number)
        record('update_seconds', perf_counter() - started)

        # Save a resumable checkpoint, plus a copy every checkpoint_every episodes for evaluating progress
        save_latest_checkpoint(episode + 1)
        if config['checkpoint_every'] and (episode + 1) % config['checkpoint_every'] == 0:
            save_checkpoint(checkpoint.with_name(f'episode_{episode + 1:05}.pt'), policy, value, project, layout,
                            evaluation_config())
        if progress_callback is not None:
            latest = {name: numbers[-1] for name, numbers in metrics.items()}
            latest['success_rate'] = sum(metrics['success']) / len(metrics['success'])
            progress_callback(episode + 1, latest)

    # Save latest.pt even when resuming found nothing left to do
    if completed == config['episodes']:
        save_latest_checkpoint(completed)

    # Record run-level metrics and save the final checkpoint
    for name, number in inference_metrics.items():
        record(name, number)
    record('process_lifetime_peak_rss_kib', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    save_checkpoint(checkpoint, policy, value, project, layout, evaluation_config())
    return policy, value, metrics


def _validate_config(config: Config) -> None:
    """Check sizes, the learning rate and the curriculum."""
    # Check the sizes
    for name in ('episodes', 'replay_episodes', 'batch_size', 'updates_per_episode', 'embedding_dim', 'hidden_dim'):
        if not isinstance(config[name], int) or config[name] < 1:
            raise ValueError(f'{name} must be a positive integer')
    if type(config['checkpoint_every']) is not int or config['checkpoint_every'] < 0:
        raise ValueError('checkpoint_every must be a nonnegative integer')

    # Check the learning rate and the curriculum
    if not math.isfinite(config['learning_rate']) or config['learning_rate'] <= 0:
        raise ValueError('learning_rate must be finite and positive')
    validate_curriculum(config)


def _final_checkpoint_path(scenario_path: PathLike, config: Config, checkpoint_path: PathLike | None) -> Path:
    """Return checkpoint_path, or a dated default under checkpoints/."""
    if checkpoint_path is not None:
        return Path(checkpoint_path)
    now = datetime.now()
    details = (f'{Path(scenario_path).stem}_seed{config["seed"]}_episodes{config["episodes"]}'
               f'_search{config["search_budget"]}_embed{config["embedding_dim"]}_hidden{config["hidden_dim"]}')
    return Path('checkpoints') / now.strftime('%Y-%m-%d') / details / now.strftime('%H-%M-%S-%f') / 'final.pt'
