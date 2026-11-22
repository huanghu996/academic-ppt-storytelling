# LaTeX Route: SJTUBeamer

Use the real [sjtug/SJTUBeamer](https://github.com/sjtug/SJTUBeamer) GitHub project. The bundled starter pins release [v3.2.0](https://github.com/sjtug/SJTUBeamer/releases/tag/v3.2.0), commit `b3dcba72d80892c7d2558e1bf838d4c298d910bd`; it is not a hand-drawn imitation of that theme.

## 1. Copy the complete starter

Copy [assets/sjtubeamer-template](../assets/sjtubeamer-template/README.md) into the talk workspace, including its `.sty` files, `vi/`, and notices. Edit `main.tex`, not the Skill's reusable copy. The theme runtime is local, so a build needs no GitHub download. A suitably provisioned TeX distribution is still required.

The new English starter uses `beamer`, `aspectratio=169`, and `\usetheme[min,red,light,en,default]{sjtubeamer}`. It avoids system-specific fonts, external code execution, and a bibliography processor. User-selected templates and theme options take priority over these defaults.

## 2. Compile both reading modes

From the copied starter directory:

```bash
latexmk -xelatex main.tex
latexmk -xelatex handout.tex
```

If needed, run XeLaTeX twice per document:

```bash
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

Repeat with `handout.tex`. The local `latexmkrc` uses XeLaTeX without shell escape. Do not enable shell escape merely to compile this starter. Overleaf users should upload the whole directory and select XeLaTeX.

For Chinese content later, switch deliberately to an appropriate `ctexbeamer` configuration and verify its fonts; English Skill documentation does not restrict the user's slide language. Do not add an untested operating-system-specific font set as a universal requirement.

## 3. Implement the narrative in source

The starter follows question, available evidence, hypothesis, design, evidence, limits, and answer. Replace or merge frames according to the actual talk; it is not a mandatory chapter list.

Use explicit frame titles, short source lines, and native math. Keep critical conditions in the body; source comments and Beamer notes cannot replace visible limitations. The figure helper compiles an honest empty slot until an actual figure is supplied. It never synthesizes research data.

For a stable figure with a later explanation:

```latex
\begin{frame}{Matched comparison}
  % Keep the complete comparison and its units visible from the start.
  \includegraphics[width=.75\textwidth]{figures/verified-comparison.pdf}
  \uncover<2->{\par State the supported difference and its conditions.}
\end{frame}
```

This snippet requires an actual figure at the named path; the starter's `\evidencefigure` helper handles a missing figure explicitly. `\uncover` reserves layout space and reveals a discrete PDF state. Avoid overlapping `\only` alternatives unless the handout explicitly selects a complete, non-overlapping version.

## 4. Add optional discussion paths

```latex
\begin{frame}[label=main-result]{Main result}
  % Evidence and conditions remain here.
  \hyperlink{backup-proof}{\beamerbutton{Proof details}}
\end{frame}
\begin{frame}[label=backup-proof]{Backup proof}
  % Additional reasoning, with assumptions.
  \hyperlink{main-result}{\beamerbutton{Return to result}}
\end{frame}
```

Test both destinations in the produced PDF. Keep the talk understandable if links are not used. Do not scatter navigation controls over every page.

## 5. Count and validate the correct artifact

The provided starter has **9 frames**, including the cover and backup; the two-state design frame makes **10 presentation PDF pages**. Handout mode gives **9 complete pages**. It suppresses SJTUBeamer's automatic part page at the appendix so that backup pages are explicit.

After content changes, recount from the actual output. A requested exact slide count must be interpreted consistently as frames, handout pages, or exported presentation pages. The optional JSON checker counts storyboard entries, not actual overlay pages.

Inspect the build log for errors, undefined references, missing glyphs, and overfull boxes. Render all output pages and inspect the intermediate state. Verify the source's empty figure slot, equation, table, hyperlinks, and complete handout. Compilation alone is insufficient visual review.

## 6. Troubleshooting

| Symptom | Check | Fix |
|---|---|---|
| `beamerthemesjtubeamer.sty` missing | Working directory and copied files | Copy the entire starter, not only `main.tex` |
| Missing `vi/...` file | Identity asset directory | Preserve the bundled `vi/` paths |
| A TeX package is missing | Distribution package availability | Install the named package through that distribution; do not rewrite the theme to conceal the error |
| Extra PDF pages | Overlays and automatic divider frames | Review frame/page counts; remove unneeded hooks or use handout mode |
| Handout text overlaps | Mutually exclusive overlay content | Select a handout-specific variant or use numbered static annotations |
| Long title or table overflows | Actual rendered frame | Shorten, split, or simplify before shrinking the whole page |
| Broken backup return | Named frame destinations | Verify labels and actual PDF link targets |

## 7. Provenance and delivery

Deliver maintained `.tex` sources, required figures/data sources actually available, dependencies or a precise dependency description, and the compiled PDF. Include both presentation and handout when both are requested; explain their page-count difference.

Keep [THIRD-PARTY-NOTICES.md](../assets/sjtubeamer-template/THIRD-PARTY-NOTICES.md) and upstream notices. Theme code and institutional identity assets have different terms. Do not claim affiliation or relicense upstream assets as part of the Skill's MIT notice.
