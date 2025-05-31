import ROOT
import os
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.patches as mpatches
import matplotlib.tri as tri
print('test')
ROOT.gInterpreter.Declare("""
    int em_trigger(int n,ROOT::VecOps::RVec<Float_t> dep,ROOT::VecOps::RVec<Int_t> ID) { \
         int count = 0; \
         for (int i=0;i<n;i++) { \
             if (dep[i] > 0.1 && ID[i]==100) { \
                 count++; \
             } \
             if (count >= 2) { \
                 return true; \
             } \
         } \
         return false; \
     }
     int reco(int n,ROOT::VecOps::RVec<Int_t> dimuon_matched) { \
         for (int i=0;i<n;i++) { \
             if (dimuon_matched[i]==1) { \
                 return true; \
             } \
         } \
         return false; \
     }
""")
#with open("Brem_muons_eff.txt","w") as file:
#    pass
with open("Brem_electrons_eff.txt","w") as file:
    pass
'''
with open("Eta_muons_eff.txt","w") as file:
    pass
with open("Eta_electrons_eff.txt","w") as file:
    pass
with open("Pion_electrons_eff.txt","w") as file:
    pass
'''
'''
with open("mu_file_list.txt","r") as file:
    test=0
    for line in file:
        if not ( "Eta" in line or "Brem" in line or "Pion" in line):
            continue
        #print(line)
        #test=test+1
        #print(test)
        line=line.strip()
        if not os.path.exists(line):
            print("?")
            continue
        logeps=float(line[line.find("eps_")+4:line.find(".txt")])
        if "Eta" in line:
            mAp=float(line[line.find("Eta_")+4:line.find("_z500")])
        if "Brem" in line:
            mAp=float(line[line.find("Brem_")+5:line.find("_z500")])
        if "Pion" in line:
            mAp=float(line[line.find("Pion_")+5:line.find("_z500")])
        rdf=ROOT.RDataFrame("Events",line)
        N_tot=rdf.Count().GetValue()
        #continue
        reco_eff=rdf.Filter("reco(n_dimuons,dimuon_matched)").Count().GetValue()/N_tot
        trig_eff=rdf.Filter("nim_trigger[3]>0 || fpga_trigger[0]>0 || em_trigger(n_hits,hit_edep,hit_detID)").Count().GetValue()/N_tot
        trig_eff_em=rdf.Filter("em_trigger(n_hits,hit_edep,hit_detID)").Count().GetValue()/N_tot
        trig_eff_dimuon=rdf.Filter("nim_trigger[3]>0 || fpga_trigger[0]>0").Count().GetValue()/N_tot
        both_eff=rdf.Filter("reco(n_dimuons,dimuon_matched) && (nim_trigger[3]>0 || fpga_trigger[0]>0 || em_trigger(n_hits,hit_edep,hit_detID))").Count().GetValue()/N_tot
        both_eff_em=rdf.Filter("reco(n_dimuons,dimuon_matched) && (em_trigger(n_hits,hit_edep,hit_detID))").Count().GetValue()/N_tot
        both_eff_dimuon=rdf.Filter("reco(n_dimuons,dimuon_matched) && (nim_trigger[3]>0 || fpga_trigger[0]>0 )").Count().GetValue()/N_tot
        if "Eta" in line:
            print("Eta mu"+" "+str(logeps)+" "+str(mAp)+" "+str(reco_eff)+" "+str(trig_eff)+" "+str(both_eff)+" "+str(trig_eff_em)+" "+str(trig_eff_dimuon)+" "+str(both_eff_em)+" "+str(both_eff_dimuon))
            with open("Eta_muons_eff.txt","a") as file:
                file.write(f"{str(mAp)} {str(logeps)} {str(reco_eff)} {str(trig_eff)} {str(both_eff)} {str(trig_eff_em)} {str(trig_eff_dimuon)} {str(both_eff_em)} {str(both_eff_dimuon)}\n")
        if "Brem" in line:
            print("Brem mu"+" "+str(logeps)+" "+str(mAp)+" "+str(reco_eff)+" "+str(trig_eff)+" "+str(both_eff)+" "+str(trig_eff_em)+" "+str(trig_eff_dimuon)+" "+str(both_eff_em)+" "+str(both_eff_dimuon))
            with open("Brem_muons_eff.txt","a") as file:
                file.write(f"{str(mAp)} {str(logeps)} {str(reco_eff)} {str(trig_eff)} {str(both_eff)} {str(trig_eff_em)} {str(trig_eff_dimuon)} {str(both_eff_em)} {str(both_eff_dimuon)}\n")
'''
test=0
with open("e_file_list.txt","r") as file:
    
    for line in file:
        if not ( "Eta" in line or "Brem" in line or "Pion" in line):
            continue
        #print(line)
        #test=test+1
        #print(test)
        line=line.strip()
        if not os.path.exists(line):
            continue
        logeps=float(line[line.find("eps_")+4:line.find(".txt")])
        if "Eta" in line:
            mAp=float(line[line.find("Eta_")+4:line.find("_z500")])
        if "Brem" in line:
            mAp=float(line[line.find("Brem_")+5:line.find("_z500")])
        if "Pion" in line:
            mAp=float(line[line.find("Pion_")+5:line.find("_z500")])
        rdf=ROOT.RDataFrame("Events",line)
        N_tot=rdf.Count().GetValue()
        #continue
        reco_eff=rdf.Filter("reco(n_dimuons,dimuon_matched)").Count().GetValue()/N_tot
        trig_eff=rdf.Filter("nim_trigger[3]>0 || fpga_trigger[0]>0 || em_trigger(n_hits,hit_edep,hit_detID)").Count().GetValue()/N_tot
        trig_eff_dimuon=rdf.Filter("nim_trigger[3]>0 || fpga_trigger[0]>0").Count().GetValue()/N_tot
        trig_eff_em=rdf.Filter("em_trigger(n_hits,hit_edep,hit_detID)").Count().GetValue()/N_tot
        both_eff=rdf.Filter("reco(n_dimuons,dimuon_matched) && (nim_trigger[3]>0 || fpga_trigger[0]>0 || em_trigger(n_hits,hit_edep,hit_detID))").Count().GetValue()/N_tot
        both_eff_em=rdf.Filter("reco(n_dimuons,dimuon_matched) && (em_trigger(n_hits,hit_edep,hit_detID))").Count().GetValue()/N_tot
        both_eff_dimuon=rdf.Filter("reco(n_dimuons,dimuon_matched) && (nim_trigger[3]>0 || fpga_trigger[0]>0 )").Count().GetValue()/N_tot
        if "Pion" in line:
            print("Pion e"+" "+str(logeps)+" "+str(mAp)+" "+str(reco_eff)+" "+str(trig_eff)+" "+str(both_eff)+" "+str(trig_eff_em)+" "+str(trig_eff_dimuon)+" "+str(both_eff_em)+" "+str(both_eff_dimuon))
            with open("Pion_electrons_eff.txt","a") as file:
                file.write(f"{str(mAp)} {str(logeps)} {str(reco_eff)} {str(trig_eff)} {str(both_eff)} {str(trig_eff_em)} {str(trig_eff_dimuon)} {str(both_eff_em)} {str(both_eff_dimuon)}\n")
                
        if "Eta" in line:
            print("Eta e"+" "+str(logeps)+" "+str(mAp)+" "+str(reco_eff)+" "+str(trig_eff)+" "+str(both_eff)+" "+str(trig_eff_em)+" "+str(trig_eff_dimuon)+" "+str(both_eff_em)+" "+str(both_eff_dimuon))
            with open("Eta_electrons_eff.txt","a") as file:
                file.write(f"{str(mAp)} {str(logeps)} {str(reco_eff)} {str(trig_eff)} {str(both_eff)} {str(trig_eff_em)} {str(trig_eff_dimuon)} {str(both_eff_em)} {str(both_eff_dimuon)}\n")
                
        if "Brem" in line:
            print("Brem e"+" "+str(logeps)+" "+str(mAp)+" "+str(reco_eff)+" "+str(trig_eff)+" "+str(both_eff)+" "+str(trig_eff_em)+" "+str(trig_eff_dimuon)+" "+str(both_eff_em)+" "+str(both_eff_dimuon))
            with open("Brem_electrons_eff.txt","a") as file:
                file.write(f"{str(mAp)} {str(logeps)} {str(reco_eff)} {str(trig_eff)} {str(both_eff)} {str(trig_eff_em)} {str(trig_eff_dimuon)} {str(both_eff_em)} {str(both_eff_dimuon)}\n")
                
