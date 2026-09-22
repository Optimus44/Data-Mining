# Chapter 3 Linear Regression Lab

This folder contains the practical R Markdown lab for the Linear Regression
topic in the Data Mining module.

## Contents

- [ch03_lab.Rmd](ch03_lab.Rmd) - lab source file.
- [ch03_lab.pdf](ch03_lab.pdf) - compiled lab submission.
- [ch03_lab.tex](ch03_lab.tex) - generated LaTeX source.
- `ch03_lab_files/` - figures generated during rendering.

## Topics Covered

The lab covers:

- simple and multiple linear regression
- confidence and prediction intervals
- residual and diagnostic plots
- interaction terms
- polynomial and other non-linear transformations
- qualitative predictors and dummy coding
- variance inflation factors
- writing a small reusable R function

## Datasets and Packages

The lab uses the `Boston` and `Carseats` datasets from `ISLR2`. It also loads
`MASS` and `car` for supporting statistical utilities and variance inflation
factor calculations.

Install the required packages in R if necessary:

```r
install.packages(c("MASS", "ISLR2", "car"))
```

## How to Run

1. Open [ch03_lab.Rmd](ch03_lab.Rmd) in RStudio.
2. Install any missing packages.
3. Run the code chunks in order or select **Knit** to regenerate the PDF and
   LaTeX output.

The `Boston` dataset is accessed as `ISLR2::Boston` in the lab because its
location differs between editions of *An Introduction to Statistical Learning*.

See the [Chapter 3 README](../README.md) for the overview of the chapter
materials.
