import csv

counter = 0
standard_type_counter = 0
standard_value_counter = 0
Ligand_ID_counter = 0
Molecular_weight_counter = 0
AlogP_counter = 0
PSA_counter = 0
canonical_smiles_counter = 0

with open("uncurated_list.csv", "r", newline='') as f:
    reader = csv.reader(f, delimiter='\t')  # we download as a .txt but with the tab as delimiter from CHEMBL

    for row in reader:  # we go through first row and find the locations of the different columns we are interested in

        for col in row:


            counter += 1
            if "STANDARD_TYPE" == col:

                standard_type_counter=counter-1
            elif "STANDARD_VALUE" in col:

                standard_value_counter=counter-1
            elif "CMPD_CHEMBLID" == col:

                Ligand_ID_counter=counter-1
            elif "LOG" in col:

                AlogP_counter=counter-1
            elif "PSA" in col:

                PSA_counter=counter-1
            elif "SMILE" in col:
                canonical_smiles_counter=counter-1
            elif "MOLWEIGHT" in col:
                Molecular_weight_counter=counter-1
        break
    f.seek(0)  # brings us back to the beginning of the file

    with open ("curated_ligand_list.csv", "w", newline='') as tmp:
        writer=csv.writer(tmp, delimiter='\t')

        for row in reader:

            writer.writerow((row[Ligand_ID_counter],row[Molecular_weight_counter],row[AlogP_counter],
                                    row[PSA_counter],row[canonical_smiles_counter], row[standard_type_counter],"STANDARD_VALUE (nM)"))
            break                       #have to write the first row with the column headers
        f.seek(0)
        next(reader)

        for row in reader:              #only writing rows with standard values within our specifications
            if 'Ki'==row[standard_type_counter] and (row[standard_value_counter] is not ""):
                if float(row[standard_value_counter])<10:
                    writer.writerow((row[Ligand_ID_counter],row[Molecular_weight_counter],row[AlogP_counter],
                                    row[PSA_counter],row[canonical_smiles_counter], row[standard_type_counter],row[standard_value_counter]))
            if 'EC50'==row[standard_type_counter] and (row[standard_value_counter] is not ""):
                if float(row[standard_value_counter])<10:
                    writer.writerow((row[Ligand_ID_counter], row[Molecular_weight_counter], row[AlogP_counter],
                                    row[PSA_counter], row[canonical_smiles_counter], row[standard_type_counter],
                                    row[standard_value_counter]))
            if 'IC50'==row[standard_type_counter] and (row[standard_value_counter] is not ""):
                if float(row[standard_value_counter])<10:
                    writer.writerow((row[Ligand_ID_counter], row[Molecular_weight_counter], row[AlogP_counter],
                                    row[PSA_counter], row[canonical_smiles_counter], row[standard_type_counter],
                                    row[standard_value_counter]))
            if 'Kd'==row[standard_type_counter] and (row[standard_value_counter] is not ""):
                if float(row[standard_value_counter])<10:
                    writer.writerow((row[Ligand_ID_counter], row[Molecular_weight_counter], row[AlogP_counter],
                                    row[PSA_counter], row[canonical_smiles_counter], row[standard_type_counter],
                                    row[standard_value_counter]))







        f.close()
        tmp.close()
'''
with open ("ligand_list.csv", "w", newline='') as f:
    writer=csv.writer(f, delimiter='\t')
    with open("temp.csv", "r", newline='') as tmp:
        reader = csv.reader(tmp, delimiter='\t')

        for row in reader:
            writer.writerow(row)
        tmp.close()
        f.close()

print(ligand_counter, "Ligands parsed")
'''
