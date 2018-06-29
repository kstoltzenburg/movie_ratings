#!/usr/bin/env python2

import re
from bs4 import BeautifulSoup

input_file = 'testdata/blog-small-example.xml'
output_file = 'output.xml'

# might be to heavy on memory for a large file?
fobj = open(input_file, 'r')
data = fobj.readlines()
fobj.close()

output = open(output_file, 'a')  # append to this file
# for each <category add a new line
for eachLine in data:
    result = re.sub('<category', '\n<category', eachLine)
    output.write(result)

output.close()

# only keep lines containing term='filmfern'
# https://stackoverflow.com/questions/4310659/remove-lines-from-a-text-file-which-do-not-contain-a-certain-string-with-python
with open('output.xml', 'r') as rfp:
    with open('more_output.xml', 'w') as wfp:
        for line in rfp:
            if 'filmfern' in line:
                wfp.write(line)


# Extract the sections of interest from those

fobj = open('more_output.xml', 'r')
soup = BeautifulSoup(fobj, 'lxml')

# aDict = soup.find_all({'title': True, 'content': True})
interest = soup.find_all('title')

print(interest)

fobj.close()
