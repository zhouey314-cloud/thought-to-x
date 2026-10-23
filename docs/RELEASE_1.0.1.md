# Thought-to-X 1.0.1

This release brings the source, Python package and new GitHub tag to 1.0.1, above the historical v1.0.0 workflow release. The earlier v0.1.0 and v1.0.0 tags stay unchanged. Future releases update pyproject.toml, runtime version, release notes and tag together; rebuild and verify wheel/sdist before publishing.

Includes the installed-resource and CLI input fixes merged in PR #1, plus unchanged supporting Markdown (`SKILL.md`, `workflows/`, `examples/`) in wheel/sdist. Prompt text, pipeline, model configuration, editorial gates, authors and MIT license are unchanged.

## Reproduce

Download and check SHA256SUMS from the Release, create a fresh Python 3.11+ virtual environment outside the source checkout, then:

```sh
python -m pip install ./thought_to_x-1.0.1-py3-none-any.whl
thought-to-x "A tentative synthetic thought." --prompt-only
python /path/to/source/scripts/verify_installed_resources.py /path/to/source
python -m unittest discover -s /path/to/source/tests -v
```

The verifier rejects a source-package import, compares all 18 portable resource files byte-for-byte and assembles prompt-only without a provider. Baseline at a305e230d256aad2728e13395324bddfe35f1b1f passes 13 traditional tests; its wheel lacks SKILL.md and the supporting workflow/examples. No real provider calls or new AI editorial quality evaluation are part of this packaging patch. Mechanical checks do not certify voice preservation or publishing quality.

GitHub release assets include exact source commit/tree, wheel/sdist hashes and validation evidence. Agensi is separate: this work prepares a local review update bundle only. The existing listing identity and installation URL must be retained; no new listing, URL replacement, message or external platform publication is authorized here.
