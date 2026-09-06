# AGENTS.md

Instructions for AI agents working in this repository.

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
