#!/usr/bin/env python2

import re
# from bs4 import BeautifulSoup

# TODO: input file as command line argument, exit if not provided
inf = 'testdata/blog-small-example.xml'
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

# TODO extract blogpost title as well?

output = open(ouf, 'r')
filetext = output.read()
output.close()

# movie titles
# NOTE: only works if nothing but movie titles are bolded
movies = re.findall("&lt;b&gt;(.*?)&lt;/b&gt;", filetext)
print movies

# movie ratings
# NOTE: could movie title and rating get out of sync?
ratings = re.findall(" ([0-9]/10)", filetext)
print ratings

# Extract the sections of interest from those

# fobj = open('more_output.xml', 'r')
# soup = BeautifulSoup(fobj, 'lxml')

# print soup.prettify()

# todo - get all the titles as well together with the content?
# todo - extract only bold, and ratings.


# contentTag = soup.content
# print contentTag.contents


# aDict = soup.find_all({'title': True, 'content': True})
# interest = soup.find_all('title')

# print(interest)

# fobj.close()
