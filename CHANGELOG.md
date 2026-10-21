# Changelog

All notable changes follow Semantic Versioning.

## Unreleased

- Include the unchanged default prompts and style profile in wheel/sdist installations; CI exercises a non-editable installation outside the source checkout.
- Accept long literal thoughts without treating them as invalid filesystem paths, and report file decoding errors through the CLI error exit.
- Add offline process regressions for long text, stdin, UTF-8 files, and malformed input. Prompt wording, model configuration, and publishing behavior are unchanged.

## [0.1.0] - 2026-08-13

Initial release

- Thought → X workflow
- Portable `SKILL.md`
- Personal style profile
- Modular prompt system
- De-AI review
- Quality scoring
- CLI foundation
- Examples
