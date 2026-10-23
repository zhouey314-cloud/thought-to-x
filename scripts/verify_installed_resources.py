"""Verify wheel-installed portable assets against their unchanged source files.

Run with the installed environment's Python from outside the source checkout:
python /path/to/checkout/scripts/verify_installed_resources.py /path/to/checkout
No provider or network is used.
"""
from importlib.metadata import version
from pathlib import Path
import hashlib
import json
import sys

import thought_to_x
from thought_to_x.pipeline import PipelineRequest, ThoughtToXPipeline
from thought_to_x.resources import default_resource_root

source = Path(sys.argv[1]).resolve()
package = Path(thought_to_x.__file__).resolve()
if package.is_relative_to(source):
    raise AssertionError("must test an installed package outside the source checkout")
root = default_resource_root()
paths = [Path("SKILL.md")]
for pattern in ("prompts/*.md", "config/*.yaml", "workflows/*.md", "examples/*.md"):
    paths.extend(sorted(path.relative_to(source) for path in source.glob(pattern)))
checked = []
for relative in paths:
    expected = (source / relative).read_bytes()
    actual = root.joinpath(relative.as_posix()).read_bytes()
    if actual != expected:
        raise AssertionError(f"missing or changed installed resource: {relative}")
    checked.append({"path": relative.as_posix(), "sha256": hashlib.sha256(actual).hexdigest()})
request = PipelineRequest("A tentative synthetic thought.")
system, user = ThoughtToXPipeline().build_prompts(request)
assert "A tentative synthetic thought." in user
assert "never fabricate" in system.lower()
print(json.dumps({"status": "PASS", "version": version("thought-to-x"),
                  "resources": checked, "prompt_only": "PASS", "provider_calls": 0,
                  "semantic_quality": "NOT_RUN"}, indent=2))
