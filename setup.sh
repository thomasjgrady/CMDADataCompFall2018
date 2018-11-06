#!/bin/bash
mkdir images
mkdir data
mkdir bin
mkdir models

virtualenv --python=python3.6 venv

pip3 install -r requirements.txt
