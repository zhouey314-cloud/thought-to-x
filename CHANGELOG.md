# Changelog

All notable changes follow Semantic Versioning.

## [1.0.1] - 2026-10-24

- Reconcile the source/package version with the historical v1.0.0 workflow release; old tags and assets are unchanged.
- Bundle unchanged SKILL.md, workflow and example Markdown alongside prompts/config so the portable skill references remain available after wheel installation.
- Verify all installed resource bytes against source and exercise prompt-only outside the checkout in CI.

Previously merged fixes included in this release:

- Include the unchanged default prompts and style profile in wheel/sdist installations; CI exercises a non-editable installation outside the source checkout.
- Accept long literal thoughts without treating them as invalid filesystem paths, and report file decoding errors through the CLI error exit.
- Add offline process regressions for long text, stdin, UTF-8 files, and malformed input. Prompt wording, model configuration, and publishing behavior are unchanged.

## [1.0.0] - 2026-09-23

Historical GitHub workflow release at `72ade9cb22d52100489b3d2d41914c0b88f5f945`. This tag did not bump Python package metadata, which still read 0.1.0. No wheel assets were attached. Version 1.0.1 unifies these numbering surfaces without moving the historical tag.

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
