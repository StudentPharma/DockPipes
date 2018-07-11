#!/bin/bash
mkdir pdbqt
mkdir pdb
python3 CSV_parser.py uncurated_list.csv && python3 ligand_converter.py

echo "Converting to pdbqt"

for ligand in $(ls pdb/*pdb); do
	
	ligandname=`echo "$ligand" | cut -d'.' -f1| cut -d'/' -f2`
	obabel $ligand -O pdbqt/$ligandname.pdbqt
	echo "Converted to pdbqt"
done

echo Ligand Prep Complete!

mkdir configs
mkdir output
mkdir logs

echo Creating Configuration File...
constant_suffix="_conf.txt"
for ligand in $(ls pdbqt/*pdbqt); do
	#echo $ligand
	ligandname=`echo "$ligand"|cut -d'/' -f2`
	
	bash ./conf_maker.sh $ligandname 
	

	config_path="configs/${ligandname}_conf.txt"
	#config_path="$config_path$constant_suffix"
	
	echo Docking ${ligandname}...
	vina --config $config_path

done

#!/bin/bash
echo "">candidate_list.csv
echo "Computing Best Ligands..."
for file in $(ls logs/*.txt); do
	
	python3 log_reader.py $file
done

python3 evaluator.py candidate_list.csv > Candidate_smile.txt

echo "Complete"