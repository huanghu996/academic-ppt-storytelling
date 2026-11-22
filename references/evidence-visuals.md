# Evidence-Driven Visuals

Choose the relationship to inspect before choosing a chart. Each visual should compare, explain, locate, or define something relevant to the argument.

## 1. Match the visual to the question

| Audience needs to inspect | Useful forms | Preserve |
|---|---|---|
| Within-object differences | Paired points, difference plots, aligned images | Pairing, baseline, sampling unit, comparable display ranges |
| Values across conditions | Points with intervals, concise tables, bars when appropriate | Interval meaning, sample count, grouping, order |
| Continuous trends | Curves or scatter using actual coordinates | Units, sampling, uncertainty, fitting/interpolation status |
| Distribution and variation | Individual observations, boxes, density where justified | Observation versus summary, definitions, sample count |
| Spatial field differences | Aligned fields, difference maps, profiles | Coordinates, slice, mask, scale, units, subtraction direction |
| Method or mechanism | Input/output, process, relationship diagrams | Arrow semantics, variables, observed versus hypothesized links |
| Theoretical reasoning | Aligned derivation, geometric explanation, counterexample | Assumptions, notation, necessary equivalences |
| Disagreement in literature | Source-linked evidence matrix or grouped results | Source, conditions, methods, and evidence limitations |

Do not substitute decorative 3D bars, radar area, or large numbers for a comparison the audience needs to evaluate.

## 2. Preserve scientific meaning

- **Axes**: show units. Identify truncated or logarithmic scales. Length-encoded bars generally retain a zero baseline; explain exceptions. Similar layouts do not make different scales directly comparable.
- **Controls**: align field scales, views, and cropping. If separate scales are necessary, mark them prominently and do not use color alone to imply a quantitative comparison.
- **Variation**: identify SD, SE, confidence interval, or another range and its unit of replication. Never invent unavailable intervals.
- **Samples**: distinguish subjects, cases, geometries, records, frames, and seeds. Do not label correlated observations independent replicates.
- **Transformations**: record normalization, reference scales, smoothing, interpolation, filtering, resampling, and masking. Fitted curves are not original sampling locations.
- **Image handling**: do not crop away a counterexample or condition that changes interpretation. Locate detail views on the original image and retain context.
- **Sources**: associate each figure with a source and version. Identify redrawing and processing. Preserve applicable attribution and reuse conditions.

Every precise number must trace to data or an inspected source. A visually large difference does not automatically establish statistical or practical importance.

## 3. Organize a slide around inspection

Prefer one main visual, a descriptive or supported-result title, and a few annotations guiding attention. Multiple panels can share a legend and axes when they remain readable. Keep only table columns needed for the current comparison; put a complete table in a backup when appropriate.

Decide what the audience sees first, inspects next, and should retain. Use restrained emphasis. If a figure is too dense, remove irrelevant panels, separate questions, directly label curves, or redraw from actual data before reducing the whole slide's type size.

Stable visual identity means consistent object colors, label positions, and comparison conventions. It does not require decorative texture, glow, or a new palette on each slide.

## 4. Adaptable starting points

| Setting | Starting approach | Motion |
|---|---|---|
| General lab meeting or conference | Light background, dark text, large main figure, stable grid | Static with localized emphasis |
| Theory | Clear symbols and spacing, few emphasis colors | Reveal dependent steps while retaining assumptions |
| Imaging or field visualization | Background selected for the evidence, shared scales, spatial labels | Local detail or real recorded evolution |
| Institutional defense | User's required template and identity rules | Respect venue and device constraints |

For a two-object comparison, blue `#0072B2` and orange `#D55E00` are possible starting colors, supplemented by direct labels and line styles. Avoid red/green as the sole distinction. Select sequential, diverging, or cyclic maps according to variable meaning.

## 5. Editability and asset boundaries

With data, retain editable chart data and labels where the target format permits. Scientific raster evidence may remain an image, with surrounding labels and annotations editable. Explain limitations; a full-slide screenshot is not a fully editable PowerPoint.

For LaTeX, editability means maintained `.tex` sources and the data/figure sources actually available. A PDF does not become a native editable PowerPoint. Keep scientific plots in an appropriate plotting workflow and include their provenance.

Retain necessary source evidence even when it does not perfectly match the deck's style. AI imagery may explain a clearly labeled concept; it cannot fill gaps with invented experimental images, simulation fields, spectra, or microscopy.
