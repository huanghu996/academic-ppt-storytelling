# Academic SJTUBeamer Starter

An English, 16:9 academic presentation starter using the real GitHub SJTUBeamer theme. The required theme runtime files are included locally; no GitHub fetch is needed during compilation.

## Build

Use a TeX distribution with Beamer, TikZ, tcolorbox, and XeLaTeX, such as an appropriately provisioned TeX Live installation. From this folder:

```bash
latexmk -xelatex main.tex
latexmk -xelatex handout.tex
```

If `latexmk` is unavailable, run `xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex` twice, and repeat for `handout.tex`.

For Overleaf, upload the entire folder, select XeLaTeX, and choose `main.tex` or `handout.tex` as the main document. No shell escape, Biber, external images, or system-specific fonts are required by this starter.

## Edit

- Replace the metadata and bracketed instructional text in `main.tex`.
- Add an actual evidence figure as `figures/key-evidence.pdf`, or change the filename. Until then, the source shows an explicit empty figure slot and compiles without a missing-file error.
- Replace the generic error definition if it does not describe the study. Do not treat the template's content as scientific evidence.
- Change `min,red,light,en,default` in `\usetheme` only as needed. Upstream provides additional cover and theme options.
- Maintain source locations, units, sampling definitions, and limits when replacing content.

## Overlays and static use

There are **9 logical frames**, including the cover and one backup frame. The design frame has two overlay states, so `main.pdf` has **10 pages**; `handout.pdf` has **9 pages** with the complete static content. These are deliberate examples, not a required talk length.

The metric-details button links from the design frame to the backup; the backup has a return link. The linear talk remains readable without using them. PDF-viewer keyboard and link support can vary.

Beamer overlays are discrete pages. They do not implement continuous PowerPoint animation. Use `handout.tex` when the required delivery count means one static page per frame.

## Files and provenance

`main.tex` is the editable presentation source. `handout.tex` reuses that source in handout mode. `latexmkrc` selects a local XeLaTeX build. The `.sty` files and `vi/` assets are unchanged upstream dependencies.

See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for the pinned GitHub source and separate licensing notices. For the full upstream manual and examples, use [the v3.2.0 release](https://github.com/sjtug/SJTUBeamer/releases/tag/v3.2.0).
