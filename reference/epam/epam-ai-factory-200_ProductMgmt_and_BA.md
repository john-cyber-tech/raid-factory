**Introduction**

**Not Started**

10 minutes

**Focus:** Turn the validated opportunity into the executable spec the rest of the SDLC builds against — product and solution framing, AI-native requirements (behaviour over output, non-determinism), acceptance criteria with embedded eval criteria, and a traceability chain that survives every handoff. Applies on every project (classic delivery, GenAI delivery, strategy engagements alike); spec discipline gains new dimensions when the system itself contains AI.

**Deep for:** Product Managers, Product Owners, Business Analysts (and the expanded BA roles — Feature Owner, Product Owner-as-BA, embedded analyst).

**Total time per learner:**

- Wide path: 45 min Theory + 120 min Katas (8 × 15) + 60 min Final Kata ≈ 3.75h

- Deep path (own role): + 180 min Theory + 270 min Katas (9 × 30) ≈ +7.5h (Final Kata is universal — done once)

This is where opportunity becomes executable. If the spec is bad, the agents downstream produce fast garbage — quickly, confidently, and at scale. PROD/BA is the highest-impact station in an L3 SDLC because everything after it amplifies what happens here: a falsifiable acceptance criterion downstreams into a design, a test, and an eval; an ambiguous one downstreams into three different guesses. The L3 distinction for this role is **spec-as-contract** — executable, evaluable, traceable artefacts that humans and agents act on together — backed by Decision Memory that compounds across quarters instead of evaporating. This module trains you to produce that contract, and to consume it well when someone hands one to you.

**Objectives**

- **Learn to do:** take one feature from a framed opportunity to a developer-ready spec pack — vision, personas, stories with AI-native acceptance criteria, a prioritised backlog, a one-page PRD, a traceability matrix, and a release-readiness/communication pack (Wide); author the specialist spec-and-eval pack — golden set, eval rubric, AI Eval Cards, DoR/DoD, and an eval-gated release brief — for a feature on your own project (Deep).

- **Skills (role):** product & solution framing, AI-native requirements with falsifiable acceptance criteria, evaluator-driven prioritisation and traceability, Decision Memory authoring.

- **Skills (tooling):** AI spec/story drafting, adversarial critique in a fresh session, Mermaid journey maps, RICE/WSJF spreadsheets, AI Eval Cards, eval platforms (Promptfoo / Braintrust / LangSmith), decision-NNN.md.

- **Outcome:** one-page PRD + traceability matrix + release-readiness/communication pack on Case A — Meridian (Wide); the Deep path adds the specialist eval pack (golden set, rubric, AI Eval Cards, DoR/DoD, release brief); a PROD/BA role-agent spec (Final Kata).

- **Tested by:** the Wide kata chain K 2.W.1–8 + the Final Kata K 2.3; the Deep path adds K 2.D.1–9.

**Role Context**

**1 — Role names and who they apply to**

This module covers anyone who turns a validated problem into something a team — human or agent — can build and verify. Common job titles:

- **Product Manager (PM)** — owns product-level direction: vision, strategy, prioritisation, outcome ownership.

- **Product Owner (PO)** — owns the backlog and the "ready for sprint" call in a Scrum delivery.

- **Business Analyst (BA)** — owns requirements depth: elicitation, current/future/gap analysis, business rules, detailed spec.

- **Expanded BA roles** — **Feature Owner** (owns one feature end-to-end), **BA-as-PO** (backlog when no embedded PM), **BA-as-Analyst** (the metrics layer when there's no dedicated data analyst).

- Common synonyms across firms: Requirements Lead · Systems Analyst · Product Analyst · Solution Analyst · Functional Consultant · Technical Product Manager.

If your title varies, the test is functional: do you spend material time deciding *what* gets built and writing it down so others can act on it without re-asking you? If yes, this module covers you. The PM and BA disciplines are taught together because at L3 they converge — both produce executable, evaluable, traceable artefacts that agents and humans consume from the same repo.

**2 — Role description and core duties**

The PROD/BA owns the surface between *"we should solve this"* and *"here is exactly what to build and how we'll know it worked."* In observable verbs:

- **Frames** the product and solution — what kind of product this is (mobile app, service, agent, automation, decision-support) and which capabilities it offers.

- **Specifies** the executable spec: user stories, [acceptance criteria](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#acceptance-criteria), [eval criteria](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#ai-eval-card), business rules, [non-functional requirements](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#nfr).

- **Validates** the spec against real and synthetic signal before engineering invests — the three-stage loop (synthetic → prototype → metrics).

- **Prioritises** the backlog (frameworks inform; the human decides) and maintains the traceability matrix from opportunity → spec → design → tests → production signal.

- **Records** scope decisions, rejected alternatives, and rationale in [Decision Memory](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#decision-memory) so the team's reasoning compounds.

What this role does *not* own: implementation, the UI visual design (Design owns the pixels; PROD/BA owns the usability *requirements*), the technical architecture (PROD/BA states the requirements *of* the architecture, not the architecture), and production sign-off. Those belong downstream.

**3 — Main processes**

The recurring workflows this role runs:

- **Vision & strategy framing** — produce the one-paragraph Product/Solution Vision that sits above the spec and survives iterations; ground it in [OKRs](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#okr) and a [north star metric](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#north-star-metric).

- **Elicitation** — the prepare / conduct / confirm discipline that produces the requirements the spec rests on.

- **Requirements analysis** — current state → future state → gap analysis; conflict detection across sources before they reach engineering.

- **Spec co-creation** — draft the executable spec with AI as a synthesis-and-challenge partner; embed eval criteria at spec time.

- **Backlog refinement & prioritisation** — cluster, de-dupe, size, and rank; enforce the "ready for sprint" checklist.

- **Estimation & sprint planning** — team-velocity-grounded sizing; surface the dependency map and critical path before commit.

- **Traceability & change control** — keep the chain intact across iterations; version the spec; manage scope change against a baseline.

- **Validation** — synthetic-user panels, functional prototypes, and live experiments, in that order.

- **Rollout & communication** — release-scope alignment, demos, stakeholder notifications, release notes, spec updates.

- **Outcome auditing** — close the loop from production signal back to the spec; decide what a metric movement *means*.

**4 — Role in SDLC**

PROD/BA sits **downstream of Consulting/SME** and **upstream of every build role**. It receives the [Opportunity Brief](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#opportunity-brief) (value hypothesis, ROI hypothesis, risk-gate verdict, business context) and turns it into the spec package the rest of the SDLC consumes. The central audience contract — what you send PROD/BA and what you get back:

| **Your role**  | **You send PROD/BA**                                 | **You expect back**                                                                                                                                                          |
|----------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Consulting/SME | Opportunity brief, business context, stakeholder map | Validated problem, prioritised opportunity                                                                                                                                   |
| Design         | Usability signals, pattern reuse, prior research     | [JTBD](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#jobs-to-be-done), user segments, scope boundaries, success metrics |
| Architecture   | Technical non-negotiables, existing systems          | Behavioural spec + proposed AI capabilities + open questions                                                                                                                 |
| Engineering    | Feasibility signals, what's already built            | Acceptance criteria evaluable by [LLM-as-judge](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#llm-as-judge)             |
| Quality        | Test-signal availability, "done" shape               | Eval rubrics embedded at spec time, not after                                                                                                                                |
| Data           | Behavioural data inventory, what's measurable        | Spec-stated metrics + data dependencies                                                                                                                                      |
| Infra          | NFR constraints, operational reality                 | Spec-stated operational requirements                                                                                                                                         |
| Security       | Threat-model implications, compliance constraints    | AI capability scope + trust requirements                                                                                                                                     |
| Management     | Velocity and capacity signals                        | Portfolio-rollup spec + eval criteria for tracking                                                                                                                           |

The single most common upstream failure: a PM hands a *feature list* instead of a *problem statement*. If that happens, discovery wasn't done — and Design and Engineering will solve the wrong problem faster.

**5 — How the role changed with AI (general)**

Two shifts, at high level:

- **Shift 1 — AI accelerates the requirements work itself.** Story drafting from transcripts, requirements synthesis, [traceability matrix](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#traceability-matrix) generation, stakeholder summaries, Decision Memory authoring. This applies on every project — classic, GenAI, strategy alike. The PROD/BA's day moves from typing requirements to supervising AI drafts and holding the line on quality.

- **Shift 2 — when the system being specified contains AI, the spec takes on new dimensions.** Eval criteria are embedded in the spec (not produced later by QA); the PM proposes which AI capabilities the product offers and at what autonomy; acceptance criteria describe *behavior* (distributions, refusal contracts, quality thresholds) because there are no exact-string ACs for non-deterministic outputs.

What collapsed: the mechanical drafting that used to fill a PROD/BA's week. What amplified: synthesis throughput, validation speed, and the ability to build a functional prototype in hours instead of waiting weeks for a dev spike. What survived and got more valuable: judgement — problem selection, scope trade-offs, "good enough to ship," and the calibration to tell fluent AI output from correct AI output.

**6 — What changed at L2 (AI-assistant)**

At L2 the human still owns the spec; AI is a copilot. Where AI assists:

- Drafting user stories and acceptance criteria from interview notes and transcripts.

- Multi-source synthesis (tickets, surveys, workshop notes) into one structured input.

- Generating the first-pass traceability matrix and stakeholder/RACI matrix.

- Summarising for stakeholders; drafting Decision Memory entries from meeting notes.

Stays human at L2 (the lines that do not move): **scope and trade-offs**, **prioritisation** (frameworks rank; the human decides), **ethical boundaries** on what gets built, and **"good enough to ship."** A PM who uses AI only for spec-writing is operating at L2.

**Carry-Forward**

Two artefacts leave this module.

**1 — Spec Package**

- **Artefact name:** Spec Package.

- **Source:** the Wide series (06-prd.md + 06-traceability.md, built from 00-feature → 05-backlog, plus the 07-release-comms.md pack) for all learners; extended by the Deep series eval pack (01-ai-metrics → 06-release-brief, plus 07-review-pack) for specialists. Produced on one [Reference Case](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#running-case) (Case A — Meridian unless you have a live engagement) so the handoff is coherent.

- **Consuming stage(s):**

  - **Design** — consumes [JTBD](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#jobs-to-be-done), user segments, scope boundaries, success metrics, and usability ACs to ground personas, journeys, and prototypes.

  - **Architecture** — consumes the behavioural spec, the proposed AI capabilities, and the [NFRs](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#nfr) to evaluate technical options and confirm feasibility.

  - **Engineering** — consumes acceptance criteria evaluable by [LLM-as-judge](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#llm-as-judge) as the build contract.

  - **QA** — consumes the embedded eval rubric, [golden set](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#golden-dataset), and [DoR](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#definition-of-ready)/[DoD](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#definition-of-done); runs the harness in CI and as [Eval-as-monitor](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#eval-as-monitor) in production.

  - **Data** — consumes spec-stated metrics and data dependencies.

  - **Infra & Ops** — consumes spec-stated operational requirements and the release brief's rollback triggers and monitors.

  - **Security** — consumes the AI-capability scope, trust requirements, and sensitive-data handling.

  - **Management** — consumes the portfolio-rollup spec, eval criteria, and [Decision Memory](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#decision-memory) for tracking.

  - **Final Assembly Line** — the Spec Package is station 2 of the end-to-end agentic delivery scenario (after the Consulting/SME Opportunity Brief).

- **Format:** Markdown in the engagement repo — /specs/\[feature\].md (PRD + stories + ACs / [AI Eval Card](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#ai-eval-card)), /specs/\[feature\]-traceability.md, the eval pack (rubric.md, golden-set.jsonl, eval-run.md, dor-dod.md, release-brief.md), and [Decision Memory](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#decision-memory) entries in /decisions/. Each story links forward to a test/eval and back to an outcome metric.

**2 — PROD/BA Role-Agent Spec**

- **Artefact name:** Role-Agent Spec.

- **Source:** Final Kata K 2.3 (all learners; specialists add the depth-add sections).

- **Consuming stage(s):** **the downstream build roles (Design through Management)** load .claude/skills/pm-ba/ or .claude/agents/pm-ba.md when no PROD/BA is on the team — read in place for spec context, not transformed. **Final Assembly Line** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, with the guardrails (human-owned decisions) inline.

- **Engine guide target:** .ai-run/guides/project.md, under header \## Acceptance-criteria style + ambiguity heuristics (from Module 200 — PROD/BA). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** product-owner-stand-in — the Final Assembly Line's decision-router uses it at gates requirements.ambiguous and spec.clarification; the spec's escalation triggers map to its decision / confidence / risk_flags verdict.

# Wide Theory

**Not Started**

45 minutes

🎓**Before you start — managerial on-ramp.** In a managerial role with beginner-level AI experience? [The EPAM AI RUN — Gen AI Introduction for AMs & BDMs course](https://kb.epam.com/pages/viewpage.action?pageId=2812808369&spaceKey=EPMGPT&title=Curriculum%2BAI%2BRUN%2BGen%2BAI%2BIntroduction%2Bfor%2BAMs%2BBDMs) is the recommended on-ramp: practical GenAI katas for non-technical specialists, a short overview of EPAM GenAI services, and an introduction to vibe coding with Lovable and Claude Code. You could take this learn course as additional study.

﻿

**Why This Matters for You**

Two questions sit under everything a PROD/BA does: a Product Manager asks *are we building the right thing?* and a Business Analyst asks *are we building it completely and correctly?* You may never hold either title, but you live downstream of both answers — so the first job here is to make those two questions yours.

The role is shifting on two fronts at once — AI accelerates the requirements work itself, and the spec takes on new dimensions when the system being specified *contains* AI. Index §0.5 covers both shifts; what matters here is the consequence for you. When the spec is ambiguous, engineers build the wrong thing, QA tests behaviours nobody wanted, and Design prototypes the wrong problem. So here is the one mental model to carry out of this module: at L3 the spec is the **contract between humans and agents**. AI amplifies whatever clarity or noise you ship — so a bad spec produces fast garbage, confidently and at scale.

Forty-five minutes here gives you the vocabulary to read a spec critically, name the four risks every spec must clear before delivery starts, push back when a handoff is thin, direct AI to draft the role's artefacts, and recognise when a feature is past what you should cover alone.

﻿

**Goal**

Build literacy with what L3 PROD/BA work produces — executable specs, embedded eval criteria, traceability chains, Decision Memory — and how to consume those artefacts as a downstream role. You leave able to *recognise and pressure-test* a spec, not to author a specialist one (that's the Deep path).

﻿

**Time**

~45 min.

﻿

**Audience**

Anyone not specialising in PROD/BA — consultants, designers, engineers, QAs, architects, data, infra, security, management.

﻿

**Prerequisites**

The Onboarding, Fundamentals, and Consulting/SME modules completed; the Opportunity Brief from Consulting/SME in hand (or a Reference Case to stand in for it).

**Must Cover**

**The spec is the contract between humans and agents. A bad spec produces fast garbage — confidently, and at scale.**

This section covers seven topics. The first four run in dependency order — what PROD/BA inherits becomes a framed product, which becomes the executable spec, which only holds once it clears the right risks and reaches the right people; the last three cover what you do with a spec once it exists.

- **Discovery & context** — what PROD/BA inherits: organisational context, the tech-landscape brief, stakeholder mapping and validation, and where AI helps and where it doesn't.

- **Product framing** — product vs solution framing, naming the user (persona, journey map, JTBD), the vision that sits above the spec, the product's AI capabilities, and outcome- over feature-driven delivery.

- **Requirements: the executable spec** — the spec as context not only commands, acceptance criteria as behaviour, quality thresholds and NFRs, evals as part of the requirements, Decision Memory, and traceability.

- **Cross-functional fluency** — the four SVPG risks, who owns the role, the Product Trio, PM ↔️ Commercial, the audience contract, and PM vs SME vs user.

- **The build-and-validate interface** — Definition of Ready, UAT-script review, defect triage, and release readiness and communication.

- **How to ask AI to do PROD/BA work** — the give-it-X, ask-for-Y pattern and the one thing to check on each artefact.

- **When to pull in a real PM/BA** — the escalation triggers where covering the role with AI stops being safe.

**Key Messages / Ideas**

- **Everything PROD/BA produces is a transformation of inherited context** — discovery is a three-stage filter (synthetic pre-validation → prototype validation with real users → metrics validation), not a single "go talk to users" event, and the spec is only as good as the stakeholders you validate it against.

- **Product / Solution Vision and framing sit *above* the spec** — they survive iterations while specs change underneath; the PM proposes the AI capabilities and Architecture confirms feasibility.

- **The spec is the contract between humans and agents — a bad spec produces fast garbage.** Acceptance criteria are the highest-impact artefact (they downstream into designs, code, and tests), an AI feature's evals are part of its definition not a QA afterthought, and outcome-driven delivery names how you'll know it worked *in production*.

- **Every spec must address all four SVPG risks** before delivery starts — the most-skipped are viability and feasibility, and the PROD/BA project configuration changes *what* breaks, not *whether* something breaks.

- **PROD/BA work doesn't stop at the spec** — Definition of Ready, UAT-script review, defect triage, and release readiness are how the spec survives contact with the build and reaches the people who act on it.

- **AI drafts, you validate** — AI doesn't change what makes a good story (clear, testable, valuable); it changes how *often* you can produce one and how *dangerous* a bad one becomes, so fluent output is not correct output.

- **Covering the role with AI has a boundary** — escalate to a specialist on one-way-door decisions, stakeholder conflict, regulated domains, or a non-trivial safety contract; the cost of not escalating is a confident spec for the wrong thing, built fast and at scale.

**Structure (Per-topic context blocks)**

Each block elaborates one topic from the list above — mental model first, then the precise definition.

# Block 1 — Discovery & context (what PROD/BA inherits)

*The thread: everything PROD/BA produces is a transformation of what Consulting/SME hands over — so the spec is only ever as good as the context you carry forward and the stakeholders you validate it against.* Four inputs set the constraints every later block inherits:

- **Organizational context** — goals, capabilities, drivers, policies.

- **Tech-landscape brief** — the AI-vs-classical framing, produced upstream. Consume it; don't redo it.

- **Stakeholder mapping & validation** — a [RACI](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#raci) plus a communication plan naming who hears what, through which channel, how often. AI drafts the matrix; you own the relationship calls.

- **Where AI helps and where it doesn't** — synthesis and multi-source aggregation: yes; problem selection, ethics, stakeholder trust, and organisational politics: human-owned.

*On Meridian (Case A),* the stakeholder you validate the click-&-collect availability feature against is the store-operations lead who owns the phantom-stock problem — name the wrong stakeholder and the spec solves a pain nobody has.

# Block 2 — Product framing (PM core)

Inputs aren't requirements yet. PROD/BA is **where opportunity becomes executable**, and that translation starts with a product decision, not a backlog — frame the product wrong and every requirement in Block 3 inherits the error.

- **Product vs solution framing** — Consulting/SME owns *problem* framing; the PM picks what kind of product this is (e.g. assistant, agent, automation, decision-support) and the shape of the solution.

- **Name the user before the vision** — a **persona** is a one-paragraph sketch of one user (goal, friction, current workaround — not demographics); a **journey map** traces that user's path through the task with the pain points marked; **JTBD** frames the underlying job in one sentence — *"When \[situation\], I want to \[action\], so I can \[outcome\]."* When a story says "users can X," ask *which persona, in what moment, getting which job done?* (How to build these is the Deep path.)

- **Vision sits above the spec** — the Product / Solution Vision survives across iterations while the spec changes underneath it. It pairs with a **strategy** (where you compete and what you will *not* build) and a **roadmap** that lists outcomes (NOW / NEXT / LATER), not features.

<img src="media/image1.png" style="width:6.26806in;height:2.79931in" />

- **AI capabilities of the product** — the PM *proposes* which capabilities the product offers (chat, classification, retrieval, generation, agentic action) and at what autonomy; **Architecture confirms** feasibility, cost, and runtime guarantees.

- **Outcome-driven, not feature-driven** — the L3 PM measures outcome lift, not feature count.

*On Meridian,* the proposed capability is a stock-availability predictor that tells a shopper whether an item is really collectable before they drive over — a retrieval-plus-prediction call Architecture has to size.

# Block 3 — Requirements: the executable spec (BA core)

A framed product is still only intent until it's written down as something buildable. Block 3 is where it becomes the **executable spec** — the contract agents act on at L3. A clear acceptance criterion downstreams into a design, a test, and an eval; an ambiguous one downstreams into three guesses.

<img src="media/image2.png" style="width:6.26806in;height:3.14444in" />

 **The spec is context, not only commands** — agents work better with the *reasoning* behind the ask. The executable spec carries the why, so an agent can act on it without re-asking you.

 **Acceptance criteria name behaviour, not output** — for a deterministic feature an AC reads in [**Gherkin**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#gherkin) / Given–When–Then form; for a non-deterministic one there is no exact string to match, so the AC names *behaviour* (refuse, retry, delegate, complete) plus a threshold. *(How to author one is the Deep path.)*

 **Quality thresholds are acceptance criteria** — the AC also names the [**non-functional requirements**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#nfr): latency (p95 \< 2s), output quality (factuality ≥ 85%) by [LLM-as-judge](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#llm-as-judge). For AI features these are acceptance criteria, not QA afterthoughts.

 **Evals are part of the requirements** — every AI feature ships with the evals that define "working." The eval *is* the acceptance criterion for a probabilistic system.

 [**Decision Memory**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#decision-memory) — a short entry per significant scope call: the decision, the rationale, and the rejected alternative. The rationale and the rejected option are the point — they keep the *why* with the spec instead of in someone's head. When AI drafts the entry, make it write that reasoning too, not only the verdict.

 **Traceability** — a continuous chain: opportunity → spec → design → implementation → tests → production signal → back to opportunity.

<img src="media/image3.png" style="width:6.26806in;height:4.02778in" />

- **The supporting moves** (named here, learned in Deep) — current → future → gap analysis, cross-source conflict detection, backlog prioritisation (RICE for ranking, MoSCoW for scope; Kano and WSJF as alternates), prototype and [synthetic-user](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#synthetic-persona) validation, and velocity-grounded estimation, where AI suggests ranges from your team's own closed-story history and the team owns the number. AI does not estimate.

- **Outputs PROD/BA produces:** executable specs, [user stories](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#user-story) with acceptance criteria, eval criteria, Decision Memory, traceability matrices. **Consumers:** Design (prototypes), Architecture (NFRs), Engineering (implementation), QA (tests/evals), Management (portfolio rollup).

*On Meridian,* the predictor's AC is falsifiable: phantom-stock cancellations at pickup ≤ 2%, p95 response \< 1s, and a "stock unknown" fallback when confidence is low.

🏛️**EPAM perspective.** In an [AI Factory](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#ai-factory) — an AI-native delivery team — the spec is not a one-off document but a version-controlled artefact that compounds across engagements, alongside the prompts, evals, and Decision Memory it carries. That is why traceability and Decision Memory are *requirements*, not paperwork: they are what lets the next team reuse the spec instead of re-deriving it.

# Block 4 — Cross-functional fluency (who works with whom)

A spec is only as good as the risks it clears and the people who act on it.

<img src="media/image4.png" style="width:6.26806in;height:2.74097in" />

 [**SVPG Four Risks**](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#risk-gates) — every spec must address **Value** (is the problem real and worth solving?), **Usability** (will users adopt it?), **Feasibility** (can this team and tech build it?), and **Viability** (does it work for the business — revenue, compliance, support cost?). Most "shipped but failed" features skipped one — usually viability ("legal will figure it out") or feasibility ("engineering will say if it's too hard").

 **Who owns the role** — every project runs in one of four configurations, each with a named risk: PM only (edge cases under-specified), BA only (the team builds what the client *asked for*, not what they *need*), both (coordination breaks), or neither (no one owns the right problem). At L3, AI compresses discovery and drafting enough that one person can cover both jobs — know which you're in before the project starts.

<img src="media/image5.png" style="width:6.26806in;height:3.94931in" />

 **The Product Trio** — PM/BA + Designer + Engineer collaborate from the problem statement forward, not sequentially. The classic failure is waterfall in disguise: the constraints that would have changed the hypothesis surface only at the end, when change is most expensive.

 **PM ↔️Commercial** — the PM sends the value proposition, target segment, and "do-not-promise" boundaries, and receives win/loss patterns and market signal. Red flag — **spec-by-demo**: sales promises a feature before the PM has seen the request.

 **The audience contract** — what each role sends PROD/BA and expects back is the §0.4 interfaces table. If a PM hands you a feature *list* instead of a problem *statement*, discovery wasn't done.

 **PM vs SME vs user** — SMEs tell you *how the problem space works*; users tell you *what their day is like*; the PM frames *what's worth solving*. Outsourcing discovery to the SME produces a technically accurate spec for the wrong user problem.

# Block 5 — The build-and-validate interface

PROD/BA work doesn't stop at the spec — you sit on the other side of every build handoff, and the Wide audience (QA, engineers, management) *receives* these artefacts:

- **Definition of Ready (DoR)** — a story that fails the gate (no falsifiable AC, no named user role, unsized, no eval rubric for an AI feature) goes back to refinement, not into the sprint.

- **UAT-script review** — PROD/BA checks the User Acceptance Tests cover every AC, error path, and NFR, not only the happy path.

- **Defect triage** — defects are scored by business impact (severity × reach × strategic fit) and called release-blocker / ship-with-known-issue / defer; QA owns the fix, PROD/BA owns the priority.

- **Release readiness & communication** — a numeric go/no-go, plus a comms pack: delivery leads get scope + open risks, business stakeholders get the behaviour change + benefit + dates, and every line of the release note traces back to a story that actually shipped.

<img src="media/image6.png" style="width:6.26806in;height:1.42708in" />

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

# Block 7 — When to pull in a real PM/BA

⚠️**Covering the role with AI has a boundary.** Escalate to a specialist when any of the conditions below holds — the cost of not escalating is a confident spec for the wrong thing, built fast and at scale.

- an **irreversible, high-impact decision** is in play — pricing, the data model, a compliance commitment (a 1-way door; AI informs, a human owns it);

- **more than one stakeholder group is in active conflict** and the call is political, not analytical;

- the spec is for a **regulated domain** where the traceability chain *is* the audit evidence;

- you **can't tell whether an inherited goal is the right problem** to solve;

- the **four SVPG risks can't all be answered** from the brief in front of you;

- the **AI feature's safety or refusal contract is non-trivial** — it can cause harm, leak data, or must refuse whole categories of request.

# Anti-Patterns

**Spec-level (the PROD/BA's own work):**

- Polished prose with no falsifiable acceptance criteria — it passes a read-through but every engineer interprets it differently, so the build diverges and the rework lands in QA.

- ACs like "the output should be accurate" — an [LLM-as-judge](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#llm-as-judge) can't evaluate them, so "done" is never defined and the feature ships on a vibe.

- Treating AI-generated stories as finished without grounding in real user signal — you scale plausible-but-wrong requirements faster than anyone can catch them.

- "Throw the spec over the wall" — no traceability back to the opportunity brief, no eval criteria forward to QA, so nobody can tell whether what shipped was what was asked for.

- Hidden assumptions baked into prompts but not in the spec — the agent acts on context no human reviewed; lose the prompt and the behaviour is unreproducible. Done right: every assumption the prompt relies on appears as a spec line.

- Specifying *how* (implementation) instead of *what* (behaviour) — strips downstream of design space and locks in a solution before Architecture has weighed in.

- Skipping Decision Memory because "we'll remember why we made that call" — three months on no one does, and the team relitigates the decision or silently reverses it.

**Cross-role (visible to other teams):**

- **Feature factory** — PM sends a feature list, not a problem statement. Design and Eng solve the wrong problem faster.

- **Discovery theatre** — interviews happen, but the output is a feature list anyway.

- **PM as proxy** — PM "represents" users without talking to them in months.

- **Scope creep via AI** — PM generates 50 stories with AI and adds them all; engineering load explodes, nothing ships.

- **Trio by name only** — three people exist but never meet until sprint planning.

- **Sales drives the roadmap** — the roadmap becomes a collection of deals, not a product strategy.

# Outcomes

By the end of Wide Theory, the non-specialist can:

- Name the four SVPG risks every spec must clear before delivery starts.

- Tell a falsifiable acceptance criterion from an aspirational one.

- Direct AI to draft a PROD/BA artefact, then validate the draft rather than ship it.

- Name when to pull in a real PM/BA instead of covering the role solo.

<img src="media/image7.png" style="width:6.26806in;height:3.13125in" />

**Assessment Questions \[Optional\]**

**Awaiting Action**

5 minutes

What should be done

\*

Knowledge Check (3 retrieval-practice questions)

1.  **(Wide Theory)** Name the four [SVPG risks](https://eu.git.epam.com/airun-mission-26-ai-factory/curriculum/-/blob/main/modules/000-glossary.md#risk-gates) every spec must address, and explain why *"the output should be accurate"* fails as an acceptance criterion. Rewrite it as one falsifiable AC for a non-deterministic feature (name a metric, a threshold, and whether it's a gate or a monitor).

2.  **(Deep Theory)** Walk the 4-block operating model on one feature: name the **Context Engineering** inputs, the **Spec Co-Creation** artefact, what the **Agentic Prototype** tested, and the **Outcome Auditing** signal that would reopen the spec. Then state what *evaluator-driven requirement definition* changes about the order of work — and why the eval is written before the feature.

3.  **(Katas / Final Kata)** What does the Deep eval pack (K 2.D.1–8) require that a one-page PRD does not? Name three of its artefacts, and write one rollback trigger from the release brief in the correct form (*signal \> threshold sustained for a time window*). Then name one decision the Final-Kata role-agent must **escalate** rather than make.

Self-Reflection (2–3 comparison prompts against the L3 standard)

1.  Compare your last real spec to the **spec-as-contract** L3 standard. Would a downstream engineer — or their role-agent — build the right thing from it without booking a call with you, or would ambiguity force a meeting? Of its acceptance criteria, how many were falsifiable ("refusal rate ≤ 5%") versus aspirational ("works well")?

2.  Compare your team's prioritisation to the *framework-informs-the-human-decides* standard. The last time you ranked a backlog, did the framework's \#1 silently become the decision — and was the rationale written somewhere a teammate could challenge it three months later, or did it live in your head?

3.  **(Specialist)** Honest check on your eval pack: could a release manager make a mechanical go/no-go at 2 a.m. from your release-readiness brief without you in the room — are the gates and rollback triggers numeric with time windows, or do some still say *"if it breaks"*?

﻿

Web Search: SVPG four product risks Marty Cagan \[15.30s\]

Usage Statistics

**1. The Four SVPG Risks**

According to Marty Cagan and the Silicon Valley Product Group (SVPG), every product specification and discovery cycle must address the following four core risks before writing production code \[superpm.app\]:

1.  **Value Risk:** Will the customer choose to buy or use this solution? \[roadmap.one\]

2.  **Usability Risk:** Can the user figure out how to navigate and use it? \[roadmap.one\]

3.  **Feasibility Risk:** Can our engineers actually build this with the time, technology, and skills available? \[roadmap.one\]

4.  **Business Viability Risk:** Does this solution fit our business constraints (e.g., legal, compliance, sales, marketing, and finance)? \[roadmap.one\]

**2. Why "The output should be accurate" Fails as an Acceptance Criterion (AC)**

The phrase *"the output should be accurate"* is a classic anti-pattern in product specifications. It fails as an acceptance criterion for several reasons:

- **It is subjective and ambiguous:** There is no shared definition of "accurate." What a product manager considers accurate might differ vastly from an engineer's, QA's, or end-user's interpretation.

- **It is not falsifiable or testable:** A QA engineer cannot write a binary pass/fail test for "accurate" because there are no clear, quantifiable parameters or benchmarks defined.

- **It ignores the reality of non-deterministic systems:** For features utilizing Machine Learning (ML), Large Language Models (LLMs), recommendation engines, or complex heuristics, absolute (100%) accuracy is mathematically and practically impossible. These systems function on probabilities, not certainty. Without a tolerated error margin, the developer has no target, and the QA team can never sign off on the release.

- **It lacks operational context:** It fails to specify whether this accuracy is a release-blocking condition checked during build time or a runtime metric monitored in production.

**3. Rewritten Falsifiable Acceptance Criterion**

To write a falsifiable AC for a non-deterministic system, you must specify **what** to measure (metric), **what** standard to meet (threshold), and **when/how** it is enforced (gate vs. monitor).

Here is how you can rewrite that criterion for a **non-deterministic LLM-based customer support auto-tagger**:

***Acceptance Criterion (AC):** The automated ticket-tagging classifier must achieve a **Macro F1-Score of ≥ 90%** when evaluated against the static golden validation dataset (**support_eval_v2.json**).*

- ***Metric:** Macro F1-Score (balances precision and recall across all customer support categories).*

- ***Threshold:** ≥ 90%.*

- ***Enforcement Type:** **Gate** (This evaluation is automated in the CI/CD build pipeline; if the F1-Score drops below 90%, the build fails, and the code/model cannot be deployed to production).*

Every spec must address the four SVPG risks: **Value** (will they use it), **Usability** (can they use it), **Feasibility** (can we build it), and **Business Viability** (does it align with business constraints) \[roadmap.one\].

The acceptance criterion (AC) "the output should be accurate" fails because it is subjective, untestable, and impossible to guarantee in non-deterministic systems like AI.

To be falsifiable, an AC for a non-deterministic feature must define a specific metric, a target threshold, and whether it acts as a release gate or an active production monitor.

For example: *"The recommendation engine must maintain a **Precision@5** metric of **≥ 85%** on the offline evaluation dataset."*

For a customer-support auto-responder, **Context Engineering** inputs domain guidelines, **Spec Co-Creation** produces a machine-readable **SPEC.md**, the **Agentic Prototype** tests usability/value with real users, and **Outcome Auditing** reopens the spec if the live human-draft rejection rate exceeds 15% \[superpm.app\]. Writing evals *before* building provides the autonomous AI agent with a mathematical objective function to self-correct and iterate against until it achieves a "green build" \[deepeval.com\].

While a PRD is descriptive, a **Deep Eval Pack** is machine-executable; three of its artifacts are the **Golden Dataset**, **Metric Config Spec**, and **Release Brief** \[deepeval.com, github.com\].

An operational rollback trigger from the Release Brief takes the form: *“Canary user-refusal rate \> 5% sustained for 10 minutes”* \[oneuptime.com\].

Lastly, the autonomous agent must **escalate** any decision that breaches business viability, such as migrating to a more expensive LLM model that exceeds the quarterly budget \[superpm.app\].
