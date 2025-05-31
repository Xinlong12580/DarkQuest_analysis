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
Allmumass=("0.22" "0.25" "0.27" "0.29" "0.31" "0.33" "0.35" "0.37" "0.39" "0.41" "0.43" "0.45" "0.47" "0.49" "0.51" "0.53" "0.55")
Allemass=("0.0011" "0.0013" "0.0016" "0.002" "0.0025" "0.003" "0.0035" "0.004" "0.005" "0.007" "0.01" "0.02" "0.04" "0.06" "0.08" "0.1" "0.12" "0.14" "0.16" "0.18" "0.2" "0.22" "0.25" "0.27" "0.29" "0.31" "0.33" "0.35" "0.37" "0.39" "0.41" "0.43" "0.45" "0.47" "0.49" "0.51" "0.53" "0.55")

> "Eta_electrons_500_600.txt"
{
for eps in "${Alleps[@]}"; do
	for emass in "${Allemass[@]}"; do
		if [ -e ./e/eta/m_$emass.lhe ]; then
			./bin/displacedHepmc e/eta/m_$emass.lhe Eta_"$emass"_$eps.root Eta electron 0 $eps $emass 500 600 1 | tee -a "Eta_electrons_500_600.txt"		
		fi
	done
done
}
exit
> "Pion_electrons_500_600.txt"
{
for eps in "${Alleps[@]}"; do
	for emass in "${Allemass[@]}"; do
		if [ -e ./e/pion/m_$emass.lhe ]; then
			./bin/displacedHepmc e/pion/m_$emass.lhe Pion_"$emass"_$eps.root Pion electron 0 $eps $emass 500 600 1 | tee -a  "Pion_electrons_500_600.txt"	
		fi
	done
done
}
<<COMMENT
> "Eta_muons_500_600.txt"
{
for eps in "${Alleps[@]}"; do
	for mumass in "${Allmumass[@]}"; do
		if [ -e ./mu/eta/m_$mumass.lhe ]; then
			./bin/displacedHepmc mu/eta/m_$mumass.lhe Eta_"$mumass"_$eps.root Eta muon 0 $eps $mumass 500 600 1 | tee -a "Eta_muons_500_600.txt"		
		fi
	done
done
}
COMMENT
echo finished

