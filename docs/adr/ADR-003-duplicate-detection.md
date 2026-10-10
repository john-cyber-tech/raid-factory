# ADR-003: Duplicates are found by a fixed key-word rule in the CLI

**Status:** Accepted (2026-10-10, with the approval of stage 3)
**Owner:** Project owner · **Date:** 2026-10-10
**Driven by:** REQ-023, REQ-024, NFR-004, NFR-010; DEC-01; NEED-04
**Review trigger:** stage 5 tuning on the test notes shows the rule misses too many real duplicates or raises too many false ones.

## Context

Sean's main complaint is the same risk appearing three times. DEC-01 fixed the behaviour: same type plus a similar title or matching key words, suggest only, the manager confirms every merge. The open choice is how "similar" is computed.

## Alternatives considered

| # | Option | For | Against |
|---|---|---|---|
| 1 | **Rule-based, in Python: same type, and either identical titles ignoring case, spacing and punctuation, or at least 2 shared key words making up at least half of the shorter title's key words** | Deterministic, so it can be tested exactly. Offline. The manager can understand why something was flagged | Blind to rewording: "supplier delay" and "vendor running late" share no key words |
| 2 | Model-assisted: `/raid-extract` reads the existing log and marks proposals it thinks are duplicates | Understands rewording | The extraction command would have to read the log, widening what it can touch (ADR-002). Results vary between runs and cannot be asserted in pytest. A marker arriving in `pending.json` is untrusted input |
| 3 | Character-level similarity ratio from the standard library, with a threshold | Catches typos and small edits; offline | A threshold on a ratio is hard to explain and tune; long titles that differ in one important word score as near-identical |
| 4 | No detection; rely on the manager spotting duplicates | Nothing to build | Does not meet REQ-023 |

## Decision

Option 1, as a pure function (COMP-06) that takes a proposal and the log's items and returns the IDs of likely duplicates. It runs when a proposal is shown and again if its type or title is edited. It only suggests. The key-word list and the threshold (assumption A-10) are constants to be tuned in stage 5 against the test notes.

## Consequences

- Good: every case in REQ-023 and EPIC-3-03 is an exact, repeatable test.
- Good: no new dependency and no change to the extraction boundary.
- Bad: reworded duplicates are missed. The mitigation in v1 is the manager's own eye during review; there is no command to merge two items that are already in the log.
- Bad: short titles of two or three key words will match easily and produce false suggestions. A false suggestion costs one keystroke ("keep separate").
- Decided: a merge adds the proposal's source to the existing item and keeps the existing item's values (DEC-15).
- Decided: a Closed item is offered as a likely duplicate, the same as an open one, and `raid add` does not run the check (DEC-17).
- Bad: an item added by hand can therefore duplicate an existing one without any warning.
- Bad: merging into a Closed item leaves it Closed, because a merge keeps the existing item's values (DEC-15). A risk that has come back must be reopened by the manager as a separate step.

## Agent-readable summary

Duplicate detection is a deterministic pure function on type and title key words. Do not call a model for it and do not let `/raid-extract` read the log. It never merges; a merge happens only when the manager chooses it in review.
