# Chapter 5 Resampling Methods Lab

This folder contains the practical R Markdown lab for Resampling Methods in the
Data Mining module.

## Contents

- [ch05_lab.Rmd](ch05_lab.Rmd) - lab source file.
- [ch05_lab.pdf](ch05_lab.pdf) - compiled lab submission.
- [ch05_lab.tex](ch05_lab.tex) - generated LaTeX source.
- `ch05_lab_files/` and `figure/` - figures generated during rendering.

## Topics Covered

The lab introduces and compares:

- the validation-set approach
- leave-one-out cross-validation (LOOCV)
- $k$-fold cross-validation
- the bootstrap
- training error versus test error
- model selection using resampling
- bootstrap estimates of regression coefficients and portfolio weights

## Datasets Used

The lab uses datasets supplied by `ISLR2`:

- `Auto` for polynomial regression and prediction-error estimation
- `Portfolio` for bootstrap estimates of portfolio weights

## Required R Packages

Install the required packages in R if necessary:

```r
install.packages(c("ISLR2", "boot"))
```

## How to Run

1. Open [ch05_lab.Rmd](ch05_lab.Rmd) in RStudio.
2. Install any missing packages.
3. Select **Knit to PDF** to regenerate the PDF and LaTeX output.

The document uses the shared preamble at `../../_common/preamble.tex` for the
common course cover page.
