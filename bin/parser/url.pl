#!/usr/bin/perl
use URI;

if (@ARGV != ''){
    $url = @ARGV[0];
    $x = URI->new($url);
    print 'scheme=' . $x->scheme . ', host=' . $x->host . ", port=" . $x->port;
}