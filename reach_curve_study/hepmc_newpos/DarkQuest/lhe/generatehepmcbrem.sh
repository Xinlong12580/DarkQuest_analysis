Alleps=()

startn=-9.0
endn=-3.0
interval=0.3

current=$startn
while (( $(echo "$current <= $endn" | bc -l) )); do
	Alleps+=("$current")
	current=$(echo "$current + $interval" | bc)
done

echo "${Alleps[@]}"
Allmumass=("0.22" "0.25" "0.27" "0.29" "0.31" "0.33" "0.35" "0.37" "0.39" "0.41" "0.43" "0.45" "0.47" "0.49" "0.51" "0.53" "0.55" "0.57" "0.59" "0.61" "0.63" "0.65" "0.67" "0.69" "0.71" "0.73" "0.75" "0.77" "0.79" "0.81" "0.83" "0.85" "0.87" "0.89" "0.91" "0.93" "0.95" "0.97" "0.99" "1.01" "1.03" "1.05" "1.07" "1.09" "1.11" "1.13" "1.15" "1.17" "1.19" "1.21" "1.23" "1.25" "1.27" "1.29" "1.31" "1.33" "1.35" "1.37" "1.39" "1.41" "1.43" "1.45" "1.47" "1.49")
Allemass=("0.0011" "0.0013" "0.0016" "0.002" "0.0025" "0.003" "0.0035" "0.004" "0.005" "0.007" "0.01" "0.02" "0.04" "0.06" "0.08" "0.1" "0.12" "0.14" "0.16" "0.18" "0.2" "0.22" "0.25" "0.27" "0.29" "0.31" "0.33" "0.35" "0.37" "0.39" "0.41" "0.43" "0.45" "0.47" "0.49" "0.51" "0.53" "0.55" "0.57" "0.59" "0.61" "0.63" "0.65" "0.67" "0.69" "0.71" "0.73" "0.75" "0.77" "0.79" "0.81" "0.83" "0.85" "0.87" "0.89" "0.91" "0.93" "0.95" "0.97" "0.99" "1.01" "1.03" "1.05" "1.07" "1.09" "1.11" "1.13" "1.15" "1.17" "1.19" "1.21" "1.23" "1.25" "1.27" "1.29" "1.31" "1.33" "1.35" "1.37" "1.39" "1.41" "1.43" "1.45" "1.47" "1.49")
#Allemass=("0.0011")

> "Brem_electrons_3300_3800.txt"
{
for eps in "${Alleps[@]}"; do
	for emass in "${Allemass[@]}"; do
		echo ./e/brem/SpinQuestAprimeToElectronsLHE_Brem_mAp_"$emass"_GeV.txt
		if [ -e ./e/brem/SpinQuestAprimeToElectronsLHE_Brem_mAp_"$emass"_GeV.txt ]; then
			./bin/displacedHepmc ./e/brem/SpinQuestAprimeToElectronsLHE_Brem_mAp_"$emass"_GeV.txt Brem_"$emass"_$eps.root Brem electron 0 $eps $emass 3300 3800 0 | tee -a "Brem_electrons_3300_3800.txt"		
		fi
	done
done
}

> "Brem_muons_3300_3800.txt"
{
for eps in "${Alleps[@]}"; do
	for mumass in "${Allmumass[@]}"; do
		echo ./mu/brem/SpinQuestAprimeToMuonsLHE_Brem_mAp_"$mumass"_GeV.txt
		if [ -e ./mu/brem/SpinQuestAprimeToMuonsLHE_Brem_mAp_"$mumass"_GeV.txt ]; then
			./bin/displacedHepmc ./mu/brem/SpinQuestAprimeToMuonsLHE_Brem_mAp_"$mumass"_GeV.txt Brem_"$mumass"_$eps.root Brem muon 0 $eps $mumass 3300 3800 0 | tee -a "Brem_muons_3300_3800.txt"		
		fi
	done
done
}
echo finished

