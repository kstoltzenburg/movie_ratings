#!/bin/bash

# Repository:    https://github.com/kstoltzenburg/movie_ratings
# Description:   Extract movie titles and rating
#                from the xml export of a blog
# Example input: ./testdata/blog-small-example.xml

# usage message

# set -x

if [ -z "$1" ]
then 
    echo "Please provide an input file"
    echo "usage: sh " + "$0" + " <inputfile>"
    exit 1
fi

inf="$1" 
ouf="movies_rated_sh.txt"

# preprocess input - each blogpost in its own line
# http://tldp.org/LDP/abs/html/x23170.html - sed in bash
sed -e "s/<\/updated>/<\/updated>\\n/g" "$inf" > "$ouf" 

# Only keep the lines we're interested in ('filmfern')
sed -n '/filmfern/p' "$ouf" > "$ouf.tmp" 
mv "$ouf.tmp" "$ouf"

exit

