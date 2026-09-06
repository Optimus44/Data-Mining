# Agricultural Input Adoption and Household Profiling

A reproducible data-mining project using agricultural household survey microdata.

The project addresses two tasks:

1. **Classification:** predict whether a household reports using agricultural inputs.
2. **Clustering:** explore agricultural household profiles using K-means clustering.

The final model comparison includes Logistic Regression, Random Forest, Gradient Boosting, a tuned Gradient Boosting model, and an Artificial Neural Network.

## Repository Structure

```text
final_submission/
├── README.md
├── .gitignore
├── requirements.txt
├── run_end_to_end.py
├── notebooks/
│   ├── 01_data_inventory.ipynb
│   ├── 02_data_loading_and_merge.ipynb
│   ├── 03_modeling_baseline.ipynb
│   └── 08_end_to_end_workflow.ipynb
├── src/
│   ├── prepare_household_data.py
│   ├── 04_leakage_safe_modeling.py
│   ├── 05_improvement_methods.py
│   ├── 06_deep_learning_ann.py
│   ├── 07_clustering.py
│   └── 09_generate_report_figures.py
├── report/
│   ├── agricultural_input_adoption_report.tex
│   └── agricultural_input_adoption_report.pdf
├── figures/
├── results/
└── data/raw/
```

## Final Findings

- Modeling population: 16,057 households.
- Candidate predictors: 60.
- Best model: tuned Gradient Boosting.
- Best F1-score: 0.8645.
- Best ROC-AUC: 0.8583.
- ANN F1-score: 0.8532.
- Selected clustering solution: K-means with `k=2`, interpreted cautiously because the clusters are highly imbalanced.

## Setup

Use the existing project virtual environment or create one for this repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The source survey files are not included in this submission repository because of their size and distribution constraints. To rerun the workflow from raw data, place the Stata files in:

```text
stata/*.dta
```

at the repository root. The prepared CSV files and final result tables are already included under `results/` as submission evidence.

## Reproduce the Analysis

After placing the raw Stata files in `stata/`, run:

```bash
python run_end_to_end.py
```

The runner executes data preparation, baseline classification, tuned improvement, ANN comparison, clustering, and figure generation. It validates the expected output artifacts at the end.

For the prepared submission outputs, open:

- `report/agricultural_input_adoption_report.pdf`
- `results/final_model_comparison.csv`
- `results/phase_4_cluster_metrics.csv`
- `figures/model_comparison.png`

## Report Details

Compile the report with a LaTeX installation:

```bash
cd report
pdflatex agricultural_input_adoption_report.tex
pdflatex agricultural_input_adoption_report.tex
```

## Reproducibility Notes

All preprocessing is fitted inside modeling pipelines. Numeric variables use median imputation and scaling; categorical variables use most-frequent imputation and one-hot encoding. The household identifier and direct target-generating agricultural-input fields are excluded from the predictor matrix.
