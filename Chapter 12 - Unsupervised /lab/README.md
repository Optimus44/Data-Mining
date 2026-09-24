# Chapter 12 Unsupervised Learning Lab

This folder contains the practical Chapter 12 lab from *An Introduction to
Statistical Learning*, adapted to the course submission format.

## Contents

- [ch12_lab.Rmd](ch12_lab.Rmd) - lab source file.
- [ch12_lab.tex](ch12_lab.tex) - generated LaTeX source.
- [ch12_lab.pdf](ch12_lab.pdf) - compiled lab submission.
- `figure/` - figures generated during rendering.

## Topics Covered

The lab explains and applies:

- principal component analysis (PCA)
- explained variance and PCA loadings
- hierarchical clustering with complete, average, and single linkage
- dendrograms and cutting hierarchical trees
- $K$-means clustering and the within-cluster sum of squares
- elbow plots and the choice of $K$
- PCA and clustering for the `USArrests` data
- high-dimensional PCA and clustering for the `NCI60` gene-expression data

## Required R Package

Install `ISLR2` if necessary:

```r
install.packages("ISLR2")
```

The lab uses base R functions for PCA and clustering, including `prcomp()`,
`hclust()`, `cutree()`, and `kmeans()`.

## How to Run

1. Open [ch12_lab.Rmd](ch12_lab.Rmd) in RStudio.
2. Install any missing packages.
3. Select **Knit to PDF** to regenerate the PDF and LaTeX output.

The document uses the shared course preamble at `../../_common/preamble.tex`
for the standard cover page.
