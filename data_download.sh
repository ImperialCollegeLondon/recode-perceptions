#PBS -l walltime=08:00:00
#PBS -l select=1:ncpus=1:mem=1gb

cd $PBS_O_WORKDIR
cd emily/phd/recode-perceptions       # ENTER PATH to recode-perceptions from $PBS_O_WORKDIR

wget http://data.csail.mit.edu/places-private/places365/train_256_places365standard.tar -O input/places365standard_easyformat.tar

cd input
tar -xvf places365standard_easyformat.tar

GLOBIGNORE=$(paste -s -d : keep.txt)
rm -rf places365_standard/train/*
rm -rf places365_standard/val/*
unset GLOBIGNORE
