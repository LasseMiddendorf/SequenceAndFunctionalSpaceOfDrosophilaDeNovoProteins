import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def nondiag(mat):
    if mat.shape[0] != mat.shape[1]:
        raise ValueError("Matrix must be square")
    return mat[~np.eye(mat.shape[0], dtype=bool)].reshape(mat.shape[0], -1)

def downsample(data, max_points=1000):
    if len(data) > max_points:
        return np.random.choice(data, max_points, replace=False)
    return data

os.chdir("/Users/larseicholt/Desktop/zenodo_github/EmbeddingsAnalyses")

plt.rcParams.update({
    'font.size': 6,
    'axes.labelsize': 8,
    'axes.edgecolor': 'black',
    'axes.linewidth': 0.5,
    'legend.frameon': False
})

# Load and downsample data
rr = downsample(nondiag(np.loadtxt("random-random_dist.txt")).flatten())
dr = downsample(np.loadtxt("denovo-random_dist.txt").flatten())
dd = downsample(nondiag(np.loadtxt("denovo-denovo_dist.txt")).flatten())
dc = downsample(np.loadtxt("denovo-conserved_dist.txt").flatten())
cc = downsample(nondiag(np.loadtxt("conserved-conserved_dist.txt")).flatten())
rc = downsample(np.loadtxt("random-conserved_dist.txt").flatten())
ee = downsample(nondiag(np.loadtxt("consrand-consrand_dist.txt")).flatten())
ce = downsample(np.loadtxt("conserved-consrand_dist.txt").flatten())
re = downsample(np.loadtxt("random-consrand_dist.txt").flatten())
de = downsample(np.loadtxt("denovo-consrand_dist.txt").flatten())

alldata = [rr, dr, dd, dc, rc, cc, ce, de, re, ee]


colors = ['#3A3C43', '#BE3E48', '#869A3A', '#C4A535', '#4E76A1', 
          '#855B8D', '#568EA3', '#B8B8B8', '#888987', '#FB001E']

fig, ax = plt.subplots(figsize=(5, 3), dpi=300)


ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgray', zorder=0)
ax.set_axisbelow(True)  


sns.violinplot(data=alldata, ax=ax, inner=None, scale='width', cut=0, palette=colors, linewidth=0, edgecolor='none')


for i, data in enumerate(alldata):
    median = np.median(data)
    ax.scatter(i, median, color='white', s=10, zorder=3, edgecolors='black', linewidth=0.5)

ax.set_ylabel("L1 Distance")
ax.set_xticks(range(10))
ax.set_xticklabels(["R-DN\nR-DN", "DN\nR-DN", "DN\nDN", 
                    "DN\nC", "R-DN\nC", "C\nC", 
                    "C\nR-C", "DN\nR-C", 
                    "R-DN\nR-C", "R-C\nR-C"], 
                   rotation=45, ha='right')

plt.tight_layout()
plt.savefig("Plot_distances.pdf", dpi=300, bbox_inches='tight')
plt.close()