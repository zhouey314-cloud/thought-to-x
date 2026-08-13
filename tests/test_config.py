from pathlib import Path
import tempfile
import unittest

from thought_to_x.config import ConfigError, load_style_profile


class ConfigTests(unittest.TestCase):
    def test_default_style_profile_loads(self) -> None:
        profile = load_style_profile()
        self.assertEqual(profile["language"], "zh-CN")
        self.assertEqual(profile["platform"], "X")
        self.assertIs(profile["preferences"]["preserve_original_idea"], True)

    def test_invalid_style_profile_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "style.yaml"
            path.write_text("language: zh-CN\n", encoding="utf-8")
            with self.assertRaisesRegex(ConfigError, "missing required key"):
                load_style_profile(path)
