# Chapter 8 Tree-Based Methods Lab

This folder contains the Chapter 8.3 lab from *An Introduction to Statistical
Learning*, adapted to the course submission format.

## Contents

- [ch08_lab.Rmd](ch08_lab.Rmd) - lab source file.
- [ch08_lab.pdf](ch08_lab.pdf) - compiled lab submission.
- [ch08_lab.tex](ch08_lab.tex) - generated LaTeX source.
- `figure/` - figures generated during rendering.

## Topics Covered

The lab follows the textbook sequence:

- classification trees with `Carseats`
- cross-validation and pruning
- regression trees with `Hitters`
- Bagging with the `Boston` data
- Random Forests and variable importance
- Gradient Boosting
- Bayesian Additive Regression Trees (BART)
- test-set MSE comparisons

## Required R Packages

Install the required packages in R if necessary:

```r
install.packages(c("ISLR2", "tree", "randomForest", "gbm", "BART"))
```

## How to Run

1. Open [ch08_lab.Rmd](ch08_lab.Rmd) in RStudio.
2. Install any missing packages.
3. Select **Knit to PDF** to regenerate the PDF and LaTeX output.

The document uses the shared preamble at `../../_common/preamble.tex` for the
common course cover page.
