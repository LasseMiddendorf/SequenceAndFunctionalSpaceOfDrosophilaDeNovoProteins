import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Path')

# age groups (young 0-5, intermedia 5-30, old >30, -0.1 for 0.0 values)
bins = [-0.1, 5, 30, df['age'].max()]
labels = ['Young', 'Intermediate', 'Old']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# Count the number of occurrences in each age group
counts = df['age_group'].value_counts().loc[labels].fillna(0)

# colours as in llps analysis
colors = ["#8cc098", "#437995", "#141a3c"]

# plotting
plt.figure(figsize=(10, 6))
plt.bar(labels, counts, color=colors, edgecolor="black")
plt.xlabel('')
plt.ylabel('Count')
plt.title('Age Groups of de novo proteins annotated with ECOD architecture')
plt.savefig('/Users/larseicholt/Desktop/age_groups_foldseek.pdf', format='pdf', dpi=600)
plt.show()