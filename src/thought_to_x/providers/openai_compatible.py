"""Standard-library adapter for OpenAI-compatible chat completion APIs."""

from __future__ import annotations

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .base import BaseProvider, ProviderError


class OpenAICompatibleProvider(BaseProvider):
    """Call a `/chat/completions` endpoint without locking the core to one SDK."""

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 60.0,
    ) -> None:
        self.api_key = api_key or os.getenv("THOUGHT_TO_X_API_KEY", "")
        self.base_url = (base_url or os.getenv("THOUGHT_TO_X_BASE_URL", "https://api.openai.com/v1")).rstrip("/")
        self.model = model or os.getenv("THOUGHT_TO_X_MODEL", "")
        self.timeout = timeout
        if not self.api_key:
            raise ProviderError("Missing THOUGHT_TO_X_API_KEY")
        if not self.model:
            raise ProviderError("Missing THOUGHT_TO_X_MODEL")

    def generate(self, *, system_prompt: str, user_prompt: str) -> str:
        payload = json.dumps(
            {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "temperature": 0.7,
            }
        ).encode("utf-8")
        request = Request(
            f"{self.base_url}/chat/completions",
            data=payload,
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=self.timeout) as response:  # noqa: S310 - configured endpoint is intentional
                body = json.loads(response.read().decode("utf-8"))
            return str(body["choices"][0]["message"]["content"]).strip()
        except (HTTPError, URLError, KeyError, IndexError, json.JSONDecodeError) as exc:
            raise ProviderError(f"Provider request failed: {exc}") from exc
