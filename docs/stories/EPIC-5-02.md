# EPIC-5-02 — Every change to an item is recorded in an append-only history

**Epic:** EPIC-5 Data safety and audit · **Covers:** REQ-020, NFR-007 · **Size:** M · **Build order:** 5 of 25
**Depends on:** EPIC-1-01, EPIC-5-01, EPIC-5-05 · **Open questions:** none

**Story:** As a project manager, I want each item to carry a record of when it was created and every change since, so that the client's PMO can audit the log.

## Acceptance criteria

1. Given the stored name "Sean Murphy" and a proposal accepted as R-001, then R-001's history has one entry recording its creation with a timestamp and the name "Sean Murphy".
2. Given R-001 with an empty owner, when the owner is set to "Priya Nair", then its history has two entries and the second shows field `owner`, old value empty, new value "Priya Nair", a timestamp and the name "Sean Murphy".
3. Given R-001 with two history entries, when any CLI command built so far runs, then those two entries are byte-identical afterwards.
4. Given R-001, when an update is refused (for example an invalid value), then no history entry is added.

## Notes

The name comes from EPIC-5-05 (decision DEC-02); it is unauthenticated. This story provides the 'created' and 'last changed' dates that EPIC-3-02 and EPIC-4-01 use.
