# AGENTS.md

Instructions for AI agents working in this repository.

## Embedding YouTube videos in Markdown

GitHub strips `<iframe>` tags from rendered Markdown, so a real embedded
player is not possible. The convention in this repo is a **clickable
thumbnail** that links out to YouTube:

```
[![Título del vídeo](https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg)](https://www.youtube.com/watch?v=VIDEO_ID "Título del vídeo")
```

- `https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg` is YouTube's official
  thumbnail CDN and works for any valid video ID without needing scraping.
- **Never guess or fabricate a `VIDEO_ID`.** Only use IDs confirmed via an
  actual web search result (a real URL you observed), never invented from
  memory — a wrong ID silently links to an unrelated or nonexistent video.
- Prefer well-known, reputable educational channels for the subject.

## Math notation convention (GitHub Flavored Markdown)

All `.md` files in this repo must use **GitHub's supported math syntax** for LaTeX
expressions, per the official docs:
https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions

- **Inline math:** wrap the expression in single dollar signs.
  ```
  This sentence uses `$` delimiters to show math inline: $\sqrt{3x-1}+(1+x)^2$
  ```
- **Block math:** start a new line and wrap the expression in double dollar signs
  (`$$`), each on its own line.
  ```
  $$
  \lim_{x\to2}(3x^2-5x+4)
  $$
  ```
- Do **NOT** use LaTeX-only delimiters `\(...\)` (inline) or `\[...\]` (block) —
  GitHub does not render these. Always use `$...$` and `$$...$$` instead.
- To show a literal `$` inside a math expression, escape it: `\$`. Outside a math
  expression on the same line, wrap it in `<span>$</span>`.

When creating or editing any markdown file in this repo, follow this convention
consistently. If you find `\(`, `\)`, `\[`, or `\]` used as math delimiters in
existing files, convert them to `$` / `$$`.

- **Avoid wrapping inline math in redundant literal parentheses**, especially
  inside bold/italic text — e.g. `**...($Q(x)$)...**` renders oddly. Just
  write `**...$Q(x)$...**` without the extra `(` `)` around the `$...$` span.

## Generating graphs / Cartesian plane images

GitHub Markdown (MathJax) can render math **notation**, but it cannot draw
graphs or plots. Any Cartesian-plane graph or function drawing must be
generated as a **static PNG image** with Python (matplotlib) and embedded with
standard Markdown image syntax — never attempt to "draw" a graph using math
delimiters, Mermaid, or ASCII art.

### Setup

A local venv already exists at `.venv/` with `matplotlib` and `numpy`
installed. Reuse it instead of creating a new one:

```
source .venv/bin/activate
```

If it doesn't exist yet:

```
python3 -m venv .venv && source .venv/bin/activate
pip install matplotlib numpy
```

### Where things live

- Script that generates all graphs: [scripts/generate_graphs.py](scripts/generate_graphs.py)
- Output images:
  - `calculo1/limites/img/` — graphs for the exam/solutions/theory (e.g. `ejercicio1.png`)
  - `calculo1/limites/pre-saberes/img/` — graphs for prerequisite/function-type docs (e.g. `lineal.png`)

### Adding a new graph

1. Add a new plotting block to `scripts/generate_graphs.py` following the
   existing pattern: use the `new_axes(xlim, ylim, title)` helper to create
   consistent axes (with x/y axis lines and grid), plot the function, mark
   any asymptote (vertical with `ax.axvline`, horizontal with `ax.axhline`,
   dashed, red for asymptotes / green for horizontal asymptotes) or "hole"
   (open circle marker), then save with `save(fig, "<path>.png")`.
   - Split the domain into separate `np.linspace` ranges around any
     discontinuity/asymptote so matplotlib doesn't draw a vertical line
     connecting the two branches.
2. Re-run the script to regenerate **all** images (fast, safe to re-run):
   ```
   source .venv/bin/activate && python3 scripts/generate_graphs.py
   ```
3. Embed the image in the relevant `.md` file(s) using a relative path from
   that file's own directory, e.g.:
   ```
   ![Gráfica del Ejercicio N](img/ejercicioN.png)
   ```
4. View the generated PNG (e.g. with the image-viewing tool) to sanity-check
   the plot before considering the task done.

## Generating explanatory animations with Manim

Use a GIF only when motion clarifies a changing quantity, an approach from two
sides, or a sequence of algebraic transformations. Keep static definitions and
single-state graphs as PNGs.

- Generator: [scripts/generate_animations.py](scripts/generate_animations.py)
- Final output: `calculo1/limites/animaciones/`
- Intermediate Manim files: `.manim-media/` (ignored by Git)

Install the Python dependencies from `requirements.txt`. On macOS, the Manim
runtime also needs `cairo`, `pango`, and `ffmpeg` (available through Homebrew).
Generate every animation with:

```bash
.venv/bin/python scripts/generate_animations.py
```

Embed a GIF with a relative path from the Markdown document, add descriptive
alternative text, and reuse an animation when it explains the same concept in
several documents. Before finishing, inspect frames from the beginning, middle,
and end to catch clipped labels, overlap, or points leaving the axes.
