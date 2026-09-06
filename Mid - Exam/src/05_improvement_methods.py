import pandas as pd
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = Path('prepared_household_data.csv')
RESULTS_PATH = Path('phase_4_improvement_results.csv')


def build_preprocessor(numeric_columns, categorical_columns):
    return ColumnTransformer(
        transformers=[
            (
                'numeric',
                Pipeline([
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler()),
                ]),
                numeric_columns,
            ),
            (
                'categorical',
                Pipeline([
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False)),
                ]),
                categorical_columns,
            ),
        ],
        remainder='drop',
    )


def score_model(label, pipeline, X_test, y_test):
    predictions = pipeline.predict(X_test)
    probabilities = pipeline.predict_proba(X_test)[:, 1]
    return {
        'Model': label,
        'Accuracy': accuracy_score(y_test, predictions),
        'Precision': precision_score(y_test, predictions, zero_division=0),
        'Recall': recall_score(y_test, predictions, zero_division=0),
        'F1': f1_score(y_test, predictions, zero_division=0),
        'ROC_AUC': roc_auc_score(y_test, probabilities),
    }


def main():
    raw = pd.read_csv(DATA_PATH, low_memory=False)
    leak_columns = [column for column in raw.columns if column.startswith('s5q')]
    feature_columns = [
        column for column in raw.columns
        if column not in {'idquest', 'target'} and column not in leak_columns
    ]
    X = raw[feature_columns].copy()
    y = raw['target'].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    numeric_columns = X.select_dtypes(include=['number']).columns.tolist()
    categorical_columns = [column for column in X.columns if column not in numeric_columns]

    baseline = Pipeline([
        ('preprocessor', build_preprocessor(numeric_columns, categorical_columns)),
        ('model', GradientBoostingClassifier(random_state=42)),
    ])
    baseline.fit(X_train, y_train)
    baseline_result = score_model('Gradient Boosting (Phase 3 baseline)', baseline, X_test, y_test)

    tuned_pipeline = Pipeline([
        ('preprocessor', build_preprocessor(numeric_columns, categorical_columns)),
        ('model', GradientBoostingClassifier(random_state=42)),
    ])
    parameter_grid = {
        'model__n_estimators': [100, 200, 400],
        'model__learning_rate': [0.03, 0.05, 0.1],
        'model__max_depth': [2, 3, 5],
    }
    search = GridSearchCV(
        tuned_pipeline,
        parameter_grid,
        scoring='f1',
        cv=3,
        n_jobs=-1,
        refit=True,
    )
    search.fit(X_train, y_train)
    tuned_result = score_model('Gradient Boosting (tuned)', search.best_estimator_, X_test, y_test)

    results = pd.DataFrame([baseline_result, tuned_result])
    results['F1_change_vs_baseline'] = results['F1'] - baseline_result['F1']
    results.to_csv(RESULTS_PATH, index=False)

    print(f'Rows: {len(raw):,}; predictors: {len(feature_columns)}')
    print(f'Train/test rows: {len(X_train):,}/{len(X_test):,}')
    print(f'Best parameters: {search.best_params_}')
    print(f'Best cross-validation F1: {search.best_score_:.4f}')
    print(results.to_string(index=False))
    print(f'Saved {RESULTS_PATH}')


if __name__ == '__main__':
    main()
