"""Read and write scenario Markdown files (a Configuration and a Data YAML block)."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import fields, replace
from numbers import Integral, Real
from pathlib import Path
import re
from typing import Any

import yaml

from planner.core.distributions import DurationDistribution
from planner.core.project import (
    SCHEMA_VERSION, Config, Deadline, Mode, PathLike, Project, Task, ValidationReport, Worker,
    content_hash, project_record,
)
from planner.core.validation import validate_project


def scenario_filename(config: Config) -> str:
    """Return scenario_w{workers}_t{tasks}_s{skills}_seed{seed}_{config hash}.md."""
    for name in ("n_workers", "n_tasks", "n_skills", "seed"):
        if name not in config or not isinstance(config[name], Integral):
            raise ValueError(f"Resolved generation config requires integer {name}")
    filename_config = {name: value for name, value in config.items() if name not in {"output_dir", "output_path"}}
    suffix = content_hash(filename_config)[:8]
    return f"scenario_w{config['n_workers']}_t{config['n_tasks']}_s{config['n_skills']}_seed{config['seed']}_{suffix}.md"


def write_scenario(project: Project, output_dir: PathLike, *, generation_config: Config | None = None) -> Path:
    """Validate and save a project as Markdown, and return the path.

    Trivial projects go to output_dir/trivial_scenarios; an existing different file is never overwritten.
    """
    # Check the project and classify its triviality
    report = validate_project(project, check_triviality=True)
    if not report.is_correct:
        raise ValueError("Incorrect project: " + "; ".join(report.errors))

    # The Configuration block must agree with the project's own counts
    actual_config = {
        "schema_version": project.schema_version,
        "n_dedication_levels": project.n_dedication_levels,
        "n_workers": len(project.workers),
        "n_tasks": len(project.tasks),
    }
    config = dict(generation_config) if generation_config is not None else {}
    for name, expected in actual_config.items():
        if name in config and (not isinstance(config[name], Integral) or config[name] != expected):
            raise ValueError(f"Configuration {name} must match project value {expected}")
        config[name] = expected

    # Render the two YAML blocks, saving the report with the data
    data = project_record(project)
    data["validation"] = {item.name: getattr(report, item.name) for item in fields(report)}
    configuration_yaml = yaml.safe_dump(_to_plain_yaml(config), sort_keys=False)
    data_yaml = yaml.safe_dump(_to_plain_yaml(data), sort_keys=False)
    text = f"# Configuration\n\n```yaml\n{configuration_yaml}```\n\n# Data\n\n```yaml\n{data_yaml}```\n"

    # Name the file by its content, and keep trivial projects apart
    filename = f"scenario_{report.project_key}.md" if generation_config is None else scenario_filename(config)
    directory = Path(output_dir)
    if report.is_trivial:
        directory /= "trivial_scenarios"
    directory.mkdir(parents=True, exist_ok=True)
    # Write with exclusive creation, which never replaces an existing file; an identical file is fine
    path = directory / filename
    try:
        with path.open("x", encoding="utf-8") as output:
            output.write(text)
    except FileExistsError:
        if path.read_text(encoding="utf-8") != text:
            raise FileExistsError(f"Refusing to overwrite different scenario: {path}") from None
    return path


def load_project(path: PathLike) -> Project:
    """Parse a scenario file into a validated Project with its validation report attached."""
    # Read and check the Configuration block
    config, data = _read_yaml_blocks(Path(path).read_text(encoding="utf-8"))
    config = _require_fields(
        config, "Configuration", {"schema_version", "n_dedication_levels", "n_workers", "n_tasks"}, allow_extra=True,
    )
    if config["schema_version"] != SCHEMA_VERSION:
        raise ValueError(f"schema_version must be {SCHEMA_VERSION}")

    # Build the project from the Data block
    data = _require_fields(data, "Data", {"workers", "tasks", "distributions", "tpg_edges", "deadline"},
                           {"validation"})
    workers = tuple(
        Worker(**_require_fields(record, f"Worker {index}", {"id"}))
        for index, record in enumerate(_require_list(data["workers"], "workers"))
    )
    distributions = _read_distributions(data["distributions"])
    tasks = _read_tasks(data["tasks"])
    deadline = Deadline(**_require_fields(data["deadline"], "deadline", {"delta"}))
    edges = _read_edges(data["tpg_edges"])
    project = Project(
        workers, tasks, edges, deadline, distributions,
        schema_version=config["schema_version"], n_dedication_levels=config["n_dedication_levels"],
        validation=_read_report(data.get("validation")),
    )
    # The declared counts are not part of project_key, so always check them
    for name, actual in (("n_workers", len(project.workers)), ("n_tasks", len(project.tasks))):
        if not isinstance(config[name], Integral) or config[name] != actual:
            raise ValueError(f"Configuration {name} must match Data count {actual}")

    # Check the project, reusing the saved report when it is current
    report = validate_project(project)
    if not report.is_correct:
        raise ValueError("Incorrect project: " + "; ".join(report.errors))
    return replace(project, validation=report)


def _read_yaml_blocks(text: str) -> tuple[Any, Any]:
    """Return the parsed Configuration and Data YAML blocks."""
    sections = re.split(r"^# (Configuration|Data)[ \t]*$", text, flags=re.MULTILINE)
    block_pattern = re.compile(r"^```yaml[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)
    if len(sections) != 5 or sections[1::2] != ["Configuration", "Data"] or len(block_pattern.findall(text)) != 2:
        raise ValueError("Expected Configuration then Data, with exactly two YAML blocks")
    blocks = []
    for name, section in zip(sections[1::2], sections[2::2]):
        matches = block_pattern.findall(section)
        if len(matches) != 1:
            raise ValueError(f"{name}: expected exactly one YAML block")
        try:
            blocks.append(yaml.load(matches[0], Loader=_ScenarioLoader))
        except yaml.YAMLError as error:
            raise ValueError(f"Invalid {name} YAML: {error}") from error
    return blocks[0], blocks[1]


def _read_distributions(value: Any) -> dict[str, DurationDistribution]:
    """Restore distributions under their saved keys; validation checks that the keys match."""
    distributions = {}
    for key, record in _require_fields(value, "distributions", set(), allow_extra=True).items():
        specification = _require_fields(record, f"Distribution {key}", {"family"}, allow_extra=True)
        family = specification.pop("family")
        probabilities = specification.pop("probabilities", {})
        try:
            distributions[key] = DurationDistribution(family, specification, probabilities)
        except (TypeError, ValueError) as error:
            raise ValueError(f"Distribution {key}: {error}") from error
    return distributions


def _read_tasks(value: Any) -> tuple[Task, ...]:
    """Return the tasks with their modes, checking each record's fields."""
    tasks = []
    for index, record in enumerate(_require_list(value, "tasks")):
        record = _require_fields(record, f"Task {index}", {"id", "modes"},
                                 {"milestone"})
        modes = []
        for mode in _require_list(record["modes"], f"Task {record['id']} modes"):
            mode = _require_fields(mode, f"Task {record['id']} mode", {"id", "dedication", "distribution_hash"})
            if not isinstance(mode["dedication"], Mapping):
                raise ValueError(f"Task {record['id']}, mode {mode['id']}: dedication must be a mapping")
            modes.append(Mode(**mode))
        tasks.append(Task(record["id"], tuple(modes), record.get("milestone", False)))
    return tuple(tasks)


def _read_edges(value: Any) -> tuple:
    """Return the precedence edges as (predecessor, successor) tuples."""
    return tuple(tuple(_require_list(edge, "precedence edge")) for edge in _require_list(value, "tpg_edges"))


class _ScenarioLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _unique_yaml_mapping(loader: _ScenarioLoader, node: yaml.MappingNode) -> dict:
    """Build a mapping, raising on a duplicate or unhashable key."""
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        try:
            duplicate = key in result
        except TypeError as error:
            raise yaml.constructor.ConstructorError(None, None, "unhashable mapping key", key_node.start_mark) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate mapping key {key!r}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=True)
    return result


_ScenarioLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _unique_yaml_mapping)


def _require_fields(
    value: Any, context: str, required: set[str], optional: set[str] | None = None, *, allow_extra: bool = False,
) -> dict:
    """Check a mapping's fields and return a copy."""
    if not isinstance(value, Mapping):
        raise ValueError(f"{context}: expected a mapping")
    missing = required - value.keys()
    extra = value.keys() - required - (optional or set())
    if missing:
        raise ValueError(f"{context}: missing fields {sorted(missing)}")
    if extra and not allow_extra:
        raise ValueError(f"{context}: unexpected fields {sorted(extra, key=str)}")
    return dict(value)


def _require_list(value: Any, context: str) -> list:
    """Return value if it is a list, otherwise raise ValueError."""
    if not isinstance(value, list):
        raise ValueError(f"{context}: expected a list")
    return value


def _to_plain_yaml(value: Any) -> Any:
    """Convert read-only mappings, tuples, and NumPy numbers to plain YAML data."""
    if isinstance(value, Mapping):
        return {_to_plain_yaml(key): _to_plain_yaml(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_to_plain_yaml(item) for item in value]
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        return float(value)
    return value


def _read_report(value: Any) -> ValidationReport | None:
    """Return a saved validation report only if it is complete and well formed; otherwise None."""
    # Check the fields and their types
    names = {item.name for item in fields(ValidationReport)}
    if not isinstance(value, dict) or set(value) != names:
        return None
    if not isinstance(value["project_key"], str) or not isinstance(value["is_correct"], bool):
        return None
    if not isinstance(value["validation_version"], Integral):
        return None
    for name in ("errors", "reasons", "structural_flags"):
        if not isinstance(value[name], list) or not all(isinstance(item, str) for item in value[name]):
            return None

    # Check that triviality and its classification agree
    trivial = value["is_trivial"]
    classification = value["classification"]
    if trivial is None:
        if classification is not None:
            return None
    else:
        if not isinstance(trivial, bool) or not isinstance(classification, str):
            return None
        if classification not in {"impossible", "guaranteed_success", "no_decisions", "unclassified"}:
            return None
        if trivial != (classification != "unclassified"):
            return None
    if value["is_correct"] and value["errors"]:
        return None

    # Rebuild the report with tuples, as the dataclass stores them
    record = dict(value)
    for name in ("errors", "reasons", "structural_flags"):
        record[name] = tuple(record[name])
    return ValidationReport(**record)
