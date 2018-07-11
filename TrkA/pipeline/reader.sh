#!/bin/bash
echo "">candidate_list.csv
echo "Computing Best Ligands..."
for file in $(ls logs/*.txt); do
	
	python3 log_reader.py $file
done

python3 evaluator.py candidate_list.csv > Candidate_smile.txt

echo "Complete"
