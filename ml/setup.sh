#!/bin/bash
mkdir images
mkdir data
mkdir data/scores
mkdir bin
mkdir models

virtualenv --python=python3.4 env
source venv/bin/activate

pip3 install -r requirements.txt
