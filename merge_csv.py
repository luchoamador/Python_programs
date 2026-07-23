import pandas as pd

# 1. Load the CSV files
df_main = pd.read_csv('Caudata_pi_phylosubset154.csv')
df_lookup = pd.read_csv('Caudata_matrix_April2026.csv')

# 2. Identify the common species column name (adjust 'Species' if necessary)
species_col = 'Species'

# 3. Merge the datasets (keeps all rows in df_main and adds matching columns from df_lookup)
df_merged = pd.merge(df_main, df_lookup, on=species_col, how='left')

# 4. Save the updated data to a new CSV file
df_merged.to_csv('Caudata_updated_piphylo.csv', index=False)
