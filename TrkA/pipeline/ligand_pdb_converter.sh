#!/bin/bash


SMILE=$2

obabel -:${2} -O pdb/${1}.pdb --gen3d
echo to pdb










