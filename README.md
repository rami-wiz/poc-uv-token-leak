# PoC: uv run token leak via pyproject.toml build hook

This demonstrates how `uv run` can leak CLI secrets when a malicious `pyproject.toml` is present.

## Vulnerability

When `uv run` detects a `pyproject.toml` in the working directory, it installs the project
(executing build hooks) BEFORE running the target script. A build hook can read the parent
process's command line from `/proc` to steal secrets passed as arguments.

## To exploit

1. Fork this repo
2. Add `pyproject.toml`, `src/__init__.py`, and `hatch_build.py` (see below)
3. Open a PR - the build hook will capture the token

## Attack files

See the `exploit-branch` for the malicious files.
