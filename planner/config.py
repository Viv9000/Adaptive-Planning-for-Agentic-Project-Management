"""The paper's settings, in one place: every default here is the value used in the paper's evaluation."""


# Search (MCTS) ------------------------------------------------------------------------------------------------

# Evaluation search: no root noise, the most visited action is taken.
DEFAULT_SEARCH_CONFIG = {
    "search_budget": 800,  # Simulations at the first searched decision of each day.
    "c_puct": 1.5,  # Exploration weight in the PUCT score.
    "root_noise_fraction": 0.0,  # Share of Dirichlet noise in the root priors; training uses 0.25.
    "root_noise_concentration": 10.0,  # Dirichlet alpha per legal action = concentration / action count.
    "top_up_visits": 25,  # The day's later searched decisions only top their reused root up to this many visits.
}


# Training -----------------------------------------------------------------------------------------------------

DEFAULT_TRAINING_CONFIG = {
    "device": "cpu",
    "seed": 48,
    "embedding_dim": 16,  # Task embedding size in both networks.
    "hidden_dim": 128,  # Trunk width in both networks.
    "episodes": 1500,  # Instances of S; see EPISODES_BY_GROUP.
    "replay_episodes": 300,  # Replay buffer size: all decisions of the most recent episodes.
    "checkpoint_every": 50,  # Also save checkpoints/episode_NNNNN.pt every this many episodes; 0 disables.
    "batch_size": 32,
    "updates_per_episode": 8,  # Gradient steps per network after each episode.
    "learning_rate": 1e-3,
    "search_budget": 400,  # Training search: simulations at the first searched decision of each day.
    "c_puct": DEFAULT_SEARCH_CONFIG["c_puct"],
    "root_noise_fraction": 0.25,  # Share of Dirichlet noise in the root priors during training.
    "root_noise_concentration": DEFAULT_SEARCH_CONFIG["root_noise_concentration"],
    "top_up_visits": DEFAULT_SEARCH_CONFIG["top_up_visits"],
    # Ranked reward (planner/network/ranked_reward.py)
    "curriculum_rollouts": 100,  # Random rollouts whose completion days set the first bar.
    "ranked_percentile": 0.75,  # Reward 1 for beating this share of recent completion days.
    "ranked_window": 100,  # Number of recent completion days that set the bar.
}

# Training episodes of the AlphaZero-based method per instance set (S: 5-12 workers, L: 17-61).
EPISODES_BY_GROUP = {"S": 1500, "L": 2500}


# Evaluation ---------------------------------------------------------------------------------------------------

# The shared futures: future seed s fixes the realized duration of every task and mode in that episode.
EVALUATION_FUTURES = tuple(range(10_000, 10_500))

# Seeds of each method's three runs per instance; greedy is deterministic and runs once.
SEEDS = {
    "alphazero": (48, 49, 50),
    "ppo": (20000, 20001, 20002),
    "ga": (20000, 20001, 20002),
    "sa": (20000, 20001, 20002),
    "cpsat": (2026, 2027, 2028),
    "greedy": (0,),
}


# Methods ------------------------------------------------------------------------------------------------------

PPO_EPISODES = 50_000  # Training episodes of PPO, with DEFAULT_TRAINING_CONFIG's network and ranked reward.
SCHEDULE_EVALUATIONS = 500_000  # Schedules assessed by each GA and SA run.
CPSAT_SECONDS = 3600  # Time limit of each CP-SAT solve.
CPSAT_THREADS = 8  # CP-SAT search workers; preparation time counts wall time times this.
