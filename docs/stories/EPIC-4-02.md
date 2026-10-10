# EPIC-4-02 — Summary shows top risks, what is blocked by whom, and decisions needed

**Epic:** EPIC-4 Weekly summary · **Covers:** REQ-031, REQ-032, REQ-037 · **Size:** S · **Build order:** 24 of 25
**Depends on:** EPIC-4-01, EPIC-2-05, EPIC-2-07 · **Open questions:** OQ-01

**Story:** As a client sponsor, I want the summary to show the biggest risks and what is waiting on whom, so that I know what could hurt the project and where it is stuck.

## Acceptance criteria

1. Given open risks R-001 High and R-002 Medium and closed risk R-003 High, then "Top risks" lists R-001 only.
2. Given open D-001 "Acme finance year-end close" waiting on "Acme finance team", then the summary shows that title and "Acme finance team" on the same line.
3. Given a Closed dependency, then it does not appear in the dependencies section.
4. Given open R-001 and open I-001 marked as needing a decision, open R-002 unmarked and closed A-001 marked, then "Decisions needed" lists R-001 and I-001 only.

## Notes

Criterion 1 is written against the OQ-01 default (High/Medium/Low, top = High). Tom's "what could hurt go-live" and "what Acme needs to do" have no section of their own in v1 (decision DEC-03).
