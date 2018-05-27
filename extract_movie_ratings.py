#!/usr/bin/env python2

import re
# import string

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

# remove any lines not containing term='filmfern'
