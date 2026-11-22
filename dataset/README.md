# Dataset

- `test_instances/S/`: 60 instances with 5 to 12 workers
- `test_instances/L/`: 60 instances with 17 to 61 workers
- `generator/`: makes an instance from an MSLIB instance

Each instance has 30 tasks and comes from one MSLIB4 instance (Snauwaert & Vanhoucke, 2023). Teams of workers are
modes, each with a stochastic PERT duration, and the deadline is 1.25 times the makespan of a CP-SAT schedule on the
mean durations.

## Reading an instance

`test_instances/<set>/<MSLIB instance>/` holds the instance (`scenario_*.md`) and `instance.json` (its deadline and
the CP-SAT schedule behind it). Load it with

```python
from planner.core.scenario_file import load_project

project = load_project('dataset/test_instances/S/MSLIB_Set4_16/scenario_w7_t32_s0_seed0_df6d29cb.md')
project.workers, project.tasks, project.tpg_edges, project.deadline.delta, project.distributions
```

Times are in quarter days. Each task has modes; a mode gives each worker's dedication (in steps of 0.25) and a PERT
duration with minimum `a`, most likely value `b` and maximum `c`. A task's duration is a sample `X`, rounded up to
`ceil(max(0, X))`. The first and last tasks are milestones with zero duration. `tpg_edges` are the precedences.

## Generating instances

Download MSLIB version 2.2 (`MSLIB_v2_2.zip`) from its [releases](https://github.com/mariovanhoucke/MSLIB-Multi-Skilled-Resource-Constrained-Project-Library/releases), unzip it, unzip
`MSLIB_v2_2/MSLIB4.zip` inside it, then

    python -m dataset.generator.generate MSLIB_v2_2/MSLIB4/MSLIB_Set4_16.msrcp --output dataset/regenerated

Regenerated instances can differ slightly from `test_instances/`: CP-SAT's five-minute search and the last digits of
the PERT parameters depend on the machine, and in 8 L instances (MSLIB_Set4_633, 672, 768, 1428, 1615, 2223, 2334,
3542) a few modes differ, because the original generator's order of trying workers varied between runs. Use
`test_instances/` to reproduce the paper.
