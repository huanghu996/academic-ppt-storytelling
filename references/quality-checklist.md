# Quality Checks: Argument, Explanation, and Artifact

Record **passed / needs correction / unverified / not applicable**, with a concrete reason. A high aggregate score cannot compensate for missing evidence.

## A. Delivery blockers

Any failed item prevents describing the result as a fully verified academic presentation. Correct fixable problems. When required evidence is unavailable, deliver only a clearly identified draft and its consequential gaps.

- [ ] **Facts and provenance**: major scientific claims have precise sources; no invented values, citations, significance, replicate counts, or mechanism evidence.
- [ ] **Inference strength**: titles, annotations, and explanations remain within the evidence. Hypothesis, interpretation, author claim, and presenter's assessment are distinguishable.
- [ ] **Figure meaning**: units, reference, axes, scales, masks, normalization, and interval definitions retain their actual meaning.
- [ ] **Evidence status**: missing, unchecked, illustrative, or generated content is not presented as a confirmed finding.
- [ ] **Complete information**: consequential conditions and limits remain visible in the main talk and static version.
- [ ] **Logical continuity**: the central argument has no unexplained prerequisite or unsupported inference left between slides. Repairable gaps have been fixed; source-dependent gaps are explicitly identified in a draft.
- [ ] **Usable target artifact**: files exist, open, match the requested format and count, and retain readable essential content; editability claims are accurate.

## B. Argument and slide inspection

- [ ] Opening question, central evidence, and closing answer concern the same research problem.
- [ ] The audience task determines explanation depth, not just the palette or theme.
- [ ] A gap is supported by literature or diagnosis, or explicitly remains unverified.
- [ ] Each slide has a role and main point. Multi-panel figures serve the same question.
- [ ] Result titles are supported; setup titles can accurately name their subject.
- [ ] Necessary terms, comparison conditions, and notation precede the inference.
- [ ] Controls, counterexamples, and contrary outcomes appear where they affect interpretation.
- [ ] Training/validation/test, measurement/simulation/schematic, and time samples/independent repeats remain distinct.
- [ ] Transitions explain why the next question follows, with enough time to read and interpret central evidence.
- [ ] Every adjacent pair and section boundary has been checked against what the intended audience knows and what the next slide requires.
- [ ] Missing necessary explanations were automatically supplied by clarification, reordering, or substantive bridging slides; dividers and connective phrases did not substitute for them.
- [ ] Added or reorganized pages have a distinct purpose, traceable support or labeled reasoning, and valid incoming/outgoing relationships; count and time limits still hold.
- [ ] Paper discussions separate authors' claims and the presenter's critique; proposals do not contain fabricated findings.

## C. Visual and source inspection

- [ ] Aligned controls use consistent coordinates, scales, units, colors, and ordering; necessary exceptions are prominent.
- [ ] Relevant conditions and evidence status remain stable across successive states.
- [ ] Individual claims and figures have locatable sources on the slide, in notes, or the maintained ledger as appropriate.
- [ ] Labels, intervals, and consequential source lines are readable at intended display size.
- [ ] No clipped text, overlap, missing glyphs, broken figures, or cropped-away conditions.
- [ ] Emphasis follows the scientific point and uses more than color alone.
- [ ] Required editable objects or maintained source remain available; rasterized slides are not described as fully editable PowerPoint.
- [ ] Reused, redrawn, visually estimated, and generated material are identified correctly.

## D. Motion, interaction, and static completeness

- [ ] Each change performs an explanatory task and preserves the comparison baseline.
- [ ] Important intermediate states retain necessary labels and limitations.
- [ ] Condition switching is distinguished from real physical time; real sequences have units and playback information.
- [ ] Static delivery is complete. Extra states do not silently break a page limit.
- [ ] Media, builds, and optional backup links have been checked in the relevant output, or their unverified scope is stated.
- [ ] HTML content remains readable with reduced motion or unavailable dynamic resources.
- [ ] Beamer handouts merge builds without hidden information or overlapping alternatives; overlay states are described as discrete PDF pages.

## E. Timing and actual output

- [ ] Main-talk seconds fit the agreed speaking budget; Q&A and backups are handled separately.
- [ ] Reading time matches complexity. Important evidence is not rushed at the ending.
- [ ] All rendered pages were inspected, with closer review of dense figures, formulas, tables, and font substitutions.
- [ ] Counts, hidden pages, notes, media, links, and remaining placeholders match the actual delivery scope.
- [ ] For LaTeX, the log, logical frames, presentation PDF pages, and complete handout were checked separately.
- [ ] If rehearsal overruns, repeated background and side branches are removed before essential conditions or limits.

## F. Diagnose before polishing

| Symptom | Likely issue | Repair |
|---|---|---|
| Attractive page, unclear point | Title and figure answer different questions | State the point and align evidence; downgrade to a question if support is missing |
| Compelling story, weak support | Ledger or inference gap | Inspect the owning source and narrow the claim |
| Dense paper screenshot | Too many questions in one figure | Retain relevant panels and location; redraw from data when available |
| Method is clear but motivation is not | Design choices disconnected from hypothesis | Connect choices to the explanations they test |
| Slides make sense individually but the talk jumps between them | A prerequisite, design rationale, or comparison condition is missing | Audit the handoff; move or add the actual explanation, using a new page only when needed |
| Every slide competes for attention | No hierarchy or pacing | Remove branches and reserve interpretation time for central evidence |
| Many effects or incomplete export | Builds lack purpose or a static plan | Remove motion, use numbered annotations, or add permitted step pages |
| Backup navigation confuses the talk | Branches replace the linear argument | Keep main inference in the main talk and test short optional return paths |
| Ending consists of contribution slogans | Opening question unanswered | Give a concrete evidence-supported answer with conditions |

## G. Optional structural checker

From the Skill root:

```bash
python scripts/check_plan.py assets/storyboard.example.json
python scripts/check_plan.py path/to/storyboard.json --json
```

Exit `0`: no structural blockers. Exit `1`: blockers found. Exit `2`: file-read or JSON-parse failure. Warnings can coexist with exit `0` and must be reviewed.

Checks cover required fields, duplicate IDs, dangling evidence references, findings/interpretations without usable evidence, misuse of missing/illustrative evidence, main-time overrun, an optional total-entry count, static fallbacks, and real-time labels. Supplied but unchecked sources generate warnings.

The checker does not inspect source truth, causal validity, logical continuity between slides, statistical power, chart/data correspondence, rendered layout, actual frame/page counts, or playback. The agent must perform the transition audit itself. Complete applicable scientific and artifact review even when the checker reports zero blockers.

## H. Skill-level scenario validation

After changing workflow decisions, run the relevant cases in [evals/scenarios.md](../evals/scenarios.md). Review the actual output for preserved intent, inference strength, audience adaptation, timing, and static completeness.

These are behavior scenarios, not established benchmark results. Record the cases and artifacts actually examined. Do not infer a narrative-quality improvement from field validation or claim an A/B performance gain without running a controlled comparison.
