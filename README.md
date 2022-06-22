# PyTorch implementation for end-to-end training of a deep learning model

Recode Perceptions is a pyTorch implementation of a deep convolutional neural network model trained on Places365 data, developed by Emily Muller.

This model is trained on a subset of 100K images which have outcome labels that are associated to factors which are relevant for environmental health.

## How to Use this Repository

This repository has 3 core learning components:

- Substantive introduction to environmental health monitoring using imagery: this will give you a brief introduction to this field of research including seminar texts which you can familiarise yourself with.
- Foundations of Deep CNN's using PyTorch: we will demonstrate some core components of pytorch CNN implementation using benchmark datasets and transfer learning. This jupyter notebook is also in the learning folder.
- deep_cnn: you will run the image task locally before exporting the entire folder to the HPC. Here, you will be able to make use of the numerous GPU's for effective hyperparamter optimisation.

The final component of the repository will challenge you to be comfortable with bash scripts and the command line since we will no longer be using jupyter notebooks.

## Overview

- learning/ contains learning material to help you understand the science of deep learning and the substantive background of urban perception.
- demo/ contains a notebook showing how to import a dataset, load a model and run it on that dataset making forward and backward passes.
- deep_cnn/ contains code for full model training pipeline.
- model/ contains an already trained model.
- input/ contains the original image data (to download - see below) and metadata.
- output/ folder for model training outputs.
- tests/ contains unit tests for the codebase.

## Getting started

Clone this repository into your local drive. root_dir will now refer to the /local_path/to_this/directory/recode-perceptions.

```sh
git clone
cd recode-perceptions
pip install -r requirements.txt
```

### Installation

We assume that you're using Python 3.7 with pip installed.

### Setting up a virtual environment

We will set up a virtual environment for running our scripts. In this case, installing specific package versions will not interfere with other programmes we run locally as the environment is contained. Initially, let's set up a virtual environment with python version 3.7:

```
virtualenv --python=python3.7 venv
```

This will create a new folder named venv in your repository. We can activate this environment by running

```
source venv/bin/activate
```

Let's configure our environment by installing all the necessary packages located in requirements.txt

```
pip install -r requirements.txt
```

The final command requires you to have python installed and will install all the packages contained within the requirements.txt file. If an error occurs at this stage, don't panic! Often, this will be a result of python version conflict for a certain package/packages. Make sure that python3.7 version is being used.

### Dataset

The dataset can be downloaded from dropbox. Run wget (below) to download all of the Places365 train/val images (~21GB) and put them in the input/ directory:

```
wget -O /root_dir/recode/input/places365standard_easyformat.tar http://data.csail.mit.edu/places/places365/places365standard_easyformat.tar
```

where root_dir is the path to the recode repository. Unzip/extract all files in the same location

```
tar -xvf places365standard_easyformat.tar
```

We will remove categories which are not substantively interesting for the theme of environmental health. To do so run

```
cd input
GLOBIGNORE=$(paste -s -d : keep.txt)
cd places365standard_easyformat/places365_standard/train
rm -rf *
cd ../val
rm -rf *
unset GLOBIGNORE
```

GLOBIGNORE specifies folders which should be ignored when performing recursive deletes.

Download the test set

```
wget -O /root_dir/recode/input/places365standard_easyformat/ http://data.csail.mit.edu/places/places365/test_256.tar
```

The datasets were not released by us and we do not claim any rights on them. Use the datasets at your responsibility and make sure you fulfill the licenses that they were released with. If you use any of the datasets please consider citing the original authors of [Places365](http://places2.csail.mit.edu/PAMI_places.pdf).

### Testing

To run all tests, install pytest. After installing, run

```
pytest tests/ -v
```

### License

This code and the pretrained model is licensed under the MIT license.


