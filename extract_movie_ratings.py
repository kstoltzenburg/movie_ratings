#!/usr/bin/env python2

# Repository:    https://github.com/kstoltzenburg/movie_ratings
# Description:   Extract movie titles and rating
#                from the xml export of a blog
# Example input: ./testdata/blog-small-example.xml

import re
import sys

if len(sys.argv) != 2:
    print "Please provide an input file"
    print "usage: python " + sys.argv[0] + " <inputfile>"
    sys.exit(1)

inf = sys.argv[1]
ouf = 'output.xml'

# from input, split lines by category, write to output
fobj = open(inf, 'r')
output = open(ouf, 'w')

for eachLine in fobj:
    # split lines by adding a line ending before each category tag
    split_line = re.sub('<category', '\n<category', eachLine)
    output.write(split_line)
fobj.close()
output.close()

# Only keep the lines we're interested in ('filmfern')
output = open(ouf, 'r')
lines = output.readlines()
output.close()

output = open(ouf, 'w')
for line in lines:
    if 'filmfern' in line:
        output.write(line)
output.close()

# Extract sections of interest
output = open(ouf, 'r')
filetext = output.read()
output.close()

# TODO extract blogpost title as well?

# movie titles, ranking
# NOTE: brittle, relies on a consistent structure in the xml
# FIXME: currently fails to retrieve all movies and their ratings

# regexes matching movie title and rating
re_b = "&lt;b&gt;(.*?)&lt;/b&gt;.*? ([0-9]?.?[0-9]/10)"
re_bold = "bold;\"&gt;(.*?)&lt.*? ([0-9]?.?[0-9]/10)"


movie_ranking = re.findall(re_b, filetext)
movie_ranking.extend(re.findall(re_bold, filetext))

# write extracted data in file line by line
output = open(ouf, 'w')

for item in movie_ranking:
    output.write("%s\n" % ', '.join(map(str, item)))

output.close()

# Report on data retrieved
print "Input file: " + inf
print str(len(movie_ranking)) + " movies and rankings extracted"
print "Output file: " + ouf
