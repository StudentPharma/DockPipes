import csv

with open("ligand_list.csv","r",newline='') as f:
    counter=0
    reader=csv.reader(f, delimiter='\t')
    for row in reader:

        for col in row:
            counter+=1

            if "VALUE" in col:
                counter=counter-1       #finding the standard value
                break
        break

    f.seek(0)

    with open ("temp.csv", "w", newline='') as tmp:
        writer=csv.writer(tmp, delimiter='\t')

        for row in reader:
            print(row)
            writer.writerow(row)
            break                       #have to write the first row with the column headers
        f.seek(0)
        next(reader)
        ligand_counter=0
        for row in reader:              #Looping through the rest of the rows
            if row[counter]:                #checks if the IC50 value isnt null

                if 100>float(row[counter])>0:       #filtering out IC50s below 100nM
                    writer.writerow(row)
                    print(row[counter])
                    ligand_counter+=1
        f.close()
        tmp.close()

with open ("ligand_list.csv", "w", newline='') as f:
    writer=csv.writer(f, delimiter='\t')
    with open("temp.csv", "r", newline='') as tmp:
        reader = csv.reader(tmp, delimiter='\t')

        for row in reader:
            writer.writerow(row)
        tmp.close()
        f.close()

print(ligand_counter, "Ligands parsed")
