# Stage 1 (and Stage 2) — requirements

> Trimmed excerpt of the EPAM AI Factory notes. Sections included:
> - epam-ai-factory-200_ProductMgmt_and_BA.md — Block 3
> - epam-ai-factory-200_ProductMgmt_and_BA.md — Block 6
> - epam-ai-factory-600_Quality.md — Block 2

---

<!-- source: epam-ai-factory-200_ProductMgmt_and_BA.md -->
# Block 3 — Requirements: the executable spec (BA core)

A framed product is still only intent until it's written down as something buildable. Block 3 is where it becomes the **executable spec** — the contract agents act on at L3. A clear acceptance criterion downstreams into a design, a test, and an eval; an ambiguous one downstreams into three guesses.

 **The spec is context, not only commands** — agents work better with the *reasoning* behind the ask. The executable spec carries the why, so an agent can act on it without re-asking you.

 **Acceptance criteria name behaviour, not output** — for a deterministic feature an AC reads in [**Gherkin**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#gherkin) / Given–When–Then form; for a non-deterministic one there is no exact string to match, so the AC names *behaviour* (refuse, retry, delegate, complete) plus a threshold. *(How to author one is the Deep path.)*

 **Quality thresholds are acceptance criteria** — the AC also names the [**non-functional requirements**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#nfr): latency (p95 \< 2s), output quality (factuality ≥ 85%) by [LLM-as-judge](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#llm-as-judge). For AI features these are acceptance criteria, not QA afterthoughts.

 **Evals are part of the requirements** — every AI feature ships with the evals that define "working." The eval *is* the acceptance criterion for a probabilistic system.

 [**Decision Memory**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#decision-memory) — a short entry per significant scope call: the decision, the rationale, and the rejected alternative. The rationale and the rejected option are the point — they keep the *why* with the spec instead of in someone's head. When AI drafts the entry, make it write that reasoning too, not only the verdict.

 **Traceability** — a continuous chain: opportunity → spec → design → implementation → tests → production signal → back to opportunity.

- **The supporting moves** (named here, learned in Deep) — current → future → gap analysis, cross-source conflict detection, backlog prioritisation (RICE for ranking, MoSCoW for scope; Kano and WSJF as alternates), prototype and [synthetic-user](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#synthetic-persona) validation, and velocity-grounded estimation, where AI suggests ranges from your team's own closed-story history and the team owns the number. AI does not estimate.

- **Outputs PROD/BA produces:** executable specs, [user stories](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#user-story) with acceptance criteria, eval criteria, Decision Memory, traceability matrices. **Consumers:** Design (prototypes), Architecture (NFRs), Engineering (implementation), QA (tests/evals), Management (portfolio rollup).

*On Meridian,* the predictor's AC is falsifiable: phantom-stock cancellations at pickup ≤ 2%, p95 response \< 1s, and a "stock unknown" fallback when confidence is low.

🏛️**EPAM perspective.** In an [AI Factory](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#ai-factory) — an AI-native delivery team — the spec is not a one-off document but a version-controlled artefact that compounds across engagements, alongside the prompts, evals, and Decision Memory it carries. That is why traceability and Decision Memory are *requirements*, not paperwork: they are what lets the next team reuse the spec instead of re-deriving it.


<!-- source: epam-ai-factory-200_ProductMgmt_and_BA.md -->
# Block 6 — How to ask AI to do PROD/BA work

At L3 you direct the role's work even when no PM/BA is on the team. For each ask, give AI the input, name the artefact you want back, and check the one thing fluent output gets wrong:

| **Task**                          | **The ask (give it X → ask for Y)**                                                   | **What you check**                                              |
|-----------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **Draft an acceptance criterion** | the user story + the outcome metric → Given/When/Then plus one error path and one NFR | it's falsifiable — could an LLM-as-judge score it?              |
| **Synthesize scattered inputs**   | the tickets, notes, and transcripts → one structured requirement set                  | nothing load-bearing was dropped or invented                    |
| **Surface conflicts**             | two or more sources → where they contradict                                           | each candidate against the real rule — AI surfaces, you resolve |
| **Draft a Decision Memory entry** | the scope call → the rationale and the rejected alternative, not only the verdict     | the reasoning is yours, not the model's                         |
| **Attack your own framing**       | in a **fresh session**, your vision or spec → what's hand-wavy or unfalsifiable       | you patch what it finds                                         |

The pattern under all five: AI drafts, *you* validate. Fluent output is not correct output.


<!-- source: epam-ai-factory-600_Quality.md -->
# Block 2 — Requirements Validation and Acceptance Criteria

The thread: the plan selects risks, but acceptance criteria define the behaviour the tests can observe. Vague criteria make every later result ambiguous.

Give an approved AI tool thirty user stories. Ask it to flag criteria that lack observable behaviour and rank the likely rework.

Copy-ready requirements-audit prompt

**Sources:** Read these 30 approved user stories, their acceptance criteria, linked personas, API contracts, and risk labels.

**Task:** Review each story and its criteria as a set. Flag missing observable triggers and outcomes, plus failure paths or measurable boundaries where the feature and risk make them relevant. Rank findings by expected rework.

**Output:** Return a table with Story, Criterion, Missing observable element, Likely rework, Source evidence, and Suggested question.

**Evidence rule:** Quote the criterion and cite its story. Keep product suggestions separate from source-backed findings.

**Uncertainty:** Add Missing inputs and conflicts. Identify stories that lack risk labels, contracts, data, or persona evidence.

**Human decision:** Leave Blocks refinement blank. The BA, PM, and QA lead decide which findings block readiness.

The first list can arrive in under a minute. A QA lead might spend forty minutes on the initial read. The AI result is a hypothesis, so confirm the top five findings against the story and product intent.

Compare these criteria:

**Weak AC:** “Checkout works.”

**Observable AC:** “After successful payment, create the order with the paid total. Decrement inventory exactly once. Show a confirmation containing the order number. After declined payment, preserve the cart and create zero orders.”

The first version allows different interpretations. The second version names results a test can observe.

The **Definition of Ready** is the team-agreed entry gate before testing starts. In this course example, a story is ready when:

- the acceptance criteria name observable behaviour;

- the user and the risk are named, such as revenue or regulatory exposure;

- the story is sized well enough for the team to plan the required test depth;

- required inputs exist, including API contracts, prepared test data, and personas;

- the test item and agreed QA environment are ready.

Without these inputs, the tests may score the wrong behaviour. The story can pass while customers still find the bug.

This check can become recurring work. On every story-status change, an agent can compare the criteria with linked test cases and flag drift.

**Human-owned call:** which findings block refinement and which remain accepted gaps.
