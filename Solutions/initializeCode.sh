#!/bin/bash
#script for initialize all empty code, must be run with root
for ((i=2600; i<3500;i++))
do
    filename="$i."
    mkdir $filename
    sudo chown -R jerryhu $filename
    cd $filename
    touch python.py
    touch cpp.cpp
    sudo chown -R jerryhu python.py cpp.cpp
    cd ..
done
echo "Done initializing..."
