# SPEC-EPIC-5-04 — The tool stays local: no network, no API key

**Story:** EPIC-5-04 · **Covers:** NFR-004, NFR-006 · **Components:** COMP-02 to COMP-09 (whole Python tool)
**Build order:** 3 of 25 · **Risk tier:** MEDIUM (Adds the suite-wide safety net; no product behaviour.) · **Depends on:** SPEC-EPIC-1-01

## Why

As a delivery manager, I want the tool to keep everything in local files and never contact a service, so that client notes do not leave my machine through it.

Client notes must not leave the machine through the tool (NEED-06): no network, no key, no writes outside the project folder (NFR-004, NFR-006).

## Capabilities

- `tests/conftest.py`: a fixture applied to every test that replaces socket creation with a function that fails the test.
- `tests/test_boundaries.py`: an import check that parses every file under `src/` and fails on `socket`, `urllib`, `http`, `requests`, `httpx`, `subprocess` used to start a model, or any `anthropic` package.
- A fixture that snapshots a parent folder around the project folder and fails if anything outside the project folder is created or changed.
- A test that runs each command with every `*_API_KEY` and `ANTHROPIC_*` variable removed.

## Constraints

- The Python code never calls a model, a model-calling subprocess, or the network (ADR-002, NFR-004).
- Every file the tool writes is in the project folder (ADR-005, NFR-006).
- `jsonschema` is the only third-party runtime dependency (ADR-004, DEC-12).

## Non-goals

- Checking what the Claude Code session does with notes (OQ-08 is the owner's sign-off).
- Operating-system firewalls or sandboxing.

## Success signal

The full suite passes with sockets blocked, and the import check and the outside-write check both pass.

## Test plan

The Criteria column gives the story's acceptance criterion numbers; CF-n is an item carried forward from the stage 3 review.

| Test | Criteria | Checks |
|---|---|---|
| `test_suite_runs_with_sockets_blocked` | 1 | The blocking fixture is active for every test; a canary test proves a socket attempt fails. NFR-004. |
| `test_no_network_imports_in_src` | 2 | Zero forbidden imports under `src/`. NFR-004. |
| `test_import_check_catches_a_planted_import` | 2 | Failure path: the checker flags a sample file that imports `urllib`. |
| `test_no_writes_outside_project_folder` | 3 | `raid review` and `raid list` change nothing outside the folder. NFR-006. |
| `test_commands_work_without_api_keys` | 4 | Each command built so far exits 0 with key variables unset. NFR-004. |
| `test_only_declared_dependency_is_jsonschema` | 2 | Edge: `pyproject.toml` lists exactly one runtime dependency. DEC-12. |

**Test data:** No product data. The outside-write check uses a temporary parent folder with a sentinel file.

## Definition of done

- Every test in the test plan exists and passes under `pytest` on Python 3.13, with no Claude Code session and no network.
- Every test names the REQ or NFR it checks, in its name or docstring (NFR-010).
- The whole suite is still green, and the code uses nothing Python 3.12 lacks (DEC-14).
- Later specs add their commands to the outside-write and no-key tests.
- Tests are written before the code for this spec, in the same session.
- MEDIUM tier: show the owner the diff before committing.
