import pandas as pd
from pathlib import Path

base_path = Path('stata')


def mode_non_null(series):
    valid = series.dropna()
    if valid.empty:
        return None
    return valid.mode().iloc[0]


def sum_numeric(series):
    return pd.to_numeric(series, errors='coerce').fillna(0).sum()


def aggregate_household_records(df):
    grouped = df.groupby('idquest', sort=False)
    aggregations = {
        column: mode_non_null if not pd.api.types.is_numeric_dtype(df[column]) else sum_numeric
        for column in df.columns
        if column != 'idquest'
    }
    out = grouped.agg(aggregations)
    return out.reset_index()


base = pd.read_stata(base_path / 'S0_General Information.dta')
land = pd.read_stata(base_path / 'S2_Land tenure and crops planted.dta')
ext = pd.read_stata(base_path / 'S3_Extension services and agricultural programmes.dta')
inputs = pd.read_stata(base_path / 'S5_Agricultural Inputs.dta')
practices = pd.read_stata(base_path / 'S6_Agricultural Practices.dta')
animals = pd.read_stata(base_path / 'S9_Number of animals.dta')

# Create the binary target from the agricultural inputs module.
inputs = inputs.copy()
inputs['target'] = inputs['s5q1_1'].map({'Yes': 1, 'No': 0}).astype('Int64')
if inputs['target'].isna().any():
    raise ValueError('Unexpected or missing values found in s5q1_1')

target_table = inputs[['idquest', 'target']].drop_duplicates('idquest')

# Keep the main base table at household level
base_core = (base.loc[base['idquest'].notna(), ['idquest', 's0q1', 's0q2', 's0q3', 's0q4']]
             .drop_duplicates('idquest'))
land_core = land[['idquest', 's2q1', 's2q2', 's2q3', 's2q4', 's2q5', 's2q6', 's2q7_1', 's2q7_2', 's2q7_3', 's2q15_1', 's2q15_2', 's2q15_3']].copy()
practices_core = practices[['idquest', 'dummy_cropping_B', 'cropping', 's6q1_1', 's6q1_2_1', 's6q1_2_2', 's6q1_2_3', 's6q1_3', 's6q1_4_1', 's6q1_4_2', 's6q1_4_3', 's6q2_1', 's6q2_2_1']].copy()

# Animal data have repeated records and copied household fields. Aggregate only
# genuine S9 variables before merging so the result stays household-level.
animal_columns = ['idquest'] + [column for column in animals.columns if column.startswith('s9')]
animals_agg = aggregate_household_records(animals[animal_columns])

# Merge only non-target features in one-to-one household form.
final_df = target_table.merge(base_core, on='idquest', how='left', validate='one_to_one')
final_df = final_df.merge(land_core, on='idquest', how='left', validate='one_to_one')
final_df = final_df.merge(practices_core, on='idquest', how='left', validate='one_to_one')
final_df = final_df.merge(animals_agg, on='idquest', how='left', validate='one_to_one')

# Remove duplicate or unneeded helper columns introduced by merge suffixing if present
final_df = final_df.drop(columns=[c for c in final_df.columns if c.endswith('_x') or c.endswith('_y')], errors='ignore')

if not final_df['idquest'].is_unique:
    raise ValueError('Prepared data contains duplicate household IDs')

# Save
output_path = Path('prepared_household_data.csv')
audit_path = Path('phase_2_feature_audit.csv')
final_df.to_csv(output_path, index=False)
source_groups = {
    'idquest': 'identifier',
    'target': 'target',
}


def source_group(column):
    if column in source_groups:
        return source_groups[column]
    for prefix, group in [
        ('s0', 'household_context'),
        ('s2', 'land_and_crops'),
        ('s6', 'agricultural_practices'),
        ('s9', 'livestock_aggregated'),
    ]:
        if column.startswith(prefix):
            return group
    return 'review_required'


feature_audit = pd.DataFrame({
    'column': final_df.columns,
    'source_group': [source_group(column) for column in final_df.columns],
    'dtype': final_df.dtypes.astype(str).values,
    'missing_count': final_df.isna().sum().values,
    'missing_share': final_df.isna().mean().round(4).values,
    'distinct_values': final_df.nunique(dropna=True).values,
})
feature_audit.to_csv(audit_path, index=False)
print(f'Prepared dataset rows={final_df.shape[0]} cols={final_df.shape[1]}')
print('Target distribution:')
print(final_df['target'].value_counts().to_dict())
print(f'Feature columns={final_df.shape[1] - 2}')
print(f'Saved to {output_path} and {audit_path}')
