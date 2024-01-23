#this scirpt was used to map ECOD domains to de novo protein structures BEFORE MD simulations
#Input files are the raw foldseek results files from querying the de novo protein structures against the PDB and a file containing the ECOD domains for all PDB chains
#Input files can be downloaded from the complementary Zenodo repository


import pandas as pd
import numpy as np
import os
import sys

def parse_foldseek_results(foldseek_results_file, TmScore=0.5, evalue=0.1, tcov=0.0):
    
    names = [
        "query",
        "target",
        "alntmscore",
        "qtmscore",
        "ttmscore",
        "lddt",
        "lddtfull",
        "prob",
        "evalue",
        "fident",
        "alnlen",
        "qcov",
        "tcov",
        "taxid",
        "taxname",
        "qstart",
        "qend",
        "tstart",
        "tend"
    ]

    foldseek_result = pd.read_csv(foldseek_results_file, sep='\t', names=names, index_col=False, header=None)
    foldseek_result = foldseek_result[(foldseek_result["alntmscore"] >= TmScore) & (foldseek_result["evalue"] <= evalue)].reset_index(drop=True)
    foldseek_result = foldseek_result[foldseek_result["tcov"] >= tcov].reset_index(drop=True)

    foldseek_result["query"] = foldseek_result["query"].apply(lambda x: x.rsplit("_ranked_0.pdb")[0])
    foldseek_result["target_chain"] = foldseek_result["target"].apply(lambda x: x.rsplit("_")[-1])
    foldseek_result["target"] = foldseek_result["target"].apply(lambda x: x.rsplit(".")[0])

    return foldseek_result

def match_PDB_with_ECOD(foldseek_results: pd.DataFrame, ecod_path: str):
    
    ecod = pd.read_csv(ecod_path, skiprows=4, header=0, index_col=False, sep="\t")
    results = pd.DataFrame(columns=["id", "target", "arch_name", "x_name", "h_name", "t_name",])

    for protein in foldseek_results["query"].unique():
        selection = foldseek_results[foldseek_results["query"] == protein].sort_values(by="alntmscore", ascending=False).reset_index(drop=True).head(1)
        ecod_selection = ecod[(ecod["pdb"] == selection["target"].values[0]) & (ecod["chain"] == selection["target_chain"].values[0])].reset_index(drop=True)

        try:
            results.loc[len(results)] = [protein, ecod_selection["pdb"].values[0], ecod_selection["arch_name"].values[0], ecod_selection["x_name"].values[0], ecod_selection["h_name"].values[0], ecod_selection["t_name"].values[0]]
        except:
            pass
    
    return results


if __name__ == "__main__":
    foldseek_results_file = sys.argv[1]
    ecod_path = sys.argv[2]
    results = match_PDB_with_ECOD(parse_foldseek_results(foldseek_results_file, evalue=100000, tcov=0.8), ecod_path)
    results.to_csv("foldseek_ecod_results.csv")

         
             



