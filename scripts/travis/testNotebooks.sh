#!/bin/bash

# Script to convert jupyter notebooks to python and execute
# Issue 69

# Must be run from the main directory of the project

if [ ! -d examples ]; then
	echo 'Examples directory does not exist'
	exit 1
fi

cd examples

echo "jupyter version: $(jupyter --version)"
echo "nbconvert version: $(jupyter nbconvert --version)"

for nbFile in *.ipynb; do
	jupyter nbconvert --to python $nbFile
done

for pyFile in *.py; do
	# comment out the get_ipython functions
	sed -i 's/get_ipython/#get_ipython/' $pyFile
	outFile=out_$pyFile
	python $pyFile > $outFile
	if [ $? == 0 ]; then
		echo Script $pyFile passed
		rm $pyFile $outFile
	else
		echo Script $pyFile failed
		exit 1
	fi
done

cd ..

