import ROOT
import numpy as np
pzs=np.arange(0,100,8)
Allcounts=np.zeros_like(pzs)
Recocounts=np.zeros_like(pzs)

with open("file_list.txt","r") as listfile:
    for line in listfile:
        line=line.strip()
        file=ROOT.TFile.Open(line)
        tree=file.Events
        for entry in tree:
            if entry.n_truthdimuons>0:
                print(entry.truthdimuon_pz[0])
                ind=round(entry.truthdimuon_pz[0]/8)
                if ind>=len(pzs):
                    continue
                Allcounts[ind]=Allcounts[ind]+1
                if entry.n_dimuons>0:
                    Recocounts[ind]=Recocounts[ind]+1
with open ("pz_eff.txt","w") as file:
    for i in range(len(pzs)):
        file.write(f"{pzs[i]} {Recocounts[i]/Allcounts[i]}\n")

