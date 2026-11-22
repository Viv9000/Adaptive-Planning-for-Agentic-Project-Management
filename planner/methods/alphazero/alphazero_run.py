"""The AlphaZero-based method: train policy and value networks by self-play with search, then search at each decision.

Training is in training/ (train.py), the graph search in mcts/, and the player that searches at each decision in
player.py; the networks are shared with PPO (planner/network).

Usage, from the repository root (the same options for every method):
    python -m planner.methods.alphazero.alphazero_run [--instances all|S|L|ID ...] [--seeds N ...] [--parallel K] [--output results]
Results go to results/runs/<instance>/alphazero/seed<seed>/; see planner/runner.py.
"""

from pathlib import Path

from planner.config import DEFAULT_SEARCH_CONFIG, DEFAULT_TRAINING_CONFIG, EPISODES_BY_GROUP
from planner.core.artifacts import write_json
from planner.methods.alphazero.mcts import MCTS
from planner.methods.alphazero.player import MCTSPlayer
from planner.methods.alphazero.training.checkpoints import load_checkpoint
from planner.methods.alphazero.training.train import train_sequential
from planner.network.inference import make_inference_callbacks
from planner.runner import main, run_method


def training_config(group, seed):
    """The paper's training settings, with the set's episodes."""
    return dict(DEFAULT_TRAINING_CONFIG, seed=seed, episodes=EPISODES_BY_GROUP[group])


def search_config():
    """The paper's evaluation search."""
    return dict(DEFAULT_SEARCH_CONFIG)


def contract(group, seed, settings):
    """The method settings frozen with a run."""
    return dict(training=training_config(group, seed), evaluation_search=search_config(),
                ppo=None)


def prepare(project, scenario, group, seed, folder, settings, identity):
    """Train, or resume from checkpoints/latest.pt; return the final networks and the evaluation search settings."""
    train = training_config(group, seed)
    final = folder / 'checkpoints' / 'final.pt'
    latest = final.with_name('latest.pt')
    if not final.exists():
        def progress(episode, metrics):
            if episode % 25 == 0:
                print(f'TRAIN {identity} {episode}/{train["episodes"]}', flush=True)
        _, _, metrics = train_sequential(scenario, train, checkpoint_path=final,
                                         resume_from=latest if latest.exists() else None, progress_callback=progress)
        write_json(folder / 'metrics.json', metrics)
    policy, value, layout, _ = load_checkpoint(final, project)
    return dict(policy=policy, value=value, layout=layout, search=search_config())


def make_player(mdp, prepared):
    """Search at every decision with the trained networks and take the most visited action."""
    prior, estimate = make_inference_callbacks(mdp, prepared['layout'], prepared['policy'], prepared['value'], 'cpu')
    return MCTSPlayer(MCTS(mdp, prior, estimate, prepared['search'], rng=None), explore=False)


def run(instances=('all',), seeds=None, parallel=1, output='results'):
    """Run the AlphaZero-based method on the test instances (all, S, L or IDs) and seeds (default: the paper's), and evaluate it."""
    run_method('alphazero', instances, seeds, parallel, Path(output))


if __name__ == '__main__':
    main('alphazero', __doc__)
