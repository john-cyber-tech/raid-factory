# ADR-005: The user's name is kept in a file inside the project folder

**Status:** Accepted (2026-10-10, with the approval of stage 3)
**Owner:** Project owner · **Date:** 2026-10-10
**Driven by:** REQ-035, REQ-020, NFR-006; DEC-02; stage 2 finding T-03
**Review trigger:** a later version lets two people work in the same project folder. v1 is single-user by decision (DEC-13).

## Context

DEC-02: "The tool has one local user. Ask for a name once, store it in a config file, and stamp it on every history entry." NFR-006 says the tool writes only inside the project folder. Those two pull apart: "once" suggests one place per person, "inside the project folder" suggests one place per project. Sean runs three projects.

## Alternatives considered

| # | Option | For | Against |
|---|---|---|---|
| 1 | **`raid-config.json` in the project folder** | Keeps NFR-006 exactly as approved: nothing is written outside the project. A project folder is self-contained and can be copied or archived whole | The name is asked for once per project, so three times for Sean. If a folder is ever shared, the second person's changes are stamped with the first person's name |
| 2 | One file per user in the home directory | Truly asked once. Correct if a folder is shared between people | Breaks NFR-006 as written; the tool now writes outside the project folder, which the confidentiality argument relies on being able to say it does not |
| 3 | No file: take the name from an environment variable or the operating system's login name | Nothing to store | Does not match DEC-02 ("ask once, store it"). Login names are often not a person's real name, and the audit trail is for the client's PMO to read |

## Decision

Option 1. Identity (COMP-09) reads `raid-config.json` from the project folder. If it has no name, the first command that changes the log asks for one and saves it. Read-only commands never ask. The name is not verified.

## Consequences

- Good: NFR-006 and its test stay simple: every file the tool writes is in the project folder.
- Bad: "once" means once per project, not once ever.
- Bad: the name is whatever was typed. It is an attribution aid, not proof of who made a change; the history must not be presented to the client's PMO as authenticated.
- Bad: this is only right while one person uses a folder, which is the v1 decision (DEC-13) and a listed known limitation. A multi-user version should switch to option 2 and amend NFR-006.

## Agent-readable summary

The user's name lives in `raid-config.json` in the project folder. The tool writes no file outside the project folder. Ask for the name only on commands that change the log.
