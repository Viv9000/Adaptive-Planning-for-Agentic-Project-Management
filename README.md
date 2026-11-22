# Beating the Clock: Adaptive Planning for Agentic Project Management

Code and dataset of the paper *Beating the Clock: Adaptive Planning for Agentic Project Management*

## Install

    pip install -r requirements.txt

## Run

    python -m planner.methods.greedy.greedy_run --instances S --parallel 8

The same works for `alphazero`, `ppo`, `cpsat`, `ga` and `sa`, with the paper's settings (`planner/config.py`).
Results go to `results/runs/`; print the tables with
`python -m planner.evaluate.tables --llm results/llm` (the LLM-based method's results are in `results/llm`).

For the LLM-based method, see [planner/methods/llm/README.md](planner/methods/llm/README.md).

## Data

The test instances are derived from MSLIB4 of the [MSLIB](https://github.com/mariovanhoucke/MSLIB-Multi-Skilled-Resource-Constrained-Project-Library) benchmark library: J. Snauwaert and
M. Vanhoucke, A classification and new benchmark instances for the multi-skilled resource-constrained project
scheduling problem, European Journal of Operational Research 307(1), 1–19, 2023,
https://doi.org/10.1016/j.ejor.2022.05.049.

## Contents

- `dataset/`: the 120 test instances (S, L) and their generator; see [dataset/README.md](dataset/README.md)
- `planner/core/`: the problem: projects, the MDP and the simulator
- `planner/methods/`: one folder per solution method
- `planner/evaluate/`: evaluation on shared sampled durations, and the tables
