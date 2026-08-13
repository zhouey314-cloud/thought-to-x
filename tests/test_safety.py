from pathlib import Path
import re
import unittest


class SafetyTests(unittest.TestCase):
    def test_no_hardcoded_api_credentials(self) -> None:
        root = Path(__file__).resolve().parents[1]
        files = [*root.glob("src/**/*.py"), *root.glob("prompts/*.md"), root / "SKILL.md"]
        secret_patterns = [
            re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
            re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
            re.compile(r"Bearer\s+[A-Za-z0-9._-]{24,}"),
        ]
        for path in files:
            text = path.read_text(encoding="utf-8")
            for pattern in secret_patterns:
                self.assertIsNone(pattern.search(text), f"possible credential in {path}")

    def test_prompt_integrity(self) -> None:
        root = Path(__file__).resolve().parents[1]
        corpus = "\n".join(path.read_text(encoding="utf-8") for path in [root / "SKILL.md", *root.glob("prompts/*.md")]).lower()
        self.assertIn("preserve the idea", corpus)
        self.assertTrue("no fabrication" in corpus or "never fabricate" in corpus)
        self.assertIn("de-ai", corpus)
