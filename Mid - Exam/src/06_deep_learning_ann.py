import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA_PATH = Path('prepared_household_data.csv')
ANN_RESULTS_PATH = Path('phase_5_ann_results.csv')
FINAL_RESULTS_PATH = Path('final_model_comparison.csv')


def main():
    raw = pd.read_csv(DATA_PATH, low_memory=False)
    raw = raw.copy()

    # Remove direct agricultural-input module (all s5q columns)
    leak_cols = [c for c in raw.columns if c.startswith('s5q')]
    exclude_cols = {'idquest', 'target'}
    feature_cols = [c for c in raw.columns if c not in exclude_cols and c not in leak_cols]

    X = raw[feature_cols].copy()
    y = raw['target'].astype(int)

    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = X[col].astype(str).replace({'nan': 'Missing', 'None': 'Missing', '<NA>': 'Missing'})
        elif pd.api.types.is_numeric_dtype(X[col]):
            X[col] = pd.to_numeric(X[col], errors='coerce')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    numeric_cols = X.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = [c for c in X.columns if c not in numeric_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                'num',
                Pipeline([
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler()),
                ]),
                numeric_cols,
            ),
            (
                'cat',
                Pipeline([
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
                ]),
                categorical_cols,
            ),
        ]
    )

    print(f'Data: rows={len(raw)}, features={len(feature_cols)}')
    print(f'Train/test split: {len(X_train)}/{len(X_test)}')
    print(f'Target distribution: {y.value_counts().to_dict()}')
    print()

    # ============ BASELINE (Gradient Boosting) ============
    print('='*70)
    print('BASELINE: Gradient Boosting')
    print('='*70)

    baseline_model = GradientBoostingClassifier(random_state=42)
    pipe_baseline = Pipeline([('preprocessor', preprocessor), ('model', baseline_model)])
    pipe_baseline.fit(X_train, y_train)

    pred_baseline = pipe_baseline.predict(X_test)
    proba_baseline = pipe_baseline.predict_proba(X_test)[:, 1]

    baseline_result = {
        'Model': 'Gradient Boosting (Baseline)',
        'Accuracy': accuracy_score(y_test, pred_baseline),
        'Precision': precision_score(y_test, pred_baseline, zero_division=0),
        'Recall': recall_score(y_test, pred_baseline, zero_division=0),
        'F1': f1_score(y_test, pred_baseline, zero_division=0),
        'ROC_AUC': roc_auc_score(y_test, proba_baseline),
    }

    baseline_df = pd.DataFrame([baseline_result])
    print(baseline_df.to_string(index=False))
    print()

    # ============ DEEP LEARNING: Multi-layer Perceptron (ANN) ============
    print('='*70)
    print('DEEP LEARNING: Artificial Neural Network (MLP)')
    print('='*70)
    print('Architecture: Input -> Hidden(256) -> Hidden(128) -> Hidden(64) -> Output')
    print('Training with L2 regularization (alpha=0.001), early stopping patience=50')
    print()

    ann_model = MLPClassifier(
        hidden_layer_sizes=(256, 128, 64),
        activation='relu',
        solver='adam',
        alpha=0.001,
        batch_size=32,
        learning_rate_init=0.001,
        max_iter=500,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=50,
        random_state=42,
        verbose=0,
    )

    pipe_ann = Pipeline([('preprocessor', preprocessor), ('model', ann_model)])
    pipe_ann.fit(X_train, y_train)

    pred_ann = pipe_ann.predict(X_test)
    proba_ann = pipe_ann.predict_proba(X_test)[:, 1]

    ann_result = {
        'Model': 'ANN (256-128-64)',
        'Accuracy': accuracy_score(y_test, pred_ann),
        'Precision': precision_score(y_test, pred_ann, zero_division=0),
        'Recall': recall_score(y_test, pred_ann, zero_division=0),
        'F1': f1_score(y_test, pred_ann, zero_division=0),
        'ROC_AUC': roc_auc_score(y_test, proba_ann),
    }

    ann_df = pd.DataFrame([ann_result])
    print(ann_df.to_string(index=False))
    print()

    # ============ COMPARISON ============
    print('='*70)
    print('SUMMARY: Baseline vs Deep Learning')
    print('='*70)

    comparison = pd.concat([baseline_df, ann_df], ignore_index=True)
    comparison.to_csv(ANN_RESULTS_PATH, index=False)
    print(comparison.to_string(index=False))
    print()

    # Calculate improvement
    f1_baseline = baseline_result['F1']
    f1_ann = ann_result['F1']
    improvement = ((f1_ann - f1_baseline) / f1_baseline) * 100

    print(f'F1 Improvement: {improvement:+.2f}%')
    print(f'Recommended model: {"ANN" if f1_ann > f1_baseline else "Gradient Boosting"}')

    # Combine all supervised results using the same held-out test protocol.
    phase_3_path = Path('phase_3_baseline_results.csv')
    phase_4_path = Path('phase_4_improvement_results.csv')
    phase_3 = pd.read_csv(phase_3_path)
    phase_4 = pd.read_csv(phase_4_path)
    tuned = phase_4.loc[phase_4['Model'].eq('Gradient Boosting (tuned)')]
    final_comparison = pd.concat(
        [phase_3, tuned.drop(columns=['F1_change_vs_baseline']), ann_df],
        ignore_index=True,
    )
    final_comparison = final_comparison.sort_values('F1', ascending=False).reset_index(drop=True)
    final_comparison.to_csv(FINAL_RESULTS_PATH, index=False)
    print(f'Saved {ANN_RESULTS_PATH} and {FINAL_RESULTS_PATH}')


if __name__ == '__main__':
    main()
