#!/bin/bash

# test runner for the scripts to extract movie titles and rating
# https://github.com/kstoltzenburg/movie_ratings
# 
# Runs a script on ./testdata/blog-small-example.xml
# Compares the output with ./gold/movies_rated.txt

# set -x
set -u
set -e

# TODO: make this an validated input value
type=python

input=./testdata/blog-small-example.xml
output=./movies_rated_$type.txt
gold=./gold/movies_rated.txt

# run python variant
echo "... run $type script"
$type ./extract_movie_ratings.py $input

# compare the output
echo "... comparing $output with gold file ($gold)"

if cmp $output $gold
then
    echo "Success! Movies and ratings extracted as expected."
else
    echo "Failure! Movies and ratings not extracted as expected."
    echo "Please check $output"
fi
