# Stage 5 — build, execution and defects (also read s4-specs.md)

> Trimmed excerpt of the EPAM AI Factory notes. Sections included:
> - epam-ai-factory-600_Quality.md — Block 5
> - epam-ai-factory-600_Quality.md — Block 6
> - epam-ai-factory-600_Quality.md — Block 7

---

<!-- source: epam-ai-factory-600_Quality.md -->
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

“Everything is green” hides which families ran. Two hundred passing UI tests provide zero evidence about a changed API contract.

For engineers, selected agent-driven flows become CI jobs only after they are saved as deterministic automated tests with explicit assertions and stable test data. A required Playwright test can then block a merge and attach its trace to a defect.

Agent-driven execution also creates a new review burden. The runner may recover from an unexpected screen in a way a scripted test would reject. It may skip a blocked assertion or interpret similar text as a match. Read recovery steps, retries, and skipped assertions with the same care as failures.

**Human-owned call:** run priority, borderline interpretation, and whether a flaky result comes from product behaviour or the environment.


<!-- source: epam-ai-factory-600_Quality.md -->
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

When the feature itself calls a model, add the exact prompt, exact response, inputs, and model version. These details make the defect reproducible after a model change.

For engineers, the minimal sequence becomes the failing test before the fix when the failure is reproducible. For intermittent failures, the evidence first guides added instrumentation or a diagnostic test that can capture the condition.

**Human-owned call:** severity and priority. Business context determines both.


<!-- source: epam-ai-factory-600_Quality.md -->
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

**“Sometimes slow” is not a condition — it is an excuse. The condition is always more specific.** Ask which state, request, dependency, or missing control made the failure possible.

For engineers, the guard test belongs in the same PR as the fix. This keeps the repair and its protection together.

**Human-owned call:** confirmed condition and final guard-test selection.
