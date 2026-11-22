---
name: academic-ppt-storytelling
description: Create or restructure academic presentations for paper discussions, lab meetings, conferences, research proposals, defenses, and progress reports. Build a scientific argument, write a slide-by-slide narrative, and match claims to traceable evidence, readable visuals, and restrained animation. Deliver the requested editable PowerPoint, LaTeX Beamer source with PDF, or outline. Use for whole-talk content and communication design; isolated formatting fixes, manuscript editing, and data analysis do not require the full workflow.
---

# Academic PPT Storytelling · Make the Scientific Argument Visible

**Goal**: Turn a paper, dataset, existing deck, or research idea into a talk whose audience can explain the question, follow the reasoning, assess the evidence, and recognize the limits of the conclusion.

A strong academic presentation connects **argument**, **sequence**, and **visual explanation**. The argument establishes what follows from the evidence. The sequence supplies information when the audience needs it. The visual explanation makes the decisive comparison or relationship easy to inspect. Set these decisions before choosing effects.

Use the user's language, template, slide count, and output format. This Skill is written in English; it does not require every resulting talk to be in English. A topic without results can support a proposal or question-led outline, never fabricated findings.

For PowerPoint, deliver an editable `.pptx`. For LaTeX, use the bundled **SJTUBeamer** starter unless the user selects another theme, and deliver source plus compiled PDF. Do not substitute one format for another without agreement.

## Reference Map

Read by phase. For a narrow revision, load only the relevant guidance.

| Reference | Purpose | Read when |
|---|---|---|
| [audience-to-design.md](references/audience-to-design.md) | Translate audience needs into narrative, visuals, pacing, and stable context | Establishing a new talk or changing its audience |
| [scientific-argument.md](references/scientific-argument.md) | Claims, evidence ledger, inference strength, and talk-specific argument structures | Building or reviewing the scientific argument |
| [storyboard.md](references/storyboard.md) | Slide cards, transitions, pacing, timing, and a complete worked outline | Planning a multi-slide narrative |
| [evidence-visuals.md](references/evidence-visuals.md) | Match visual encodings to evidence and preserve scientific meaning | Selecting, redrawing, or laying out figures |
| [animation-patterns.md](references/animation-patterns.md) | Stable diagrams, progressive emphasis, real time, and static alternatives | Adding any reveal, animation, or temporal sequence |
| [implementation.md](references/implementation.md) | Format routing, editable objects, source management, and verification | Producing presentation files |
| [sjtubeamer.md](references/sjtubeamer.md) | Pinned GitHub theme, build commands, overlays, handouts, citations, and troubleshooting | Producing LaTeX slides |
| [quality-checklist.md](references/quality-checklist.md) | Delivery blockers, visual review, rehearsal, and repair decisions | Before every delivery |

## Workflow

### Phase 1 · Frame the Question and the Audience's Task

Establish the audience, setting, speaking time, Q&A allocation, language, page count, output format, and available evidence from the supplied material. A requested total includes the cover and ending unless specified otherwise. In Beamer, distinguish logical frames from overlay PDF pages before interpreting an exact page limit.

Proceed with reasonable assumptions for ordinary preferences. If missing material changes a scientific conclusion, finish independent work and ask for that material together. Do not require the user to approve every intermediate stage.

Without timing or page guidance, start with a **10-minute talk and roughly 8–10 main slides, including the cover and ending**, plus optional backup slides. State the assumption and revise it when needed.

Read `references/audience-to-design.md` and write two short statements:

> **Audience task**: The audience starts with [knowledge or uncertainty] and should leave able to [explain, distinguish, evaluate, or decide].
>
> **Talk contract**: For [audience], in [time], answer [scientific question]. [Evidence] supports [conclusion or current judgment] under [conditions].

A proposal replaces the conclusion with a testable hypothesis and a verification plan. An inconclusive progress report states what is observed and what remains unresolved. If the conclusion is unknown, retain the question rather than inventing a stronger message.

Read `references/scientific-argument.md`. Build a compact **claim–evidence ledger** with source locations, support scope, and limitations. Separate observation, interpretation, hypothesis, and plan. In a paper discussion, distinguish the original authors' claims from the presenter's assessment.

**Output of this phase**: audience task, talk contract, available sources, key claims, and consequential evidence gaps. A paper's title or a visual theme alone is insufficient preparation for scientific slides.

### Phase 2 · Write the Audience's Reasoning Path

Read `references/storyboard.md`. Use the following structure when it fits, merging or reordering stages as the research requires:

```text
Problem: What concrete phenomenon or failure needs explanation?
Gap: What specific factor or condition do current approaches leave unresolved?
Insight: What testable explanation follows from the observation?
Method: What design or mechanism addresses that explanation?
Evidence: What decisive comparison or derivation supports the claim?
Boundary: Under which conditions does it hold, and where does it fail?
Takeaway: What answers the opening question, and what remains open?
```

Theory may rely on definitions, assumptions, derivations, and counterexamples. Reviews may revolve around disagreements between bodies of evidence. Proposals organize around discriminating tests. Negative results organize around excluded explanations and residual uncertainty. Do not force a success story onto every study.

Before laying out slides, write a card for each:

```text
ID and role: Which step of the argument does this slide perform?
Title and point: What should the audience understand or accept?
Evidence and scope: Where is the support, and what does it establish?
Needs and adds: What prior knowledge does this slide require, and what does it establish?
Main visual: What comparison or relationship should be inspected?
Explanation and transition: How is it read, and why is the next slide needed?
Timing and build: Estimated seconds, reveal states, and static alternative.
```

One main point can use several panels that answer the same question. Use supported takeaway titles for findings. Definitions, setups, and processes may use precise subject titles. Express untested claims as questions or hypotheses.

Choose a **central evidence moment** and reserve time to read and explain it. It may be a decisive control, a key proof step, or a counterexample exposing a boundary. Multiple equally important findings may have multiple focal moments.

Plan the local rhythm: establish the reading conditions, present the evidence, pause to interpret it, then test the boundary or move to the next question. State the research question early; do not hide essential context to manufacture suspense.

**Required logic check and repair before Phase 3**: Review the storyboard as a first-time member of the intended audience. For every adjacent pair and section boundary, compare what the preceding slides establish with what the next slide requires. Detect missing definitions, unexplained design choices, unintroduced comparison criteria, and unsupported inferential jumps. Follow the transition-audit procedure in `references/storyboard.md`; perform it without waiting for the user to request connecting material.

Repair the content directly: reorder or clarify existing slides, and automatically insert the minimum necessary bridging slides when a missing explanation needs its own page. Each inserted slide must supply a specific prerequisite from available sources or clearly labeled reasoning; a generic divider or transition sentence does not supply missing scientific content. Never invent evidence to connect the story.

Respect hard page and time limits. First recover room by merging or removing lower-priority repetition. If essential reasoning still cannot fit, identify the concrete constraint conflict instead of silently exceeding the limit or omitting the prerequisite. With flexible counts, add needed pages and recalculate timing. Recheck affected transitions after every repair until no repairable dependency gap remains; flag any source-dependent gap that cannot be resolved.

**Output of this phase**: a repaired storyboard, a main-talk time total, focal evidence, and backup-slide placement, with brief working notes on added or reorganized explanations. Estimate time from reading and reasoning effort, not a universal slides-per-minute rule.

### Phase 3 · Give the Evidence a Visual Form

Read `references/evidence-visuals.md`. Choose the comparison before the chart: matched conditions for differences, real axes for trends, shared coordinates and scales for spatial fields, and explicit edge semantics for mechanisms.

Set a small visual system:

- **Composition**: follow the supplied template; otherwise start with 16:9 and stable positions for title, figure, explanatory annotation, and source.
- **Encoding**: keep the same object the same color across slides; supplement color with line style, labels, or markers. Reserve emphasis for the current explanation.
- **Typography**: use available fonts and test readability. PowerPoint can start around 30–36 pt titles and 22–28 pt body text, subject to the venue and template. Beamer has a different canvas; evaluate its rendered output rather than copying those sizes literally.
- **Context**: keep the necessary condition, baseline, units, and evidence status visible where losing them would change the interpretation. Avoid a dashboard-like status strip full of irrelevant metadata.

Redraw from actual data when available, retaining transformations and provenance. With only a published image, reuse a traceable image or a clearly located detail view. Do not represent visually estimated values as original data. A schematic can explain a hypothesis but cannot stand in for measurement or simulation evidence.

**Output of this phase**: visual decisions for each slide, shared style rules, and unresolved figure needs.

### Phase 4 · Build the Talk and Add Only Useful Motion

Read `references/implementation.md`. Use the target format and tools actually available. For LaTeX, read `references/sjtubeamer.md` and copy [the bundled starter](assets/sjtubeamer-template/main.tex), its companion files, and theme dependencies into the talk workspace.

Complete a coherent static talk first. For each optional animation, read `references/animation-patterns.md` and answer:

1. Does it explain order, correspondence, local detail, or physical time?
2. What new information appears after each action?
3. How does a static export preserve the full meaning?

Prefer a **stable base figure with changing emphasis** for complex methods. Keep coordinates, legends, and comparison baselines fixed. A short fade can be an initial transition choice; approximately 0.2–0.5 seconds is a design starting point, not a scientific requirement.

Never change data to make an animation attractive. Interpolating between separate experiments is not observed temporal evolution. Label illustrative motion; label real sequences with time units, sampling or playback information. Avoid counters, bouncing charts, and decorative particles that exaggerate an effect.

When helpful for defense questions, provide a direct link to a specific backup figure and a return link. This is an optional discussion path, not a replacement for the linear talk. Verify links and keep the main narrative understandable in a static export.

If a tool cannot implement or verify an effect, use a numbered static layout or discrete step pages and state the implemented scope. Added pages must respect the user's limit. Animation instructions alone are not implemented animation. Beamer overlays are successive PDF states, not PowerPoint-style continuous motion.

**Output of this phase**: the editable/source deck and requested speaking notes. An outline-only request does not require a presentation file.

### Phase 5 · Validate the Argument and the Actual Artifact

Read `references/quality-checklist.md`. Check claims and sources before appearance, then verify figures, timing, build states, and export. Compare key values, conditions, and wording against the owning material.

Repeat the Phase 2 logic check on the actual final slide sequence, including inserted pages and section boundaries. Check that explanations survived layout edits and static export, added pages preserve the argument and budget, and the closing answer follows from evidence shown in the main talk. Repair any remaining gaps before delivery. This is an agent reasoning task; passing the optional JSON checker does not perform it.

Render and inspect every delivered page. Inspect important intermediate states when using reveals. Static rendering does not prove playback in another viewer. For Beamer, compile and inspect both the presentation and complete handout; count frames and exported pages separately.

Missing evidence permits a clearly marked draft or a question/plan formulation. It does not permit a verified-result claim. Report consequential unverified items honestly.

Complex talks may optionally use a structured storyboard:

```bash
python scripts/check_plan.py path/to/storyboard.json
```

See [the runnable example](assets/storyboard.example.json). The checker validates structure, evidence references and status, timing, and static fallback fields. It does not verify scientific facts, source authenticity, layout, or playback. Do not manufacture JSON solely to check a small edit.

When changing this Skill, use [the scenario suite](evals/scenarios.md) to assess behavior across different research tasks. Mechanical checks alone do not establish narrative quality. Record which scenarios were actually run; do not claim an A/B benefit without an actual comparison.

**Delivery**: the requested files, a brief account of the central argument, and limitations that affect use. Keep production records out of scientific content. Include storyboards, ledgers, and checks when requested or needed for reuse.

## Example Requests

> Use $academic-ppt-storytelling to turn this paper into a 12-minute English lab-meeting talk. Deliver editable PowerPoint slides and distinguish the authors' conclusions from my critique.

> Use $academic-ppt-storytelling to create a 15-frame proposal with the bundled SJTUBeamer LaTeX template. Deliver the source and a complete handout PDF. No formal results are available.

> Use $academic-ppt-storytelling to reorganize this deck while retaining its template and total page count. Repair the evidence chain, titles, and transitions before adding progressive emphasis.

> Use $academic-ppt-storytelling to present these inconclusive experiments. Explain what the tests exclude, what remains uncertain, and which next test distinguishes the competing explanations.

## Provenance

The concise introduction, phased workflow, decision maps, pattern library, and repair checklist were inspired by [rgzn7/stunning-landing-page](https://github.com/rgzn7/stunning-landing-page), reviewed on 2026-11-22. Scientific constraints and this implementation were written for academic communication; no website animation code is included. The original project's [MIT notice](LICENSE) is retained. The bundled SJTUBeamer dependencies have separate notices in [THIRD-PARTY-NOTICES.md](assets/sjtubeamer-template/THIRD-PARTY-NOTICES.md); they are not relicensed by this Skill.
