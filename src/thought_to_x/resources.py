"""Locate canonical source assets or their bundled wheel resources."""
from importlib.resources import files
from importlib.resources.abc import Traversable
from pathlib import Path


def default_resource_root() -> Traversable:
    source_root = Path(__file__).resolve().parents[2]
    if (source_root / "prompts" / "master.md").is_file():
        return source_root
    return files("thought_to_x._resources")
