# RAID Log Manager factory

## Run it
1. `cd raid-factory && claude`
2. Read and edit `inputs/brief.md` (stack choices are at the bottom).
3. Run `/factory-next` repeatedly, or call stages directly: `/stage-1-requirements` …
4. Review the stage output in `docs/`, then `/approve 1` (or give feedback and re-run the stage).
5. After stage 6 you have a working CLI, tests, and a release note.

## Stages
| # | Command | Reference | Output |
|---|---|---|---|
| 1 | /stage-1-requirements | s1-requirements.md | docs/requirements.md |
| 2 | /stage-2-stories | s1-requirements.md, s2-stories.md | docs/epics.md, docs/stories/ |
| 3 | /stage-3-architecture | s3-architecture.md | docs/architecture.md, docs/adr/ |
| 4 | /stage-4-specs | s4-specs.md | docs/specs/, docs/task-dag.md |
| 5 | /stage-5-build | s4-specs.md, s5-build.md | src/, tests/ |
| 6 | /stage-6-release | s6-release.md | docs/threat-review.md, docs/release-note.md |

Optional: if you have the pipeline skills installed (requirements-writer, requirements-checker,
requirements-to-epics, epic-to-story-decomposer, solution-architecture-writer, adr-writer,
engineering-spec-writer, task-dag-builder, build-readiness-checker) the commands will use them;
otherwise they follow the built-in instructions.

## Using the tool
What is built so far: `raid review` and `raid list`. Extraction (`/raid-extract`), updating and
closing items, flags, duplicates and the weekly summary are not built; see
`docs/reviews/stage-5-review.md`, "Scope reduction".

**Install** (Python 3.12 or later; no network calls, no API key):

    pip install -e .            # gives the `raid` command
    pip install -e ".[test]"    # also installs pytest
    pytest                      # run the tests

Run `raid` from a project folder. It keeps three files there:

| File | What it is |
|---|---|
| `pending.json` | Proposals waiting for your decision. Until `/raid-extract` exists, write it by hand or copy an example from `tests/fixtures/pending/valid_three.json` |
| `raid-log.json` | The RAID log. Written only by the tool; do not edit it by hand |
| `raid-config.json` | Your name, asked once on your first accept and recorded in each item's history |

The tool creates these files readable by you only (mode 0600). They are plain text and can hold
client material: if the project folder is kept in git, add all three to its `.gitignore`.

Files created before that fix (commit `94dcfb1`) keep their old mode, readable by other users of the
machine, until the tool next writes them. `raid-log.json` and `pending.json` are rewritten on the
next accept or reject; `raid-config.json` is written once and is not rewritten. To fix old files
now: `chmod 600 raid-log.json pending.json raid-config.json`.

**`raid review`** checks the whole of `pending.json` first. If any proposal is invalid it lists
the problems, shows nothing and changes nothing (exit 1). Otherwise it shows each proposal with
its source excerpt and asks `Accept, edit or reject? (a/e/r):`

- `a` adds the item to the log and prints its ID (`R-001`, `A-001`, `I-001`, `D-001`). If the
  proposal has no date for the notes, or one after today, it asks for the date (YYYY-MM-DD)
  first; an empty answer cancels the accept.
- `e` asks for a field (`type`, `title`, `description`, `owner`, `severity`, `due_date`) and a
  new value, then shows the proposal again. An empty value clears `owner` or `due_date`. The
  source excerpt and source date cannot be edited.
- `r` drops the proposal. Rejections are not kept anywhere.

Each decided proposal leaves `pending.json` at once, so you can stop and carry on later. With
nothing to decide it prints `Nothing to review.`

**`raid list`** prints every item in the log: ID, type, title, owner, severity, due date and
status. An empty owner or due date shows as `-`.

    ID     Type   Title                                     Owner  Severity  Due date  Status
    R-001  Risk   Client security review may delay cutover  -      High      -         Open
    I-001  Issue  Test environment down                     Priya  High      -         Open

Both commands exit 0 on success and 1 when something was refused or failed, for example a
damaged `raid-log.json`; in that case nothing is written.
