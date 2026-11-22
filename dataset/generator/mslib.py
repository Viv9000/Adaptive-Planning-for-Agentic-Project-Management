"""Parse and validate MSLIB release files (.msrcp) for the basic deterministic variant."""

from __future__ import annotations

from dataclasses import dataclass
from graphlib import CycleError, TopologicalSorter
import hashlib
import math
from pathlib import Path
import re

from planner.core.project import PathLike


MODULE_NAMES = (
    "Project Module", "Workforce Module", "Workforce Module with Skill Levels",
    "Skill Requirements Module", "Skill Level Requirements Module", "Cost Module",
    "Common Resource Usage Module", "Rework Module",
)


@dataclass(frozen=True, slots=True)
class SourceSection:
    """An original named module, retaining its numeric rows and their order."""

    name: str
    rows: tuple[tuple[int | float, ...], ...]


@dataclass(frozen=True, slots=True)
class MSActivity:
    """Original numeric activity ID, fixed duration, successors, and skill counts."""

    id: int
    duration: int
    successors: tuple[int, ...]
    skill_requirements: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class MSInstance:
    """Parsed source plus untouched bytes and inactive variant sections for provenance.

    Worker IDs are one-based row numbers in worker_skills.
    Columns retain original skill order; required levels remain in sections.
    """

    source_path: Path
    source_bytes: bytes
    source_sha256: str
    instance_id: str
    n_skills: int
    n_skill_levels: int
    basic_best_known_makespan: int
    variant_deadline: int
    activities: tuple[MSActivity, ...]
    worker_skills: tuple[tuple[int, ...], ...]
    sections: tuple[SourceSection, ...]


def parse_msrcp(path: PathLike) -> MSInstance:
    """Parse named modules, separate source scalars, and retain all bytes and sections.

    Reject ambiguous layouts with section and line context rather than guessing row offsets.
    """
    path = Path(path)
    instance = _parse_source(path, path.read_bytes())
    validate_basic_instance(instance)
    return instance


def _parse_source(path: Path, source: bytes) -> MSInstance:
    """Parse the complete release format without validation or filesystem side effects."""
    # Split the file into named modules of numeric rows
    sections: list[SourceSection] = []
    name = None
    rows: list[tuple[int | float, ...]] = []
    for line_number, line in enumerate(source.decode("utf-8-sig").splitlines(), 1):
        line = line.strip()
        if not line:
            continue

        # A \* Name *\ line starts a new module
        header = re.fullmatch(r"\\\*\s*(.*?)\s*\*\\", line)
        if header:
            if name is not None:
                sections.append(SourceSection(name, tuple(rows)))
            name = header.group(1)
            rows = []
            if name not in MODULE_NAMES or any(section.name == name for section in sections):
                raise ValueError(f"{path}:{line_number}: unknown or duplicate module {name!r}")
            continue
        # Any other line is a row of finite numbers in the current module
        if name is None:
            raise ValueError(f"{path}:{line_number}: numeric data before a module header")
        values = []
        for token in line.split():
            try:
                value = int(token) if re.fullmatch(r"[+-]?\d+", token) else float(token)
            except ValueError:
                raise ValueError(f"{path}:{line_number}: {name}: invalid number {token!r}") from None
            if not math.isfinite(value):
                raise ValueError(f"{path}:{line_number}: {name}: non-finite number")
            values.append(value)
        rows.append(tuple(values))
    if name is not None:
        sections.append(SourceSection(name, tuple(rows)))
    modules = {section.name: section.rows for section in sections}
    if set(modules) != set(MODULE_NAMES):
        raise ValueError(f"{path}: missing modules: {sorted(set(MODULE_NAMES) - set(modules))}")

    # Project Module: the counts, then BKS and deadline rows, then one row per activity
    project_rows = modules["Project Module"]
    if not project_rows or len(project_rows[0]) != 4:
        raise ValueError(f"{path}: Project Module: expected four header integers")
    for value in project_rows[0]:
        _require_integer(value, 1, "Project Module header")
    n_activities, n_workers, n_skills, n_levels = project_rows[0]
    if len(project_rows) != n_activities + 3:
        raise ValueError(f"{path}: Project Module: expected header, BKS, deadline, and {n_activities} activity rows")
    if len(project_rows[1]) != 1 or len(project_rows[2]) != 1:
        raise ValueError(f"{path}: Project Module: BKS and variant deadline must be separate scalar rows")

    # Activities: duration, successor count, and successors, joined with their skill requirements
    requirements = modules["Skill Requirements Module"]
    if len(requirements) != n_activities:
        raise ValueError(f"{path}: Skill Requirements Module: wrong activity count")
    activities = []
    for activity_id, row in enumerate(project_rows[3:], 1):
        if len(row) < 2:
            raise ValueError(f"{path}: Project Module: activity {activity_id}: missing successor count")
        for value in row:
            _require_integer(value, 0, f"activity {activity_id}")
        if len(row) != row[1] + 2:
            raise ValueError(f"{path}: activity {activity_id}: successor count does not match row")
        activities.append(MSActivity(activity_id, row[0], row[2:], requirements[activity_id - 1]))

    # Workers: one row of binary skills each
    workforce = modules["Workforce Module"]
    if len(workforce) != n_workers:
        raise ValueError(f"{path}: Workforce Module: wrong worker count")
    return MSInstance(
        path, source, hashlib.sha256(source).hexdigest(), path.stem, n_skills, n_levels,
        project_rows[1][0], project_rows[2][0], tuple(activities), workforce, tuple(sections),
    )


def _require_integer(value: object, minimum: int, context: str) -> None:
    """Check a source integer's type and lower bound without coercing or rounding it."""
    if type(value) is not int or value < minimum:
        raise ValueError(f"{context}: expected integer >= {minimum}, got {value!r}")


def validate_basic_instance(instance: MSInstance) -> None:
    """Raise ValueError unless the instance is a well-formed basic (fixed-duration, binary-skill) MSLIB instance.

    Inactive variant modules (levels, costs, rework) are checked for shape only, not used as constraints.
    """
    if instance != _parse_source(instance.source_path, instance.source_bytes):
        raise ValueError("Source checksum or parsed fields disagree with original source bytes")
    _require_integer(instance.n_skills, 1, "skill count")
    _require_integer(instance.n_skill_levels, 1, "skill level count")
    _require_integer(instance.basic_best_known_makespan, 0, "basic BKS")
    _require_integer(instance.variant_deadline, 0, "variant deadline")
    modules = {section.name: section.rows for section in instance.sections}
    if len(instance.activities) < 3:
        raise ValueError("Expected two dummy endpoints and at least one real activity")
    _check_module_shapes(instance, modules)
    _check_worker_levels(instance, modules)
    _check_activity_graph(instance, modules)


def _check_module_shapes(instance: MSInstance, modules: dict) -> None:
    """Check each module's rows and columns, integer skill data, and value ranges."""
    n_workers = len(instance.worker_skills)
    n_activities = len(instance.activities)
    dimensions = {
        "Workforce Module": (n_workers, instance.n_skills),
        "Workforce Module with Skill Levels": (n_workers, instance.n_skills),
        "Skill Requirements Module": (n_activities, instance.n_skills),
        "Cost Module": (1 + 2 * instance.n_skills, instance.n_skill_levels),
        "Common Resource Usage Module": (1 + instance.n_skills, instance.n_skill_levels),
        "Rework Module": (instance.n_skills, instance.n_skill_levels),
    }
    # Check each module's row count, row widths (first rows of two modules differ), and values
    for name, (height, width) in dimensions.items():
        rows = modules[name]
        if len(rows) != height:
            raise ValueError(f"{name}: expected {height} rows")
        for index, row in enumerate(rows):
            expected_width = width
            if name == "Cost Module" and index == 0:
                expected_width = 2
            elif name == "Common Resource Usage Module" and index == 0:
                expected_width = 1
            if len(row) != expected_width:
                raise ValueError(f"{name}: row {index + 1}: expected {expected_width} values")
            for value in row:
                if name in ("Workforce Module", "Workforce Module with Skill Levels", "Skill Requirements Module"):
                    _require_integer(value, 0, f"{name}: row {index + 1}")
                if value < 0 or (name == "Rework Module" and value > 1):
                    raise ValueError(f"{name}: row {index + 1}: value out of range")


def _check_worker_levels(instance: MSInstance, modules: dict) -> None:
    """Check that binary worker skills agree with the workers' mastered skill levels."""
    levels = modules["Workforce Module with Skill Levels"]
    for worker_id, (skills, worker_levels) in enumerate(zip(instance.worker_skills, levels), 1):
        for skill, level in zip(skills, worker_levels):
            _require_integer(skill, 0, f"worker {worker_id}: binary skill")
            if skill not in (0, 1) or level > instance.n_skill_levels or bool(skill) != bool(level):
                raise ValueError(f"worker {worker_id}: binary skills and mastered levels disagree")


def _check_activity_graph(instance: MSInstance, modules: dict) -> None:
    """Check activity data and required levels, then that the precedence graph is acyclic with dummy source and sink."""
    n_activities = len(instance.activities)
    required_levels = modules["Skill Level Requirements Module"]
    if len(required_levels) != n_activities:
        raise ValueError("Skill Level Requirements Module: wrong activity count")
    # Check each activity's data and required levels, collecting predecessors from its successors
    predecessors: dict[int, set[int]] = {activity.id: set() for activity in instance.activities}
    for activity, row in zip(instance.activities, required_levels):
        _require_integer(activity.id, 1, "activity ID")
        _require_integer(activity.duration, 0, f"activity {activity.id}: duration")
        for count in activity.skill_requirements:
            _require_integer(count, 0, f"activity {activity.id}: skill requirement")
        count = sum(activity.skill_requirements)
        if count == 0:
            if row != (-1,):
                raise ValueError(f"activity {activity.id}: expected -1 for no required skill levels")
        else:
            if len(row) != count:
                raise ValueError(f"activity {activity.id}: wrong required skill level count")
            for level in row:
                _require_integer(level, 1, f"activity {activity.id}: required level")
                if level > instance.n_skill_levels:
                    raise ValueError(f"activity {activity.id}: required level out of range")
        if len(set(activity.successors)) != len(activity.successors):
            raise ValueError(f"activity {activity.id}: duplicate successors")
        for successor in activity.successors:
            if successor not in predecessors or successor == activity.id:
                raise ValueError(f"activity {activity.id}: invalid successor {successor}")
            predecessors[successor].add(activity.id)

    # Check that the graph is acyclic
    try:
        order = tuple(TopologicalSorter(predecessors).static_order())
    except CycleError:
        raise ValueError("Activity precedence graph contains a cycle") from None

    # Check that the first and last activities are empty dummies acting as source and sink
    start, end = instance.activities[0], instance.activities[-1]
    for dummy in (start, end):
        if dummy.duration != 0 or any(dummy.skill_requirements):
            raise ValueError(f"dummy activity {dummy.id}: must have zero duration and no requirements")
    if predecessors[start.id] or end.successors:
        raise ValueError("Dummy endpoints must be source and sink")

    # Check that every activity is reachable from the start and reaches the end
    reachable = {start.id}
    for activity_id in order:
        if activity_id in reachable:
            reachable.update(instance.activities[activity_id - 1].successors)
    reaches_end = {end.id}
    for activity_id in reversed(order):
        if activity_id in reaches_end:
            reaches_end.update(predecessors[activity_id])
    if len(reachable) != n_activities or len(reaches_end) != n_activities:
        raise ValueError("Every activity must lie between the dummy start and end")
