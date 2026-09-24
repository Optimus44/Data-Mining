# Tree-Based Ensemble Learning Paper

This folder contains the written paper for Chapter 8, Tree-Based Methods.

## Paper

- [paper.tex](paper.tex) - LaTeX source file.
- [paper.pdf](paper.pdf) - compiled paper.
- `paper.toc` - generated table of contents data.
- `paper.aux`, `paper.fls`, `paper.fdb_latexmk`, `paper.log`, and `paper.out` -
  generated LaTeX and `latexmk` build files.

## Title and Scope

**From One Tree to Many: An Intuitive and Rigorous Guide to Tree-Based
Ensemble Learning**

The paper explains:

- decision trees as the building block for ensemble learning
- Bagging and the variance-reduction identity
- Random Forests and feature-level randomisation
- out-of-bag estimation
- AdaBoost and its observation-weight update
- Gradient Boosting as functional gradient descent
- XGBoost and regularised boosted trees
- practical differences between Bagging, Random Forests, and Boosting

The paper uses equations, examples, comparison tables, and TikZ diagrams to
connect the intuition to the formal mathematics.

## Format

The paper follows the course format:

- 12-point A4 article layout
- one-inch margins
- 1.5 line spacing
- shared course cover page from `../../_common/preamble.tex`
- Roman-numbered table of contents followed by Arabic-numbered main text

## Required LaTeX Packages

The document requires a LaTeX installation with the following packages:

- `amsmath`, `amssymb`, and `amsthm`
- `graphicx`
- `booktabs`
- `tikz`
- `hyperref`
- `algorithm` and `algpseudocode`
- `natbib`
- `xcolor`
- `enumitem`
- `setspace`

## How to Compile

From this directory, run:

```bash
latexmk -pdf -interaction=nonstopmode paper.tex
```

Alternatively, open [paper.tex](paper.tex) in an editor such as TeXShop or
VS Code and compile it with `pdflatex`. The shared preamble path assumes the
paper remains inside this directory.
