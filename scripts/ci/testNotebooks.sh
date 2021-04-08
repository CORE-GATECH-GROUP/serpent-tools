#!/bin/bash

# Script to convert jupyter notebooks to python and execute
# Issue 69

# Must be run from the main directory of the project

set -e

if [ ! -d examples ]; then
	echo 'Examples directory does not exist'
	exit 1
fi

echo "jupyter version: $(jupyter --version)"
echo "nbconvert version: $(jupyter nbconvert --version)"

# Make a temporary directory
# Copy over python files

tmp_dir=$(mktemp -d)
orig_dir=$(pwd)

# Remove temp dir on exit
trap "rm -rf $tmp_dir && cd $orig_dir && echo Temporary directory $tmp_dir removed" EXIT

cp examples/*py $tmp_dir
cp examples/myConfig.yaml $tmp_dir

jupyter nbconvert --to python --output-dir=$tmp_dir examples/*.ipynb

cd $tmp_dir 

for pyFile in *.py; do
	# comment out the get_ipython functions
	sed -i 's/get_ipython/#get_ipython/' $pyFile
	outFile=out_$pyFile
	python $pyFile > $outFile
	if [ $? == 0 ]; then
		echo Script $pyFile passed
	else
		echo Script $pyFile failed
        cat $outFile
		exit 1
	fi
done
