import pandas as pd
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA_PATH = Path('prepared_household_data.csv')
RESULTS_PATH = Path('phase_3_baseline_results.csv')


def main():
    raw = pd.read_csv(DATA_PATH, low_memory=False)
    raw = raw.copy()

    # Direct agricultural-input questions are the target-generating module and must not be used as predictors.
    # This removes the entire S5 module, including the exact target variable s5q1_1.
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

    print(f'Rows: {len(raw)}')
    print(f'Target distribution: {y.value_counts().to_dict()}')
    print(f'Leak columns removed: {len(leak_cols)}')
    print(f'Feature columns used: {len(feature_cols)}')

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

    models = {
        'Logistic Regression': LogisticRegression(max_iter=2000, random_state=42),
        'Random Forest': RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            min_samples_leaf=2,
            n_jobs=-1,
        ),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    }

    results = []
    for name, model in models.items():
        pipe = Pipeline([('preprocessor', preprocessor), ('model', model)])
        pipe.fit(X_train, y_train)
        pred = pipe.predict(X_test)
        proba = pipe.predict_proba(X_test)[:, 1]
        results.append(
            {
                'Model': name,
                'Accuracy': accuracy_score(y_test, pred),
                'Precision': precision_score(y_test, pred, zero_division=0),
                'Recall': recall_score(y_test, pred, zero_division=0),
                'F1': f1_score(y_test, pred, zero_division=0),
                'ROC_AUC': roc_auc_score(y_test, proba),
            }
        )

    result_df = pd.DataFrame(results).sort_values('F1', ascending=False)
    result_df.to_csv(RESULTS_PATH, index=False)
    print('\nLeakage-safe benchmark results:')
    print(result_df.to_string(index=False))
    print(f'Saved {RESULTS_PATH}')


if __name__ == '__main__':
    main()
