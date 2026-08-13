---
name: thought-to-x
description: Turn messy thoughts, voice transcripts, notes, unfinished opinions, or weak drafts into human-sounding X posts while preserving the author's idea and voice. Use whenever the user asks to polish, rewrite, expand, distill, structure, optimize for X/Twitter, or remove AI flavor from their own thinking—even if they only say “帮我写成一条 X”, “保留我的意思但写得更好”, or paste an unstructured fragment.
compatibility: Any agent that can read Markdown. Optional Python 3.11+ CLI and OpenAI-compatible endpoint.
---

# Thought-to-X

## Purpose

Turn thinking that already exists into clearer writing. The author supplies the mind; you supply editorial structure. A polished post should feel like the author after thinking it through, not like an AI writing about the same topic.

## When to use

Use for raw thoughts, speech-to-text, notes, half-formed arguments, existing posts that need polishing, long material to distill, or requests such as:

- 帮我润色成 X / 把这个写成一条 X
- 根据 X 的传播逻辑改一下
- 这是我的一个零碎想法 / 把这段语音稿整理一下
- 保留我的意思但写得更好 / 去掉 AI 味
- Polish, rewrite, expand, or distill this into an X post

## When not to use

Do not use this workflow to invent a viewpoint for someone who supplied no idea, impersonate another writer, manufacture engagement bait, auto-publish to X, or present invented claims as facts. For pure translation, research, fact-checking, or unrelated long-form writing, use a more appropriate workflow.

## Input

Required: the author's raw thought or draft.

Optional parameters:

- `mode`: `polish | rewrite | expand | distill` (infer when omitted)
- `length`: `short | medium | long | auto` (default `auto`)
- `output`: `default | final-only` (default `default`)
- `style`: path or pasted style profile; default `config/style-profile.yaml`
- `liked_posts`: optional examples from `examples/liked-posts.md`

If a missing detail would require fabrication, retain the uncertainty or omit the unsupported detail. Ask a question only when the ambiguity prevents a faithful result; otherwise make the smallest reversible editorial assumption.

## Output

For `output=default`, return exactly:

```markdown
## Final

[copy-ready post]

## Hooks

1. [alternative]
2. [alternative]
3. [alternative]

## Core Insight

[one sentence]
```

For `output=final-only`, return only the post—no heading, notes, score, or alternatives.

## Workflow

Read `prompts/master.md`, then execute these stages in order. Do the analysis silently unless the user requests the process.

1. **Normalize** — repair transcription, punctuation, filler, and repetition without discarding thought-bearing details. Read `prompts/normalize.md`.
2. **Extract intent** — identify topic, claim, emotion, intention, reader, phrases to preserve, and uncertainty. Read `prompts/extract-intent.md`.
3. **Find core insight** — decide what single idea must survive. Read `prompts/find-insight.md`.
4. **Identify tension** — surface only tension already present in the input. Read `prompts/tension.md`.
5. **Build argument** — choose a fitting structure rather than forcing a template. Read `prompts/structures.md`.
6. **Preserve voice** — compare every important sentence with the intent map and style profile.
7. **X Content Optimization** — improve hook, density, readability, shareability, reply potential, authenticity, and novelty without claiming knowledge of X's algorithm. Read `prompts/x-optimize.md`.
8. **De-AI** — detect and rewrite mechanical AI patterns. Read `prompts/de-ai.md`.
9. **Quality review** — score and apply gates using `prompts/review.md`.

## Mode behavior

- **polish:** keep structure and wording where they already work; edit locally.
- **rewrite:** preserve the claim and values, but rebuild the argument.
- **expand:** develop implications already latent in the fragment; never add facts or personal history.
- **distill:** remove supporting material until one complete X-sized claim remains.

For `auto` length, use `short` for one clean observation, `medium` for a claim needing explanation, and `long` only when multiple necessary reasoning steps cannot be compressed honestly.

## Style rules

Treat `config/style-profile.yaml` as preferences, not content. If `examples/liked-posts.md` contains samples, learn rhythm, vocabulary, sentence length, and structural tendencies only. Never copy its phrases or import its opinions into the current post.

Avoid one-sentence paragraphs by default, excessive blank lines, mechanical parallelism, repeated “不是 A，而是 B”, fake quotes, invented experiences or data, motivational clichés, empty grandeur, forced question endings, and stock openings such as “在这个时代”. Do not fabricate depth or a persona.

## Quality gates

Score 100 points: idea preservation 20, hook 15, insight 15, human voice 20, logic 10, readability 10, shareability 10.

Fail immediately when `idea_preservation < 15`, `human_voice < 15`, or the draft invents facts/experience or changes the author's core stance. Target total: 80. If below 80, revise the weakest dimensions and rescore. Make at most two revisions; then return the most faithful version rather than gaming the score.

## Failure handling

- Contradictory fragments: preserve both and name the uncertainty; do not pick a side for the author.
- Too little content: produce a restrained short post or ask one focused question if even the claim is unknowable.
- Unsupported factual claim: frame it as the author's thought or uncertainty; do not strengthen it into fact.
- Style conflicts with fidelity: fidelity wins.
- Requested virality conflicts with authenticity: explain briefly and deliver the strongest faithful version.

## Compact example

Input: `AI真正改变的可能不是知识获取，而是一个普通人第一次拥有了无限执行力，但我还没想清楚。`

Core insight: AI's personal impact may be less about access to knowledge and more about lowering the cost of acting on an idea.

Good direction: retain “可能” and the unfinished, exploratory tone; clarify what “执行力” means. Bad direction: invent productivity statistics, claim “everyone”, or turn it into a success slogan.

See `examples/` for full process examples.
