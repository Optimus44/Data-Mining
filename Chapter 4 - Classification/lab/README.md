# Chapter 4 Classification Lab

This folder contains the practical R Markdown lab for the Classification
topic in the Data Mining module.

## Contents

- [ch04_lab.Rmd](ch04_lab.Rmd) - lab source file.
- [ch04_lab.pdf](ch04_lab.pdf) - compiled lab submission.
- [ch04_lab.tex](ch04_lab.tex) - generated LaTeX source.
- `ch04_lab_files/` - figures generated during rendering.

## Topics Covered

The lab introduces and compares:

- logistic regression
- linear discriminant analysis (LDA)
- quadratic discriminant analysis (QDA)
- naive Bayes classification
- K-nearest neighbors (KNN)
- confusion matrices and classification accuracy
- training and test-set evaluation

## Datasets Used

The lab uses three datasets supplied by `ISLR2`:

- `Smarket` for predicting daily S&P 500 market direction
- `Caravan` for predicting caravan insurance purchases
- `Bikeshare` for classifying hourly bike-share demand

## Required R Packages

Install the required packages in R if necessary:

```r
install.packages(c("ISLR2", "MASS", "class", "e1071"))
```

## How to Run

1. Open [ch04_lab.Rmd](ch04_lab.Rmd) in RStudio.
2. Install any missing packages.
3. Run the code chunks in order or select **Knit** to regenerate the PDF and
   LaTeX output.
