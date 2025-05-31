> "counts.txt"
for ind in {2..100}
do
	ind_full=$(printf "%04d" $ind)
	filename=/pnfs/e1039/persistent/users/kenichi/data_emb_e906/$ind_full/embedding_data.root
	#echo $filename
	root -l -b -q 'ana_result.C("'$filename'")' | tee -a "counts.txt"
done
