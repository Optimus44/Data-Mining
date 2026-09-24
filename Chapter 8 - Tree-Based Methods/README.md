# Chapter 8 - Tree-Based Methods

This folder contains the Chapter 8 practical lab and written paper for the
Tree-Based Methods topic in the Data Mining module.

## Overview

The materials develop decision trees from a single interpretable model to
ensemble methods that improve stability and predictive performance. The
chapter covers classification and regression trees, pruning, Bagging, Random
Forests, Boosting, and Bayesian Additive Regression Trees.

## Directory Contents

### Lab

The [lab](lab/) folder contains the textbook Chapter 8.3 lab, “Decision
Trees”:

- [ch08_lab.Rmd](lab/ch08_lab.Rmd) - lab source file.
- [ch08_lab.pdf](lab/ch08_lab.pdf) - compiled lab submission.
- [ch08_lab.tex](lab/ch08_lab.tex) - generated LaTeX source.
- `lab/figure/` - figures generated during rendering.

The lab uses `Carseats` for classification trees, `Hitters` for regression
trees, and `Boston` for Bagging, Random Forests, Boosting, and BART.

### Written Paper

The completed written paper is in [paper on boosting, random forest and
bagging](paper%20on%20boosting,%20random%20forest%20and%20bagging/):

- [paper.tex](paper%20on%20boosting,%20random%20forest%20and%20bagging/paper.tex) - LaTeX source file.
- [paper.pdf](paper%20on%20boosting,%20random%20forest%20and%20bagging/paper.pdf) - compiled paper.
- [paper README](paper%20on%20boosting,%20random%20forest%20and%20bagging/README.md) - paper-specific instructions.

The paper gives an intuitive and mathematical treatment of Bagging, Random
Forests, AdaBoost, Gradient Boosting, XGBoost, out-of-bag estimation, and model
selection considerations.

The older [paper on boosing, and bagging](paper%20on%20boosing,%20and%20bagging/)
directory is retained as an earlier source location. The newer directory above
is the organized paper location and should be used for the current submission.

## Required R Packages

Install the packages required by the lab in R if necessary:

```r
install.packages(c("ISLR2", "tree", "randomForest", "gbm", "BART"))
```

The written paper requires a LaTeX installation with packages including
`amsmath`, `booktabs`, `tikz`, `natbib`, `algorithm`, `algpseudocode`, and
`setspace`.

## How to Run

To regenerate the lab, open [ch08_lab.Rmd](lab/ch08_lab.Rmd) in RStudio and
select **Knit to PDF**. This produces the `.tex` and `.pdf` files in the lab
directory.

To compile the paper, open a terminal in the paper directory and run:

```bash
cd "paper on boosting, random forest and bagging"
latexmk -pdf -interaction=nonstopmode paper.tex
```

Both documents use the shared course preamble at `../_common/preamble.tex` for
the lab and `../../_common/preamble.tex` for the paper.

## Course Information

- Course: Data Mining
- Course code: MSDA 9124
- Programme: MSc Big Data Analytics
- Institution: Adventist University of Central Africa
- Student: Wayne Rubangisa
- Student ID: 101220
