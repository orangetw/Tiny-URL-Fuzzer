#!/usr/bin/ruby
require 'addressable/uri'

x = Addressable::URI.parse(ARGV[0])
puts 'scheme=' + x.scheme + ', host=' + x.host + ', port=' + x.port.to_s
    