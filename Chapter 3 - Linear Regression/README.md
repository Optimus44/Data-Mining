# Chapter 3 - Linear Regression

This folder contains the Chapter 3 exercises and practical lab for the Linear
Regression topic in the Data Mining module.

## Overview

The materials cover how to build, interpret, and evaluate linear regression
models in R. They include conceptual and applied exercises, simple and
multiple regression, diagnostics, interaction terms, polynomial
transformations, and qualitative predictors.

## Directory Contents

### Exercises

The [exercises](exercises/) folder contains three completed exercises from
Chapter 3:

- [chapter03_exercises.Rmd](exercises/chapter03_exercises.Rmd) — source R Markdown file.
- [chapter03_exercises.pdf](exercises/chapter03_exercises.pdf) — compiled exercise submission.
- [chapter03_exercises.tex](exercises/chapter03_exercises.tex) — generated LaTeX source.

The exercises address null hypotheses in multiple regression, the least
squares line, and regression through the origin.

### Lab

The [lab](lab/) folder contains the practical R Markdown lab and its generated
outputs:

- [ch03_lab.Rmd](lab/ch03_lab.Rmd) — lab source file.
- [ch03_lab.pdf](lab/ch03_lab.pdf) — compiled lab submission.
- [ch03_lab.tex](lab/ch03_lab.tex) — generated LaTeX source.
- `ch03_lab_files/` — figures generated during rendering.

## Topics Covered

- Simple linear regression
- Multiple linear regression
- Interaction terms
- Non-linear transformations of predictors
- Qualitative predictors
- Confidence and prediction intervals
- Residual and leverage diagnostics
- ANOVA comparisons for nested models
- Basic R function writing

## Datasets Used in the Lab

The lab uses datasets supplied by the following R packages:

- `Boston` from `ISLR2`
- `Carseats` from `ISLR2`

The lab also loads `MASS` for supporting statistical utilities and `car` for
variance inflation factor calculations.

## Prerequisites

Make sure the necessary packages are installed in R:

```r
install.packages(c("MASS", "ISLR2", "car"))
```

## How to Run

1. Open [ch03_lab.Rmd](lab/ch03_lab.Rmd) or
	[chapter03_exercises.Rmd](exercises/chapter03_exercises.Rmd) in RStudio.
2. Install any missing packages if required.
3. Run the code chunks in order or click **Knit** to regenerate the PDF and
	LaTeX output.

## Learning Objectives

By the end of this lab, the learner should be able to:

- fit simple and multiple linear regression models using `lm()`
- interpret coefficients and model summaries
- compare models and test improvements using ANOVA
- assess model assumptions through residual analysis
- include interaction and polynomial terms in the model
- work with categorical predictors and interpret dummy coding
- understand regression hypotheses and least squares properties
- fit and interpret a regression model through the origin

## Author

Wayne Rubangisa

## Date

2026-08-16
