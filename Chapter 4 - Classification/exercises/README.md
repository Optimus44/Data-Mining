# Chapter 4 Exercises

This folder contains the completed Chapter 4 exercises for the Data Mining
module's Classification topic.

## Contents

- [ch04_exercises.Rmd](ch04_exercises.Rmd) - source R Markdown file.
- [ch04_exercises.pdf](ch04_exercises.pdf) - compiled exercise submission.
- [ch04_exercises.tex](ch04_exercises.tex) - generated LaTeX source.
- `ch04_exercises_files/` - figures generated during rendering.

## Exercises Covered

The document includes:

- Exercise 5: comparing LDA and QDA under linear and non-linear Bayes
  decision boundaries.
- Exercise 10: deriving the LDA log-odds formula when there is one predictor.
- Exercise 14: predicting high or low `mpg` for the `Auto` data.
- Exercise 16: predicting high or low crime rate for the `Boston` data.

## Required R Packages

The exercises use the following R packages:

```r
install.packages(c("ISLR2", "MASS", "class", "e1071"))
```

The document uses `ISLR2::Boston` explicitly to avoid ambiguity with the
`Boston` dataset exported by `MASS`.

## How to Run

1. Open [ch04_exercises.Rmd](ch04_exercises.Rmd) in RStudio.
2. Install any missing packages.
3. Run the code chunks in order or select **Knit** to regenerate the PDF and
   LaTeX output.
