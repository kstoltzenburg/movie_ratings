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
my $filename = $ARGV[0];

print "\n$filename\n";

# -- preprocessing
# all blogposts are written in one long line in the xml file, 
# beginning of an individual blogpost is marked by <category>
# split them up by inserting a line-break before <category> element

$^I = '.bak';

while (<>) {
    s/<category/\n<category/g;
    print;
}


# Read in the xml file
#open (my $fh, '<', $filename ) or die "Can't open $filename: $!";
#    while ( my $line = <$fh> ) {
#        if ($line =~ /wanted text/ ) {
#           print $line;
#        }
#    };
#    close $fh;



# exract information - movie title (bold?), rating ([0-9]/10), year published
# store information, order, print out

