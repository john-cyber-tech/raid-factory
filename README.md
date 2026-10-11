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
