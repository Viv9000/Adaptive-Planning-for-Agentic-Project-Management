"""Fixed project data: workers, tasks, modes, deadline, and the project content key."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from graphlib import TopologicalSorter
import hashlib
import json
from numbers import Integral, Real
from pathlib import Path
from types import MappingProxyType
from typing import Any, Literal, TypeAlias

from planner.core.distributions import DurationDistribution


Config: TypeAlias = dict[str, Any]
PathLike: TypeAlias = str | Path
TPGEdges: TypeAlias = tuple[tuple[str, str], ...]

CAPACITY_TOLERANCE = 1e-9
SCHEMA_VERSION = 2
VALIDATION_VERSION = 6


@dataclass(frozen=True, slots=True)
class Worker:
    """A worker; every worker has capacity one."""

    id: str


@dataclass(frozen=True, slots=True)
class Mode:
    """One way to run a task: worker dedications (multiples of 1/N) and a duration distribution key."""

    id: int
    dedication: Mapping[str, float]
    distribution_hash: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "dedication", MappingProxyType(dict(self.dedication)))


@dataclass(frozen=True, slots=True)
class Task:
    """A task and its modes; a milestone has one zero-duration mode with no workers."""

    id: str
    modes: tuple[Mode, ...] = ()
    milestone: bool = False


@dataclass(frozen=True, slots=True)
class Deadline:
    """Project deadline in working days."""

    delta: int


@dataclass(frozen=True, slots=True)
class ValidationReport:
    """Correctness and triviality result for one project_key.

    is_trivial is None when unchecked; classification says why a project is trivial.
    """

    project_key: str
    is_correct: bool
    is_trivial: bool | None = None
    classification: Literal["guaranteed_success", "impossible", "no_decisions", "unclassified"] | None = None
    errors: tuple[str, ...] = ()
    reasons: tuple[str, ...] = ()
    structural_flags: tuple[str, ...] = ()
    validation_version: int = VALIDATION_VERSION


@dataclass(frozen=True, slots=True)
class Project:
    """Scheduling data in stored worker/task/mode order.

    tpg_edges are (predecessor, successor) pairs; distributions maps content keys to distributions.
    The cached validation report is not part of project_key.
    """

    workers: tuple[Worker, ...]
    tasks: tuple[Task, ...]
    tpg_edges: TPGEdges
    deadline: Deadline
    distributions: Mapping[str, DurationDistribution]
    schema_version: int = SCHEMA_VERSION
    n_dedication_levels: int = 2
    validation: ValidationReport | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "distributions", MappingProxyType(dict(self.distributions)))


def longest_paths(project: Project, durations: Mapping[str, Any], zero: Any = 0.0) -> dict[str, Any]:
    """Return each task's duration plus the longest chain of successors after it, in precedence order.

    With every task taking durations[task] and unlimited workers, no schedule can finish the project sooner than
    that after starting the task; the largest value is the critical path. Works for any numbers that add and compare,
    e.g. ints, floats, or 0-dimensional tensors (so tensor features stay bit-for-bit those of tensor arithmetic);
    zero is the value after the last tasks.
    """
    predecessors = {task.id: [] for task in project.tasks}
    successors = {task.id: [] for task in project.tasks}
    for before, after in project.tpg_edges:
        predecessors[after].append(before)
        successors[before].append(after)

    # From the last tasks backwards, so every successor is done before its predecessors
    paths = {}
    for task_id in reversed(tuple(TopologicalSorter(predecessors).static_order())):
        paths[task_id] = durations[task_id] + max((paths[successor] for successor in successors[task_id]), default=zero)
    return paths


def project_key(project: Project) -> str:
    """Hash all scheduling data (not generation settings or validation reports)."""
    data = project_record(project)
    data["schema_version"] = project.schema_version
    data["n_dedication_levels"] = project.n_dedication_levels

    # Sort mappings as (key, value) pairs so invalid key types still hash distinctly
    data["distributions"] = sorted(data["distributions"].items(), key=lambda pair: repr(pair[0]))
    for task in data["tasks"]:
        for mode in task["modes"]:
            mode["dedication"] = sorted(mode["dedication"].items(), key=lambda pair: repr(pair[0]))
    return content_hash(data)


def project_record(project: Project) -> dict[str, Any]:
    """Return the project as plain data, as saved in a scenario file's Data block."""
    # Distributions: a table of probabilities, or the family's parameters
    distributions = {}
    for key, distribution in project.distributions.items():
        record: dict[str, Any] = {"family": distribution.family}
        if distribution.family == "tabular":
            record["probabilities"] = {int(day): float(p) for day, p in distribution.probabilities.items()}
        else:
            record.update({name: float(value) for name, value in distribution.parameters.items()})
        distributions[key] = record

    # Tasks with their modes
    tasks = []
    for task in project.tasks:
        modes = [
            {"id": mode.id, "dedication": dict(mode.dedication), "distribution_hash": mode.distribution_hash}
            for mode in task.modes
        ]
        tasks.append({"id": task.id, "milestone": task.milestone, "modes": modes})

    workers = [{"id": worker.id} for worker in project.workers]
    return {
        "workers": workers,
        "distributions": distributions,
        "tasks": tasks,
        "tpg_edges": [list(edge) for edge in project.tpg_edges],
        "deadline": {"delta": project.deadline.delta},
    }


def task_distribution_hash(task: Task) -> str | None:
    """Return the duration key all the task's modes share, or None when they differ."""
    hashes = {mode.distribution_hash for mode in task.modes}
    return hashes.pop() if len(hashes) == 1 else None


def content_hash(data: Any) -> str:
    """Return the SHA-256 hash of canonical JSON."""
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":"), default=_json_number)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _json_number(value: Any) -> int | float:
    """Convert NumPy numbers for JSON; reject other objects."""
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        return float(value)
    raise TypeError(f"Cannot serialize {type(value).__name__}")
