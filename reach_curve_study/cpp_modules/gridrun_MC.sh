#!/bin/bash
ls / 
#ls -a /home
#ls /scratch
#ls -a /usr
#ls /cvmfs
data_type=$1
n_events=$2
in_file=$3
out_file=$4
config_file=$5

if [ -z ${CONDOR_DIR_INPUT+x} ]; then
	CONDOR_DIR_INPUT=./input;
	echo "CONDOR_DIR_INPUT is initiallized as $CONDOR_DIR_INPUT"
else
	echo "CONDOR_DIR_INPUT is set to '$CONDOR_DIR_INPUT'";
fi

if [ -z ${CONDOR_DIR_OUTPUT+x} ]; then
	CONDOR_DIR_OUTPUT=./out;
	mkdir -p $CONDOR_DIR_OUTPUT
	echo "CONDOR_DIR_OUTPUT is initiallized as $CONDOR_DIR_OUTPUT"
else
	echo "CONDOR_DIR_OUTPUT is set to '$CONDOR_DIR_OUTPUT'";
fi
ls
echo "hello, grid." | tee out.txt $CONDOR_DIR_OUTPUT/out.txt
echo "HOST = $HOSTNAME" | tee -a out.txt $CONDOR_DIR_OUTPUT/out.txt
pwd | tee -a out.txt $CONDOR_DIR_OUTPUT/out.txt
tar -xzvf $CONDOR_DIR_INPUT/input_MC.tar.gz
tar -xzvf public_MC.tar.gz
tar -xzvf e1039_MC.tar.gz
ls -lh | tee -a out.txt $CONDOR_DIR_OUTPUT/out.txt
source core-inst/this-e1039.sh
export DIR_TOP='./'
export LD_LIBRARY_PATH="./support/MC_module":$LD_LIBRARY_PATH
echo $in_file
#in_file="${file_name:1}"
echo "bare_in_file:"
bare_in_file="${in_file:1}"
echo $bare_in_file
ls
time root -b -q RecoSim.C\(\"\",\"$data_type\",$n_events,\"$bare_in_file\",\"$out_file\",\"$config_file\",true\)
echo  RecoSim.C\(\"\",\"$data_type\",$n_events,\"$bare_in_file\",\"$out_file\",\"$config_file\",true\)
RET=$?
if [ $RET -ne 0 ] ; then
	echo "Error in RecoSim.C: $RET"
	exit $RET
fi
mv *.root $CONDOR_DIR_OUTPUT/
echo "gridrun.sh finished!"
