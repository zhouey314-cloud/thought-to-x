"""Deterministic quality-gate model for agent- or provider-supplied ratings."""

from __future__ import annotations

from dataclasses import dataclass, field

MAX_SCORES = {
    "idea_preservation": 20,
    "hook": 15,
    "insight": 15,
    "human_voice": 20,
    "logic": 10,
    "readability": 10,
    "shareability": 10,
}


@dataclass(frozen=True)
class QualityScore:
    idea_preservation: int
    hook: int
    insight: int
    human_voice: int
    logic: int
    readability: int
    shareability: int
    fabricated_fact: bool = False
    fabricated_experience: bool = False
    changed_core_stance: bool = False
    hard_failures: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        for name, maximum in MAX_SCORES.items():
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= maximum:
                raise ValueError(f"{name} must be an integer between 0 and {maximum}")

    @property
    def total(self) -> int:
        return sum(getattr(self, name) for name in MAX_SCORES)

    @property
    def failures(self) -> tuple[str, ...]:
        failures = list(self.hard_failures)
        if self.idea_preservation < 15:
            failures.append("idea_preservation_below_15")
        if self.human_voice < 15:
            failures.append("human_voice_below_15")
        if self.fabricated_fact:
            failures.append("fabricated_fact")
        if self.fabricated_experience:
            failures.append("fabricated_experience")
        if self.changed_core_stance:
            failures.append("changed_core_stance")
        return tuple(dict.fromkeys(failures))

    @property
    def passed(self) -> bool:
        return self.total >= 80 and not self.failures

    @property
    def needs_revision(self) -> bool:
        return not self.passed
