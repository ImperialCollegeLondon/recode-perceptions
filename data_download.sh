#PBS -l walltime=08:00:00
#PBS -l select=1:ncpus=1:mem=1gb

cd $PBS_O_WORKDIR
cd emily/phd/recode-perceptions/input   # ENTER PATH to recode-perceptions from $PBS_O_WORKDIR

# TRAINING IMAGES
wget http://data.csail.mit.edu/places-private/places365/places365standard_easyformat.tar -O places365standard_easyformat.tar

filename='keep.txt'
while read line; do
tar -xvf places365standard_easyformat.tar places365_standard/train/$line
tar -xvf places365standard_easyformat.tar places365_standard/val/$line
done < $filename

rm places365standard_easyformat.tar