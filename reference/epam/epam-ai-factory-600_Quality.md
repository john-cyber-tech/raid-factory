# In a nutshell

At L2 you write test cases with AI in the loop and run a one-off eval to convince the team a feature works. This Deep track is for the specialists who own quality as their product — Functional QA and Test Automation Engineers, plus the Performance, Security, and Data Quality testers who swap in their own checks. The durable anchor: **quality at L3 is not a final gate before release — it is a continuous system, and the eval is infrastructure**. The rubric is versioned with the prompt that produced it, the golden set grows on a documented cadence, the LLM-as-judge is calibrated against a hand-graded anchor, and the same pack runs on every change and in production. AI does the QA work that scales poorly with human hours — drafting cases, clustering defects, scoring rubrics, generating attack variants; the human owns the rubric, the thresholds, and the release call. It sits downstream of PM/BA, Design, Architecture, and Engineering, upstream of Data, Infrastructure, and Delivery. The theory runs on an Intermediate → Advanced → Expert arc.

# Role Context

- **Who it's for.** Functional QA and Test Automation Engineer specialists. Performance, Security, and Data Quality testers read for the patterns and swap their own checks for the rubric examples. Anyone running QA on a feature that calls a language model is in scope.

- **What the role does (plain verbs).** Functional QA decides *what* to test — owns acceptance criteria, the risk framing, the rubric, golden-set curation, defect triage, and the release recommendation. The Test Automation Engineer decides *how* the checks run — owns the framework, the CI integration, the three-layer eval stack, the healer loop, and the run instrumentation (cost, latency, pass rate, judge agreement).

- **Where it sits.** Downstream of every other role, at the junction of all of them. You receive user stories and ACs from BA/PM, code and CI access from Engineering, personas from Design, NFR budgets from Architecture, and production signals from Ops; you hand back the rubric, the test cases wired into CI, persona-grounded golden entries, a performance plan, new defects, and the release recommendation a PM signs against.

- **What you don't own.** The acceptance-criteria definition of "good enough" co-signs with PM/Legal; the rollback action belongs to Ops/Engineering; the release sign-off is the call you author but the PM signs against the evidence.

- **The L2 → L3 shift.** From a one-off eval that proves a feature works once to an eval pack that is versioned infrastructure — the rubric moves with the prompt, the judge is calibrated on a cadence, the same pack runs in production as the drift monitor, and every code, prompt, model, and production change triggers a step in one of four agentic workflow chains.

# Why this matters for you

The job changes from "running tests on a feature" to "running a quality system that runs tests on every feature." Non-deterministic outputs, model drift, and failure modes that exist for AI features only break the deterministic playbook: a judge inflates over weeks, a vendor point-release silently stops escalating allergy complaints, a prompt edit drops a policy-lookup tool call, and the dashboards stay green. Every discipline in this track exists to catch one of those before a customer screenshot lands in finance. The Deep theory is the design of that system — built on the universal QA disciplines you already practice (ISTQB test design, ISO/IEC/IEEE 29119-3 test documentation, the ISO/IEC 25010 and 25019:2023 quality models) and extended for the AI surface.

<img src="media/image1.png" style="width:6.26806in;height:2.57292in" />

**Topic recap**

The track runs in three layers on an Intermediate → Advanced → Expert arc — read it in chain order, not layer order. Here is each discipline in brief.

- **Test Plan & Test Strategy (Intermediate).** Two artefacts, two scopes: the Plan is per-release (objectives, approach, entry/exit criteria, changes every release); the Strategy is per-product (standards and reusable templates, changes quarterly). For AI features the Plan adds three sections — eval scope, drift-monitor plan, red-team posture — or it describes the deterministic surface and leaves the AI surface implicit.

- **Risk assessment → four knobs (Intermediate).** Two passes before any test design — project-level (regulatory, revenue, trust, safety exposure) and per-surface (blast radius). The output is a one-page table per feature where likelihood × severity sets four controls: rubric strictness, threshold height, eval cadence, and red-team depth. AI drafts the table; the scores stay human-owned because they encode business judgement.

- **Requirements review, DoR, AC-diff agent (Intermediate).** The testability check is sharper for AI features — "the bot is helpful" is not testable; a 3-rule behavioural rubric is. The **AC-diff agent** runs on every story status change, diffs the AC against the linked test cases and rubric rules, and posts mismatches before FQA looks — compressing requirements review from an hour to a ten-minute confirm.

- **Impact analysis & cross-requirement validation (Intermediate).** When a story arrives, map every component, tool call, persona path, and downstream system it touches, with an explicit test-or-skip scope per area — skipping this is how the eval scores green on the model layer while the payments API path silently breaks. Validate new requirements against existing ones in refinement, where a feature that contradicts a standing policy is cheapest to catch.

- **Test Design depth — RTM, BDD, maintenance (Intermediate).** The Requirements Traceability Matrix is the spine, with two extra AI columns — the rubric rule(s) a case exercises and the golden entries it uses; a rule with no entry is theory, an entry with no rule is noise. BDD steps gain explicit rubric verbs; orphan cases are the suite-rot signal; golden-set growth and 90-day rubric-rule retirement are the AI-specific maintenance moves; MR review replays any prompt change against the golden set.

- **Test Data — the six-family menu (Intermediate).** API, SQL, security (incl. OWASP LLM Top 10 for chatbots and decisioners), performance, contract-testing, and PII obfuscation — each with its own coverage discipline. For AI features add persona-grounded **synthetic users** sampled from the Design persona pack. FQA writes the discipline; AI produces the volume.

- **Chain \#1 — Test design (Advanced).** Trigger: a story moves to "Ready for QA". Owner: FQA. Eight steps from req review to summary, with the AC-diff agent at the front and the human design-approval gate before execution. Output: an approved checklist + rubric delta + golden-set delta, all linked to the source story in the RTM.

- **Chain \#2 (closed) — Regression (Advanced).** Trigger: a code, prompt, model, or rubric change to an existing feature. The **defect-clustering** pass runs a similarity score (default 85%) that turns ~50 raw failures into ~8 unique defects; the threshold is the human-owned knob (lower over-dedups, higher under-dedups). Output: a triage report of confirmed unique defects with severity, priority, and owner.

- **Chain \#3 — Automation (Advanced).** Trigger: Chain \#1 cases stable on two consecutive runs. Owner: Test Automation Engineer. The **healer loop** reads a CI failure trace, identifies the likely cause (selector drift, schema rename, prompt-shifted output), proposes a fix, and re-runs — bounded by three non-negotiable budgets (selector-stability 3, schema-validation 2, eval-policy 2). Over-budget loops hide drift, relax assertions to nothing, or burn the API quota.

- **Chain \#4 — Production feedback (Advanced).** Trigger: a production signal (safety-adjacent always routes here). **Eval-as-monitor** keeps the Chain \#1 eval pack running in production; the **calibration loop** re-grades a judge sample by hand to keep it honest. Output: the **release recommendation** — decision / evidence / risk / conditions / signer, where the decision line and signature are never delegated.

- **Execution, defect management & reporting (Advanced).** The four chains are not independent — \#1 feeds \#3, \#3 builds the suite \#2 (closed) runs, \#2 (closed)'s report feeds \#4. Around them: eight execution types (UI, API, accessibility, integration, data, usability, security, performance) each plug into named chains; defect management runs a preliminary duplication check and the six-field template plus two AI fields; defect analysis runs six mining disciplines; reporting rolls up rubric pass rate, judge agreement, drift signals, and outstanding red-team findings.

- **Production quality monitoring (Expert).** Four signal classes feed Chain \#4 — user-reported, system-observed, business-metric (the class that catches the regression that never throws an error), and the AI-only eval-observed (online rubric pass rate, LLM confidence, judge agreement). Anomaly detection runs both rules-based and learned-baseline alerts, routed separately.

- **The three-layer eval stack (Expert).** A rubric on paper does not gate releases. Three layers run *in order*: Layer 1 code-based checks (deterministic, free, milliseconds); Layer 2 LLM-as-judge (per-rule 1–5 score with reasoning, costs tokens); Layer 3 human review (three defined triggers, not a fallback). Reversing the order wastes tokens on outputs a 5ms rule could reject.

- **Golden-set design (Expert).** The set is built, not collected: five buckets, each for a reason — happy-path (baseline), edge (spec boundaries), adversarial (confirmed red-team attacks kept as regression), multilingual (the languages production speaks), sensitive (where a wrong answer is an incident). Every entry carries the input, the expected per-rule behaviour, and two tags: the rule it exercises and the source it traces from.

- **Thresholds, retries, escalation (Expert).** Three FQA-owned policies versioned with the rubric: the per-rule pass threshold, the retry policy (how many, what changes between retries, what counts as success), and the escalation policy (stricter judge, human, defect, or merge block when retries are exhausted).

- **Calibration — eval-of-evals (Expert).** The judge drifts over weeks; without calibration the false-pass rate rises silently. Weekly (high-risk) or monthly (low-risk): sample 30 scored outputs, a human re-scores by hand, agreement is computed per rule (healthy ≥ 85%), and the set always holds at least one known-bad output as the lower anchor. A drop \> 5 points over two calibrations triggers a judge-prompt rewrite.

- **Red-teaming (Expert).** Negative testing under adversarial pressure: Security owns threat-payload intelligence, QA owns the repeatable run and the release evidence. AI expands Security's seed payloads into 30–50 variants; FQA picks ten to run **in a fresh session** that does not have the rubric in context, and logs the actual prompt, response, classification, mitigation, and severity per attack.

- **Drift monitoring & bias spot-check (Expert).** The drift plan names four components — daily eval subset, alert rule (numeric threshold + duration), recall criteria, owner + cadence; "if quality drops" is not an alert. The bias spot-check is a 12-prompt test that holds intent constant and varies one protected attribute on a *moderate* scenario, run per release because model upgrades change the bias surface.

<img src="media/image2.png" style="width:6.26806in;height:2.72847in" />

# Key terms

<img src="media/image3.png" style="width:5.92392in;height:5.89614in" />

**Key takeaways**

1.  The four chains — test design, regression, automation, production feedback — are the core model; every QA task maps to one, and knowing the chain tells you the trigger, the output, and the owner of each step.

2.  The four AI-automation moves define L3 QA — the AC-diff agent (Chain \#1), defect clustering (Chain \#2 (closed)), the healer loop (Chain \#3), and eval-as-monitor plus the calibration loop (Chain \#4); without them the team is at L2 with extra prompting.

3.  The eval is versioned infrastructure — the rubric, golden set, and threshold policy live in the same repo, same commit, with a change-log entry per modification; split them and last Tuesday's CI result is unreproducible.

4.  The three-layer eval stack runs in order — code checks first, judge second, human review third; reversing it wastes tokens on outputs a deterministic rule rejects in 5ms.

5.  Calibration keeps the system honest — without eval-of-evals on a cadence, with a known-bad output as the lower anchor, the judge inflates and the false-pass rate climbs silently until a customer incident.

6.  Numbers, not vibes — drift criteria, recall criteria, and alert rules name a threshold and a duration; severity is not priority; and the human-owned knobs (healer-loop budgets, the 85% clustering threshold, the recalibration trigger) are set, not defaulted.

7.  The boundary stays human — the rubric definition, the risk score, severity, recall criteria, and the release sign-off are human-authored; the eval pack is evidence, the human signs against it, and every AI-generated artefact carries a label or the audit trail breaks.

8.  Adversarial work runs in a fresh session — the context that wrote the rubric cannot run the red-team, or the red-team avoids exactly the prompts the rubric already catches.

**Course Repo: <https://epa.ms/ai-run-26-curriculum-repo>**

# Wide Theory

45 minutes

**Focus:** Quality at L3 is not a final gate before release. It is a continuous system — **rubric** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#rubric), golden set, **LLM-as-judge** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#llm-as-judge) calibrated against a human anchor, **drift** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#drift) monitor, **red-team** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#red-teaming) posture, **traceability** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#traceability-matrix) spine — that runs on every code change, every prompt change, every model upgrade, and every production signal. The headline shift: AI now does the QA work that scales poorly with human hours (drafting cases, generating data, clustering defects, scoring rubrics, generating attack variants); the human owns the calibration, the thresholds, and the release call.

Deep for: Functional QA, Test Automation Engineer. Specialists in Performance, Security, and Data Quality testing read this module for the patterns and substitute their own checks.

Total time per learner:

- Wide path: 50 min Theory + ~90 min kata series + 60 min Final Kata ≈ 3.3h

- Deep path (own role): + 180 min Theory + ~180 min kata series ≈ +6h

At L2, you write test cases with AI in the loop and run an ad-hoc eval to convince the team a feature works. At L3 the eval is infrastructure: the rubric is versioned with the prompt that produced it, the golden set grows on a documented cadence as production complaints arrive, the LLM-as-judge is calibrated against a hand-graded anchor set, and the release recommendation is a structured artefact a PM signs against. This module is the design of that system for an AI-enabled SDLC — built on the universal QA disciplines you already practice (ISTQB test design, IEEE 829 / ISO/IEC/IEEE 29119-3 test documentation, the ISO/IEC 25010 product-quality model and the ISO/IEC 25019:2023 quality-in-use model) and extended for non-deterministic outputs, model drift, and the failure modes that exist for AI features only.

**Objectives**

- **Learn to do:** build a risk-based test strategy and ship a test report + improvement backlog on a real app; specialists ship an eval harness + red-team + drift-monitor suite for an AI feature.

- **Skills (role):** test planning, risk-driven case design, defect logging with RCA and guard tests, reporting.

- **Skills (tooling):** AI case expansion, Faker/Mockaroo test data, Playwright execution, LLM-as-judge calibration, OWASP LLM Top 10 (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#owasp-llm-top-10) red-team taxonomy.

- **Outcome:** test report + improvement backlog (Wide); eval pack (rubric + golden set + judge config + red-team log + drift plan + bias spot-check) plus a runnable QA agent/skill spec (Deep + Final Kata).

- **Tested by:** the Wide artefact chain + the Deep eval/red-team suite + the Final Kata.

# 0 — Role Context

**0.1 — Role names and who they apply to**

Two roles carry most of the day-to-day work in this module:

- **Functional QA** — decides *what* to test. Owns the rules for "good enough", the test case list, the rubric, and the risk framing. Synonyms: Quality Engineer (QE), Test Analyst, QA Lead.

- **Test Automation Engineer** — decides *how* the checks run. Owns the automation framework, the CI integration, the eval pipeline. Synonyms: SDET (Software Development Engineer in Test), Test Architect, Quality Engineer (Automation).

Larger teams also include specialists who own a slice of quality and read this module for the patterns:

- **Performance Tester** — load, latency, throughput, model-response-time budgets.

- **Security Tester** — auth, data exposure, prompt injection, jailbreaks, sensitive-data leakage in model outputs.

- **Data Quality Specialist** — schemas, freshness, completeness, and drift in the data the product (and any AI feature) depends on.

**0.2 — Role description and core duties**

**Functional QA owns:**

- Authoring **acceptance criteria** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#acceptance-criteria) as testable behaviours (not exact strings) and rubric rules with explicit anchor descriptions.

- Designing test cases by risk; categorising into smoke, regression, critical-path, and edge buckets.

- Curating the golden set — picking real example inputs, growing the set per production signal.

- Triaging defects: severity vs priority calls, root-cause analysis, problematic-area identification.

- Writing the release recommendation that a PM signs against.

**Test Automation Engineer owns:**

- The automation framework and the CI integration that runs both deterministic tests and AI evals.

- The three-layer eval stack — code-based checks first, LLM-as-judge second, human review third.

- The healer loop (selectors, waits, data adjustments) and the retry budget per failing run.

- The monitoring wiring that surfaces production signals into Chain \#4.

- Instrumentation: tracking cost, latency, pass rate, judge agreement rate per run.

**0.3 — Main processes**

QA runs five workflows. The first is the classic test cycle; the next four are the **agentic QA workflow chains** that pull AI into every step.

- **Test cycle (classic).** Plan → design → execute → report → re-test. The backbone every other workflow plugs into.

- **Chain \#1 — Test design.** req review → testability → risk → design → data → execution → defect → summary. Starts when a requirement is ready. Ends with reviewed test cases linked to the source requirement.

- **Chain \#2 (closed) — Regression.** impact → regression → suite → execution → clustering → triage → report. Starts when a code, prompt, or model change affects an existing feature. Ends with a triage report.

- **Chain \#3 — Automation.** review → automation → script → execution → analysis → defect. Starts when test cases are stable enough to automate. Ends with tests running in CI on every change.

- **Chain \#4 — Production feedback.** prod signal → root cause → regression → execution → release decision. Starts when a production signal arrives. Ends with a release recommendation.

The four chains are not independent. Chain \#1 produces the test cases Chain \#3 automates. Chain \#3 builds the suite Chain \#2 (closed) runs. Chain \#2 (closed) produces the regression report Chain \#4 consumes when a production signal arrives. Chain \#4's targeted regression is a scoped Chain \#2 (closed) applied to a live incident.

**0.4 — Role in SDLC**

QA sits at the junction of every other role. What it receives upstream and hands off downstream:

<img src="media/image4.png" style="width:5.83363in;height:2.86126in" />

If any of these handoffs is missing, QA cannot do its job. The module is **only as strong as the artefacts upstream sends in**.

**0.5 — How the role changed with AI (general)**

Manual scripting shrinks. Rubric authoring, golden-set curation, eval pipeline supervision, and judge calibration grow. AI is useful in QA when the task is **fast to draft and cheap to review** — let AI produce a first version fast, let a human approve or fix it.

Where AI helps:

- Drafting test cases, BDD scenarios, fake test data, and bug reports from a spec.

- Looking through bug reports, grouping duplicates, guessing the common cause.

- Reading an AI answer and scoring it against a rubric (LLM-as-judge).

- Looking at what code changed and suggesting which existing tests to re-run.

- Summarising a long test run into a short release recommendation.

Where AI does not help (yet) — firmly human-owned:

- Acceptance criteria — what "good enough" means for this feature.

- Risk assessment — how strict the rubric and the gate should be.

- Release decision — does this ship?

- Edge-case and high-impact reviews — a human inspects what the rubric flags.

**0.6 — What changed at L2 (AI-assistant)**

AI is a per-task assistant — it drafts the artefact in front of you, then disappears. You:

- Ask an AI chat to draft test cases from an AC; review them by hand.

- Ask an AI to draft a bug report from a session note; edit the result.

- Run a one-off eval — a handful of inputs, a hand-written prompt to a model, a quick read of the responses — to convince the team a new AI feature works.

- Maintain a golden set as a Google Doc or a folder of files; update it when the next incident reminds the team.

The artefacts exist as drafts produced session-by-session. Each session is its own context. The audit trail is whatever you remembered to save. AI saves typing time inside your day; the structure of the day does not change.

**0.6 — What changed at L2 (AI-assistant)**

AI is a per-task assistant — it drafts the artefact in front of you, then disappears. You:

- Ask an AI chat to draft test cases from an AC; review them by hand.

- Ask an AI to draft a bug report from a session note; edit the result.

- Run a one-off eval — a handful of inputs, a hand-written prompt to a model, a quick read of the responses — to convince the team a new AI feature works.

- Maintain a golden set as a Google Doc or a folder of files; update it when the next incident reminds the team.

The artefacts exist as drafts produced session-by-session. Each session is its own context. The audit trail is whatever you remembered to save. AI saves typing time inside your day; the structure of the day does not change.

**0.7 — What changed at L3 (AI-native)**

QA is restructured around AI workers that automate the steps that scale poorly with human hours: an AC-diff agent flags requirement drift on every status change, a defect-clustering pass dedupes 50 failures into 8 unique defects, the healer loop re-runs and self-heals brittle UI tests inside CI, an LLM-as-judge scores 500 outputs against the rubric overnight, the same eval pack runs in production as the drift monitor, and a calibration loop keeps the judge honest. The human specifies, calibrates, and decides — sets the rubric, sets the budgets, sets the thresholds, signs off the release. The eval is infrastructure, not a one-off. The shape changes on every axis:

- **The rubric is versioned** with the prompt and the model version that produced it; the change log names every modification.

- **The golden set grows on a documented cadence** — every production complaint becomes a candidate entry; every adversarial finding from the red-team becomes a candidate entry.

- **The LLM-as-judge is calibrated** against a hand-graded anchor set with at least one known-bad output; the agreement rate per rule is tracked; below 85% the rule is sharpened.

- **The three-layer eval stack runs in order** — code-based checks first, LLM-as-judge second, human review third — with explicit thresholds, retry budgets, and escalation rules.

- **The drift monitor runs daily** on a slice of the golden set with numeric alert thresholds and named recall criteria; the owner is a person, not a role.

- **The red-team posture is defined** — what attack categories are in scope, who runs them, on what cadence, in a fresh session that does not have the rubric in context.

- **The release recommendation is a structured artefact** the PM signs against, naming the eval-pack version, the model version, and the residual risk.

Quality becomes a continuous system: every code change, every prompt change, every model upgrade, every production signal triggers a step in one of the four chains, and the eval pack is the evidence the release decision rests on.

# 1 — Theory

See Wide Theory (50 min, all learners).

See Deep Theory (180 min, role specialists).

# 2 — Materials and Links 

Templates the module uses (test plan, test cases, defect, RCA + guard test, test report; eval rubric, golden set, judge config, red-team log, drift-monitor plan, bias spot-check, QA agent spec), the AI-native QA tool table (EPAM DIAL / CodeMie, Playwright MCP, Faker / Mockaroo, Promptfoo / OpenAI Evals, OWASP LLM Top 10 — course Glossary: ./modules/000-glossary.md#owasp-llm-top-10), internal knowledge links, an optional external-reference shelf, and the reference-case task menu (Case A — Meridian primary; Case B — Kepler secondary).

# 3 — Practice

**Practice rule for every kata and the Final Kata in this module:** the Wide series runs on your chosen reference case — **Case A — Meridian** unless you have a live engagement (Case B — Kepler is the secondary). Stay on one case across all six Wide katas; switching mid-series breaks the carry-forward chain into the test report and Eval Pack that Modules 700, 800, and 1000 inherit.

**3.1 — Wide Katas**

K 6.W.1 → K 6.W.6 (~90 min, 15-min cap each). Superpower: *take a feature spec and ship a risk-ranked test plan, ~20 categorised cases, realistic PII-safe data, an executed defect log, an RCA + guard test, and a one-page report.* Chains into the Wide test report + improvement backlog.

**3.2 — Deep Katas**

K 6.D.1 → K 6.D.6 (~180 min, 30-min cap each). Specialist outcome: *an eval pack for an AI feature* — rubric + golden set + LLM-as-judge config + red-team log + drift-monitor plan + bias spot-check.

**3.3 — Final Kata**

K 6.3 — specify a runnable QA role-agent / Skill in a native format another teammate can load when no QA specialist is on the team, with the human-owned decisions (scope, severity, the release call) inline as guardrails.

# 4 — Carry-Forward

Two artefacts leave this module.

**4.1 — Eval Pack**

- **Artefact name:** Eval Pack (plus the Wide test report).

- **Source:** Wide kata series K 6.W.1–6 (test report + improvement backlog); Deep kata series K 6.D.1–6 (eval pack).

- **Artefact (Wide):** test report + improvement backlog — a 1-page rollup of coverage, pass rate, top problematic areas, a 5-item ranked improvement backlog, residual risk, and a release recommendation. Format: Markdown (05-report.md).

- **Artefact (Deep):** eval pack — rubric (00-rubric.md) + golden set (01-golden-set.jsonl) + LLM-as-judge configuration (02-judge-run.md) + red-team log (03-red-team.md) + drift monitor plan (04-drift-plan.md) + bias spot-check (05-bias.md). Format: a folder per AI feature, with each artefact saved as the named file.

- **Consuming stage(s):** The **Data** module consumes the Wide test report when designing data-pipeline quality checks. The **Infrastructure & Operations** module consumes the eval pack's drift-monitor plan and the production-signal wiring when standing up live monitoring. The **Delivery & Project Management** module consumes both artefacts as inputs to the release governance pack.

**4.2 — QA Role-Agent Spec**

- **Artefact name:** Role-Agent Spec.

- **Source:** Final Kata K 6.3 (all learners; specialists add the depth-add sections). A native Claude Skill or sub-agent that automates **one** QA workflow step (per the QA single-step overlay).

- **Consuming stage(s):** **the downstream roles** load .claude/skills/qa/ or .claude/agents/qa.md when no QA specialist is on the team — read in place to automate one QA step (expand cases, structure defects, roll up a report, run the judge, extend the golden set, generate red-team variants), not transformed. **Final Assembly Line** lists it in the agent roster a joining teammate reads.

- **Format:** a runnable Claude Skill or sub-agent, ≤ 2 pages of body, scoped to one step, with the guardrails (human-owned decisions) inline.

- **Engine guide target:** .ai-run/guides/quality-gates.md, under header \## Quality gates + eval calibration (from Module 600 — Quality). This is the authoritative chain mapping; the spec's \<!-- chain:rules:start guide=… topic=… --\> delimiter attributes mirror it, and on any disagreement this line wins.

- **Optional stand-in override (Deep only):** tech-lead-reviewer overlay — gates qa.drift, qa-checklist.approved, qa-tests.approved; the spec's escalation triggers map to its decision / confidence / risk_flags verdict.

# Why This Matters for You

AI can compress a team-week of quality work into about two days.

Give it a specification on Monday. By Wednesday, the team can have:

- a risk-ranked test plan;

- about 20 reviewed test cases;

- 15 realistic test-data records;

- an executed defect log;

- a root-cause analysis with a guard test;

- a one-page test report.

Treat the time estimates in this chapter as illustrative working targets. Actual time depends on feature complexity, environment readiness, evidence quality, and the review required.

This speed changes the work. Ownership of judgement stays with people.

A human still makes the three calls that decide quality:

1.  What is in scope?

2.  How serious is the defect?

3.  Is the remaining risk acceptable enough to ship?

Your role may sit outside Quality. You still depend on these calls. You may spec, build, deploy, sell, or defend the feature after an incident.

This chapter gives you the vocabulary and evidence questions to challenge a quality claim. It also gives you a practical capability many non-QA roles leave unused: reading a test plan and report without taking either on trust.

One question runs through the chapter:

**What did we test, what did we skip, and how do we know it is good enough to ship?**

Any role can ask that question.

**Two ways to ship**

**The shortcut.** Someone builds a feature and clicks through it three times. The available inputs work, so the team ships.

Two weeks later, a customer finds a path nobody tried. A half-paid order remains stuck. A delivery slot uses the wrong timezone. The team loses a sprint reconstructing what happened.

**The workflow.** The team writes down what “working” means. It ranks the risks and tests happy paths, edges, and failures that lose money.

Each defect carries enough evidence for another person to reproduce it. The team traces the worst defect to its triggering condition. The release follows only when the report makes the remaining risk visible.

When the half-paid order appears, it becomes a guard test. The next regression run catches the same condition and its neighbours.

The difference is process, rather than talent. One team can define “good” and prove what it checked. The other team relies on a successful demonstration.

<img src="media/image5.png" style="width:6.26806in;height:4.17153in" />

L3 changes the speed and scale. Human judgement remains the release boundary.

One case needs extra disciplines. When the feature itself calls a model, ordinary tests cover only part of the risk. Block 10 introduces that Deep path.

# Goal

Build cross-role literacy in AI-assisted quality work.

By the end, you can:

- read a one-page test plan and challenge its gaps;

- recognise acceptance criteria that can support a test;

- review an AI-expanded test suite for risk and coverage;

- log a defect another person can reproduce;

- distinguish a root-cause condition from a symptom;

- read a test report well enough to support a release decision.

The chapter also prepares one practical superpower. You can take a feature specification and review the Monday-to-Wednesday package described above.

The goal is cross-role judgement, rather than specialist test execution. AI can draft the volume. People with domain context decide which evidence matters.

Your role may keep you outside test execution. You still need to challenge what the team tested, what it skipped, and what evidence supports the release.

# Time

~50 min: about 40 minutes for prose and tables, plus 10 minutes for diagrams and checks.

# Audience

All learners outside Functional QA and Test Automation Engineering. This includes consultants, PMs, BAs, designers, architects, engineers, data, infrastructure, security, delivery, and management.

QA specialists can use this as a refresher. Specialist depth lives in Deep Theory.

Quality often becomes visible to non-QA roles only when something fails. By then, the missing decision may sit several handoffs upstream. A vague acceptance criterion becomes a shallow test. A shallow test becomes a confident green report. The release then transfers the hidden risk to customers and support.

Wide literacy lets you interrupt that chain earlier. You can ask whether the plan covers the risk your role introduced. You can challenge a defect report that lacks reproducible steps and supporting evidence. You can ask which production signal will reveal a silent failure.

This capability changes collaboration with QA. Instead of requesting “more testing,” you can name the behaviour, input, or boundary that needs evidence. QA keeps specialist ownership while every role improves the material entering the quality system.

# Prerequisites

Complete Onboarding (010), Fundamentals (020), and Modules 100–500.

Bring these upstream artefacts when available:

- the **Spec Package** from PM/BA, especially its acceptance criteria;

- personas from Design, which provide realistic input shapes;

- the Architecture Context Pack, including latency, cost, and error-rate limits;

- the Engineering PR record, which says what the code change should do.

# Must Cover

**AI is the fast first-drafter; you are the editor with domain context. Humans own scope, severity, priority, thresholds, and the ship decision.**

The ten topics follow one feature through the quality cycle and beyond release:

- **Risk-based test strategy** — a one-page plan naming scope, exclusions, top risks, and the conditions that gate release.

- **Requirements validation and acceptance criteria** — observable behaviour that gives every later test a clear pass or fail.

- **Test cases** — five human seeds expanded by AI, then curated into happy, edge, and negative coverage.

- **Test data** — realistic, varied, personally identifiable information (PII)-safe records that change on every meaningful axis, rather than only the ID.

- **Execution** — browser-agent runs whose step traces prove which assertions actually ran.

- **Reproducible defects** — minimal steps, expected and actual results, reproduction context, evidence, severity, and priority.

- **Root cause and guard tests** — the triggering condition, plus regression variations that stop the defect returning.

- **Test report and improvement backlog** — six sections that expose coverage, failures, residual risk, and the release recommendation.

- **Production monitoring** — user, system, and business signals with numeric thresholds, durations, owners, and response paths.

- **Testing AI features** — the Deep path for rubrics, golden sets, judges, red-teaming, drift, and bias checks.

Run the drafting work on the approved GenAI stack. EPAM examples use DIAL or CodeMie (codemie-claude). The test plan, cases, data notes, defect log, and report are shared, version-controlled delivery artefacts. Save them with the work rather than in a private chat.

**Terms Used in This Section**

Load-bearing terms are defined here at first use. The course Glossary provides the full definitions (Learn portal or curriculum repo: ./modules/000-glossary.md).

<img src="media/image6.png" style="width:5.89614in;height:6.60451in" />

# Key Messages / Ideas

One division of labour governs every block:

**AI is the fast first-drafter. You are the editor with domain context.**

AI drafts plans, cases, data, defects, clusters, and reports at volume. Humans own scope, severity, priority, thresholds, and the ship decision.

<img src="media/image7.png" style="width:6.26806in;height:2.83681in" />

The eleven messages below match the recap card. Its footer adds the AI-feature Deep path:

1.  **AI drafts at volume; humans own the judgement.** Scope, severity, priority, thresholds, and release stay human-owned.

2.  **A plan that lists everything tests nothing.** Set scope through exclusions, top risks, and entry/exit criteria.

3.  **Acceptance criteria describe observable behaviour.** “Checkout works” gives a test nothing to check.

4.  **Five human seeds beat fifty unreviewed AI cases.** AI expands; the human curates and forces a negatives floor.

5.  **Useful data varies on the dimensions real users vary.** Change locale, persona, and order shape, rather than only IDs.

6.  **A defect report needs a reproduction path or sufficient evidence.** Trim its steps to the smallest known condition and preserve evidence for intermittent failures.

7.  **Root cause names the condition.** A guard test covers that condition and neighbouring variations.

8.  **“More testing” is not a backlog item.** Name the test and input that would have caught the defect.

9.  **A report exists to support a decision, not to inform.** Expose coverage, remaining risk, and the release recommendation.

10. **Monitoring continues the quality cycle after release.** Every alert names a number and a duration.

11. **Engineers own the code-level enforcement.** CI gates, automated suites, and guard tests belong with the code change.

During execution, read the trace. A “passed” summary remains a claim until the steps show that the assertion ran.

When the feature itself calls a model, the Deep path adds rubrics, evals, red-teaming, drift, and bias checks.

# Structure (Per-topic context blocks)

The running example is **FreshCart**, a fictional grocery-delivery product.

It contains three features with different risk levels:

- **Checkout and payment — high risk.** It takes money and schedules fulfilment. A defect can lose revenue or double-charge.

- **Delivery-slot booking — medium risk.** It reserves pickup or delivery time. Most mistakes are recoverable, but they disrupt a customer’s day.

- **Product catalogue and descriptions — low risk.** It shows items, prices, and copy. Review can catch many errors before customers see them.

Each block reintroduces the feature it needs. The katas apply the same concepts to your chosen reference case, with Meridian as the default.

# Block 1 — Risk-Based Test Strategy in One Page

The thread: a specification creates many possible checks. Risk decides which checks deserve time and which ones gate release.

Give an approved AI chat the specification, risk register, and previous defect log. It can draft a one-page plan in about two minutes.

**Copy-ready plan prompt**

**Sources:** Read the approved feature specification, risk register, previous defect log, Architecture Context Pack, and linked acceptance criteria.

**Task:** Draft a one-page risk-based test plan for this release.

**Required sections:** In scope, Out of scope and why, Top three risks, Entry criteria, Exit criteria, and Human sign-off owner.

**Evidence rule:** Cite the source section behind every scope boundary, risk, and threshold. Mark a proposed threshold as Draft for human approval when the sources provide none.

**Constraints:** Treat every downstream system as an explicit scope decision. Include it when the release changes its use, data, contract, configuration, or risk exposure. Otherwise, list it as out of scope and cite the existing contract or integration evidence that supports the exclusion. Keep the plan to one page. Exclude individual test cases and schedules.

**Uncertainty:** End with Missing evidence and conflicts. List unsupported assumptions and conflicting source statements.

**Human decision:** Leave final scope, risk order, exit thresholds, and release sign-off to the QA lead and feature owner.

Your job is to challenge the draft:

- Which important risk is missing?

- Which downstream system is included without a risk-based reason?

- Which excluded system lacks evidence supporting that exclusion?

- Which entry or exit number is too weak?

- Which person owns the release sign-off?

A useful plan answers four questions:

1.  What is in scope?

2.  What is out of scope, and why?

3.  What are the top three risks?

4.  What conditions start and end testing?

<img src="media/image8.png" style="width:6.26806in;height:2.98819in" />

**FreshCart example**

**In scope.** Cart, payment, order-confirmation write, and inventory decrement. Run end-to-end checks across priority browsers and one mobile profile.

**Out of scope.** The downstream payment provider’s internal behaviour. FreshCart still checks its own contract and sandbox integration with the provider. Also exclude the marketing email and warehouse-picking system.

**Top three risks.**

1.  The customer is charged, but the order is missing.

2.  A retry decrements inventory twice and causes overselling.

3.  Partial payment leaves the cart in an unrecoverable state.

**Entry criteria.** Build deployed to QA; payment sandbox loaded; previous defect log attached.

**Exit criteria.** Critical-path pass rate ≥ 95%; zero open severity-1 defects; feature-owner sign-off.

“In scope: everything” is the common failure. **A plan that lists everything tests nothing.**

Ask which downstream system the tests leave untouched. There is always a boundary: payment provider, authentication layer, analytics pipeline, or warehouse system.

For engineers, the in-scope critical paths are candidates for CI-gate scope. If the release plan names checkout as a required merge gate, its deterministic automated suite blocks the merge.

**Human-owned call:** scope, exclusions, risk ranking, exit threshold, and sign-off owner.

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

<img src="media/image9.png" style="width:6.26806in;height:3.57917in" />

This check can become recurring work. On every story-status change, an agent can compare the criteria with linked test cases and flag drift.

**Human-owned call:** which findings block refinement and which remain accepted gaps.

# Block 3 — Test Cases: From Seed List to AI-Expanded Suite

The thread: acceptance criteria provide the promise. Human-written seeds select the business flows, then AI expands the permutations.

This is the single biggest daily change at L3. Five human seeds, preserved as base cases, can become about 20 reviewed cases after AI adds three variations to each. The illustrative target is fifteen minutes; actual time depends on feature and review complexity. The same work may otherwise take a senior QA about half a day and a junior QA about one day.

AI has seen many test patterns. It can produce permutations a person may overlook. It lacks this release’s risk context, so a human curates the result.

**Copy-ready expansion prompt**

**Sources:** Read the approved feature specification, acceptance criteria, one-page test plan, and the five seeds below.

**Task:** Preserve each seed as one base case. For each seed, generate one happy-path variation, one edge-case variation, and one negative variation. This produces five base cases plus fifteen generated variations.

**Classification:** Record Generated variation as base, happy, edge, or negative; this records where the draft came from, rather than its full taxonomy. Separately record Path as positive or negative, Boundary as standard or edge, and one or more relevant Suite tags: smoke, regression, or critical-path. Add priority 1 to 4.

**Outcome rule:** Every case must name a user-visible or business-visible result. A status code alone is insufficient.

**Output:** Return a Markdown table with ID, Seed, Generated variation, Path, Boundary, Preconditions, Steps, Expected outcome, Suite tags, Priority, and Source AC.

**Uncertainty:** Add Gaps and invented assumptions. List behaviour missing from the sources. Keep each unsupported assumption outside the test requirements.

**Human decision:** Leave release-gating status blank for the feature owner or QA lead.

**Workflow**

1.  Write five one-sentence seeds: two happy paths, two known failures, and one edge.

2.  Keep each seed as a base case and run the expansion prompt for fifteen additional variations.

3.  Delete wrong cases and deduplicate near-copies.

4.  Correct path, boundary, suite tags, and priority.

5.  Count the negatives. Keep at least five distinct negative cases.

6.  Save the reviewed suite.

If fewer than five negatives survive, use this follow-up:

Generate five additional negative cases. Use a different failure mode for each. Include one partial-failure recovery case. Keep the same table schema and cite the source acceptance criterion. Put any unsupported behaviour under Gaps and invented assumptions.

The first draft contains twenty cases: five base cases and fifteen generated variations. After review and deduplication, keep the cases that add distinct coverage; use the negative follow-up when fewer than five distinct negatives survive. The human pass is essential.

<img src="media/image10.png" style="width:6.26806in;height:2.53264in" />

<img src="media/image11.png" style="width:5.91697in;height:2.14594in" />

Check that at least half the cases name a user-visible outcome. This makes the suite easier to translate into meaningful assertions.

For engineers, the reviewed cases become input to the automated suite.

**Human-owned call:** seed choice, negative-case relevance, path, boundary, suite tags, priority, and release-gating status.

# Block 4 — Test Data Essentials

The thread: cases describe behaviour, but data decides which parts of that behaviour the test actually reaches.

Useful data is realistic, varied, and PII-safe. AI can help produce fifteen records, ten personas, and four locales in fifteen minutes.

Use Faker (free and local) or Mockaroo (free tier in the browser) for valid shapes. Use an approved AI chat for language and persona variation. Together, they cover structure and human variation.

**Copy-ready data prompts**

**1. Field shapes**

Produce 15 fictional customer records as JSON.

Use four locales: IT, DE, JP, and US. Include syntactically valid emails and postcodes, three to five prior orders, and varied payment methods.

Return a JSON array plus a short field dictionary. Use synthetic values only. Add a generation_notes field describing the variation strategy.

**2. Behaviour variations**

For the delivery-slot feature, produce 10 fictional booking requests.

Use these personas: tired parent, formal B2B buyer, non-native speaker mixing English and Italian, typo-prone user, last-minute user, careful planner, repeat customer, first-timer, mobile user, and accessibility-reliant user.

Tag each request with its persona, locale, urgency, and expected interpretation. Keep personal details synthetic.

**3. PII safety pass**

Review the generated records for real-looking names, emails, phone numbers, and addresses.

Replace risky values with deterministic synthetic forms such as fake-name-7@example.com. Return the cleaned dataset and a one-paragraph masking note. List values with uncertain classification.

Cross records with personas, then remove combinations that make little sense. Document the generation and masking method.

Shape generators and language models solve different parts of the problem. Faker and Mockaroo produce valid names, dates, identifiers, and postcodes. An AI chat can vary tone, intent, mistakes, and context. Use both when the feature depends on both structure and behaviour.

The combination still needs review. A formal B2B buyer may conflict with a child account. A Japanese postcode paired with a US-only shipping method may create noise rather than useful coverage. Keep combinations that reach a meaningful rule or risk.

Review at least three or four field combinations against the feature rules. This check catches plausible individual values that form an impossible record together.

The one-paragraph masking note matters. It lets Security, Data, and audit reviewers see how the dataset became safe. “Synthetic data” is a claim; the method makes that claim reviewable.

Useful test data has three properties:

- **Realistic:** it matches production shapes and broad distributions.

- **Varied:** it changes several meaningful dimensions.

- **PII-safe:** personal identifiers are synthetic or safely obfuscated.

The dominant failure is realistic data on one axis and identical data on every other axis. Ten plausible names still provide weak coverage when every order uses the same city, items, and card type.

Vary locale, persona, and order shape together.

<img src="media/image12.png" style="width:6.26806in;height:2.42778in" />

**Human-owned call:** meaningful field combinations and acceptable masking evidence.

# Block 5 — Execution: Browser Agents and the Five Families

The thread: reviewed cases and data become evidence only after execution. The trace proves what the runner actually did.

An AI browser agent can operate the running application from plain-English instructions. It opens pages, fills forms, checks visible results, and returns a step trace.

Before AI browser agents, the same work needed a scripted Selenium flow or a manual session. The first required engineering time. The second often left weak evidence.

Claude Desktop or Cursor can run Playwright through an approved Model Context Protocol (MCP) server. Setup takes about ten minutes once. Follow **600-QA:Wide:Katas — Setup, one-time (before Kata 6.W.4)** (curriculum repo: ./modules/600-qa/600-wide-katas.md).

**Copy-ready execution prompt**

**Environment:** Use the approved QA environment and the test account named in the runbook. Treat every other environment as out of scope.

**Case:** Open the cart, add the kettle, pay with the approved test card, and verify that the confirmation page displays the order number.

**Evidence:** Record every navigation, input, visible assertion, redirect, console error, screenshot, and network failure. Include timestamps.

**Stop rule:** Stop before any destructive action outside the test account. Ask for human approval if the environment or account differs from the runbook.

**Output:** Return Result, Step trace, Assertions executed, Evidence links, and Unverified steps. A final passed label must name the assertion that completed.

Read the trace before accepting the summary. An agent may report “passed” after a redirect prevented the final assertion.

The trace is evidence. The summary is a claim about that evidence.

This shift matters beyond QA. A designer can inspect the screen and state the agent observed. A BA can compare the asserted outcome with the acceptance criterion. An engineer can use the failed step and network record to reproduce the problem. One execution trace becomes a shared evidence surface.

**Five test families**

These families form a memory aid. They mix layers, a level, and a test type in formal International Software Testing Qualifications Board (ISTQB) language.

<img src="media/image13.png" style="width:5.35444in;height:2.21539in" />

<img src="media/image14.png" style="width:6.26806in;height:1.62708in" />

“Everything is green” hides which families ran. Two hundred passing UI tests provide zero evidence about a changed API contract.

For engineers, selected agent-driven flows become CI jobs only after they are saved as deterministic automated tests with explicit assertions and stable test data. A required Playwright test can then block a merge and attach its trace to a defect.

Agent-driven execution also creates a new review burden. The runner may recover from an unexpected screen in a way a scripted test would reject. It may skip a blocked assertion or interpret similar text as a match. Read recovery steps, retries, and skipped assertions with the same care as failures.

**Human-owned call:** run priority, borderline interpretation, and whether a flaky result comes from product behaviour or the environment.

# Block 6 — Defects You Can Reproduce

The thread: execution finds a failure. A structured defect turns that observation into work another person can repeat and fix.

A two-paragraph Slack message often mixes symptoms, assumptions, and frustration. An approved AI tool can structure it in seconds and highlight missing evidence.

The discipline remains human-owned. AI removes typing, rather than the need for observation.

A useful defect report has six core fields:

1.  **Title:** one line naming user impact.

2.  **Steps to reproduce:** numbered and minimal.

3.  **Expected result.**

4.  **Actual result.**

5.  **Severity:** how serious the impact is.

6.  **Priority:** how soon the team should act.

It also carries two evidence sections:

- **Reproduction context:** environment, build or version, browser or device when relevant, account state, test data, timing, and reproducibility frequency.

- **Evidence:** screenshots, video, logs, traces, request IDs, and links to the execution run. Mark missing evidence explicitly.

**Copy-ready defect prompt**

Convert the session note below into a defect report with six core fields plus reproduction context and evidence.

Use these fields: Title, Steps to reproduce, Expected result, Actual result, Severity, and Priority.

Add Reproduction context with environment, build or version, browser or device when relevant, account state, test data, timing, and reproducibility frequency.

Preserve observed facts. Put interpretations under Hypotheses. Mark missing evidence as Needed from reporter.

Reduce the reproduction sequence to the smallest known sequence. Keep every step until evidence shows its removal preserves the failure.

Leave Severity and Priority as Human decision required. Offer impact questions rather than assigning either value.

End with Evidence attached and Evidence missing.

**Session note:** \[paste the PII-safe note here\]

A useful title names impact: “Customer charged but order missing after payment retry.” A report with neither a reproduction path nor sufficient evidence is not actionable yet. An intermittent or production-only failure can still be a valid defect when logs, traces, request IDs, frequency, or other evidence establish what happened.

Minimal steps matter. When removing one more step loses the condition, the sequence is small enough. Ten steps may describe a workflow rather than the trigger.

Reproducibility reduces more than typing. It removes the back-and-forth where Engineering asks for browser, account state, data, timing, and expected outcome across ten messages. A complete defect transfers the observation in one handoff.

Preserve uncertainty while structuring the report. If the reporter remembers the result but lacks a screenshot, mark the screenshot as missing. If the environment is unclear, ask for it. A polished guess creates more delay than an explicit gap.

Severity and priority are independent:

- A homepage typo may be severity 3 and priority 1 because leadership noticed it.

- A rare order-corruption case may be severity 1 and priority 3 because it affects one customer each month.

Use the shared scale consistently: severity 1 means blocker and severity 4 means cosmetic. Priority 1 means act now; priority 4 means act when capacity allows.

<img src="media/image15.png" style="width:6.26806in;height:4.00764in" />

When the feature itself calls a model, add the exact prompt, exact response, inputs, and model version. These details make the defect reproducible after a model change.

For engineers, the minimal sequence becomes the failing test before the fix when the failure is reproducible. For intermittent failures, the evidence first guides added instrumentation or a diagnostic test that can capture the condition.

**Human-owned call:** severity and priority. Business context determines both.

# Block 7 — Root Cause, Symptom, and Guard Test

The thread: the defect describes what happened. Root-cause analysis names the condition that allowed it, then a guard test protects that condition.

Give an approved AI tool the last 30 complete defect records. It can cluster them by candidate condition in about two minutes. If only titles are available, cluster them by symptom and do not present the result as candidate root causes.

**Copy-ready clustering prompt**

**Sources:** Read the last 30 approved defect records, including titles, reproduction steps, evidence, and fix notes.

**Task:** Cluster defects by candidate root-cause condition and frequency. Keep symptoms separate from conditions.

**Output:** Return a table with Cluster, Candidate condition, Defects, Frequency, Shared evidence, Conflicting evidence, and Confidence.

**Evidence rule:** Cite every defect ID. Quote the evidence that supports each candidate condition. Label a cluster Title-only when detailed evidence is absent.

**Uncertainty:** Add Alternative explanations and missing evidence.

**Human decision:** Recommend two or three candidates for investigation. Leave root-cause confirmation to the QA lead and engineer.

Possible clusters include payment retry, stale inventory read, UI race, and infrastructure timeout. The result gives two or three hypotheses to investigate.

Pattern-mining that took a senior QA an afternoon can take ten minutes. The saved afternoon goes into confirming the top two candidates against evidence.

Clustering is valuable because many symptoms can share one condition. Five checkout defects may look unrelated when titles mention a spinner, duplicate charge, timeout, stale cart, and missing confirmation. A retry condition can connect them. The cluster directs investigation and remains a hypothesis until confirmed.

A symptom is what the user saw. A root cause is the condition that made the symptom possible.

**FreshCart double-charge**

**Symptom:** two charges and one order.

**Root cause:** the payment request missed an idempotency key. This key tells the payment service to treat repeated requests as one operation. A network retry submitted the charge twice. The order write deduplicated by order ID and created one order.

A loading spinner may reduce double-clicks. The network-retry condition remains.

The fix adds an idempotency key. A repeated request with the same key and the same parameters is treated as the same operation and returns the recorded result. Reusing the key with conflicting parameters is rejected.

The **guard test** starts from that condition. It covers the original failure plus three or four meaningful variations:

- another payment method;

- a slow network;

- a double-click;

- a retry after timeout.

Use this prompt to draft candidates:

The confirmed root-cause condition is: \[condition\].

Generate six guard-test variations that exercise this condition without copying only the original failing input.

For each variation, return Setup, Trigger, Expected invariant, and Why this exercises the condition.

Separate true condition variations from cases that only repeat the symptom. Cite the defect or RCA evidence used. Leave final suite selection to the QA lead and engineer.

Keep the three or four variations that truly exercise the condition.

<img src="media/image16.png" style="width:6.26806in;height:3.87847in" />

**“Sometimes slow” is not a condition — it is an excuse. The condition is always more specific.** Ask which state, request, dependency, or missing control made the failure possible.

For engineers, the guard test belongs in the same PR as the fix. This keeps the repair and its protection together.

**Human-owned call:** confirmed condition and final guard-test selection.

# Block 8 — Test Report and Improvement Backlog

The thread: execution creates many results. The report compresses them into evidence for one decision: whether the remaining risk is acceptable.

Give an approved AI tool the defect log, pass rates, scope, and impact criteria. It can draft the report and rank five improvement candidates in about two minutes.

**Copy-ready report prompt**

**Sources:** Read the approved test plan, execution results, defect log, pass rates by label, skipped-scope list, and impact criteria.

**Task:** Draft a one-page test report and a five-item improvement backlog.

**Required sections:** Coverage, Pass rate by label, Top two problem areas, Five-item improvement backlog, Residual risk, and Release recommendation.

**Evidence rule:** Cite the run, defect, or plan entry behind every number and risk claim. Keep skipped surfaces beside the relevant pass rate.

**Ranking:** For each backlog item, state customer impact, recurrence, detectability, effort, and the test or input that would have exposed the problem.

**Uncertainty:** Add Missing evidence and disputed interpretation.

**Human decision:** Label the recommendation Draft. Leave residual-risk acceptance, backlog order, and the ship decision to the accountable release owner.

The human audits the ranking, edits the recommendation, and signs the residual risk.

A useful report has six sections. The first four present the evidence. The last two turn that evidence into a release decision:

1.  **Coverage:** tested and skipped surfaces.

2.  **Pass rate:** total plus breakdown by defined label.

3.  **Top two problem areas:** where failures cluster.

4.  **Five-item improvement backlog:** specific changes ranked by impact.

5.  **Residual risk:** what can still fail, who may be affected, and why the risk remains.

6.  **Release recommendation:** ship, hold, or ship with named conditions and an accountable owner.

The report should also preserve exclusions and confidence. A high pass rate means little when the highest-risk integration was skipped. Put the skipped surface beside the number, rather than in a separate appendix.

The dimensions can overlap: one case may have Path = negative, Boundary = edge, and the critical-path suite tag. State the denominator for each dimension or tag and do not add overlapping counts to produce a total.

An improvement backlog converts evidence into the next engineering actions. Ranking should consider customer impact, recurrence, detectability, and effort. AI can calculate or explain a draft order. The release owner decides which risk deserves capacity first.

**FreshCart report excerpt**

**Coverage:** Tested checkout and inventory decrement against 10 critical-path inputs. Skipped marketing email and warehouse handoff.

**Pass rate:** 10/10 critical-path, 4/8 edge, and 2/3 negative.

**Problem areas:** Payment retry failed in 3/6 retry cases. Concurrent orders double-counted inventory in 2/4 cases.

**Improvement backlog:** Add an idempotency key. Make inventory decrement atomic. Add partial-payment recovery. Wire checkout to the merge gate. Add a concurrent-order test.

**Residual risk:** Payment retries still fail in 3/6 cases. Concurrent orders still double-count inventory in 2/4 cases.

**Release recommendation (draft):** Hold. Re-run both problem areas after the fixes; the feature owner signs only when the named exit criteria are met.

“More testing” names neither an action nor a decision. Ask which test and input would have caught the defect.

<img src="media/image17.png" style="width:6.26806in;height:3.69931in" />

**A report exists to support a decision, not to inform.** If the recommendation remains unclear, expose the missing evidence or unresolved risk.

**Human-owned call:** impact criteria, backlog order, residual-risk statement, and release recommendation.

# Block 9 — Production Monitoring

The thread: pre-release testing covers known conditions. Production monitoring catches changes in traffic, dependencies, configuration, and user behaviour after release.

After release, the environment changes without a code commit:

- traffic exceeds test levels;

- a dependency degrades;

- a feature flag changes;

- a third-party API slows;

- user behaviour reveals an unseen path.

Production monitoring runs three signal classes together:

The three classes answer different questions. User reports reveal felt impact, but they arrive late and unevenly. System signals reveal technical failure, but they can stay green during a valid-looking business failure. Business metrics reveal lost outcomes, but they need a product owner who understands the normal range.

Use all three because each covers another class’s blind spot.

<img src="media/image18.png" style="width:5.79196in;height:1.88204in" />

A team watching only system signals can miss a clean 200 response that quietly damages conversion.

One release kept error rate and latency green for three days. Checkout completion fell from 78% to 71%. The business alert fired on day two and exposed a configuration regression.

An enforceable alert names a number and a duration:

Alert when checkout completion falls by more than 5 percentage points day over day for two consecutive days.

“If something looks wrong” omits the threshold, window, and response trigger.

When an alert fires, run a targeted subset of the release suite against a controlled production-like environment by default. Run checks in production only when the runbook explicitly permits them, using approved synthetic accounts, non-destructive cases, isolated test data, and a cleanup or rollback path. The pre-release suite becomes an incident-response asset.

Role ownership remains distributed:

- **PM/BA:** include the monitoring plan before release.

- **Engineering:** provide logs, metrics, alert thresholds, owners, and runbooks.

- **Design:** warn monitor owners when a flow or entry point changes.

- **Delivery/management:** confirm the business metric, owner, and out-of-hours response.

- **Data:** protect the schemas and pipelines that dashboards depend on.

When the live feature calls a model, add sampled eval pass rate as a fourth signal. A provider upgrade can change behaviour without a code change. Deep Theory covers that monitor.

**Human-owned call:** threshold, time window, owner, and response path.

# Block 10 — Testing AI Features: The Deep Path

The thread: ordinary QA still applies to AI features. Non-deterministic outputs add risks that exact expected values cannot cover.

An **AI feature** calls a model as part of product behaviour. Examples include a support chatbot and a summarisation button.

The same input can produce different valid answers. One exact string is therefore a weak assertion.

Five extra disciplines sit above ordinary testing:

1.  **Rubric and golden set:** behaviour rules run against a fixed set of representative inputs.

2.  **LLM-as-judge:** one model scores another model’s output against the rubric, so hundreds of outputs can be reviewed consistently.

3.  **Red-team:** a reviewer tries to trigger unsafe behaviour and records the exact prompt and response.

4.  **Drift monitoring:** the eval runs on sampled live traffic and after model or prompt changes.

5.  **Bias spot-check:** one protected attribute changes while the substantive question stays fixed.

<img src="media/image19.png" style="width:6.26806in;height:1.69236in" />

A judge needs calibration against human-labelled examples. A red-team needs a fresh session without the rubric in context. A drift alert needs a numeric threshold and owner.

These controls solve different failure modes. The rubric defines “good” for open-ended output. The golden set makes the check repeatable. Calibration tests whether the judge applies the rubric like the human anchor. Red-teaming searches for unsafe behaviour. Drift monitoring asks whether behaviour changed after release.

Keep the boundary explicit: the model can score volume, generate attacks, and suggest clusters. Humans define rubric meaning, label the anchor examples, accept residual risk, and decide release.

These practices form the Deep path. Read **600-QA:Deep:Theory** (curriculum repo: ./modules/600-qa/600-deep-theory.md) before releasing an AI feature without a QA specialist. The six Deep exercises are **K 6.D.1–6**.

Every role contributes inputs:

- Design personas become bias-test variations.

- BA acceptance criteria become rubric rules.

- Engineering prompts become red-team targets.

- Architecture limits become latency and cost gates.

- Production complaints become golden-set candidates.

Well-specified, diverse inputs are quality infrastructure.

**Human-owned call:** rubric meaning, calibration labels, risk threshold, escalation, and release decision.

# Anti-Patterns

These patterns are visible before they reach Quality. Use the final column as a push-back question.

<img src="media/image20.png" style="width:5.75724in;height:6.93786in" />

# Outcomes

By the end of this chapter, you can:

- read a one-page test plan and identify what it leaves out;

- write or challenge acceptance criteria using observable behaviour;

- direct AI to expand five human seeds into a reviewed suite;

- enforce a floor of five negative cases and a user-outcome check;

- generate realistic, varied, PII-safe test data and document its method;

- review an AI browser-agent trace instead of trusting its summary;

- log a defect with minimal reproducible steps or sufficient evidence, plus reproduction context;

- distinguish severity from priority;

- separate a root-cause condition from a symptom;

- explain how a guard test protects neighbouring variations;

- read a six-section report, identify residual risk, and reject vague backlog items;

- name the three production signal classes and the parts of an alert rule;

- locate each role’s highest-impact contribution to quality;

- recognise an AI feature and name the five Deep-path disciplines it needs.

The transferable principle is simple:

**AI scales the draft. Humans define good, inspect the evidence, and own the release call.**

<img src="media/image21.png" style="width:6.26806in;height:2.82222in" />
