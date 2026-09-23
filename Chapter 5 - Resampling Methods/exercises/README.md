# Chapter 5 Exercises

This folder contains the completed Chapter 5 exercises for the Data Mining
module's Resampling Methods topic.

## Contents

- [ch05_exercises.Rmd](ch05_exercises.Rmd) - source R Markdown file.
- [ch05_exercises.pdf](ch05_exercises.pdf) - compiled exercise submission.
- [ch05_exercises.tex](ch05_exercises.tex) - generated LaTeX source.
- `ch05_exercises_files/` and `figure/` - figures generated during rendering.

## Exercises Covered

The document includes:

- Exercise 1: deriving the minimum-variance investment weight in a two-asset
  portfolio.
- Exercise 5: estimating logistic-regression test error with a validation set
  using the `Default` data.
- Exercise 9: using the bootstrap to estimate the mean, median, and 10th
  percentile of `Boston$medv`.

The explanations connect the computational results to the underlying
probability, variance, cross-validation, and bootstrap mathematics.

## Required R Packages

Install the required packages in R if necessary:

```r
install.packages(c("ISLR2", "boot"))
```

## How to Run

1. Open [ch05_exercises.Rmd](ch05_exercises.Rmd) in RStudio.
2. Install any missing packages.
3. Select **Knit to PDF** to regenerate the PDF and LaTeX output.

The document uses the shared preamble at `../../_common/preamble.tex` for the
common course cover page.
