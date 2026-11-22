"""Project correctness checks and triviality classification."""

from __future__ import annotations

from dataclasses import replace
from graphlib import CycleError, TopologicalSorter
import math
from numbers import Integral, Real

from planner.core.distributions import distribution_key, duration_bounds
from planner.core.project import (
    CAPACITY_TOLERANCE, SCHEMA_VERSION, VALIDATION_VERSION, Project, ValidationReport, longest_paths, project_key,
)


def validate_project(project: Project, check_triviality: bool = False) -> ValidationReport:
    """Return a correctness report, reusing the project's cached report when it is current.

    Checks: schema version, positive dedication levels and deadline, nonempty unique IDs,
    known and acyclic precedence edges, distribution keys matching their specifications,
    positive unique mode IDs with known distributions, milestone rules,
    and dedications that are positive, at most one, and on the j/N grid.
    """
    # Hash the project; data that cannot be hashed is invalid
    try:
        key = project_key(project)
    except (AttributeError, TypeError, ValueError) as error:
        return ValidationReport("", False, errors=(f"Invalid project data: {error}",))

    # Reuse the cached report if it describes this project under the current rules
    cached = project.validation
    if cached is not None and cached.project_key == key and cached.validation_version == VALIDATION_VERSION:
        if check_triviality and cached.is_correct and cached.is_trivial is None:
            return assess_triviality(project, cached)
        return cached

    # Check the project-wide settings
    errors = []
    if not isinstance(project.schema_version, Integral) or project.schema_version != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    levels = project.n_dedication_levels
    valid_levels = isinstance(levels, Integral) and levels > 0
    if not valid_levels:
        errors.append("n_dedication_levels must be a positive integer")
    if not isinstance(project.deadline.delta, Integral) or project.deadline.delta <= 0:
        errors.append("deadline.delta must be a positive integer")

    # Check the IDs, precedence edges, distributions, and each task
    worker_ids = _collect_ids(project.workers, "worker", errors)
    task_ids = _collect_ids(project.tasks, "task", errors)
    _check_edges(project, task_ids, errors)
    for saved_key, distribution in project.distributions.items():
        if saved_key != distribution_key(distribution):
            errors.append(f"Distribution key {saved_key!r} does not match its specification")
    for task in project.tasks:
        _check_task(project, task, worker_ids, levels if valid_levels else None, errors)

    report = ValidationReport(key, not errors, errors=tuple(errors))
    if report.is_correct and check_triviality:
        return assess_triviality(project, report)
    return report


def _collect_ids(records: tuple, kind: str, errors: list[str]) -> set[str]:
    """Return the valid IDs, recording empty, invalid, and duplicate IDs as errors."""
    ids = set()
    if not records:
        errors.append(f"Project must have at least one {kind}")
    for record in records:
        if not isinstance(record.id, str) or not record.id:
            errors.append(f"{kind} ID must be a nonempty string: {record.id!r}")
        elif record.id in ids:
            errors.append(f"Duplicate {kind} ID: {record.id}")
        else:
            ids.add(record.id)
    return ids


def _check_edges(project: Project, task_ids: set[str], errors: list[str]) -> None:
    """Record unknown or malformed precedence edges and cycles."""
    valid_edges = True
    for edge in project.tpg_edges:
        unknown_task = any(not isinstance(task_id, str) or task_id not in task_ids for task_id in edge)
        if len(edge) != 2 or unknown_task:
            errors.append(f"Invalid precedence edge: {edge!r}")
            valid_edges = False
    if valid_edges and len(task_ids) == len(project.tasks):
        try:
            precedence_order(project)
        except CycleError as error:
            errors.append(f"Precedence cycle: {error.args[1]}")


def _check_task(project: Project, task, worker_ids: set[str], levels: int | None, errors: list[str]) -> None:
    """Record mode, milestone, and dedication errors for one task; levels is None when invalid."""
    # Check the task's modes and milestone flag
    context = f"Task {task.id}"
    if not isinstance(task.milestone, bool):
        errors.append(f"{context}: milestone must be true or false")
    if not task.modes:
        errors.append(f"{context}: at least one mode is required")
    if task.milestone and task.modes and len(task.modes) != 1:
        errors.append(f"{context}: milestone requires exactly one mode")

    mode_ids = set()
    for mode in task.modes:
        # Check the mode ID
        mode_context = f"{context}, mode {mode.id}"
        if not isinstance(mode.id, Integral) or mode.id <= 0:
            errors.append(f"{mode_context}: mode ID must be a positive integer")
        elif mode.id in mode_ids:
            errors.append(f"{mode_context}: duplicate mode ID")
        else:
            mode_ids.add(mode.id)

        # Check the distribution; a milestone takes no time and needs no workers
        distribution = None
        if isinstance(mode.distribution_hash, str):
            distribution = project.distributions.get(mode.distribution_hash)
        if distribution is None:
            errors.append(f"{mode_context}: unknown distribution hash {mode.distribution_hash!r}")
        if task.milestone:
            if mode.dedication:
                errors.append(f"{mode_context}: milestone requires empty worker dedication")
            if distribution is not None and (distribution.family != "tabular" or distribution.probabilities != {0: 1}):
                errors.append(f"{mode_context}: milestone requires tabular duration {{0: 1}}")

        # Check each dedication: a known worker, in (0, 1], on the j/N grid
        for worker_id, dedication in mode.dedication.items():
            dedication_context = f"{mode_context}, worker {worker_id}"
            if worker_id not in worker_ids:
                errors.append(f"{dedication_context}: unknown worker")
            if not isinstance(dedication, Real) or not math.isfinite(dedication) or dedication <= 0:
                errors.append(f"{dedication_context}: dedication must be finite and positive")
                continue
            if dedication > 1 + CAPACITY_TOLERANCE:
                errors.append(f"{dedication_context}: dedication exceeds unit capacity")
                continue
            if levels is not None:
                level = round(dedication * levels)
                on_grid = 1 <= level <= levels and abs(dedication - level / levels) <= CAPACITY_TOLERANCE
                if not on_grid:
                    errors.append(f"{dedication_context}: dedication is not on the j/{levels} grid")


def precedence_order(project: Project) -> tuple[list[str], dict[str, set[str]], bool]:
    """Return a topological task order, each task's predecessors, and whether the order is unique."""
    predecessors = {task.id: set() for task in project.tasks}
    for predecessor, successor in project.tpg_edges:
        predecessors[successor].add(predecessor)

    # Sort level by level; the order is unique when every level holds one task
    sorter = TopologicalSorter(predecessors)
    sorter.prepare()
    order = []
    unique = True
    while sorter.is_active():
        ready = sorter.get_ready()
        unique = unique and len(ready) == 1
        order.extend(ready)
        sorter.done(*ready)
    return order, predecessors, unique


def assess_triviality(project: Project, report: ValidationReport) -> ValidationReport:
    """Classify a correct project as trivial or not, checking in this order:

    1. impossible: the shortest critical path exceeds the deadline.
    2. guaranteed_success: doing every task one after another, in its fastest worst-case mode, meets the deadline.
    3. no_decisions: one mode per task, plus a unique precedence order or no competition for workers.
    4. unclassified: none of the above.
    """
    if not report.is_correct or report.project_key != project_key(project) or report.validation_version != VALIDATION_VERSION:
        raise ValueError("Triviality assessment requires a current, correct validation report")

    # Bound each task's duration: shortest possible, and longest in its best mode
    order, predecessors, unique_order = precedence_order(project)
    minimum_days = {}
    serial_maximum = 0
    for task in project.tasks:
        hashes = [mode.distribution_hash for mode in task.modes]
        bounds = [duration_bounds(project.distributions[key]) for key in hashes]
        minimum_days[task.id] = min(lower for lower, _ in bounds)
        serial_maximum += min(upper for _, upper in bounds)

    # Even unlimited workers cannot finish before the shortest critical path.
    critical_path = max(longest_paths(project, minimum_days, zero=0).values())

    # Check the structure for choices: several modes, several precedence orders, or competition for workers
    single_mode = all(len(task.modes) == 1 for task in project.tasks)
    no_competition = single_mode and all(
        math.fsum(task.modes[0].dedication.get(worker.id, 0) for task in project.tasks) <= 1 + CAPACITY_TOLERANCE
        for worker in project.workers
    )
    flags = []
    if single_mode:
        flags.append("single_mode_per_task")
    if unique_order:
        flags.append("unique_precedence_order")
    if no_competition:
        flags.append("no_resource_competition")

    # Classify, in the order listed above
    reasons = [f"Shortest critical path: {critical_path} days; worst-case serial bound: {serial_maximum} days"]
    if critical_path > project.deadline.delta:
        classification = "impossible"
        reasons.append("The shortest critical path exceeds the deadline")
    elif serial_maximum <= project.deadline.delta:
        classification = "guaranteed_success"
        reasons.append("A feasible serial schedule always finishes by the deadline")
    elif single_mode and (unique_order or no_competition):
        classification = "no_decisions"
        reasons.append("Starting ready tasks immediately leaves no meaningful scheduling choice")
    else:
        classification = "unclassified"
        reasons.append("Neither deadline bounds nor structural checks decide triviality")
    return replace(
        report, is_trivial=classification != "unclassified", classification=classification,
        structural_flags=tuple(flags), reasons=tuple(reasons),
    )
