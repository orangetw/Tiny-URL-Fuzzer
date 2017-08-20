#!/usr/bin/ruby
require 'net/http'
require 'uri'

res = Net::HTTP.get_response( URI.parse(ARGV[0]) )
puts res.body