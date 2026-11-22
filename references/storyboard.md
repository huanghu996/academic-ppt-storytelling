# Storyboard: Give Each Slide a Reason to Exist

Write the slide cards before layout. A storyboard describes the audience's reasoning path; a paper's section list rarely provides enough detail.

## 1. Minimal slide card

```text
ID / main talk or backup / estimated seconds:
Role: question, concept, evidence, counterexample, or synthesis.
Title: precise subject or supported finding.
Point: the one thing the audience should understand.
Claim type: observation, interpretation, hypothesis, question, plan, setup, or limit.
Evidence: E IDs and source locations, or why empirical evidence is not required.
Scope: conditions that must accompany the point.
Needs: prerequisites not already part of the intended audience's knowledge.
Adds: the explanation, observation, or definition established on this slide.
Main visual: comparison, relationship, and first place to look.
Explanation: teach the reading conditions, identify the pattern, explain its meaning.
Transition: what remains unresolved, and why the next slide follows.
Build: initial state and each meaningful change; what context remains visible.
Static version: how all necessary information is retained.
```

A table is sufficient. Structured JSON is optional.

## 2. Titles follow slide responsibilities

| Responsibility | Title form | Wording example only |
|---|---|---|
| Definition or setup | Precise subject | "Matched conditions and error definitions" |
| Untested judgment | Question or hypothesis | "Does near-wall error depend on the training scale?" |
| Supported result | Finding with scope | "Error concentrates near the wall in the tested cases" |
| Inconclusive result | Observation and limit | "The current record does not distinguish the two explanations" |
| Plan | Specific test | "A controlled test of the scale-shift hypothesis" |

The example result title requires real supporting material before use in an actual talk.

## 3. Design local pacing, not artificial suspense

For a central figure, plan four beats: orient the audience, expose the comparison, interpret the evidence, and examine the boundary. These beats may occupy one slide or several; they are not a fixed quota.

State the research question early. Necessary definitions and comparison conditions must precede the judgment they support. After a dense figure, allow a simpler synthesis or boundary statement. Use visual continuity to reduce reorientation, rather than making every slide equally busy.

Establish what an audience should inspect before pointing to a winning value. Present contrary evidence where it affects the inference. A focal evidence moment is valuable because it clarifies the argument, not because it creates surprise.

## 4. Order information by dependency

- Introduce only the concepts needed to read the next evidence or reasoning step.
- For a complex method, show the whole system and input/output first, then explain the parts that matter to the hypothesis.
- Read results through conditions, relationship, strength of evidence, and boundary.
- Let controls address competing explanations. An ablation indicates design dependence; it does not automatically identify a unique mechanism.
- Close by answering the opening question at the supported level. A discussion invitation can share the ending; a separate thank-you-only slide is optional.

A transition should express an inference, for example: "This comparison estimates overall error, but does not locate its source. The next slide separates the spatial regions." Avoid narrating a table of contents between every slide.

## 5. Automatic transition audit and repair

Run after drafting the storyboard, before visual production, and again on the final sequence. Do not wait for the user to notice missing connecting slides. This requires reading the content; the structural checker cannot infer whether one scientific explanation follows from another.

### Inspect every handoff

For each adjacent pair A and B, including chapter boundaries, identify what the preceding material establishes, what B requires, and which open question makes B relevant. Compare the actual definitions, evidence, and conditions rather than just the titles. A deliberate change of branch should state its relationship to the research question; it need not imply causation.

Look especially for:

- **Problem to insight**: the observation or diagnosis that motivates the hypothesis is absent.
- **Insight to method**: the design appears without explaining why it addresses the proposed factor.
- **Method to evidence**: the baseline, test conditions, independence, or metric needed to read the result has not been introduced.
- **Evidence to conclusion**: interpretation, alternative explanations, or scope are skipped.
- **Any boundary**: a new object, scale, acronym, symbol, or assumption is used before introduction.

Use Phase 1's audience assumptions. Do not add elementary explanations the intended audience already knows, and do not require a separate slide for every item in this list.

### Repair the smallest necessary unit

1. Reorder existing explanations if they already contain the prerequisite.
2. Add a concise definition, rationale, or comparison condition to an existing slide when it remains readable.
3. Insert a bridging slide when the missing content answers a distinct necessary question that needs its own explanation or visual.

For an inserted page, record its specific question, the prerequisite it supplies, source or clearly labeled rationale, incoming/outgoing relationship, and speaking time. Keep it in the main talk when the central argument depends on it. An empty section divider, generic connective wording, or an explanation hidden only in speaker notes does not close a content gap.

**Example, conditional on supplied material**:

```text
Before:
Failure under shifted conditions → Module Y architecture → Error comparison

After:
Observed failure under shifted conditions
→ Diagnostic observation motivating factor X [added prerequisite]
→ How module Y uses X
→ Matched baseline, test conditions, and error definition [added prerequisite]
→ What the error comparison establishes within those conditions
```

Use the diagnostic page only if a diagnostic observation is actually available. Otherwise retain X as a hypothesis and explain how it would be tested; do not manufacture the observation or present it as an established cause.

### Recheck the repaired sequence

Recheck the incoming and outgoing transitions of every inserted, merged, or moved page, then read the complete main argument again. Stop when the intended audience has the necessary prerequisites, each move serves a clear question, and no supported-content gap remains. Record unresolved source gaps accurately rather than declaring them fixed.

Honor hard page counts and speaking budgets. Remove redundant or lower-priority material to make room first; do not conceal essential reasoning in backups or silently add overlay pages. If the constraints cannot accommodate the necessary explanation, report the specific conflict and seek a change only after attempting a concrete revision. With flexible counts, add only necessary pages and update timing and numbering.

## 6. Complete example: a ten-minute proposal without formal results

**Context**: A researcher wants to examine possible causes of cross-geometry flow-reconstruction error. Only a research idea is available; no checked dataset or completed literature review is supplied. This example demonstrates planning, not scientific findings.

**Contract**: Explain the cross-geometry question and propose a controlled test that can distinguish scale shift from competing explanations. Do not report an improvement result.

| Slide | Title | Point and evidence status | Main visual and explanation | Next dependency | Seconds |
|---|---|---|---|---|---|
| 1 | Cross-geometry reconstruction: a validation plan | State the question and research stage | Minimal title and concrete question | Define cross-geometry validation | 20 |
| 2 | Validation target and scope | Separate geometry and operating-condition changes; definition | Object schematic labeled illustrative | Check what prior studies cover | 55 |
| 3 | Literature coverage remains to be checked | A gap is not yet established | Fields for a literature comparison; mark entries pending, invent no authors | State testable explanations without presupposing the gap | 60 |
| 4 | Does scale shift affect near-wall error? | Hypothesis and competing explanations | Dashed hypothesis relationships and confounders | Control conditions to distinguish explanations | 65 |
| 5 | Matched controls and data partitioning | Specify the comparison and protect independence | Stable training/validation/test diagram | Define the measurements | 85 |
| 6 | Metrics and regional analysis | Examine overall and near-wall behavior; plan | Metric definition and regions, no invented result curves | Connect measures to interpretation | 60 |
| 7 | How outcomes distinguish explanations | Prespecify supportive and contrary observations | Decision table explicitly labeled expected outcomes | Check sampling requirements | 80 |
| 8 | Replication, sampling, and uncertainty | Separate temporal observations and independent training repeats | Layered sampling schematic; unresolved counts marked pending | Address resource limits | 70 |
| 9 | Risks and alternative tests | Identify what can still be learned under constraints | Risks linked to fallback designs | Summarize the decision | 65 |
| 10 | The validation plan to confirm | Restate question, hypothesis, and next action | Concise scope and unresolved conditions | Discussion | 40 |

Total: **600 seconds**. These times belong to this example, not a universal slide budget. If reliable results are provided, replace relevant planned-test slides with evidence slides and reassess titles, sources, and timing.

Slide 5 may retain one diagram while emphasizing model-selection data, test objects, and matched conditions. Its handout uses numbered annotations. Slide 7 should preserve the full decision table so that expected success is not privileged by reveal order.

## 7. Backup paths and compression

Keep assumptions and limits needed for the main conclusion in the main talk. Put detailed derivations, extra conditions, and complete parameter tables in backups. Optional links should point to a named backup and return to a named main slide.

For shorter talks, remove duplicate background and nonessential branches first. Preserve comparison conditions, uncertainty meaning, and scope. For a fixed page count, merge or simplify explanation rather than silently adding reveal pages.
