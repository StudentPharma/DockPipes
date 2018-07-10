import csv
import subprocess
import sys

counter =0
row_sum=0


with open("curated_ligand_list.csv","r",newline='') as f:
	
	reader=csv.reader(f, delimiter='\t')
	
	for row in reader:  #we find which column we have our SMILES in
		
		for col in row: #iterating through the rows
			counter+=1
			
			if "SMILE" in col: 
				counter=counter-1
				break
		break
	
	
	#We have already gone past the first row, no need to skip it. 
	
	progress_counter=0
	percent_complete=0
	

	for x in reader:
		
		if x[counter] is not "":	#some SMILES are empty
			subprocess.call(['bash', 'ligand_pdb_converter.sh',x[0], x[counter]],shell=False)
			progress_counter=progress_counter+1
		

	print(progress_counter,"Molecules converted to PDB")
	f.close()


