"""PPO training with the ranked reward, resumable at batch boundaries."""

from dataclasses import asdict
import json
from pathlib import Path
from time import perf_counter

import numpy as np
import torch

from planner.methods.ppo.agent import PPO, PPOSettings
from planner.core.project import project_key
from planner.network.ranked_reward import Curriculum


def training_seed(seed, episode):
    """The duration seed of a training episode, derived so it never coincides with an evaluation future's seed."""
    return int(np.random.SeedSequence([seed, episode, 20261115]).generate_state(1, dtype=np.uint64)[0])


def restore_journal(path, completed, last_batch):
    """Make progress.jsonl match the checkpoint after an interruption.

    Drops lines of batches after the checkpoint (and a half-written last line), and adds the checkpoint's last batch if
    the run stopped between saving the checkpoint and writing its line.
    """
    rows = []
    if path.exists():
        lines = path.read_text().splitlines()
        for index, line in enumerate(lines):
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                if index != len(lines) - 1:
                    raise
                break
            if row['episode'] <= completed:
                rows.append(row)
    if last_batch is not None and (not rows or rows[-1]['episode'] < completed):
        rows.append(last_batch)
    path.write_text(''.join(json.dumps(row) + '\n' for row in rows))


def train(project, config, root, progress=None, settings=None):
    """Train PPO for config['episodes'] episodes, or resume from root/latest.pt, and return the agent.

    Each batch: fix the ranked bar, collect settings.episodes_per_batch episodes, update the networks, then move the
    bar with the batch's completion days. latest.pt is saved after every batch, and progress.jsonl gets one line.
    """
    session_started = perf_counter()
    settings = settings or PPOSettings()
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    checkpoint = root / 'latest.pt'
    journal = root / 'progress.jsonl'
    agent = PPO(project, config, settings)
    identity = dict(project_key=project_key(project), config=config, ppo=asdict(settings))
    completed, seconds, last_batch = 0, 0.0, None
    previous_seconds = 0.0
    # Resume from the last finished batch, or start: drawing the curriculum's random rollouts counts as training time
    if checkpoint.exists():
        # Only this runner's own trusted local checkpoints are loaded.
        saved = torch.load(checkpoint, map_location='cpu', weights_only=False)
        if saved['identity'] != identity:
            raise ValueError('PPO checkpoint project or settings differ')
        agent.policy.load_state_dict(saved['policy'])
        agent.value.load_state_dict(saved['value'])
        agent.optimizer.load_state_dict(saved['optimizer'])
        agent.rng.bit_generator.state = saved['rng']
        torch.set_rng_state(saved['torch_rng'])
        agent.environment_steps = saved['environment_steps']
        agent.optimizer_steps = saved['optimizer_steps']
        curriculum = Curriculum(project, config, saved=saved['curriculum'])
        completed, seconds, last_batch = saved['completed'], saved['training_seconds'], saved['last_batch']
        previous_seconds = seconds
    else:
        started = perf_counter()
        curriculum = Curriculum(project, config)
        seconds = perf_counter() - started
    restore_journal(journal, completed, last_batch)
    while completed < config['episodes']:
        # Fix the ranked bar for this batch
        started = perf_counter()
        context = curriculum.episode_context(completed + 1)
        curriculum.state['context'] = context
        mdp = curriculum.training_mdp(context)
        count = min(settings.episodes_per_batch, config['episodes'] - completed)
        # Collect the batch's episodes, checking each played schedule
        trajectories, outcomes = [], []
        for episode in range(completed + 1, completed + count + 1):
            trajectory = agent.collect(mdp, training_seed(config['seed'], episode), check_schedule=True)
            trajectories.append(trajectory)
            outcomes.append(dict(episode=episode, completion=trajectory.terminal.day,
                                 success=bool(mdp.success_indicator(trajectory.terminal)),
                                 reward=trajectory.reward, decisions=len(trajectory.states)))
        collection_seconds = perf_counter() - started
        # Rewards stay fixed for PPO's on-policy update; only future batches get the new bar.
        for trajectory in trajectories:
            curriculum.record_completion(trajectory.terminal.day, mdp.is_complete(trajectory.terminal))
        updated = perf_counter()
        metrics = agent.update(mdp, trajectories)
        completed += count
        seconds = previous_seconds + perf_counter() - session_started
        last_batch = dict(episode=completed, context=context, outcomes=outcomes, **metrics,
                          collection_seconds=collection_seconds, update_seconds=perf_counter() - updated,
                          training_seconds=seconds, allocated_cpu_hours=seconds / 3600, threads=1)
        # Save the checkpoint atomically, then log the batch
        saved = dict(identity=identity, policy=agent.policy.state_dict(), value=agent.value.state_dict(),
                     optimizer=agent.optimizer.state_dict(), rng=agent.rng.bit_generator.state,
                     torch_rng=torch.get_rng_state(), environment_steps=agent.environment_steps,
                     optimizer_steps=agent.optimizer_steps, curriculum=curriculum.state,
                     completed=completed, training_seconds=seconds, last_batch=last_batch)
        temporary = checkpoint.with_suffix('.tmp')
        torch.save(saved, temporary)
        temporary.replace(checkpoint)
        with journal.open('a') as stream:
            stream.write(json.dumps(last_batch) + '\n')
        if progress:
            progress(completed, last_batch)
    agent.policy.eval()
    agent.value.eval()
    return agent
