
import subprocess
import csv
attachments={"methyl":"C","ethyl":"CC", "methanol":"CO","ethanol":"CCO"}
counter =0
length=0
modded_ligand=''
new_name=''
subprocess.call("rm -r *.png", shell=True)				#erase any old images
with open("Candidate_smile.txt","r") as f:
	reader=csv.reader(f)

	for row in reader:
		for col in row:
			length=len(col)	#getting length of SMILE string

			
			subprocess.call(['bash', 'mol_convert.sh', col,str(counter)])
			if "C(O" in col or "C(=O)O" in col or "OC" in col:						#we only mod the ligands that have these groups
				
				if ("C(O" in col):	
					ind=col.find("C(O")							#this is for single bonded oxygens that are branched from main chain
					for key in attachments:
						
						modded_ligand=col[:ind+3]+attachments[key]+col[ind+3:]
						new_name=str(counter)+"_modded_"+key
						subprocess.call(['bash', 'mol_convert.sh', modded_ligand,new_name])
				if "OC(=" in col and col.find("OC(=")==0:							#terminal oxygens
					for key in attachments:
						
						modded_ligand=attachments[key]+col
						new_name=str(counter)+"_modded_"+key
						subprocess.call(['bash', 'mol_convert.sh', modded_ligand,new_name])
				if "OC(=" not in col and "OC" in col and col.find("OC")==0:			#terminal oxygens attached to a ring. have to check index so we dont add to COC
					for key in attachments:
						modded_ligand=attachments[key]+col
						new_name=str(counter)+"_modded_"+key
						subprocess.call(['bash', 'mol_convert.sh', modded_ligand,new_name])
				if "C(=O)O" in col:									#carboxylic acid
					ind=col.find("C(=O)O")
					for key in attachments:

						modded_ligand=col[:ind+6]+attachments[key]+col[ind+6:]
						new_name=str(counter)+"_modded_"+key
						subprocess.call(['bash', 'mol_convert.sh', modded_ligand,new_name])
				
				
			counter=counter+1			#counter used for naming


