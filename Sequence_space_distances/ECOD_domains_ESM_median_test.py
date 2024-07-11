import pandas as pd
from scipy.stats import mannwhitneyu

df = pd.read_csv('/Users/larseicholt/Desktop/zenodo_github/denovos_withECOD_ESMdist.tsv', sep='\t')

median_L1_dist = df['L1-dist'].median()
print(f"Median of 'L1-dist': {median_L1_dist}")

# De novo to Conserved median L1 distance
other_median = 91.13
stat, p = mannwhitneyu(df['L1-dist'], [other_median]*len(df['L1-dist']))

print(f"Mann-Whitney U test result: U={stat}, p-value={p}")