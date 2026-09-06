"""Run the complete project workflow from raw Stata modules to final artifacts."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
PYTHON = sys.executable
STEPS = [
    ('Prepare household dataset', 'src/prepare_household_data.py'),
    ('Run baseline classification', 'src/04_leakage_safe_modeling.py'),
    ('Run tuned improvement', 'src/05_improvement_methods.py'),
    ('Run ANN comparison', 'src/06_deep_learning_ann.py'),
    ('Run clustering', 'src/07_clustering.py'),
    ('Generate report figures', 'src/09_generate_report_figures.py'),
]
REQUIRED_OUTPUTS = [
    'results/prepared_household_data.csv',
    'results/phase_2_feature_audit.csv',
    'results/phase_3_baseline_results.csv',
    'results/phase_4_improvement_results.csv',
    'results/phase_4_cluster_metrics.csv',
    'results/phase_4_cluster_assignments.csv',
    'results/phase_4_cluster_profiles.csv',
    'results/phase_5_ann_results.csv',
    'results/final_model_comparison.csv',
    'figures/target_distribution.png',
    'figures/model_comparison.png',
    'figures/cluster_sizes.png',
]


def main():
    (ROOT / 'results').mkdir(exist_ok=True)
    for label, script in STEPS:
        print(f'\n=== {label} ===')
        subprocess.run([PYTHON, script], cwd=ROOT, check=True)

    csv_outputs = [name for name in REQUIRED_OUTPUTS if name.startswith('results/')]
    for result_path in csv_outputs:
        generated = ROOT / Path(result_path).name
        destination = ROOT / result_path
        if generated.is_file():
            generated.replace(destination)

    missing = [name for name in REQUIRED_OUTPUTS if not (ROOT / name).is_file()]
    if missing:
        raise FileNotFoundError(f'Missing workflow outputs: {missing}')

    print('\n=== Workflow validation ===')
    print(f'Validated {len(REQUIRED_OUTPUTS)} generated artifacts.')
    print('End-to-end workflow completed successfully.')


if __name__ == '__main__':
    main()
