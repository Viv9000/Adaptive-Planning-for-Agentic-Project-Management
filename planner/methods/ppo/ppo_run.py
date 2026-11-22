"""PPO: train the policy and value networks with PPO and the ranked reward, then act without search.

The PPO algorithm is in agent.py and the training with the ranked reward in training.py.

Usage, from the repository root (the same options for every method):
    python -m planner.methods.ppo.ppo_run [--instances all|S|L|ID ...] [--seeds N ...] [--parallel K] [--output results]
Results go to results/runs/<instance>/ppo/seed<seed>/; see planner/runner.py.
"""

from pathlib import Path

from dataclasses import asdict

from planner.config import DEFAULT_TRAINING_CONFIG, PPO_EPISODES
from planner.methods.ppo.agent import PPOPlayer, PPOSettings
from planner.methods.ppo.training import train
from planner.runner import main, run_method


def training_config(seed):
    """The paper's settings: the network sizes and ranked reward of planner/config.py, trained for PPO_EPISODES."""
    return dict(DEFAULT_TRAINING_CONFIG, seed=seed, episodes=PPO_EPISODES, checkpoint_every=0)


def contract(group, seed, settings):
    """The method settings frozen with a run."""
    return dict(training=training_config(seed), evaluation_search=None, ppo=asdict(PPOSettings()))


def prepare(project, scenario, group, seed, folder, settings, identity):
    """Train, or resume at a batch boundary from checkpoints/; return the trained agent."""
    config = training_config(seed)

    def progress(episode, metrics):
        print(f'TRAIN {identity} {episode}/{config["episodes"]} loss={metrics["loss"]:.4f}', flush=True)
    return train(project, config, folder / 'checkpoints', progress)


def make_player(mdp, agent):
    """Take the policy's most probable legal action."""
    return PPOPlayer(mdp, agent.policy, agent.layout)


def run(instances=('all',), seeds=None, parallel=1, output='results'):
    """Run PPO on the test instances (all, S, L or IDs) and seeds (default: the paper's), and evaluate it."""
    run_method('ppo', instances, seeds, parallel, Path(output))


if __name__ == '__main__':
    main('ppo', __doc__)
