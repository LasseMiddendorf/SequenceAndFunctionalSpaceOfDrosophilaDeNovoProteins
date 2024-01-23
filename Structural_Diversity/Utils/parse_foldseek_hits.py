#This scirpt was used to parse the foldseek results for queries against the AlphaFold Database
#Input files are the raw foldseek results files, which can be downloaded from the complementary Zenodo repository
#This script generated the files "conserved_AFDB50_bestHits.csv", "denovo_AFDB50_bestHits.csv", and "random_AFDB50_bestHits.csv" which are used in the analysis notebook

import pandas as pd
import os
import sys 

def main(file, filename):

    df = pd.read_csv(file, names=["query","target","alntmscore","qtmscore","ttmscore","lddt","lddtfull","prob","evalue","fident","alnlen","qcov","tcov", "taxid", "species"], sep="\t", header=None, index_col=None)
    result = pd.DataFrame(columns=["id", "AFDB50_highest_Tm", "AFDB50_highest_Tm_ID", "AFDB50_seqIdent", "AFDB50_qcov", "AFDB50_tcov", "AFDB50_evalue", "species"])

    #iterate over all queries and store entry with highest Tm in results dataframe

    for id in df["query"].unique():
        sel = df[df["query"] == id]
        id = id.rsplit(".pdb")[0]
        id = id.rsplit("_ranked")[0]

        print(f"Processing {id}")

        sel = sel.sort_values("alntmscore", ascending=False, ignore_index=True)
        sel = sel[(~sel["species"].str.contains("Drosophila"))].reset_index(drop=True)
        sel = sel[~sel["species"].str.contains("Drosophila")].reset_index(drop=True)

        
        try:
            result.loc[len(result)] = [id, sel["alntmscore"].iloc[0], sel["target"].iloc[0], sel["fident"].iloc[0], sel["qcov"].iloc[0], sel["tcov"].iloc[0], sel["evalue"].iloc[0], sel["species"].iloc[0]]
        except:
            pass

        
    result.to_csv(filename)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])