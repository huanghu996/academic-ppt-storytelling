# Academic Storytelling

**Make the scientific argument visible.**

An AI-agent Skill for turning research into clear academic presentations, with evidence-driven visuals and restrained animation. Supports PowerPoint, LaTeX Beamer, and presentation outlines through the agent's available tools.

## The core idea

**Problem → Gap → Insight → Method → Evidence → Boundary → Takeaway**

1. **Problem** — Open with a concrete phenomenon or failure case.
2. **Gap** — Establish what is missing through literature or diagnostic evidence.
3. **Insight** — State the hypothesis and the observation behind it.
4. **Method** — Explain how the design addresses the hypothesis.
5. **Evidence** — Make the decisive comparison the talk's **Signature Moment**.
6. **Boundary** — Show where the conclusion holds and where it fails.
7. **Takeaway** — Answer the opening question and identify what remains open.

Each slide has one main point, appropriate evidence, and a reason to lead into the next. Adapt the structure to proposals, theory, and inconclusive results without inventing findings.

## Start with

Copy this prompt to your agent:

```text
Clone https://github.com/huanghu996/academic-ppt-storytelling into your Skills directory, read SKILL.md, use $academic-ppt-storytelling to create my academic presentation, and report reproducible bugs in the repository's issues.
```

## Included

- [Complete Skill](SKILL.md) and eight reference guides.
- Slide-by-slide planning and an optional [storyboard checker](scripts/check_plan.py).
- [SJTUBeamer starter](assets/sjtubeamer-template/README.md), with source and compiled previews.

File generation requires suitable authoring tools; LaTeX compilation requires a TeX distribution.

## Credits and license

Inspired by [stunning-landing-page](https://github.com/rgzn7/stunning-landing-page). LaTeX theme: [SJTUBeamer](https://github.com/sjtug/SJTUBeamer).

Skill instructions and helper code: [MIT](LICENSE). Bundled theme and identity assets retain their [separate terms](assets/sjtubeamer-template/THIRD-PARTY-NOTICES.md).
