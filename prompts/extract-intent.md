# 02 Extract Intent

Input: `normalized_thought`.

Map what the author actually supplied. Use `unknown` or an empty list when evidence is absent.

```yaml
topic:
core_claim:
emotion:
user_intention:
target_reader:
important_phrases: []
must_preserve: []
uncertain_points: []
```

Separate the core judgment from background, repetition, examples, and unresolved questions. Do not infer demographics, experience, authority, or certainty.
