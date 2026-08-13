"""Configuration loading for Thought-to-X."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


DEFAULT_STYLE_PATH = Path(__file__).resolve().parents[2] / "config" / "style-profile.yaml"


class ConfigError(ValueError):
    """Raised when a style profile is missing or malformed."""


def load_style_profile(path: str | Path | None = None) -> dict[str, Any]:
    """Load and minimally validate a YAML style profile."""
    profile_path = Path(path) if path else DEFAULT_STYLE_PATH
    if not profile_path.is_file():
        raise ConfigError(f"Style profile not found: {profile_path}")

    try:
        data = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ConfigError(f"Invalid YAML in style profile: {profile_path}") from exc

    if not isinstance(data, dict):
        raise ConfigError("Style profile must be a YAML mapping")
    for key in ("language", "platform", "voice", "preferences", "avoid", "format"):
        if key not in data:
            raise ConfigError(f"Style profile is missing required key: {key}")
    return data
