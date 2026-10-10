# Introduction

**Not Started**

10 minutes

**Focus.** Every team learns to take a real user journey, find where it breaks, redesign it in a workshop, prototype the fix, and hand it off so an AI coding agent can build it — after checking whether AI even belongs in the feature. Designers go further: when AI ships *inside* the product, they own the trust surface — confidence, citations, refusal, **human-in-the-loop** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#human-in-the-loop-hitl), and error states — plus the AI risk register. For designers this moves the craft from L1 (ad-hoc AI use) to L3 (AI-native); everyone else learns to recognise and consume what a designer produces.

**Deep for:** UX, Visual, Experience Consultant / Service, and Content designers on AI-native delivery teams.

**Total time per learner:**

- Wide path: 45 min Theory + ~120 min katas (8 × 15) + 60 min Final Kata ≈ 3.75h

- Deep path (own role): + 180 min Theory + ~180 min katas (6 × 30) ≈ +6h (the Final Kata is universal — done once)

**Objectives**

- **Learn to do:** Wide — redesign a real user journey from evidence into a feasibility-gated, workshop-driven clickable prototype with an agent-ready recommendation pack. Deep — design the trust / HITL / error surface and the AI risk register for an AI feature.

- **Skills (role):** JTBD framing + journey/heuristic evidence, AI feasibility gating + AI-aware acceptance criteria, workshop prep/facilitation/synthesis, validation planning + agent-ready handoff.

- **Skills (tooling):** Mermaid journey maps, vision-LLM heuristic review, vibe-coded prototypes (v0 / Lovable / Claude Artifacts), Sheets synthesis, CONTEXT.md + SPEC.md handoff.

- **Outcome:** Wide — a clickable lo-fi prototype + recommendations doc + agent-ready handoff pack. Deep adds a trust / HITL prototype + AI risk register + a production SPEC.md slice.

- **Tested by:** the Wide kata chain (K 3.W.1 → K 3.W.8) + the Final Kata (K 3.3); Deep adds the specialist series (K 3.D.1 → K 3.D.6).

# Role Context

**1 — Role names and who they apply to**

This module covers anyone who owns the experience surface — how the product looks, reads, and feels to use. Typical titles:

- **UX Designer** — interaction, flows, usability, prototypes.

- **Visual Designer** — visual language, assets, design-system application.

- **Experience Consultant / Service Designer** — end-to-end journeys and service blueprints across touchpoints.

- **Content Designer** — UX writing, tone of voice, microcopy.

- Synonyms across firms: Product Designer · UX/UI Designer · Experience Designer · Interaction Designer · Design Lead.

The test is functional, not the title: do you spend real time deciding how a product is experienced — its flows, visuals, copy, or service journey? If yes, take **Deep**. Everyone else takes **Wide** — you collaborate with a designer, or stand in for one.

**2 — Role description and core duties**

The designer owns the surface between *"here's what to build"* and *"here's how it's experienced and how a developer builds it."* The role is accountable for four outcomes; the activities that produce them, in order, are in §0.3:

- **The experience** — flows, interactions, visuals, copy, and the service journey: how the product looks, reads, and feels to use.

- **The evidence behind it** — proof that the design solves a real user problem and works, from research and evaluation rather than opinion.

- **The buildable spec** — the agent-ready handoff (CONTEXT.md + SPEC.md + design tokens) engineering and AI coding agents build from directly.

- **The AI judgment calls** — whether AI belongs at all, the trust surface when it ships in the product, and the audit that stops unchecked AI output from reaching production.

Not owned by this role: implementation, technical architecture, sprint prioritisation, and production sign-off — those are downstream.

**3 — Main processes**

Those responsibilities play out across the seven phases of a typical delivery lifecycle (activity detail in 1.1 Wide Theory):

- **FRAME** (kickoff & setup) — feasibility, problem framing, as-is journey mapping, initial exploration.

- **INVESTIGATE** (research) — user research, personas, JTBD, design-system audit, test planning.

- **ENVISION** (concept & prototype) — ideation, wireframes, clickable prototypes, usability testing.

- **ANALYZE & DEFINE** (synthesis) — iteration on testing insight, project wrap-up, AC drafting.

- **DESIGN & DEVELOP** (detailed design & handoff) — detailed design, component variants, accessibility audit, design QA, handoff.

- **LAUNCH & SCALE** (go-to-market) — launch readiness, onboarding finalisation.

- **OPERATE & OPTIMISE** (post-launch) — feedback loops, performance optimisation, design-system governance.

**4 — Role in SDLC**

Design sits **downstream of Product Management & BA** and **upstream of Engineering**. It receives the spec package — JTBD, user segments, scope boundaries, success metrics, usability ACs — and turns it into prototypes and an agent-ready handoff. The audience contract:

| **Your role**           | **You send Design**                                 | **You expect back**                                                                                       |
|-------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Product Management & BA | JTBD, user segments, success metrics, usability ACs | Prototypes, design-level ACs, a handoff pack                                                              |
| Architecture            | Technical environment, constraints                  | CONTEXT.md aligning data-flow + environment                                                               |
| Engineering             | What's already built, design-system state           | The clickable prototype + SPEC.md + CONTEXT.md + tokens an agent can build from                           |
| Quality                 | The "done" shape for AI behaviour                   | AI-AC (confidence, refusal, latency, disclosure, feedback, negative) + HITL / error states to drive tests |

The most common upstream failure: a feature list arrives instead of a problem statement, and Design solves the wrong problem faster.

**5 — How the role changed with AI (general)**

Two shifts, at a high level:

- **Production collapses, validation multiplies.** Asset generation, multi-screen UI concepts, and evaluation cycles drop from hours to minutes — and the time saved buys more validation rounds, not only a faster finish (auditing eats some of it back).

- **Value shifts from pixels to context.** The designer's most valuable output becomes the *context* that lets engineers and AI agents build the right thing — not only the polished file. The concrete L3 artefacts are in §0.7.

**6 — What changed at L2 (AI-assistant)**

At L2 the human still owns the design; AI is a copilot. Where AI assists:

- Generating visual assets (icons, illustrations, mood-board images, dummy copy).

- Generating UI concepts and multi-screen flows in greenfield mode.

- AI-accelerated heuristic evaluation and synthetic-persona walkthroughs.

- Drafting copy against a chosen tone of voice.

Stays human at L2 (the lines that don't move): **brand judgment, accessibility from lived experience, ethical trade-offs, controversial UX patterns, strategic IA, sensitive copy, and saying no** to a feature that fails the feasibility check. A designer who uses AI only to generate assets is still operating at L2.

**7 — What changed at L3 (AI-native)**

At L3 the work restructures around reusable assets and a continuous loop. The role gains reach; it does not disappear. The concrete shifts:

- **Designer as Context Architect.** The primary output is machine-readable context — CONTEXT.md, SPEC.md, design tokens, Figma MCP context — that agents consume directly, not only a visual file for human readers. Its quality drives code quality more than the pixels do.

- **The Day 1 / Day 2 loop.** Day 1 is greenfield concept generation (Figma Make / Lovable / v0); Day 2 is production-connected iteration via Figma MCP + Code Connect + tokens. The bridge between them is where most teams lose velocity.

- **Reusable prompt assets.** A structured, versioned project prompt library turns one designer's prompt wins into team capability — the design equivalent of an engineer's rule files.

- **An explicit audit step.** AI-generated assets and UI carry an audit (brand / technical / accessibility / IP) before they enter production; without it, AI UX debt accumulates as silent bugs.

- **New artefacts the role produces:** the agent-ready Design Handoff Pack, and a native-format design role-agent (Skill or sub-agent) that runs the role's work when no designer is on the team.

The Wide path teaches you to *recognise and consume* these artefacts; the Deep path teaches you to *produce* them.

# Carry-Forward

Five artefacts leave this module: two from the Wide series, two from the Deep series, plus the Final-Kata role-agent.

**1 — Journey Redesign Pack (Wide)**

- **Artefact name:** Journey Redesign Pack.

- **Source:** Wide katas K 3.W.2 → K 3.W.8 — the journey map + heuristics, the workshop decision, the clickable lo-fi prototype, and the validation plan + 1-pager narrative.

- **Consuming stage(s):**

  - **Architecture** — consumes the journey + NFR-relevant constraints to ground technical options.

  - **Engineering** — consumes the **clickable prototype** it already expects from this module (see 500-eng/500-wide-theory.md).

  - **Final Assembly Line** — the prototype + recommendations join the portfolio.

- **Format:** Markdown + Mermaid + an HTML/URL prototype — 01-journey-map.md, 03-decision.md, 05-mockup.html, 07-narrative.md, 07-validation-plan.md.

**2 — Agent-Ready Handoff (Wide)**

- **Artefact name:** Agent-Ready Handoff.

- **Source:** Wide katas K 3.W.5 (AI-AC) + K 3.W.7 (handoff pack).

- **Consuming stage(s):**

  - **Engineering** — consumes CONTEXT.md + SPEC.md as the AI-coding-agent input.

  - **Quality** — uses the AI-AC layer to drive test cases for AI-specific behaviour (confidence, refusal, latency, disclosure, feedback, negative AC).

  - **Architecture** — uses CONTEXT.md to align technical environment + data-flow constraints.

- **Format:** Markdown — 04-ai-ac.md, 06-context.md, 06-spec.md. **Quality bar:** the six-point Definition of Handoff Done from Kata K 3.W.7 — all six must pass before the pack ships.

**3 — AI Trust/HITL Prototype + Risk Register (Deep)**

- **Artefact name:** AI Trust/HITL Prototype, with a production SPEC.md slice, plus the AI Risk Register.

- **Source:** Deep katas K 3.D.5 (prototype + production SPEC slice) and K 3.D.6 (risk register), backed by K 3.D.1–4.

- **Consuming stage(s):**

  - **Engineering** — consumes the production SPEC slice for one trust component as a build contract.

  - **Quality** — consumes the HITL / error-state AC clauses emitted in K 3.D.3–4.

  - **Security and Delivery & Project Management** — prospective consumers of the AI Risk Register *(edge to wire when those modules adopt the canonical frontmatter)*.

- **Format:** a Figma/URL prototype + 04-spec-slice.md + 05-risk-register.xlsx.

**4 — Design Role-Agent (Final Kata)**

- **Artefact name:** Design Role-Agent.

- **Source:** Final Kata K 3.3 (all learners; specialists add the depth-add sections).

- **Consuming stage(s):** **Architecture, Engineering, and Quality** load .claude/skills/design/ or .claude/agents/design.md when no designer is on the team — read in place, not transformed. **Final Assembly Line** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, with the human-owned design decisions inline as guardrails.

- **Engine guide target:** .ai-run/guides/development/development-practices.md, under header \## UI conventions (from Module 300 — Design). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

**Course Repo: <https://epa.ms/ai-run-26-curriculum-repo>**

# Wide Theory

**Not Started**

45 minutes

🎓**Before you start — managerial on-ramp.**\* In a managerial role with beginner-level AI experience? [The EPAM AI RUN — Gen AI Introduction for AMs & BDMs course](https://kb.epam.com/pages/viewpage.action?pageId=2812808369&spaceKey=EPMGPT&title=Curriculum%2BAI%2BRUN%2BGen%2BAI%2BIntroduction%2Bfor%2BAMs%2BBDMs) is the recommended on-ramp: practical GenAI katas for non-technical specialists, a short overview of EPAM GenAI services, and an introduction to vibe coding with Lovable and Claude Code. You could take this learn course as additional study.

﻿

**Why This Matters for You**

This section gives every non-designer a working picture of the designer's job and where AI changes it in 2026, so you can brief one well, read their handoff, and estimate the build. On an AI-native team the **designer** owns the experience surface: the user's journey, the screens, the words on them, and, when no designer is in the room, the machine-readable brief an AI coding agent builds from. You use this when you work *with* a designer, or when you stand in because the project has no specialist.

**The one idea to keep:** *the designer architects intent; the AI executes it.* What ships is only as good as the context handed in — not the tool used.

Knowing the designer's job pays off in your own work:

- hand a designer a brief they can act on, instead of one that comes back with questions;

- read the handoff pack well enough to estimate the build;

- spot AI-generated design that needs a second look before it ships;

- cover the gap yourself — frame a job, map a journey, package a handoff — when no specialist is available.

﻿

**Goal**

Recognise what a designer does at each delivery phase, where AI accelerates it in 2026, and which signals mean something is wrong — so you can write better design requests, read handoffs fluently, and estimate AI-augmented design effort.

﻿

**Time**

~45 min reading.

**Audience**

All non-designers on an AI-native project team.

**Prerequisites**

The Onboarding, AI-Native SDLC Fundamentals, Consulting & SME, and Product Management & BA modules. Have on hand: the framed product and requirements artefacts from Product Management & BA. No design craft required.

**Must Cover**

**The designer architects intent; the AI executes it — so the quality of what ships is set by the context you hand in, not the tool.**

These concepts let a non-specialist cover a design gap with AI. The next section defines each one in enough detail to use in review:

- **Jobs-To-Be-Done (JTBD)** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#jobs-to-be-done) — the real job a user hires the product to do.

- **Journey map** — the user's steps, each tagged with an emotion, to find the worst moment.

- **Heuristic evaluation** — a structured UI check against Nielsen's 10 usability heuristics.

- **Lo-fi prototyping** — a rough clickable flow that proves the change.

- **Task-based validation** — testing by asking users to *do tasks*, not give opinions.

- **Tone of voice (the words)** — a short, reusable description of how the product speaks, so every screen sounds consistent.

- **States — a screen is more than the happy path** — empty / loading / error / content-specific edge cases; AI generates only the happy path by default.

- **AI feasibility check** — at the start, decide whether the *product* will include AI, and whether you're allowed to use AI tools in the process.

- **Agent-ready handoff** — a machine-readable handoff pack an AI coding agent builds from.

- **When to escalate** — the calls that stay human-owned.

The boundary in practice — what AI runs, what it advises, and what humans own:

**AI Executes** — drafts or generates the artefact; the output still passes a human gate before it lands: JTBD draft from the brief · journey-map first pass · heuristic-evaluation scorecard · How-Might-We questions from frustrations · UI concepts (Figma Make / Lovable) · handoff pack from the spec · synthetic-persona run.

**AI Recommends** — informs, doesn't replace judgment: concept options & revision paths · usability / accessibility / code-alignment findings · brand & compliance risk flags · validation results (synthetic & real-user).

**Human Decides** — owns CX, accessibility, ethics: brand voice & visual language · accessibility from lived experience · ethical trade-offs (show vs hide) · feasibility go / no-go · whether AI belongs in the product · sensitive copy (medical / financial) · final design sign-off.

Everything under **AI Executes** still passes a human gate — the audit — before it enters a file or handoff. Full autonomy with no human in the loop belongs only to AI that ships *inside the product* — recognise-and-escalate territory, outside this module's scope.

<img src="media/image1.png" style="width:6.49869in;height:2.26832in" />

**Key Messages / Ideas**

- **Design is evidence-first.** A journey map is a hypothesis, not a truth — it should be wrong in interesting ways. A heuristic review (or a synthetic-persona pass) cheaply surfaces UX debt before you commit to user research.

- **A workshop must close a decision.** "Align on the approach" is not a decision. Name the call before booking the room, and write down what was decided.

- **A prototype tests the idea, not the implementation.** Keep it ugly — polish shifts attention to how it looks instead of whether it works. Three rough screens beat one polished one.

- **The designer is an architect of intent.** They decide *what* to build and *why*, then hand it over as machine-readable context: the screen spec, design tokens, constraints, and live design-system context an AI agent can execute. That context is the primary output.

- **AI accelerates the *making*, not the judgment.** Asset generation, UI variants, and evaluation cycles speed up, but the time *moves* rather than vanishes. Brand decisions, novel interactions, accessibility from lived experience, and ethical trade-offs stay human. Delegating those to AI is an anti-pattern — flag it.

- **The handoff is live, not a static drop.** It's a queryable surface the AI agent reads as it builds; its quality drives code quality more than the visuals do.

- **AI design needs an explicit audit step.** Skip it and AI UX debt piles up downstream as broken states, hallucinated component names, generic visuals, and missing edge cases. Unaudited AI output reaching production → escalate.

- **Output quality = context quality.** A vague brief yields plausible-but-wrong output the same minute. The context shapes the result more than the tool does.

- **Where the time really goes.** AI speeds up the *making* — a first-draft asset, a UI, a clickable flow — but not the work around it: you still describe the users, problem, constraints, and success conditions up front, then audit the output. On a first or novel pass, especially early in a project, that can net out to about the same total time. What changes is the work itself: you describe and direct instead of drawing every state by hand. The payoff compounds later, once prompts, patterns, constraints, shared context, and skills are reused. The gain is uneven by phase: research synthesis, heuristic eval, and synthetic-persona runs pay off early; agent-driven design (Day 2) speeds up only after the context, specs, rules, and hooks are in place.

**Structure (Per-topic context blocks)**

# Block 1 — Jobs-To-Be-Done (JTBD)

Users want outcomes, not features. Format: **"When \[condition/context\], as a \[type of user\], I want \[goal/action\], so that \[benefit/outcome\]."** A feature list without a JTBD builds the wrong thing faster. **Watch:** "I want a fast app" is a solution, not a job — the outcome clause must name a real-world result, not a UI property.

<img src="media/image2.png" style="width:6.35251in;height:3.55208in" />

<img src="media/image3.png" style="width:5.92708in;height:2.56925in" />

# Block 2 — Journey map

A visual story of the user's steps through a service, each step tagged with an emotion. The classic rows: **phases** (in time order), **actions**, **touchpoints**, **thoughts & emotions**, and **pain points & opportunities** — write the pain-points row directly as **How-Might-We** questions, so the map hands off to ideation without translation. The redesign target isn't the step with the most clicks — it's the step where the experience breaks down most (usually the worst emotion). Tie each emotion to a *specific* trigger, never a bare adjective on the phase. **Watch:** AI can draft the map from a brief, but lived experience fills the emotion layer.

Worked example — a lunch-delivery order (US), all five rows (deliberately a different case from the retail-availability feature the katas use, so the technique gets practised on fresh context):

| Row ↓ / Phase →                   | 1\. Browse                                                         | 2\. Order & Pay                                                                                           | 3\. Wait & Track                                                                                                 | 4\. Handoff                                                   | 5\. Aftermath                                                  |
|-----------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
| Actions                           | Sorts by price; picks a \$13.50 bowl over a \$16 one; ETA "18 min" | Adds a drink; at checkout sees delivery + service + small-order fees + tip; pays                          | Re-opens the app 6× in 25 min; watches the ETA + map                                                             | Gets a "Delivered" push; goes to the door                     | Eats at 1:05, break gone; weighs reordering                    |
| Touchpoints                       | Home feed, price sort                                              | Cart, checkout, fee breakdown                                                                             | Tracking screen, live map, push                                                                                  | "Delivered" push + photo, door                                | Order history, rating prompt                                   |
| Thoughts & Emotions               | 🙂"\$13.50 and 18 min — cheaper *and* fast."                       | 😠"\$13.50 became \$25.70 once fees + tip stacked — and I only see it on the last screen."                | 😟→😠"ETA slid 18→45 min and the map dot hasn't moved in 8 min — stuck, or forgotten?"                           | 😮‍💨"Finally here."                                             | 😔"Overpaid by \$12 and ate at 1:05 — probably won't reorder." |
| Pain Points & Opportunities (HMW) | HMW make the true all-in price honest from the first screen?       | HMW show the full price (food + fees + tip) at browse time, not a number that nearly doubles at checkout? | HMW keep the user confident the order is progressing when the ETA slips — showing why, not only a bigger number? | HMW make "Delivered" verifiable (right door, complete order)? | HMW make value + timing visible *before* ordering?             |

## Block 3 — Heuristic evaluation

A structured check of a UI against Nielsen's 10 usability heuristics (system-status visibility, match to the real world, user control and freedom, consistency and standards, error prevention, recognition over recall, flexibility and efficiency, minimalist design, error recovery, help and documentation). A vision-capable AI runs a first pass on screenshots in minutes. **Watch:** AI produces plausible false positives — force "name the heuristic AND quote the screen element," or discard the finding.

## Block 4 — Lo-fi prototyping

A rough, clickable version of one redesigned flow should *demonstrate the change*, not look shippable. In this module, v0, Lovable, Claude Artifacts, or pen and paper are enough to create a three-screen flow from a one-paragraph brief. **Watch:** vibe-coding tools polish by default — put "rough, no branding" in the prompt.

## Block 5 — Task-based validation

Test by asking users to *do tasks*, not share opinions. "Do you like it?" reveals only politeness; "Show me how you'd check whether this item is in stock near you" reveals whether the design works. **Rule of thumb:** 5 task questions per test, each phrased "show me how you'd…"

## Block 6 — Tone of voice (the words)

Half of an experience is the words — labels, button text, empty-state messages, error copy. A *tone of voice* is a short, reusable description of how the product speaks (e.g. "calm, plain, always names the next step") so every screen sounds consistent and on-brand. AI drafts copy fast in a given voice; you set the voice and check it never alarms, over-promises, or leaves the user without a next step. **Watch:** "make it friendly" isn't a voice — name the rules (sentence case, no jargon, always offer a next action).

## Block 7 — States (a screen is more than the happy path)

Every screen has several states, not only "it worked": empty (no data yet), loading, error / failure, and content-specific edge cases. A transactions list has empty / loading / error / populated; a charge screen has unknown / pending review / resolved / normal. AI generates the happy path by default and silently skips the rest — a screen with only the success state is a demo, not a shippable feature, and the handoff SPEC must list every state. Watch: "looks done" usually means only the success state was designed.

<img src="media/image4.png" style="width:6.45744in;height:2.45176in" />

## Block 8 — AI feasibility check

At the start of a project, decide two separate things: (1) *AI in the product* — should AI appear in this user-facing feature (data readiness, regulatory constraints, worst case if it's wrong)? and (2) *AI in the process* — can the team use AI tools at all (approved tools, sensitive data, contractual permission)? **Watch:** separate decisions with separate constraints — conflating them, or treating "the client wants AI" as the answer, is where AI features fail after launch.

<img src="media/image5.png" style="width:6.09358in;height:3.07607in" />

## Block 9 — Agent-ready handoff

At L3 (AI-native — the workflow itself is built around agents) the handoff is machine-readable: **CONTEXT.md** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#contextmd) captures the feature in one sentence, audience, technical environment, hard constraints, and out-of-scope; **SPEC.md** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#specmd) captures components, states, design tokens, and acceptance criteria. An approved coding agent such as CodeMie, Cursor, or Claude Code should be able to read both without follow-up questions. **Your part:** supply the inputs (business goal, regulatory constraints, brand boundaries, data availability) and read the outputs well enough to estimate the build.

<img src="media/image6.png" style="width:6.51042in;height:2.82555in" />

## Block 10 — When to escalate to a designer

Brand judgment, accessibility from lived experience, ethical trade-offs, controversial UX patterns, strategic information architecture, sensitive copy, and saying no to an AI feature stay human-owned. Anything touching visual language, design-system governance, or the production SPEC.md should involve a specialist before shipping.

Classic concept → how we do it with AI (crosswalk)

This crosswalk separates three cases: classic design concepts that become an AI move, classic craft that gets an AI-assisted first pass, and decisions that stay human-owned.

<img src="media/image7.png" style="width:6.12495in;height:2.58107in" />

What the designer does per phase — and where AI accelerates it

Four boundaries matter before the phase tables:

Here, L3 means AI accelerates the design process. It speeds the designer's work; it isn't necessarily part of the product. (When AI ships inside the product, that's the trust / human-in-the-loop (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#human-in-the-loop-hitl) surface — recognise-and-escalate, out of scope here.)

AI moves augment the full design craft, they don't replace it. User research, interaction, visual, content and service design, accessibility, and design systems remain the foundation. The tables show only the AI-accelerated slice.

The eight phases fall in two bands — defining the strategic direction (Frame → Prioritise & Plan) and delivering at speed & scale (Design → Operate & Optimise). Phases 1–6 are taught at L3 (discovery → handoff); Phases 7–8 are recognition-only — you should spot the work, not perform it.

Maturity levels. L1 = before bootcamp; L3 = after. In between, L2 → L3 is the key shift: at L2, AI drafts and the human polishes (shared prompt templates, AI-generated first drafts). At L3, AI proposes and the human approves (an agent opens the artefact as a pull request with automated checks; the designer reviews the reasoning and merges). Every phase runs this same shift.

The Wide kata series (300-DESIGN:Wide:Katas, curriculum repo: ./modules/300-design/300-wide-katas.md) walks the discovery→handoff arc on one Meridian feature — the cross-channel availability / click-&-collect assistant: frame the job & gate the AI → K 3.W.1; walk & map the journey with evidence → K 3.W.2; prepare & run a generative workshop → K 3.W.3; synthesise & decide the change → K 3.W.4; write AI-aware acceptance criteria → K 3.W.5; build the lo-fi prototype → K 3.W.6; package the agent-ready handoff → K 3.W.7; draft the validation plan & narrative → K 3.W.8. The journey-map example above uses a lunch-delivery order, so the kata practises the technique on a different case.

Each phase also carries an AI-role verb — SCAN (FRAME) · ASSESS (INVESTIGATE) · SOLVE (DEFINE & VALIDATE) · MODEL (PRIORITISE & PLAN) · CREATE (DESIGN) · TEST (DEVELOP) · ADAPT (LAUNCH & SCALE) · BOOST (OPERATE & OPTIMISE).

<img src="media/image8.png" style="width:6.06187in;height:1.79906in" />

The twelve AI moves

AI-specific moves a designer adds on top of core craft. Each is defined once here; the per-phase tables show the before/after. *(These are the in-scope sub-skills of the EPAM AI Design Skill Matrix; full skill cards live in the Materials and Links section (**300-DESIGN:Materials**, curriculum repo: ./modules/300-design/300-materials-links.md).)*

| **AI move**                               | **What it is**                                                                                                                                           | **Active in**                                 |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **AI Prompt Engineering**                 | Write structured, reusable prompts (fixed slots for role, context, style, constraints) so any teammate gets a similar-quality result.                    | All phases                                    |
| **Prompt Library Governance**             | Keep proven prompts in one versioned library so new joiners start from what works.                                                                       | All phases                                    |
| **AI Feasibility Assessment**             | Run the two-branch gate — *can* the team use AI, *should* AI be in the product — to a Yes / Conditional / No verdict.                                    | FRAME                                         |
| **Synthetic Persona Testing**             | Prompt an AI to role-play a user segment and walk your prototype, catching obvious friction in ~30 min. A filter before real users, never a replacement. | INVESTIGATE (reused in ENVISION)              |
| **AI Service Blueprinting**               | Draft a four-lane blueprint (user actions / frontstage / backstage / support) from a one-paragraph description, then audit it.                           | INVESTIGATE (reused in ENVISION)              |
| **AI-Generated Assets**                   | Generate icons, illustrations, mood-boards, placeholder copy — and audit each for brand fit, accessibility, and IP risk before it enters a file.         | ENVISION (reused at LAUNCH)                   |
| **AI-Generated UI Design**                | Generate whole screens/flows in Figma Make or Lovable ("Day 1" greenfield), then audit against the real design system.                                   | ENVISION (reused in DESIGN & DEVELOP)         |
| **AI UX Evaluation Methods**              | Run AI-assisted heuristic reviews and usability analysis (incl. synthetic-user passes) in days, not weeks, then audit the findings.                      | ANALYZE & DEFINE (reused in OPERATE)          |
| **AI User Stories & Acceptance Criteria** | Add the six AI-specific AC clauses — confidence, refusal/fallback, latency, disclosure, feedback, negative — each testable.                              | ANALYZE & DEFINE (reused in DESIGN & DEVELOP) |
| **Agent-Ready Handoff**                   | Hand off a machine-readable CONTEXT.md + SPEC.md + tokens an agent builds from without follow-up — not a Figma link.                                     | DESIGN & DEVELOP                              |
| **Agent-Driven Design**                   | Direct an agent against your Figma library and Storybook to produce production-connected code ("Day 2").                                                 | DESIGN & DEVELOP                              |

| AI Service Blueprinting               | Draft a four-lane blueprint (user actions / frontstage / backstage / support) from a one-paragraph description, then audit it.                   | INVESTIGATE (reused in ENVISION)              |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| AI-Generated Assets                   | Generate icons, illustrations, mood-boards, placeholder copy — and audit each for brand fit, accessibility, and IP risk before it enters a file. | ENVISION (reused at LAUNCH)                   |
| AI-Generated UI Design                | Generate whole screens/flows in Figma Make or Lovable ("Day 1" greenfield), then audit against the real design system.                           | ENVISION (reused in DESIGN & DEVELOP)         |
| AI UX Evaluation Methods              | Run AI-assisted heuristic reviews and usability analysis (incl. synthetic-user passes) in days, not weeks, then audit the findings.              | ANALYZE & DEFINE (reused in OPERATE)          |
| AI User Stories & Acceptance Criteria | Add the six AI-specific AC clauses — confidence, refusal/fallback, latency, disclosure, feedback, negative — each testable.                      | ANALYZE & DEFINE (reused in DESIGN & DEVELOP) |
| Agent-Ready Handoff                   | Hand off a machine-readable CONTEXT.md + SPEC.md + tokens an agent builds from without follow-up — not a Figma link.                             | DESIGN & DEVELOP                              |
| Agent-Driven Design                   | Direct an agent against your Figma library and Storybook to produce production-connected code ("Day 2").                                         | DESIGN & DEVELOP                              |

The biggest shift across the arc is **Day 1 → Day 2**: **Day 1** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#day-1-design) is fast greenfield generation (Figma Make / Lovable / v0); **Day 2** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#day-2-design) is the production-connected loop where an agent composes from the real design system. Phases 7–8 mostly reuse earlier moves.

<img src="media/image9.png" style="width:6.26806in;height:3.31667in" />

**Directional speed-up by phase** (from the EPAM AI Design Skill Matrix; use as a planning heuristic, not a contract): FRAME ≈ 50% · INVESTIGATE ≈ 60% · DEFINE & VALIDATE ≈ 70% (highest, but Day-1 output audits slowly) · PRIORITISE & PLAN ≈ 50% · DESIGN ≈ 60% · DEVELOP ≈ 60% · LAUNCH & SCALE ≈ 40% · OPERATE & OPTIMISE ≈ 60%. Read these as gains on the *generation* step. The up-front context work and the mandatory audit offset much of them on a first pass, so the net payoff compounds with reuse.

<img src="media/image10.png" style="width:6.10417in;height:2.4454in" />

**Cross-cutting (all phases)**

| **AI move**                   | **L1 — before**                        | **L3 — after**                                                                                                |
|-------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **AI Prompt Engineering**     | Ad-hoc prompts; unpredictable results. | Structured promptframes (role / context / style / scope / constraints); reproducible; feeds the team library. |
| **Prompt Library Governance** | Prompts kept locally or not at all.    | A versioned project prompt library, handed off to new joiners. (Org-wide governance is out of L3 scope.)      |

Phase 1 — FRAME (kickoff & setup) — **AI role: SCAN**

**Goal:** align the team and client on goals; set the project up for success on a user-centric footing. **Designer does:** kickoff and goals/KPI workshops · problem framing (How-Might-We) · review of existing info · as-is journey mapping · documentation review · initial mood boards · baseline research.

| **AI move**                   | **L1 — before**                                  | **L3 — after**                                                                                                                                            |
|-------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AI Feasibility Assessment** | No systematic check; "let's add AI" without one. | A short check at kickoff: does the *product* need AI (data, regulation, worst case), and are AI tools allowed in the work — a clear verdict per question. |

Phase 2 — INVESTIGATE (research) — **AI role: ASSESS**

**Goal:** discovery — analyse the as-is, scan trends and best practice, prioritise features by impact. **Designer does:** user research · industry/user/e-commerce trends scan · persona profiles · JTBD definition · hypotheses log · design-system audit · experience opportunities · test planning (screener, recruiter brief).

| AI move                   | L1 — before                                                               | L3 — after                                                                                                                          |
|---------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Synthetic Persona Testing | Proto-personas from the designer's hypotheses; thin and quickly outdated. | Richer personas drafted from source material; used to test obvious friction before real users are recruited.                        |
| AI Service Blueprinting   | Blueprint built manually or missing.                                      | Drafted by prompt and refreshed as functionality changes; the human audits connections and consequences.                            |
| AI Research Synthesis     | Notes + desk research synthesised by hand over days.                      | AI clusters notes into themes in minutes — every theme source-traced to evidence; the new craft is catching AI-fabricated patterns. |

Phase 3 — DEFINE & VALIDATE (concept & validation) — **AI role: SOLVE**

**Goal:** envision the future experience and support strategy; validate it via prototypes, testing, and iteration. **Designer does:** envision workshop (playback + prioritisation of needs) · co-creation / ideation workshop · wireframes for key journeys · clickable prototypes · UX / usability testing.

AI move

L1 — before

L3 — after

AI-Generated Assets

Generates assets ad-hoc; ships the first acceptable output unaudited.

Generates and audits for brand fit, accessibility, and IP risk before production.

AI-Generated UI Design

Not used, or used ad-hoc without a system.

Generates full screens in Figma Make / Builder.io / Lovable (Day 1 / greenfield) and checks compliance.

Carryover from Phase 2: Synthetic Persona Testing pre-validates generated variants without a recruitment cycle; AI Service Blueprinting is taken to a full, kept-current blueprint; AI Research Synthesis re-clusters fresh test findings.

Phase 4 — PRIORITISE & PLAN (synthesis & planning) — AI role: MODEL

Goal: crystallise the target vision; prioritise by impact; build the case for change; deliver the final report. Designer does: further design iterations from testing insights · prioritisation (impact × effort) · acceptance-criteria review with BA + QA · packaged wrap-up (final report with journey, findings, plan).

AI move

L1 — before

L3 — after

AI UX Evaluation Methods

Manual heuristic eval; every new screen waits for review or recruiting.

AI-assisted heuristic scoring and synthetic-user passes create a first pass before recruiting; the human audit decides what survives.

AI User Stories & Acceptance Criteria

Designer doesn't write AC; requirements passed verbally or via Figma.

Designer adds design-specific AC — component names, states, token references, visual gates — in a format an AI coding agent (Cursor / Claude Code) can interpret and validate.

Phase 5 — DESIGN (detailed design) — AI role: CREATE

Goal: turn the validated concept into detailed, buildable design and the agent-ready spec. Designer does: detailed and micro-interaction design · component variants and design-system extension · accessibility audit · non-functional requirement (NFR) negotiation with architecture · handoff annotation.

AI move

L1 — before

L3 — after

Agent-Ready Handoff

Figma file + verbal explanation; engineering interprets intent by hand.

SPEC.md + CONTEXT.md + tokens; the agent consumes them without follow-up.

Phase 6 — DEVELOP (build & handoff) — AI role: TEST

Goal: turn the spec into a working product; build support → functional elements → testing. Designer does: design QA (built-vs-spec) · accessibility QA · build support.

AI move

L1 — before

L3 — after

Agent-Driven Design

Designs only in Figma; no link to the codebase.

Connects an approved coding agent to the Figma library through MCP (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#mcp-model-context-protocol) and Storybook; iterates via CLI/IDE — the Day-2 production-connected loop.

Phases 5 + 6 run as a band at project scale. Detailed design and the build loop overlap on a project engagement — the two phases stay named so the TEST role (AI-driven QA, design-quality CI checkpoints, SPEC-vs-built drift review) stays a visible deliverable rather than dissolving into "design and build." Carryover: Day-1 greenfield UI (Phase 3) bridges into the Day-2 loop — the designer carries forward only the parts that already match the production design system + tokens; everything else is rebuilt against real components before the loop starts. User stories & AC (Phase 4) travel into the handoff with SPEC.md.

Phase 7 — LAUNCH & SCALE (go-to-market) — **AI role: ADAPT** — *recognition only*

**Goal:** market introduction · user acquisition · scaling to a wider audience. **Designer does:** launch-readiness review · onboarding finalisation · marketing/sales coordination · scaling decisions. **In scope:** AI-Generated Assets for launch variants / localisation, AI Prompt Engineering for copy. Deeper work (A/B variant generation, launch-comms automation) is out of L3 scope.

Phase 8 — OPERATE & OPTIMISE (post-launch) — **AI role: BOOST** — *recognition only*

**Goal:** smooth operation · continuous improvement from feedback and performance data. **Designer does:** operations management · feedback collection · performance optimisation · design-system governance · mentoring · strategic direction. **In scope:** AI UX Evaluation Methods for continuous heuristic eval and regression detection. AI feedback-loop design and AI UX-debt measurement are out of L3 scope.

**Recognition only — beyond this Wide path.** When AI ships *in the product* it needs a trust surface (confidence cues, sources, refusal / "I'm not sure" states, human-in-the-loop, error states) and conversational sad-path copy — you should *spot* a missing confidence cue or a dead-end error, but designing these is a separate, in-product track. Also out of scope here (awareness only): service blueprinting where AI is a decision-making participant (Scenario B), AI-driven information architecture, design-system automation, AI-augmented CI/CD for design, Practitioner/Expert trust surfaces, AI feedback-loop design, and user-AI interaction research.

**Working with the designer — your side**

The phases above are the *designer's* work. Here's yours.

**Before design starts — the one-page Day-1 brief.** The designer can only frame the job and run the feasibility check from the context you supply. Bring, on one page:

- the business goal and its success metric — a number, not "improve the experience";

- the AI footprint — is AI in the *product* the user sees, and is it generative or predictive;

- data sensitivity and the regulatory frame (PII / PHI / financial? GDPR, EU AI Act risk class?);

- what happens when the AI is unsure (fallback, human review), and the worst case if it's wrong;

- brand boundaries and the approved-tool list.

A thin or contradictory brief produces a confident, plausible, wrong design the same minute. Name what's missing and send it back rather than letting the designer guess.

**At handoff — what to read back.** A complete handoff is CONTEXT.md + SPEC.md + design tokens an agent can build from without follow-up — not a Figma link. If the component states (loading / empty / low-confidence / error) and the negative AC ("must NOT…") aren't written down, the handoff isn't done — and that gap becomes your rework.

**When to pull in a specialist.** See *When to escalate* above — brand, lived-experience accessibility, ethics, controversial patterns, strategic IA, sensitive copy, and refusing an AI feature stay human-owned.

# Anti-Patterns

Failure modes you'll meet covering this role or working alongside a designer. Each has a name, what goes wrong, the cost, and the fix.

**Adding AI because the client asked.**

- *Wrong:* the team skips the two-branch feasibility check; "the client wants AI" is treated as the decision. Nobody checks data readiness, regulation, or whether the approved toolset can deliver it.

- *Cost:* the feature ships, then breaks three months later — stale data, a flagged consent flow, or a model never wired to live inventory. The fix costs more than the build.

- *Done right:* run the two-branch check as a named charter activity. Record the verdict (Branch 1: AI in process / Branch 2: AI in product) with a Yes/Conditional/No per branch, a one-line rationale, and a named approved-tools list. Re-run it when scope changes. "The client asked" is a driver in the rationale, not a bypass.

**Workshop with no decision to close.**

- *Wrong:* a three-hour session booked to "align" or "explore options." No decision named before the room meets.

- *Cost:* the team leaves with Post-its but no commitment. The real decision happens days later in Microsoft Teams, usually going to whoever argued loudest, and is never documented — so when it's wrong, nobody can trace it.

- *Done right:* the invite names the decision to close and the owner (by role and person). In the last 10 minutes the owner writes the decision in one sentence, reads it aloud, and the facilitator records it before the room disperses. No decision → extend or reschedule.

**Handoff as a Figma file drop.**

- *Wrong:* a Figma link in Microsoft Teams, story marked ready. No CONTEXT.md, no SPEC.md, no machine-readable tokens.

- *Cost:* engineering interprets intent by hand and asks follow-up questions; the AI coding agent (CodeMie, Cursor, or Claude Code) cannot read a Figma link as the build contract. Ambiguity here returns as build rework.

- *Done right:* the handoff isn't done until CONTEXT.md and SPEC.md pass the Definition-of-Handoff-Done checklist. CONTEXT.md: feature in one sentence, audience, technical environment, hard constraints, out-of-scope. SPEC.md: every component named by its exact design-system ID, all states covered, tokens referenced by name (not colour value), negative AC carried verbatim. Figma is linked as reference, not the deliverable.

**AI-generated UI shipped without a component-system audit.**

- *Wrong:* screens generated in Figma Make / Lovable look correct and get handed off without checking the component names against the real design system.

- *Cost:* the generated UI uses names like CardSurface and ActionChip that don't exist; the team rebuilds or reconciles screens that looked ready.

- *Done right:* before any generated screen enters a file, run a component-name parity check — list every component in the output, verify each exists in the system *by exact name* (not "looks similar"). Resolve mismatches first: rename to match, or rebuild from the system.

**Anti-Patterns**

Failure modes you'll meet covering this role or working alongside a designer. Each has a name, what goes wrong, the cost, and the fix.

**Adding AI because the client asked.**

- *Wrong:* the team skips the two-branch feasibility check; "the client wants AI" is treated as the decision. Nobody checks data readiness, regulation, or whether the approved toolset can deliver it.

- *Cost:* the feature ships, then breaks three months later — stale data, a flagged consent flow, or a model never wired to live inventory. The fix costs more than the build.

- *Done right:* run the two-branch check as a named charter activity. Record the verdict (Branch 1: AI in process / Branch 2: AI in product) with a Yes/Conditional/No per branch, a one-line rationale, and a named approved-tools list. Re-run it when scope changes. "The client asked" is a driver in the rationale, not a bypass.

**Workshop with no decision to close.**

- *Wrong:* a three-hour session booked to "align" or "explore options." No decision named before the room meets.

- *Cost:* the team leaves with Post-its but no commitment. The real decision happens days later in Microsoft Teams, usually going to whoever argued loudest, and is never documented — so when it's wrong, nobody can trace it.

- *Done right:* the invite names the decision to close and the owner (by role and person). In the last 10 minutes the owner writes the decision in one sentence, reads it aloud, and the facilitator records it before the room disperses. No decision → extend or reschedule.

**Handoff as a Figma file drop.**

- *Wrong:* a Figma link in Microsoft Teams, story marked ready. No CONTEXT.md, no SPEC.md, no machine-readable tokens.

- *Cost:* engineering interprets intent by hand and asks follow-up questions; the AI coding agent (CodeMie, Cursor, or Claude Code) cannot read a Figma link as the build contract. Ambiguity here returns as build rework.

- *Done right:* the handoff isn't done until CONTEXT.md and SPEC.md pass the Definition-of-Handoff-Done checklist. CONTEXT.md: feature in one sentence, audience, technical environment, hard constraints, out-of-scope. SPEC.md: every component named by its exact design-system ID, all states covered, tokens referenced by name (not colour value), negative AC carried verbatim. Figma is linked as reference, not the deliverable.

**AI-generated UI shipped without a component-system audit.**

- *Wrong:* screens generated in Figma Make / Lovable look correct and get handed off without checking the component names against the real design system.

- *Cost:* the generated UI uses names like CardSurface and ActionChip that don't exist; the team rebuilds or reconciles screens that looked ready.

- *Done right:* before any generated screen enters a file, run a component-name parity check — list every component in the output, verify each exists in the system *by exact name* (not "looks similar"). Resolve mismatches first: rename to match, or rebuild from the system.

<img src="media/image11.png" style="width:6.10417in;height:3.32901in" />

# Outcomes

After this section you can:

Name the eight delivery phases (each with its AI-role verb — SCAN · ASSESS · SOLVE · MODEL · CREATE · TEST · ADAPT · BOOST) and say which are in-scope for this Wide path versus recognition-only.

Identify which standard designer activities AI accelerates and which stay manual or human-owned.

Spot at least three design anti-patterns from your seat — e.g. a Figma-only handoff, hallucinated component names, an AI feature with no error states.

Brief a designer with what they need before work starts: business goal + metric, regulatory frame, brand boundaries, data availability.

Read a handoff pack (CONTEXT.md + SPEC.md + tokens) well enough to judge whether it's complete and estimate the build to first order.

<img src="media/image12.png" style="width:6.40625in;height:3.75691in" />

# Assessment Questions \[Optional\]

**Awaiting Action**

5 minutes

What should be done

\*

A short knowledge check + self-reflection. Run it after you finish reading and practicing — it verifies whether the section outcomes landed. Examples use **Case A — Meridian** (the cross-channel availability / click-&-collect assistant).

**﻿  
**

**Knowledge Check (3 retrieval-practice questions)**

1.  **(Wide Theory — framing & gate)** What makes a JTBD statement different from a feature request? Rewrite *"I want the app to show stock faster"* as a JTBD. Then name the two branches of the feasibility gate (AI **in the process** vs AI **in the product**) and one gate question for each.

2.  **(Deep Theory — trust & HITL)** What makes something a *gap* in a mental-model audit, versus "users will be confused"? Give one concrete gap for the availability assistant. Then classify three availability-assistant actions as **agent-led / confirm-then-act / human-only**, and explain why classifying *everything* as confirm-then-act defeats the point of the AI.

3.  **(Kata / Final Kata — AI-aware AC & handoff)** Name 3 of the 6 AI-specific AC layers and write one **testable** clause for the availability assistant (a number / threshold / observable condition). Why is the **negative AC** ("must NOT") the most expensive one to skip? Then name two of the six checks in the Definition of Handoff Done (K 3.W.7).

**Answer hints**

- **(Framing & gate)** A JTBD names a real-world outcome ("When I'm near a store and need an item today, I want to know it's actually on the shelf, so I don't drive over for nothing"), not a solution. Branch 1 (process): is AI permitted for the delivery team? approved tools? sensitive data? Branch 2 (product): is the stock data ready and fresh? regulatory framework? worst case if it's wrong (phantom-stock promise → wasted trip → churn)?

- **(Trust & HITL)** A gap is a specific sentence the user would say that reveals a false assumption ("It said *in stock* so I assumed it was held for me") — not a vague worry. Agent-led: estimate and display availability. Confirm-then-act: place a hold that commits store stock. Human-only: override a "no stock" signal. All-confirm kills the speed benefit — reserve confirmation for irreversible / costly actions and compensate agent-led ones with logging.

- **(AI-aware AC & handoff)** e.g. confidence (WHEN stock-confidence \< 0.7, label "Likely in stock" not "In stock"), fallback (WHEN the SAP sync is \> 30 min stale, show "Check with store" + store phone), disclosure ("Estimated from store data" badge). Negative AC: the assistant MUST NOT state an exact unit count or promise a guaranteed hold — the costliest failure is a confident false promise. Definition of Handoff Done includes (any two): ≥ 3 AI-AC refined to component / variant / token / placement / visual gate; CONTEXT.md covers feature + audience + environment + constraints + out-of-scope; SPEC.md lists ≥ 2 components with states + token references; negative AC carried into SPEC.md.

**Self-Reflection (3 comparison prompts against the L3 standard)**

1.  In your last project, where did a redesign discussion happen without a **named decision-owner**? What stalled because of it?

2.  Of the trust / HITL / error-state surfaces you've seen shipped, which is weakest in a product you use — and what's the concrete next step to fix it?

3.  When was the **last time you said no** to a "let's add AI" suggestion that failed the feasibility gate? If never — practice the exact words you'd use next time.

**Type your answers into the "Answer" block:**
