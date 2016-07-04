#!/usr/bin/env perl

=pod

Exract information from an xml export of a blog, 
on blogposts about movies containing infomration like 
title, year seen and rating.

=cut

use strict;
use warnings;

# quit unless we have the correct number of arguments

my $num_args = $#ARGV + 1;
if ($num_args != 1) {
    print "\nUsage: script.pl filename\n";
    exit;
};
 
# Read our command line argument
my $infile = $ARGV[0];

# -- preprocessing
# all blogposts are written in one long line in the xml file

# separate blogpost: break <category> elements into a new line
# http://perldoc.perl.org/functions/open.html

open (my $in, "<", $infile)   or die "Can't read input file: $!";
open (my $out, ">", "output.txt") or die "Can't write new file: $!";

while (<$in>) {
    s/<category/\n<category/g;
    print $out $_;
}


# TODO: this all looks *cough* slightly *cough* overhead

# remove unrelevant blogposts: remove lines not containing ("term='filmfern'")

open ($in, "<", "output.txt")   or die "Can't read input file: $!";
open ($out, ">", "output_2.txt") or die "Can't write new file: $!";

while (<$in>) {
    print $out $_ if /term='filmfern'/;
}

#Split by markup bold <b>

open ($in, "<", "output_2.txt")   or die "Can't read input file: $!";
open ($out, ">", "output_3.txt") or die "Can't write new file: $!";

while (<$in>) {
    s/&lt;b&gt;/\n/g;
    print $out $_;
}

close $out;




# exract information - movie title (bold?), rating ([0-9]/10), year published
# store information, order, print out

