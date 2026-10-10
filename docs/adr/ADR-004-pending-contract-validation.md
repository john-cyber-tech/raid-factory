# ADR-004: `pending.json` is defined by one JSON Schema file, checked with the `jsonschema` library

**Status:** Accepted (2026-10-10, with the approval of stage 3)
**Owner:** Project owner · **Date:** 2026-10-10
**Driven by:** REQ-005, REQ-006, REQ-041, NFR-004, NFR-005, NFR-010; brief ("the CLI validates `pending.json` against a schema")
**Review trigger:** the tool must be installed on machines that cannot install any third-party Python package.
**Confirmed by the owner:** keep the `jsonschema` dependency (DEC-12).

## Context

`pending.json` is the only way model output enters the tool (ADR-002). Two parties need the same definition of "valid": the extraction command, which must produce it, and the validator, which must enforce it. The brief names no validation library and lists no dependencies.

## Alternatives considered

| # | Option | For | Against |
|---|---|---|---|
| 1 | **One `pending.schema.json` file in standard JSON Schema, enforced by the `jsonschema` library, plus a small second check for things a schema cannot express (real calendar dates)** | One source of truth that the command can read and the validator enforces. Mature library; error paths name the proposal and field | Adds the tool's only third-party dependency. Installing it needs a package index once |
| 2 | Hand-written validator using only the standard library | No dependency at all | The rules live in code, so the command's description of the contract is a second copy that can drift. More code to test for exactly the part that guards the trust boundary |
| 3 | Typed models with `pydantic` | Good error messages; also usable for the log | Heavier dependency with compiled parts. The contract is Python code, which the extraction command cannot read as a contract |

## Decision

Option 1. The schema lists each field, its allowed values, the 80-character title limit, forbids extra fields, and forbids control characters in text. The validator (COMP-02) runs the schema over the whole file, then checks dates are real. Any failure rejects the whole file with the proposal number, field and reason. `jsonschema` is pinned to a fixed version and used offline; it makes no network calls when the schema has no external references, and the schema will have none.

## Consequences

- Good: the contract is a file a reviewer can read in a minute, and stage 5 fixtures are checked against the same file the command is told to follow.
- Good: REQ-006's "message says what is wrong" comes largely from the library's error paths.
- Bad: one dependency to install and keep pinned, and it must work on every supported Python (3.12 or later, built on 3.13, DEC-14). The owner accepted this (DEC-12).
- Bad: library error messages are technical; the validator must reword them into the plain messages REQ-006 asks for.
- Note: the severity values in the schema are High, Medium and Low (DEC-18).

## Agent-readable summary

`pending.schema.json` is the single definition of a valid `pending.json`. Change the contract by changing that file, never by adding checks elsewhere that contradict it. `jsonschema` is the only third-party runtime dependency; do not add others without a new ADR.
