#!/bin/bash

#python3 IC50_selector.py && python3 ligand_converter.py

for ligand in $(ls pdb/*pdb); do
	
	echo $ligand
	obabel $ligand -O pdbqt/$ligandname.pdbqt
done