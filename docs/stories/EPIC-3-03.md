# EPIC-3-03 — Show likely duplicates during review

**Epic:** EPIC-3 Flags and duplicates · **Covers:** REQ-023 · **Size:** M · **Build order:** 20 of 25
**Depends on:** EPIC-1-03 · **Open questions:** none

**Story:** As a delivery manager, I want to be told when a proposal looks like something already in the log, so that the same risk is not recorded three times.

## Acceptance criteria

1. Given a log holding R-001 "Client security review may delay cutover", when a Risk proposal titled "client  security review may delay CUTOVER" is reviewed, then R-001 is shown beside it as a likely duplicate, with its ID and title.
2. Given the same log, when a Risk proposal titled "Security review delay raised again" is reviewed (3 of its 5 key words are in R-001's title), then R-001 is shown as a likely duplicate.
3. Given the same log, when a Risk proposal titled "Key analyst on leave in November" is reviewed, then no likely duplicate is shown.
4. Given the same log, when an Issue proposal titled "Client security review may delay cutover" is reviewed, then no likely duplicate is shown, because the type differs.
5. Given that Issue proposal, when I edit its type to Risk during review, then R-001 is now shown as a likely duplicate.
6. Given a proposal with a likely duplicate shown, then I am still asked for my own decision and nothing is merged automatically.

## Notes

Rule from decision DEC-01, stated in REQ-023: same type, and either identical titles ignoring case, spacing and punctuation, or at least 2 shared key words making up at least half of the shorter title's key words. The threshold is assumption A-10 and is tuned on the test notes in stage 5.
