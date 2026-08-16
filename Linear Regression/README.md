# Linear Regression Lab

This folder contains the practical lab for the Linear Regression topic in the Data Mining module.

## Overview

The lab focuses on learning how to build, interpret, and evaluate linear regression models in R. It introduces both simple and multiple regression techniques, along with diagnostics and extensions such as interaction terms and polynomial transformations.

## Files

- [Lab - Linear Regression.Rmd](Lab%20-%20Linear%20Regression.Rmd) — main R Markdown document containing the exercises and code.

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

## Datasets Used

This lab uses built-in datasets from the following R packages:

- `Boston` from the `MASS` package
- `Carseats` from the `ISLR2` package

## Prerequisites

Make sure the necessary packages are installed in R:

```r
install.packages(c("MASS", "ISLR2", "car"))
```

## How to Run

1. Open [Lab - Linear Regression.Rmd](Lab%20-%20Linear%20Regression.Rmd) in R Studio.
2. Install any missing packages if required.
3. Run the code chunks in order or click Knit to generate the HTML output.

## Learning Objectives

By the end of this lab, the learner should be able to:

- fit linear regression models using `lm()`
- interpret coefficients and model summaries
- compare models and test improvements using ANOVA
- assess model assumptions through residual analysis
- include interaction and polynomial terms in the model
- work with categorical predictors and interpret dummy coding

## Author

Wayne Rubangisa

## Date

2026-08-16
