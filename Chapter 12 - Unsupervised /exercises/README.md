# Chapter 12 Exercises

This folder contains the completed Chapter 12 exercises from *An Introduction
to Statistical Learning*.

## Exercises Covered

- Exercise 4, page 547: comparing the fusion heights of single-linkage and
  complete-linkage hierarchical clustering.
- Exercise 11, page 550: implementing Algorithm 12.1 for matrix completion and
  evaluating it on standardized `Boston` features.

Exercise 11 includes:

- an R implementation with relative-error and iteration-count tracking;
- a maximum-iteration safeguard and optional progress output;
- nested missingness levels from 5% to 30%;
- ranks $M=1,\ldots,8$;
- 10 repetitions of the experiment; and
- plots and tables of mean hidden-entry approximation error.

## Contents

- [ch12_exercises.Rmd](ch12_exercises.Rmd) - source R Markdown file.
- [ch12_exercises.tex](ch12_exercises.tex) - generated LaTeX source.
- [ch12_exercises.pdf](ch12_exercises.pdf) - compiled exercise submission.
- `figure/` - figures generated during rendering.

## Required R Package

Install `ISLR2` if necessary:

```r
install.packages("ISLR2")
```

The matrix-completion algorithm itself uses base R functions, including
`svd()`, so no additional matrix-completion package is required.

## How to Run

1. Open [ch12_exercises.Rmd](ch12_exercises.Rmd) in RStudio.
2. Install any missing packages.
3. Select **Knit to PDF** to regenerate the PDF and LaTeX output.

The document uses the shared course preamble at `../../_common/preamble.tex`
for the standard cover page.
