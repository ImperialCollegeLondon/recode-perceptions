#!/bin/sh
module load anaconda3/personal
module load cuda/10.2
conda env create -f environment.yml

# perform tests
source activate perceptions
conda install -y --file requirements-dev.txt
pytest tests/ -v

# deactivate
conda deactivate
