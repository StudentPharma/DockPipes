#!/bin/bash

SMILE=$2


obabel -:$SMILE -O pdb/${1}.pdb --gen3d



