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
