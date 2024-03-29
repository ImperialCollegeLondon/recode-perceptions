# PyTorch implementation for end-to-end training of a deep learning model

## Description

Recode Perceptions is a PyTorch implementation of a deep convolutional neural network model trained on Places365 data, developed by Emily Muller.

This model is trained on a subset of 100K images which have outcome labels that are associated to factors which are relevant for environmental health.

## Learning Outcomes

- Be aware of different types of Computer Vision tasks
- Load an image dataset in PyTorch
- Be able to explain what a convolutional layer does and how it's different from a fully-connected layer
- Identify different components of a CNN
- Load a pre-trained model in PyTorch
- Be able to use PyTorch to train a model on a dataset
- Iterate on design choices for model training

## Requirements

### Academic

### System

| Program                                                    | Version                  |
| ---------------------------------------------------------- | ------------------------ |
| [Python](https://www.python.org/downloads/)                | >= 3.7                   |
| [Anaconda](https://www.anaconda.com/products/distribution) | >= 4.1                   |
| Access to Imperial's HPC (optional)                        | Last updated: 22-07-2022 |

## Getting Started

## How to Use this Repository

This repository has 3 core learning components:

| Title                                            | Description                                                                                                                                                                                                     | Location                                   | Key Learning Objectives                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Introduction to Environmental Health and Imagery | This is a short video, introducing the domain, methods and describing some pioneering work in this field                                                                                                        | [Video](https://youtu.be/-b92eKqxS0A)                             | Introduction to the field. Understand different methods. Understand different types of data. Be aware of seminal research.                                                                                                                                                                                                        |
| Foundations of Deep CNN's using PyTorch          | A Jupyter Notebook familiarising students with core components of deep learning framework using PyTorch.                                                                                                        | [Jupyter Notebook](docs/1-cnn-intro.ipynb) | Be aware of different types of Computer Vision tasks. Be able to explain what a convolutional layer does and how it's different from a fully-connected layer. Identify different components of a CNN. Load an image dataset in PyTorch. Load a pre-trained model in PyTorch. Be able to use PyTorch to train a model on a dataset |
| `deep_cnn`                                       | This module contains all the code needed to fine-tune a deep neural network on the Places365 classification task. Detailed documentation is provided in the folder README.md but requires to be set up (below). | [deep_cnn](docs/2-cnn-training.md)         | Use terminal for executing python scripts Train a PyTorch model and visualise results. Export training to the HPC. Implement bach script Iterate on model hyperparameters to optimise model.                                                                                                                                      |
| Prediction and Interpretability using Object Detections                                       | In the final analysis, the pretrained network from `deep_cnn` is used to predict on the test set. Explainable features, specifically Object Detections are extracted from the images and correlated to each scene category. |  [Jupyter Notebook](docs/3-cnn-prediction.ipynb)     | Run inference using a pre-trained model. Explore Tensorflow DeepLab API model.                                                                                                                                     |

The suggested way to use this repository is as follows:

- Continue with set-up as detailed below.
- Complete learning materials 1 ([Video](https://youtu.be/-b92eKqxS0A)) and 2 ([Jupyter Notebook](docs/1-cnn-intro.ipynb)).
- Continue to model training in 3 ([deep_cnn](docs/2-cnn-training.md)).
- Finally complete inference using pre-trained model from the previous step in 4 ([Jupyter Notebook](docs/3-cnn-prediction.ipynb))

## Getting started

Clone this repository into your local drive.

```sh
git clone https://github.com/ImperialCollegeLondon/recode-perceptions.git
cd recode-perceptions
```

### Setting up a virtual environment

We will set up a virtual environment for running our scripts. In this case, installing specific package versions will not interfere with other programmes we run locally as the environment is contained. Initially, let's set up a virtual environment:

```sh
conda env create -f environment.yml
```

This will create a new folder for the virtual environment named `perceptions` in your repository. We activate this environment by running

```sh
conda activate perceptions
```

All the dependencies are installed along with the virtual environment. We will manually install the development tools since we do not need those dependencies when we export to HPC and create a virtual environment there.

### Setting up the development virtual environment

The `pytest` and pre-commit module is required for running tests and formatting. This can be installed by running:

```sh
conda install --file requirements-dev.txt
```

Now run the tests below to make sure everything is set up correctly. Then, proceed to the video.

### Testing

To run all tests, install `pytest`. After installing, run

```sh
pytest tests/ -v
```

## Project Structure

```bash
recode-perceptions
│   README.md
│   .pre-commit-config.yaml             # pre-commit options file
│   setup.cfg                           # set-up for pre-commit
│   requirements-dev.txt                # python packages for development
│   requirements.txt                    # python packages for running programme
│   environment.sh                      # HPC environment set-up (see)
│   submit.pbs                          # job submission for HPC (see)
│
└───deep_cnn                            # module for model training (see)
│   │   __init__.py
│   │   __main__.py
│   │   logger.py
│   │   utils.py
│   │   dataset_generator.py
│   │   model_builder.py
│   │   train.py
│   │   train_model.py
|
└───docs                                # learning materials
│   │   1-cnn-intro.ipynb
|   │   2-cnn-training.md
│
└───input                               # folder to download images
│   │   keep.txt                        # images to remove
│   └───places365standard_easyformat    # images downloaded (see)
│   │   │   ...                         # metadata
│   │   └───places365_standard
│   │   │   └───train
│   │   │   └───val
│
└───outputs
│   └───logger                          # logging output from model training
│   └───models                          # save model checkpoints
│   └───results                         # save model training metrics
│
└───tests                               # folder for testing
│   └───places_test_input
│   │   ...
```
