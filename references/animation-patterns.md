# Restrained Animation: One Change, One Explanatory Task

A static talk is a complete and valid choice. Add motion or reveal order only when it improves explanation.

## 1. Patterns and static alternatives

| Explanatory task | Pattern | Preserve | Static alternative |
|---|---|---|---|
| Parts of a complex architecture | Fixed base figure, sequential emphasis | Layout, object colors, input/output, overview | Numbered annotations on the complete diagram |
| Dependent reasoning | Reveal successive steps | Assumptions, symbols, previous key relationship | Numbered derivation with conditions visible |
| Two outcomes for the same object | Matched pair, shift the focus | Coordinates, scale, legend, object location | Side-by-side views and a difference plot |
| Local detail | Overview with a located detail window | Original position, scale, context | Overview and detail shown together |
| Information flow | Emphasize the current step on an existing path | Arrow meaning and process direction | Numbered process with input/operation/output |
| Real temporal evolution | Frames or video from an actual record | Time, units, scale, sampling/playback basis | Key frames with real timestamps |
| Interpretive synthesis | De-emphasize irrelevant details or add one annotation | Contrary evidence, limits, comparison baseline | Complete figure with a concise interpretation |

Fixed-context explanation adapts a useful idea from pinned web storytelling: keep spatial relationships stable while changing the object of attention. It does not require scrolling or a particular transition.

## 2. Write a build script

```text
Frame: Matched controls and data partitioning
Initial: Complete base diagram, legend, and "planned design" label visible.
Action 1: Emphasize training and validation objects; explain model selection.
Action 2: Emphasize independent test objects; state the definition of independence.
Action 3: Add matching-condition annotations without moving the objects.
End: Complete diagram and all consequential conditions remain readable.
Static: Same figure with numbered explanations; no color-only ordering.
```

One to three builds per slide is a useful starting point, not a quota. Longer derivations may need more. Do not turn every line into a click or remove necessary conditions merely to meet a count.

## 3. Control and timing

Prefer presenter-controlled changes for explanation. Ordinary reveals can start near 0.2–0.5 seconds; tune using actual playback. Do not apply elastic overshoot to values, axes, or legends. Moving an object must not imply that its measured value changed.

Real scientific sequences should support pause/replay where possible and identify units and playback rate. Prepare static key frames for export or equipment failure. HTML versions should retain complete readable content with reduced-motion settings.

## 4. Protect evidence semantics

Morphing between separate experiments is not measured evolution. Prefer discrete switching or a matched pair. If an illustrative interpolation is needed for teaching, label it clearly and do not describe intermediate states as observations.

Keep time on a real time-series axis. Label operating conditions when sequence means condition switching. Flowing arrows that explain information transfer must not be mistaken for measured transport speed or established causal propagation.

Avoid decorative particles, floating loops, typewriter text, and counting numbers as scientific emphasis. An actual particle-tracking record is different: it is evidence and needs its scientific labels.

## 5. Verify the implementation that exists

Distinguish implemented and playback-checked, implemented but unchecked, described only, and replaced with a static alternative. State material limitations accurately.

For Beamer, overlay specifications produce successive PDF pages. They can implement reveal and emphasis, not continuous PowerPoint motion. A handout merges the necessary content into a static page per frame. Check that mutually exclusive overlay content does not overlap in the handout. Fixed page limits may require numbered static layouts rather than extra pages.
