#!/usr/bin/ruby
require 'uri'

x = URI(ARGV[0])
puts 'scheme=' + x.scheme + ', host=' + x.host + ', port=' + x.port.to_s
    