#!/usr/bin/perl
use LWP::Simple;

$url = @ARGV[0];
$res = get($url);
if (defined $res) {
    print $res;
} else {
    exit -1;
}