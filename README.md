# movie_ratings

A repository to tryout different scripting languages, solving a specific task.

## Task

Given an xml export of a blog, we want to extract a list of movie titles and ratings. The blogposts that contain movie reviews have a category term 'filmfern'. Each blogpost can contain multiple movie reviews, with a bolded title and a rating of the form 1-10/10.

Example input:    ./testdata/blog-small-example.xml
Expected output:  ./gold/movies_rated.txt

## Running scripts

~~~~
python ./extract_movie_ratings.py ./testdata/blog-small-example.xml
~~~~

## Check extracted data against expected output

~~~~
sh ./test_extraction.sh <type>
~~~~

where

'''type''' = any of: python
 
