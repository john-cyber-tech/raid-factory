# Stage 4 (and Stage 5) — engineering specs and test design

> Trimmed excerpt of the EPAM AI Factory notes. Sections included:
> - epam-ai-factory-500_Engineering.md — Block 2
> - epam-ai-factory-500_Engineering.md — Block 3
> - epam-ai-factory-500_Engineering.md — Anti-Patterns
> - epam-ai-factory-600_Quality.md — Block 1
> - epam-ai-factory-600_Quality.md — Block 3
> - epam-ai-factory-600_Quality.md — Block 4

---

<!-- source: epam-ai-factory-500_Engineering.md -->
# Block 2 — Application Development and AI Assistance

The environment provides safe context. The delivery loop then turns written intent into code, independent tests, review, and evidence.

**The mini-cycle**

The L3 engineering mini-cycle has six ordered steps:

requirement → plan / context → code → independent tests → review → evidence

1.  **Requirement** — write what the work must achieve before implementation starts.

2.  **Plan and context** — choose an approach and load the relevant project sources.

3.  **Code** — AI drafts the implementation while the engineer supervises or reviews.

4.  **Independent tests** — a separate session writes tests from the requirement.

5.  **Review** — challenge scope, assumptions, behaviour, security, and evidence.

6.  **Evidence** — package the change so another role can audit it cold.

Focus on spotting missing steps rather than memorising the loop. A gap early in the loop weakens every later claim.

**The bottleneck moved**

AI reduced the effort needed to produce working-looking code. Review effort remains.

The slow questions now require judgement:

- Does the implementation match the requirement?

- Did AI invent an interface contract?

- Are the tests genuinely independent?

- Can another team safely pick up the result?

The engineer's work shifts from typing toward intent, supervision, and evidence review. Generation became cheaper. Trust still has to be earned.

This shift changes planning conversations. A fast first draft can make a task look nearly complete. Review, integration, security, and evidence work may still remain.

Review the state of the evidence alongside the state of the code. "Generated" and "ready for merge" describe different workflow points.

**Context matters more than prompting**

*Prompt engineering* improves the wording of one request. *Context engineering* controls the sources and instructions available before the request.

A clever prompt cannot supply missing architecture decisions or current conventions. It also disappears when the team changes tools.

Maintained context survives across tasks and tools. A good prompt against stale context still produces stale output.

Context engineering also decides what stays outside the session. Irrelevant files create noise. Sensitive sources may exceed the tool's approved boundary. Historical records may conflict with current rules.

The engineer should be able to name the selected sources and explain why they fit the task. That explanation becomes part of the review trail.

For review, ask:

What context did the AI have loaded?

That question reveals more than a polished prompt transcript.

**Plan before building**

Write a short brief before asking AI to build. A paragraph or focused list is enough for Wide-level review.

The brief should answer:

- What should this component do?

- Who uses it?

- Which decisions should it support?

- Which boundaries must it respect?

- What sits outside scope?

AI fills gaps with plausible guesses. Written intent makes those guesses visible and gives review a comparison point.

The plan adds another checkpoint. It turns the brief into an approach before code makes the approach expensive to change. Reviewers can challenge scope, dependencies, and architectural fit at this cheaper stage.

Watch for a spec that emerged from the code. Acceptance criteria written after implementation often describe current behaviour. They may fail to represent the original intent.

This creates a circular proof: the code defines the tests, then the tests confirm the code. The original business need disappears from the chain.

The terms connect in order. The requirement states the need. The spec makes that need implementable. Acceptance criteria define observable pass conditions.

**The model spectrum**

Model names change, but most providers offer several capability and cost tiers. The task should determine the tier.

Claude Code commonly presents Haiku, Sonnet, and Opus families. GitHub Copilot may change or partly abstract its underlying models. Cursor lets engineers select provider models by task.

Names can change while the tiering idea survives.

The most capable model is not always the best choice. A stronger model adds little value to routine boilerplate.

A risky refactor deserves stronger reasoning. Compare the same output across two or three capability levels. Judge every result against the same pre-written quality criteria.

The cheaper tier may already satisfy the need.

The comparison only works when "good" is defined first. Otherwise the most polished answer wins, even when it misses the requirement.

Model choice also affects provenance. Record the tier or model when it materially changes cost, risk, or reproducibility. Routine drafting rarely needs a full model history.


<!-- source: epam-ai-factory-500_Engineering.md -->
# Block 3 — Code Modification and Insights

The mini-cycle produces a change. Git and CI then make that change reviewable, enforceable, and traceable.

**How a change moves**

A *commit* is a saved snapshot with a message. A *branch* isolates a line of work from the main codebase.

A *pull request* proposes merging that branch. It shows the diff, carries review discussion, and links automated checks.

For a Wide learner, the PR is the main audit surface. This is where AI-assisted evidence either appears or goes missing.

The branch keeps unfinished work away from the main codebase. Commits divide that work into reviewable snapshots. The PR then connects those snapshots to discussion and controls.

These records answer different questions. Commits show how the implementation moved. The PR shows why the team accepted it.

**Hooks and CI**

A *hook* runs on an engineer's workstation. It can block a dangerous shell command or format an edited file.

A *CI required check* runs on a shared server. Every pull request triggers it, regardless of local tool or workstation.

The boundary is direct:

**Hooks help locally. CI required checks enforce for the team.**

If a process says, "our hooks prevent dangerous patterns," ask one more question:

Does a server-side required check block the same pattern?

A workstation control can disappear after a tool, version, machine, or environment change. A required check blocks merge for every contributor.

Hooks still have value. They provide fast feedback before the engineer pushes a change. Their speed improves flow, while CI supplies the shared enforcement floor.

Use both when the control benefits from early feedback and universal enforcement. Keep the server-side check authoritative when results disagree.

**Reading CI output**

You can read a CI result without fixing its code. First identify the category and consequence.

Both security findings and formatting findings can block merge. Only one may require incident-level investigation. Read the signal before asking for a delivery date.

The check name starts the diagnosis. Open its detail, locate the failed step, and identify the affected surface. Ask Engineering or Security when the consequence remains unclear.

A green CI run has a narrow meaning. The configured checks passed for that commit. It cannot prove that those checks cover every requirement or hidden risk.

**What an AI-assisted PR should carry**

AI context and decisions stay outside commit history unless the engineer records them. The PR must carry enough evidence for the change's risk.

At minimum, ask:

- Which context and rule files did the AI use?

- Which requirement did it implement?

- Did tests come from the implementation session or a separate one?

- Where did the engineer override the AI?

- Which gaps remain incomplete, uncertain, or unverified?

The **PR provenance block** (course Glossary — Learn portal or curriculum repo: ./modules/000-glossary.md#pr-provenance-block) records this trail.

Evidence should grow with blast radius. This is *provenance proportional to risk*.

Blast radius means the damage a faulty change could cause. Authentication can expose accounts. Billing can charge incorrectly. Data migrations can alter many records at once.

Higher blast radius needs stronger reconstruction. Reviewers should see the original intent, AI context, independent checks, human decisions, and unresolved risk.

A team once ships an async feature with passing tests. The PR only says, "AI assisted with implementation."

Two months later, Security finds unsafe input validation. The team needs to know whether AI introduced the pattern. Missing provenance stretches the investigation to one week.

A two-paragraph PR note would have answered the question in five minutes.

**Your part in the change**

A non-engineering role shapes quality before, during, and after implementation. You can act at three points without reading code.

**Before build:** hand Engineering written intent, acceptance criteria, relevant context, and the approval owner.

**During review:** trace the PR to the requirement. Check context, test independence, human overrides, and open uncertainty.

**At escalation:** involve Engineering when context is missing or tests share the implementation session. Escalate high-risk authentication, billing, and data changes when evidence is thin.

Your role still owns its part of the evidence. Product owns the requirement. Design owns experience constraints. Architecture owns recorded boundaries. Security owns its risk decision.

Engineering should link those inputs rather than silently reinterpret them. A missing upstream decision should return to its owner.


<!-- source: epam-ai-factory-500_Engineering.md -->
# Anti-Patterns

These patterns break the evidence chain at different points. The cost column shows why each deserves review attention.

**Outcomes**

By the end of Wide Theory, you can:

- explain the purpose and staleness risk of hot, warm, and cold context;

- recognise a current rule file and ask who maintains it;

- explain why written intent should precede implementation;

- choose a model tier based on task risk, cost, and complexity;

- distinguish an Agent Skill's procedure from MCP-provided capabilities and data;

- distinguish local hooks from server-side CI required checks;

- apply behaviour, assumptions, drift, and evidence review lenses;

- explain why independent tests begin from the requirement in a fresh session;

- calibrate review depth for supervised and async agent work;

- match PR provenance depth to the change's blast radius;

- ask safe, source-backed repository questions with approved read-only tools;

- recognise useful answers through sources, honest gaps, and visible conflicts;

- enforce the hard boundary against sensitive data in unapproved tools.


<!-- source: epam-ai-factory-600_Quality.md -->
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


<!-- source: epam-ai-factory-600_Quality.md -->
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

Check that at least half the cases name a user-visible outcome. This makes the suite easier to translate into meaningful assertions.

For engineers, the reviewed cases become input to the automated suite.

**Human-owned call:** seed choice, negative-case relevance, path, boundary, suite tags, priority, and release-gating status.


<!-- source: epam-ai-factory-600_Quality.md -->
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

**Human-owned call:** meaningful field combinations and acceptable masking evidence.
