"""Command-line entrypoint."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .pipeline import PipelineRequest, ThoughtToXPipeline
from .providers import OpenAICompatibleProvider, ProviderError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Turn messy thoughts into human-sounding X posts.")
    parser.add_argument("input", help="Raw thought text, a UTF-8 file path, or '-' for stdin")
    parser.add_argument("--mode", choices=("polish", "rewrite", "expand", "distill"), default="rewrite")
    parser.add_argument("--length", choices=("short", "medium", "long", "auto"), default="auto")
    parser.add_argument("--output", choices=("default", "final-only"), default="default")
    parser.add_argument("--style", help="Path to a custom style-profile YAML")
    parser.add_argument("--provider", choices=("openai-compatible",), default="openai-compatible")
    parser.add_argument("--prompt-only", action="store_true", help="Print the assembled portable prompt; no API key needed")
    return parser


def read_input(value: str) -> str:
    if value == "-":
        return sys.stdin.read()
    path = Path(value)
    return path.read_text(encoding="utf-8") if path.is_file() else value


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    request = PipelineRequest(
        raw_thought=read_input(args.input),
        mode=args.mode,
        length=args.length,
        output=args.output,
        style_path=args.style,
    )
    try:
        pipeline = ThoughtToXPipeline(provider=None if args.prompt_only else OpenAICompatibleProvider())
        if args.prompt_only:
            system, user = pipeline.build_prompts(request)
            print(f"{system}\n\n--- USER INPUT ---\n\n{user}")
        else:
            print(pipeline.run(request))
    except (OSError, ValueError, RuntimeError, ProviderError) as exc:
        raise SystemExit(f"error: {exc}") from exc
