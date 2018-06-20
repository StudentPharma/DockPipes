import csv

with open("ligand_list.csv","r",newline='') as f:
	counter=0
	reader=csv.reader(f, delimiter='\t')
	for row in reader: 
		
		for col in row:
			counter+=1
			
			if "VALUE" in col: 
				counter=counter-1
				break
		break
	
	with open ("temp.csv", "w", newline='') as tmp:
		writer=csv.writer(tmp, delimiter='\t')
		
		for row in reader:
			if row[counter]:
				t=type(row[counter])
				print(t)
				print(row[counter])
				if 100>float(row[counter])>0:
					writer.writerow(row)
		f.close()
		tmp.close()
#with open("ligand_list.csv","w"
			
