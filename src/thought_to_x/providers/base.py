"""Provider-neutral generation interface."""

from __future__ import annotations

from abc import ABC, abstractmethod


class ProviderError(RuntimeError):
    """Raised when a generation provider cannot complete a request."""


class BaseProvider(ABC):
    """A minimal adapter implemented by any supported language model."""

    @abstractmethod
    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        """Generate text from provider-neutral system and user prompts."""
