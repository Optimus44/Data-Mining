from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
FIGURES = ROOT / 'figures'
FIGURES.mkdir(exist_ok=True)


prepared = pd.read_csv(ROOT / 'prepared_household_data.csv')
models = pd.read_csv(ROOT / 'final_model_comparison.csv')
clusters = pd.read_csv(ROOT / 'phase_4_cluster_profiles.csv')

plt.style.use('seaborn-v0_8-whitegrid')

ax = prepared['target'].map({0: 'Non-user', 1: 'User'}).value_counts().reindex(['Non-user', 'User']).plot(
    kind='bar', color=['#4c78a8', '#f58518'], figsize=(6, 4)
)
ax.set_title('Agricultural-input use in the modelling population')
ax.set_ylabel('Households')
ax.set_xlabel('Target class')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIGURES / 'target_distribution.png', dpi=220)
plt.close()

plot_models = models.sort_values('F1')
ax = plot_models.plot(x='Model', y=['F1', 'ROC_AUC'], kind='barh', figsize=(8, 5), color=['#54a24b', '#b279a2'])
ax.set_title('Supervised model comparison')
ax.set_xlabel('Score')
ax.set_ylabel('')
ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig(FIGURES / 'model_comparison.png', dpi=220)
plt.close()

ax = clusters.plot(x='cluster', y='households', kind='bar', legend=False, figsize=(6, 4), color='#e45756')
ax.set_title('K-means cluster sizes')
ax.set_xlabel('Cluster')
ax.set_ylabel('Households')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIGURES / 'cluster_sizes.png', dpi=220)
plt.close()

print(f'Generated figures in {FIGURES}')
