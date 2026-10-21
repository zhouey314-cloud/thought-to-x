"""Check offline CLI behavior through real processes without inherited API keys."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import thought_to_x


class CLITests(unittest.TestCase):
    def invoke(self, value, *, stdin=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            # Guard connections after Python's normal site initialization.
            guard = (
                "import socket, runpy; "
                "blocked = lambda *a, **k: (_ for _ in ()).throw("
                "RuntimeError('network forbidden in prompt-only mode')); "
                "socket.socket.connect = blocked; "
                "socket.socket.connect_ex = blocked; "
                "socket.create_connection = blocked; "
                "runpy.run_module('thought_to_x', run_name='__main__')"
            )
            package_root = Path(thought_to_x.__file__).resolve().parent.parent
            return subprocess.run(
                [sys.executable, "-B", "-c", guard, value, "--prompt-only"],
                cwd=root,
                env={
                    "PATH": os.environ.get("PATH", os.defpath),
                    "PYTHONPATH": str(package_root),
                    "PYTHONDONTWRITEBYTECODE": "1",
                },
                input=stdin, capture_output=True, text=True, timeout=20,
            )

    def test_long_literal_thought_is_not_a_filesystem_path(self):
        thought = "A tentative idea, not a verified fact. " * 100
        result = self.invoke(thought)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(thought.strip(), result.stdout)
        self.assertIn("--- USER INPUT ---", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_stdin_and_utf8_file_work_without_keys_or_network(self):
        thought = "这是一个保留不确定性的合成想法。"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "thought.txt"
            path.write_text(thought, encoding="utf-8")
            for value, stdin in (("-", thought), (str(path), None)):
                with self.subTest(value=value):
                    result = self.invoke(value, stdin=stdin)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn(thought, result.stdout)

    def test_invalid_utf8_file_has_an_actionable_error_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.txt"
            path.write_bytes(b"\xff")
            result = self.invoke(str(path))
        self.assertEqual(result.returncode, 1)
        self.assertIn("error:", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(result.stdout, "")
