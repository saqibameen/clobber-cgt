#!/bin/bash

echo "Installing Cython!"
pip install cython

echo "Compiling program in Cython"
python3 -u setup.py build_ext --inplace

