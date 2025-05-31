R__LOAD_LIBRARY(libktracker)
R__LOAD_LIBRARY(libktracker)
void ana_result(std::string fname="/pnfs/e1039/persistent/users/kenichi/data_emb_e906/0002/embedding_data.root"){
	//std::string fname("file2.root");
	std::unique_ptr<TFile> file(TFile::Open(fname.c_str(),"READ"));
	TTree * tree=(TTree*) file->Get("tree");
	SQHitVector_v1* hit_vector=new SQHitVector_v1;
	tree->SetBranchAddress("SQHitVector",&hit_vector);
	std::list<float> size_list;
	int ave_size=0;
	int count=0;
	for (int i=0;i<tree->GetEntries();i++){
		tree->GetEntry(i);
		//std::cout<<i<<" "<<hit_vector->size()<<std::endl;
		ave_size+=hit_vector->size();
		count++;
		size_list.push_back(hit_vector->size());
		
	}
	
	float average=float(ave_size)/float(count);
	float diffsum=0.0;
	float stdev=0; 
	for(int fsize : size_list){
		std::cout<<fsize<<std::endl;
		diffsum+=(float(fsize)-average)*(float(fsize)-average);
	}
	stdev=sqrt(diffsum/float(count));

	std::cout<<fname<<" "<<average<<" "<<stdev<<std::endl;
	
}	
