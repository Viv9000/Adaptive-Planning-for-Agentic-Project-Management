"""Read and write JSON result files."""

from dataclasses import asdict, is_dataclass
import json
import os
from pathlib import Path


def json_default(value):
    """Convert paths, dataclasses (such as states), and sets for JSON."""
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, (set, frozenset)):
        return sorted(value)
    raise TypeError(f"Unsupported artifact value: {type(value).__name__}")


def write_json(path: Path, data) -> None:
    """Write JSON atomically, so readers never see a partial file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w") as stream:
        stream.write(json.dumps(data, default=json_default, indent=2, allow_nan=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def read(path):
    return json.loads(Path(path).read_text())


def frozen(path, value):
    """Reject changed inputs/settings before reusing any outputs."""
    path = Path(path)
    value = json.loads(json.dumps(value))
    if path.exists() and read(path) != value:
        raise ValueError(f'{path}: saved contract differs; use a new output directory')
    write_json(path, value)
