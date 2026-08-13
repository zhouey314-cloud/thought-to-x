# 01 Normalize

Input: `raw_thought`.

Repair obvious speech-recognition errors, punctuation, sentence boundaries, filler, typos, and meaningless repetition. Merge duplicates only when they carry no new emphasis or nuance. Preserve unusual wording, emotion, uncertainty, metaphors, qualifications, contradictions, and any phrase that may encode the author's thinking.

Output internally:

```yaml
normalized_thought: ...
repairs_made: []
possible_ambiguities: []
```

Do not silently resolve an ambiguity by inventing an intended meaning.
