# Implementation and Delivery

Resolve the target format before choosing tools or backend-specific guidance. Use tools appropriate to that format, read their documentation, and follow the applicable environment guidance. Tool availability alone does not determine the output format.

## 1. Route by the requested deliverable

| Request | Deliver | Working rule |
|---|---|---|
| New talk without an explicit format, including generic "slides" or "PPT" wording | Bundled SJTUBeamer `.tex` sources, assets, and compiled PDF | This is the default; read [sjtubeamer.md](sjtubeamer.md), copy the actual starter, and compile it |
| Explicit PowerPoint / `.pptx` request | Editable `.pptx` | Override the LaTeX default; preserve required text, tables, charts, and diagrams as editable objects where feasible |
| LaTeX/Beamer | Maintained `.tex` sources, necessary assets, compiled PDF | Use the bundled SJTUBeamer route unless the user chooses another theme; read [sjtubeamer.md](sjtubeamer.md) |
| In-place edit of an existing deck | The existing format unless conversion is requested | Preserve the user's editing target; source material alone does not set the output format |
| Outline or speaker script | Requested text/document | Include purpose, evidence locations, and transitions; do not expand into file production unnecessarily |
| PDF without a specified production format | Complete static PDF, using SJTUBeamer by default | Preserve an explicitly selected template; conditions and conclusions must remain visible without clicks; render every page |
| HTML presentation | Requested HTML package | Keyboard navigation, readable reduced-motion state, and agreed offline/export behavior |
| Existing cloud slides | The existing native destination or agreed export | Use connected capabilities without silently switching platform |

The word "PPT" used casually for an academic talk is not an explicit native-file requirement. Requests for a `.pptx`/`.ppt` file, a PowerPoint deliverable, or editing in PowerPoint are explicit and take priority. Retain another requested format or template, and keep outline-only tasks as outlines. State the SJTUBeamer default briefly and proceed without a format-confirmation question when no conflicting requirement exists.

For the default route, retain the actual theme and deliver maintained source plus compiled PDF. If the compiler or a dependency is unavailable, identify the specific build gap and deliver the available LaTeX source as uncompiled. Do not silently substitute `.pptx`, a different theme, or a screenshot-based imitation. A PDF is not a substitute when editable PowerPoint was explicitly requested.

## 2. Maintain sources and assets

Record the paper, dataset, image, and template versions. For a design template, inspect master layouts, aspect ratio, fonts, identity requirements, and page conventions. A deck supplied only as a content source does not automatically prescribe its design.

Associate evidence with ledger IDs. Preserve chart data, transformations, and available generation sources. Distinguish illustrative assets from scientific evidence.

Check the actual rendering of English, Chinese where required, Greek letters, subscripts, superscripts, and mathematical symbols. Prefer available fonts and describe any consequential target-device limitations.

## 3. Build in a useful order

1. Complete a readable static argument from the ledger and storyboard.
2. Create editable objects or maintained source appropriate to the target format.
3. Validate a representative complex page before repeating its layout.
4. Add only explanatory builds and provide a complete static version.
5. Export, render, inspect all pages, and correct errors before delivery.

If a tool cannot implement an object, choose a usable alternative and state the limit. Do not default to full-slide images or claim an unwritten file exists. If the target cannot be produced after reasonable reversible repair, deliver the completed work and identify the missing deliverable accurately.

## 4. Notes and citations

Keep conditions, limitations, and sources necessary for immediate judgment on the main page. Put fuller references, source locations, reading cues, and detailed methods in notes or source comments when appropriate. Notes must not hide a condition that changes the conclusion.

Use precise references: paper/version, figure/table/section, or dataset location. An unlinked pile of citations on the final page is insufficient provenance for individual claims.

## 5. Distinguish verification layers

| Layer | Establishes | Does not establish |
|---|---|---|
| File/object inspection | Existence, parseability, counts, some object types | Readability and absence of occlusion |
| Full visual rendering | Static layout, fonts, figure clarity, content completeness | Playback in a different viewer |
| Target-viewer playback/navigation | Build order, intermediate states, media, links | Scientific validity of the evidence |

Scientific verification still requires the source material. For Beamer, also separate frame count, overlay-page count, and handout-page count. Do not claim that compilation alone validates the talk.

## 6. Optional storyboard schema

The runnable [example](../assets/storyboard.example.json) uses integer `schema_version: 1`. Top-level fields are `mode`, `main_message`, `budget_seconds`, `evidence`, `slides`, and optional `expected_total_slides`.

- `mode`: `research`, `proposal`, `progress`, `review`, `theory`, or `teaching`.
- Evidence fields: `id`, `kind`, `status`, `source`, `scope`. Kinds: `empirical`, `literature`, `derivation`, `schematic`. Statuses: `verified`, `supplied`, `missing`, `illustrative`.
- Slide fields: `id`, `title`, `role`, `point`, `claim_type`, `evidence_ids`, `duration_seconds`, `in_main`, `visual`, `transition`, `boundary`, `animation`.
- `claim_type`: `setup`, `question`, `hypothesis`, `plan`, `finding`, `interpretation`, or `limitation`. `role` describes the purpose in ordinary language.
- Animation fields: `mode`, `steps`, `static_fallback`; mode is `none`, `reveal`, `highlight`, `zoom`, or `physical-time`. Real-time mode also requires `time_basis` describing units and sampling/playback. `steps` counts builds or a video-start action.

`verified` records an actual inspection by the creator; the checker does not inspect the source itself. Main-talk slides have `in_main: true`; backup durations estimate an answer if called upon and are excluded from the speaking budget.

`expected_total_slides` counts storyboard entries including backups. For Beamer, treat each entry as a logical frame and separately check exported PDF pages. If the user limits only the main talk, check that scope separately rather than misusing the total field.

The example is a five-minute proposal with no empirical results. Its empty evidence list is intentional. Passing structural checks establishes neither scientific evidence nor a completed deck.
