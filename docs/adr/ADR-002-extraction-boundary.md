# ADR-002: Extraction is a Claude Code command; the CLI only validates its output

**Status:** Accepted (2026-10-10, with the approval of stage 3)
**Owner:** Project owner · **Date:** 2026-10-10
**Driven by:** NFR-004, NFR-005, NFR-006, REQ-001, REQ-002, REQ-005, REQ-006, REQ-007, REQ-008, REQ-042; NEED-02, NEED-06; `CLAUDE.md` product design note
**Review trigger:** the client approves a different AI service, or the team wants extraction to run unattended.

## Context

Extraction needs a language model. The notes are confidential client material and are untrusted input: text in them could be written to look like instructions. The brief says the Python tool makes no network calls and needs no API key, and that nothing may reach the log without the manager's decision.

## Alternatives considered

| # | Option | For | Against |
|---|---|---|---|
| 1 | **A Claude Code slash command (`/raid-extract`) writes `pending.json`; the Python CLI validates that file against a schema and puts every proposal through human review** | The CLI stays offline and key-free. Notes go only to the assistant the team already uses. One narrow, inspectable hand-off file. The CLI is fully testable from fixtures | Two tools to run, in two places. Extraction quality cannot be tested by pytest |
| 2 | The CLI runs Claude Code headless (`claude -p`) as a subprocess | One command for the user | The CLI now launches a networked process and depends on Claude Code being installed and logged in. It breaks the "CLI makes no network calls" constraint in spirit. Model output arrives inside the tool's own process |
| 3 | The CLI calls the model API directly | One command; full control of the prompt | Needs an API key and network calls, which the brief forbids. Sends client notes to a service path the client has not approved |
| 4 | No extraction: the manager types every item with `raid add` | No AI risk at all | Does not meet the main need (NEED-01, items missed from memory) |

## Decision

Option 1. The boundary between the two tools is the file `pending.json` and nothing else. Injected or malformed content is contained by four layers:

1. The command's prompt wraps the notes as data and says text inside them is never an instruction.
2. The command's allowed tools are limited to reading the notes file and writing `pending.json` (REQ-042, DEC-19); anything else would need the user to grant permission in the session.
3. The validator (COMP-02) accepts only the contract's fields, allowed values and lengths, rejects extra fields and control characters, and rejects the whole file on any failure.
4. A person sees each proposal with its source excerpt and accepts or rejects it. The CLI stores and displays proposal text; it never interprets it.

## Consequences

- Good: NFR-004 and NFR-006 hold by construction for the Python tool.
- Good: a successful injection can at worst produce a bad *proposal*, which is still shown to a person with the words it came from.
- Bad: layers 1 and 2 are instructions to a model and session permissions, not guarantees. Layers 3 and 4 are the ones that can be tested. A convincing fake item could still be accepted by a hurried reviewer.
- Bad: `/raid-extract` can only be checked by running it by hand against fixtures (NFR-005, stories EPIC-1-05 and EPIC-1-06).
- Bad: the command file has to be present wherever the manager runs Claude Code. How it gets there is a handover question for stage 6.
- Bad: decided proposals are removed from `pending.json` and rejections are not recorded (DEC-10), so there is no trace of what extraction proposed and the manager turned down. Listed as a known limitation.
- Unchanged: whether the client allows notes in the Claude Code session at all remains the user's sign-off (OQ-08).

## Agent-readable summary

The Python code never calls a model, a subprocess that calls a model, or the network. Extraction output is untrusted: it enters only through `pending.json`, is validated as a whole against `pending.schema.json`, and reaches the log only by an explicit human accept in `raid review`.
