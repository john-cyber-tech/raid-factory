# ADR-006: Each item carries its own append-only history, inside the log file

**Status:** Accepted (2026-10-10, with the approval of stage 3)
**Owner:** Project owner · **Date:** 2026-10-10
**Driven by:** REQ-020, REQ-019, REQ-027, REQ-029, REQ-034, NFR-007, NFR-002; NEED-12
**Review trigger:** the client's PMO asks for history that cannot be altered even by editing the file.

## Context

Acme's PMO wants to know who raised an item, when, and every change after that. The stale flag needs "last changed" and the summary needs "created this week". History must never be edited or removed by the tool (NFR-007), and must stay consistent with the item it describes even if a save is interrupted (NFR-002).

## Alternatives considered

| # | Option | For | Against |
|---|---|---|---|
| 1 | **Store each item's current values and, with them, a list of history entries; one save writes both** | Item and history can never disagree after a crash, because they are in the same atomic save (ADR-001). `raid show` reads one place. Simple to explain | History can only be guarded, not made tamper-proof: anyone can edit the file by hand. The file grows with every change |
| 2 | Event sourcing: store only the events and work out each item's current values by replaying them | History is the source of truth, so it cannot drift from the state | Every command replays everything. Much more code and many more ways to be wrong, for a tool with hundreds of items. Harder to read the file by eye |
| 3 | Keep history in a separate file beside the log | Log file stays small | Two files cannot be replaced in one step. A crash between them leaves a change with no history or history with no change, which is the failure NEED-12 is about |

## Decision

Option 1. Every change made through the log store (COMP-05) appends one entry: timestamp, user name, and what changed (created, field with old and new value, merged, closed with reason). The save guard from ADR-001 compares the outgoing file with the one on disk and refuses to save if any existing entry is different or missing. No interface edits or deletes history. "Created" and "last changed" are read from the first and last entries, not stored separately.

## Consequences

- Good: NFR-007 has one enforcement point that is easy to test.
- Good: stale detection and "new this week" need no extra fields that could disagree with the history.
- Bad: the history is trustworthy only against the tool's own mistakes. A person with a text editor can rewrite it, and the tool cannot tell. Say so if the PMO asks.
- Bad: a refused update must leave no entry behind, so validation has to happen before anything is appended.
- Bad: the user name in each entry is unverified (ADR-005).

## Agent-readable summary

Never modify or remove an existing history entry. Every state change to an item goes through the log store and appends exactly one entry in the same save. Derive created and last-changed dates from history; do not store them twice.
