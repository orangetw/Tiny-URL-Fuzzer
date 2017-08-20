#!/usr/bin/nodejs
var url = require('url');

var x = url.parse(process.argv[2]);
console.log('scheme=' + x.protocol.replace(':', '') + ', host=' + x.host + ', port=' + (x.port?x.port:''));
