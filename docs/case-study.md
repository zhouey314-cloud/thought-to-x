# Case Study — Thought to X

## Problem
Raw personal ideas are hard to publish, while generic AI rewriting can erase the author's point of view.

## Context
This is a portable writing skill with modular prompts and a Python CLI. The illustrative before/after example is not evidence of measured model performance.

## Constraints
The workflow must remain useful without an API key and must not publish to X automatically.

## My Role
Assembled the idea-first workflow, prompt modules, CLI/provider boundary, examples and offline tests.

## Architecture
`SKILL.md` and `prompts/` define extraction, structure, X formatting and de-AI steps. The CLI can assemble a prompt without a network call or optionally use an OpenAI-compatible provider.

## Key Decisions
Preserve the author's claim before optimizing the prose. Make `--prompt-only` the zero-key path and require human review of final wording.

## Hardest Problem
Separating meaningful editorial preservation from superficial fluency: a polished post may still distort intent.

## Failure/Tradeoff
Offline tests can verify prompt assembly and CLI behavior, not subjective writing quality or voice preservation across users.

## Testing
Run `PYTHONPATH=src python -m unittest discover -s tests -v` and try `thought-to-x ... --prompt-only`.

## Eval
No independent, human-rated model-quality benchmark is claimed. A useful future set would include author-approved source/target pairs and explicit distortion checks.

## Current Evidence
The repository includes runnable CLI code, prompt modules, tests and a labelled illustrative example.

## Limitations
No automatic X publishing, no guaranteed engagement outcome, and optional provider behavior depends on external configuration.

## What I Would Do in Production
Obtain opt-in author samples, measure idea retention with human review, protect private drafts, and add failure/regression cases for unsupported claims and tone drift.

## What I Learned
Workflow boundaries and editorial honesty matter more than treating a fluent draft as a verified good post.
