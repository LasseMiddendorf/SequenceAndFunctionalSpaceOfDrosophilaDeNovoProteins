# Sequence And Functional Space Of Drosophila De Novo Proteins

This repository contains code and data to reproduce the analyses from the paper Middendorf et al. (2024) "Sequence and Functional space of Drosophila de novo proteins" (DOI: ...). The files `de_novo_proteins_data.csv`, `random_sequences_data.csv`, and `established_proteins_data.csv` have been published in this [paper](https://doi.org/10.1002/prot.26652) and a detailed explaination of the features included in these datasets can be found in the corresponding [Github repository](https://github.com/LasseMiddendorf/de-novo-structure-disorder-predictor-performance/tree/main/Data).

 

### Content
- `Structural_diversity` contains the data and code to reproduce the results presented in figure 1
- `GO_Term_Analysis` contains the data and code to reporduce the results presented in figure 2. In addition to the code in this directory, [REVIGO](http://revigo.irb.hr) was used to reduce the number of predicted GO Terms based on semantic similarity.
-  `Biomolecular_condensate_formation` contains the data and code to reproduce the results presented figure 3. This directory also conatins the set of known condensate-forming proteins retrieved from the [CD-CODE](https://cd-code.org) database
- `Sequence_space_distances` contains the scripts to reproduce figure 4 and the scripts to calculate the distances of proteins from different groups in sequence space 

The raw foldseek results and ESM2 650M embeddings need to be downloaded from the accompanying [Zenodo repository](10.5281/zenodo.10557890).

### Installation

**Requirements:**
- [anaconda](https://www.anaconda.com/products/individual)

**Usage:**
1. Clone this repository
2. Create a conda environment with the required packages: `conda env create -f environment.yml`
3. Activate the environment: `conda activate Middendorf_et_al_2024`
4. Start jupyter notebook from the terminal: `jupyter notebook`
5. Open the notebooks and run the cells
