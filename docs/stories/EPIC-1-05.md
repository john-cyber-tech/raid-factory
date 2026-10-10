# EPIC-1-05 — `/raid-extract` writes proposals from a notes file

**Epic:** EPIC-1 Extraction and review · **Covers:** REQ-001, REQ-002, REQ-003, REQ-004, REQ-039 · **Size:** M · **Build order:** 9 of 25
**Depends on:** EPIC-1-02, EPIC-1-04 · **Open questions:** OQ-18

**Story:** As a delivery manager, I want to run one command on my call notes and get a list of candidate RAID items, so that I stop missing things I meant to write down.

## Acceptance criteria

1. Given `inputs/sample-meeting-notes.md` and a log holding 3 items, when I run `/raid-extract inputs/sample-meeting-notes.md`, then `pending.json` is written and the log is byte-identical to before.
2. Given that `pending.json`, when I run `raid review`, then it passes validation and the first proposal is shown.
3. Given that `pending.json`, then it contains a proposal for each of these five lines of the notes, with the stated type: the security review that has not started (Risk); the legacy ERP export assumed to be CSV (Assumption); the test environment down since Monday (Issue); cutover waiting on Acme finance's year-end close (Dependency); the key analyst on leave in November (Risk).
4. Given the test-environment proposal, then its owner is "Priya" and its due date is empty; given the CSV-export proposal, then its owner is empty.
5. Given that `pending.json`, then exactly one proposal concerns the security review, although the notes mention it on two lines.
6. Given the sample notes, whose heading is "7 Oct" with no year, then the year-end-close proposal has an empty due date; given a copy of the notes headed "7 Oct 2026", then its due date is 2026-10-25.
7. Given the sample notes, headed "7 Oct" with no year, then every proposal's source date is empty; given a copy headed "7 Oct 2026", then every proposal's source date is 2026-10-07.
8. Given the `pending.json` from the sample notes, when I accept the first proposal in `raid review`, then I am asked for its source date before it enters the log.
9. Given any proposal, then all seven fields are present, its title is at most 80 characters, and its source excerpt appears word for word in the notes file.

## Notes

Checked by running the command in a Claude Code session and comparing the output by hand; it cannot be a pytest test because the CLI never runs extraction. Criterion 3 tests REQ-004 through the Risk/Issue pair. Criteria 5 and 6 apply decision DEC-07; criteria 7 and 8 apply DEC-08; the title limit is DEC-09. Consequence to be aware of: the sample notes carry no year anywhere, so every due date and source date extracted from them is empty, and the manager supplies the source date at review. "Word for word" is my reading of NEED-07, confirm.
