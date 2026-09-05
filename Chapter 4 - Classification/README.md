# Credit Approval Classification

## Project Overview
This project focuses on binary classification using the UCI Credit Approval dataset, with the goal of predicting whether a credit application should be approved or rejected. The work is implemented in two separate notebook-based analyses:

- A classical machine learning approach using traditional classifiers
- A more advanced approach that extends the same task with a neural network model

The project explores a full data mining pipeline, including data preparation, exploratory analysis, preprocessing, model training, cross-validation, hyperparameter tuning, and final model comparison.

## Dataset
The dataset is the well-known Credit Approval dataset from the UCI Machine Learning Repository. It contains 690 records and 15 feature variables plus the class label.

### Key characteristics
- Target variable: approval status
- Positive class: approved applications
- Negative class: rejected applications
- Mixed attribute types:
  - continuous numeric variables
  - categorical variables with limited categories
  - some missing values
- Class distribution is reasonably balanced, with 44.5% approved and 55.5% rejected cases

The original dataset files are located in the `dataset/` folder and include the source metadata and prepared data files used throughout the notebooks.

## Objectives
The main objectives of this project are to:

1. Clean and prepare the credit approval dataset for classification.
2. Perform exploratory data analysis to understand the distribution of features and target classes.
3. Handle missing values, encode categorical features, and create a leakage-free preprocessing pipeline.
4. Train and evaluate classical classifiers such as Logistic Regression and Decision Tree.
5. Extend the analysis with a neural network model using a Multi-Layer Perceptron (MLP).
6. Compare models using validation metrics such as accuracy and F1-score.
7. Apply cross-validation and grid search to improve model performance and ensure robust evaluation.

## Project Structure

```text
Classification/
├── README.md
├── requirement.txt
├── dataset/
│   ├── credit.lisp
│   ├── credit.names
│   ├── crx.names
│   └── Index
├── notebooks/
│   ├── credit_approval_classical_lab2.ipynb
│   └── credit_approval_lab2.ipynb
└── prepared output files (generated during notebook execution)
```

## Notebook Descriptions

### 1. Classical Classification Notebook
File: `notebooks/credit_approval_classical_lab2.ipynb`

This notebook focuses on classical machine learning methods without neural networks. It includes:

- data loading and inspection
- missing value analysis
- preprocessing pipeline
- exploratory visualization
- Logistic Regression baseline
- Decision Tree classifier
- stratified 10-fold cross-validation
- grid search for model tuning
- performance comparison and final recommendation

### 2. Neural Network Classification Notebook
File: `notebooks/credit_approval_lab2.ipynb`

This notebook extends the same classification task by incorporating a neural network model. It includes:

- the same data preparation and exploratory steps
- imputation, categorical encoding, and scaling
- Logistic Regression baseline
- Multi-Layer Perceptron (MLP) classifier
- cross-validation and hyperparameter tuning
- comparison between classical and neural approaches

## Methodology
The workflow used in both notebooks follows a standard data mining pipeline:

1. Load the Credit Approval dataset.
2. Inspect feature types and missing values.
3. Create separate preprocessing for numerical and categorical columns.
4. Use training-only fitting to avoid data leakage.
5. Train baseline classifiers.
6. Evaluate performance on a held-out test set and through cross-validation.
7. Tune hyperparameters using grid search.
8. Compare model results using accuracy and F1-score.

This ensures that the reported model performance reflects realistic generalization rather than overly optimistic in-sample results.

## Required Libraries
The project dependencies are listed in `requirement.txt` and include the main Python data science stack:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn (if used in specific notebook runs)
- Jupyter Notebook / JupyterLab

To install dependencies:

```bash
pip install -r requirement.txt
```

## Running the Project
Open the notebooks in Jupyter Notebook or JupyterLab and execute the cells in order:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

Then open the notebook files in the `notebooks/` directory and run the analysis from top to bottom.

## Expected Outcome
The project is designed to compare the effectiveness of traditional classification algorithms against a neural-network-based model for credit approval prediction. In practice, the notebooks assess whether the added complexity of the neural model provides a measurable performance advantage over the classical baseline.

## Summary
This project demonstrates a complete classification workflow on a real-world financial dataset. It showcases both classical and deep-learning-oriented approaches, while emphasizing rigorous preprocessing, reproducible evaluation, and evidence-based model selection.

It is a strong example of applied data mining in a supervised learning context, especially for academic or coursework use in classification and model comparison.
