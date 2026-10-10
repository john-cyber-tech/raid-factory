# ADR-001: One JSON file per project, saved by write-then-replace

**Status:** Proposed (becomes Accepted when stage 3 is approved)
**Owner:** Project owner · **Date:** 2026-10-10
**Driven by:** NFR-002, NFR-003, NFR-006, REQ-010, REQ-011, REQ-019; brief (Stack: "JSON file per project")
**Review trigger:** a log is expected to exceed a few thousand items (OQ-11), or a later version must let more than one person write to the same log.

## Context

The brief asks for a local JSON file per project that "must survive a crash mid-write and never lose accepted items". The delivery manager wants local files and no new system. Log size is unknown (OQ-11); nothing in the sources suggests more than hundreds of items.

## Alternatives considered

| # | Option | For | Against |
|---|---|---|---|
| 1 | **One JSON file, whole file rewritten on each change: write to a temporary file in the same folder, flush to disk, then replace the log in one operating-system step** | Matches the brief. A person can open and read the file. Replace is all-or-nothing, so a crash leaves the old or the new file | Rewrites everything on each change. No protection if two people write at once |
| 2 | SQLite database file | Real transactions; in the standard library; handles two writers | Not what the brief asks for. Binary file the manager cannot read, diff or forward |
| 3 | Append-only file, one event per line | Natural audit trail; appends are cheap | State must be rebuilt by replaying events on every command; a torn last line needs handling; harder to read by eye |
| 4 | Write the JSON file in place, keeping a `.bak` copy | Simplest code | There is a moment when the log is truncated or half-written; recovery depends on someone noticing and restoring the backup |

## Decision

Option 1. `raid-log.json` holds a schema version, a "next number" counter per type, and the list of items. One save routine in the log store (COMP-05) is the only code that writes it: serialise, write to a temporary file beside it, flush to disk, replace. Before replacing, a save guard checks that no existing item ID and no existing history entry has disappeared or changed.

## Consequences

- Good: NFR-002 is met by a standard, testable technique. The file stays human-readable.
- Good: the per-type counter means a closed or merged item's number is never reused (REQ-011).
- Bad: every change rewrites the whole file. Acceptable at hundreds of items; not measured (NFR-001 has no target).
- Bad: two people saving at the same time means the last save wins and the other's change is lost silently. v1 is single-user by decision (DEC-13) and this is a listed known limitation. A multi-user version needs a successor to this ADR that at least detects a changed file before replacing it.
- Bad: the save is tested on macOS only (DEC-16). The same technique is expected to work on Linux and Windows but that is not verified; listed as a known limitation.
- Bad: a crash can leave a stray temporary file in the project folder. It is harmless and overwritten by the next save.

## Agent-readable summary

Only the log store writes `raid-log.json`, always through the single write-temp-then-replace save routine with its save guard. Do not write the log in place, do not add a second writer, and do not introduce a database.
