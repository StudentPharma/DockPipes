import csv
import subprocess
import sys

counter =0
row_sum=0


with open("ligand_list.csv","r",newline='') as f:
	
	reader=csv.reader(f, delimiter='\t')
	
	for row in reader:  #we find which column we have our SMILES in
		
		for col in row: #iterating through the rows
			counter+=1
			
			if "SMILE" in col: 
				counter=counter-1
				break
		break
	
	
	
	
	progress_counter=0
	percent_complete=0
	print("Running")

	for x in reader:
		

		subprocess.call(['bash', 'pipeline.sh',x[0], x[counter]],shell=False)
		progress_counter=progress_counter+1
		#percent_complete=(progress_counter/row_sum)*100	
		#row_sum=0
		#print ("Conversion Progress: "+str(round(percent_complete,2))+"%")

	print(progress_counter,"Molecules converted to PDB")
	f.close()


