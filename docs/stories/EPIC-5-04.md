# EPIC-5-04 — The tool stays local: no network, no API key

**Epic:** EPIC-5 Data safety and audit · **Covers:** NFR-004, NFR-006 · **Size:** S · **Build order:** 3 of 25
**Depends on:** EPIC-1-01 · **Open questions:** none

**Story:** As a delivery manager, I want the tool to keep everything in local files and never contact a service, so that client notes do not leave my machine through it.

## Acceptance criteria

1. Given the full test suite, when it runs with network sockets blocked, then every test passes and zero connections are attempted.
2. Given the code in `src/`, when the import check runs, then it finds zero imports of network modules (`socket`, `urllib`, `http`, `requests`, `httpx`).
3. Given a project folder, when `raid review` and `raid list` run, then no file outside that folder is created or changed.
4. Given an environment with no API key variables set, when any CLI command runs, then it works without asking for one.

## Notes

The check is added to the test suite once and then covers every later story automatically.
