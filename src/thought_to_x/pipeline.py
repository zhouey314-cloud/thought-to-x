"""Prompt orchestration independent of any specific model provider."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .config import load_style_profile
from .providers.base import BaseProvider

Mode = Literal["polish", "rewrite", "expand", "distill"]
Length = Literal["short", "medium", "long", "auto"]
Output = Literal["default", "final-only"]

STAGES = (
    "normalize",
    "extract-intent",
    "find-insight",
    "tension",
    "structures",
    "preserve-voice",
    "x-optimize",
    "de-ai",
    "review",
)


@dataclass(frozen=True)
class PipelineRequest:
    raw_thought: str
    mode: Mode = "rewrite"
    length: Length = "auto"
    output: Output = "default"
    style_path: str | Path | None = None


class ThoughtToXPipeline:
    """Assemble the portable prompt workflow and optionally execute it."""

    def __init__(self, provider: BaseProvider | None = None, project_root: Path | None = None) -> None:
        self.provider = provider
        self.project_root = project_root or Path(__file__).resolve().parents[2]

    @property
    def stages(self) -> tuple[str, ...]:
        return STAGES

    def build_prompts(self, request: PipelineRequest) -> tuple[str, str]:
        if not request.raw_thought.strip():
            raise ValueError("raw_thought cannot be empty")
        style = load_style_profile(request.style_path)
        prompt_dir = self.project_root / "prompts"
        master = (prompt_dir / "master.md").read_text(encoding="utf-8")
        modules: list[str] = []
        for stage in STAGES:
            if stage == "preserve-voice":
                modules.append("# 06 Preserve Voice\nCompare the draft with the source, intent map, and style. Preserve wording, emotion, values, and uncertainty. Do not invent a persona.")
            else:
                modules.append((prompt_dir / f"{stage}.md").read_text(encoding="utf-8"))
        system_prompt = master + "\n\n" + "\n\n---\n\n".join(modules)
        user_prompt = "\n".join(
            [
                f"mode: {request.mode}",
                f"length: {request.length}",
                f"output: {request.output}",
                "style_profile:",
                json.dumps(style, ensure_ascii=False, indent=2),
                "raw_thought:",
                request.raw_thought.strip(),
            ]
        )
        return system_prompt, user_prompt

    def run(self, request: PipelineRequest) -> str:
        if self.provider is None:
            raise RuntimeError("No provider configured. Use --prompt-only or pass a BaseProvider.")
        system_prompt, user_prompt = self.build_prompts(request)
        return self.provider.generate(system_prompt=system_prompt, user_prompt=user_prompt)
