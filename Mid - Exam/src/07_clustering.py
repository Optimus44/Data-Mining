import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA_PATH = Path('prepared_household_data.csv')
METRICS_PATH = Path('phase_4_cluster_metrics.csv')
ASSIGNMENTS_PATH = Path('phase_4_cluster_assignments.csv')
PROFILES_PATH = Path('phase_4_cluster_profiles.csv')


def main():
    raw = pd.read_csv(DATA_PATH, low_memory=False)
    raw = raw.copy()

    # Remove direct agricultural-input module (all s5q columns)
    leak_cols = [c for c in raw.columns if c.startswith('s5q')]
    exclude_cols = {'idquest', 'target'}
    feature_cols = [c for c in raw.columns if c not in exclude_cols and c not in leak_cols]

    X = raw[feature_cols].copy()

    for col in X.columns:
        if X[col].dtype == 'object':
            X[col] = X[col].astype(str).replace({'nan': 'Missing', 'None': 'Missing', '<NA>': 'Missing'})
        elif pd.api.types.is_numeric_dtype(X[col]):
            X[col] = pd.to_numeric(X[col], errors='coerce')

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
                    ('onehot', OneHotEncoder(handle_unknown='ignore')),
                ]),
                categorical_cols,
            ),
        ]
    )

    print(f'Data: rows={len(raw)}, features={len(feature_cols)}')
    print(f'Target distribution (descriptive only): {raw["target"].value_counts().to_dict()}')
    print()

    # ============ CLUSTERING: K-Means with multiple k values ============
    print('='*70)
    print('UNSUPERVISED CLUSTERING: K-Means')
    print('='*70)
    print('Testing k = 2 to 8 clusters using Silhouette and Davies-Bouldin scores')
    print()

    X_preprocessed = preprocessor.fit_transform(X)
    # Convert sparse matrix to dense for clustering evaluation
    if hasattr(X_preprocessed, 'toarray'):
        X_preprocessed = X_preprocessed.toarray()

    clustering_results = []
    best_k = 2
    best_silhouette = -2

    for k in range(2, 9):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(X_preprocessed)

        silhouette = silhouette_score(X_preprocessed, clusters)
        davies_bouldin = davies_bouldin_score(X_preprocessed, clusters)

        clustering_results.append({
            'K': k,
            'Silhouette Score': silhouette,
            'Davies-Bouldin Index': davies_bouldin,
            'Inertia': kmeans.inertia_,
        })

        if silhouette > best_silhouette:
            best_silhouette = silhouette
            best_k = k

        print(f'K={k:d} | Silhouette={silhouette:.4f} | Davies-Bouldin={davies_bouldin:.4f} | Inertia={kmeans.inertia_:.2f}')

    print()
    clustering_df = pd.DataFrame(clustering_results)
    clustering_df.to_csv(METRICS_PATH, index=False)
    print('Full results table:')
    print(clustering_df.to_string(index=False))
    print()

    # ============ FINAL BEST K CLUSTERING ============
    print('='*70)
    print(f'FINAL CLUSTERING: K={best_k} (best Silhouette={best_silhouette:.4f})')
    print('='*70)

    kmeans_final = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    final_clusters = kmeans_final.fit_predict(X_preprocessed)

    # Analyze cluster composition with respect to target
    cluster_target_composition = pd.DataFrame({
        'idquest': raw['idquest'].values,
        'cluster': final_clusters,
        'target': raw['target'].astype(int).values,
    })
    cluster_target_composition.to_csv(ASSIGNMENTS_PATH, index=False)

    print('\nCluster distribution:')
    print(cluster_target_composition['cluster'].value_counts().sort_index().to_dict())
    print()

    print('Target distribution by cluster:')
    profile_rows = []
    for c in sorted(cluster_target_composition['cluster'].unique()):
        cluster_mask = final_clusters == c
        cluster_y = cluster_target_composition.loc[cluster_mask, 'target']
        pos_rate = (cluster_y == 1).mean()
        print(f'  Cluster {c}: target=1 proportion = {pos_rate:.4f} ({int(cluster_y.sum())}/{len(cluster_y)})')
        profile_rows.append({
            'cluster': int(c),
            'households': len(cluster_y),
            'input_use_rate': pos_rate,
        })

    pd.DataFrame(profile_rows).to_csv(PROFILES_PATH, index=False)

    print()
    print(f'✓ Clustering complete: {best_k} clusters identified')
    print(f'Saved {METRICS_PATH}, {ASSIGNMENTS_PATH}, and {PROFILES_PATH}')


if __name__ == '__main__':
    main()
