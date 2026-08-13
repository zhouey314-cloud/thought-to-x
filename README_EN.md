# Thought to X

> Turn messy thoughts into human-sounding X posts.

I have ideas all day. Most of them look like this:

> “What AI really changes may not be access to knowledge, but the fact that an ordinary person can act on far more ideas…”

The idea is mine. The writing is messy.

Thought-to-X turns fragments, voice transcripts, notes, and unfinished opinions into publishable X posts without replacing your thinking with generic AI writing.

**Idea First. AI Second.**

## What makes it different

- It extracts the real claim before rewriting.
- It preserves uncertainty, values, vocabulary, and voice.
- It optimizes for X without pretending to know a secret algorithm.
- It runs a dedicated De-AI and fidelity review.
- It works as a portable Markdown skill without an API key.

```text
Your Thought → Intent → Insight → Structure → X Optimization → De-AI → Your Post
```

## Quick start

With Codex or Claude Code:

```text
Read SKILL.md and process the following raw thought:

[paste your thought]
```

With ChatGPT or Claude, upload the repository or copy `prompts/master.md` and its referenced modules into the conversation.

With Python 3.11+:

```bash
python -m pip install -e .
python -m thought_to_x input.txt --prompt-only
thought-to-x "I have a half-formed idea..." --mode rewrite --length auto --output final-only --prompt-only
```

Prompt-only mode requires no API. To use an OpenAI-compatible endpoint, configure the variables shown in `.env.example` in your environment and omit `--prompt-only`.

## Workflow

Normalize → Extract Intent → Find Core Insight → Identify Tension → Build Argument → Preserve Voice → X Content Optimization → De-AI → Quality Review.

Read [`workflows/thought-to-x.md`](workflows/thought-to-x.md) for stage contracts and [`prompts/`](prompts/) for modular instructions.

## Make it yours

Fork the project and edit [`config/style-profile.yaml`](config/style-profile.yaml) to turn the skill into your own X writer. Add writing you genuinely like to [`examples/liked-posts.md`](examples/liked-posts.md); the skill learns rhythm and tendencies, never copies sentences or imports old opinions.

## Examples

See [`examples/`](examples/) for full raw-to-final walkthroughs. The key test is simple: the final post expresses the supplied thought more clearly without adding a new mind behind it.

## Roadmap

- v0.2 Personal writing memory
- v0.3 Post performance feedback
- v0.4 Multiple writing personas
- v0.5 X draft integration

No auto-publishing in v0.1. The focus is the thought-processing system.

Contributions are welcome; read [`CONTRIBUTING.md`](CONTRIBUTING.md). MIT License.
