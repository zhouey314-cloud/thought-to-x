# 09 Quality review

Score the draft with evidence:

```yaml
idea_preservation: 0-20
hook: 0-15
insight: 0-15
human_voice: 0-20
logic: 0-10
readability: 0-10
shareability: 0-10
total: 0-100
hard_failures: []
revision_targets: []
```

Hard fail if idea preservation or human voice is below 15, or if the draft fabricates facts/experience or changes the author's core stance. The target is 80. Below target, revise only the weakest dimensions, then rerun the De-AI and review passes. Stop after two revisions and choose fidelity over a higher score.
