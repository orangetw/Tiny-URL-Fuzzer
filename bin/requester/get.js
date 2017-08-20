#!/usr/bin/nodejs
var http = require('http');
var url = require('url');

x = url.parse(process.argv[2]);


if (x.host == '') {
  trap();
}

callback = function(response) {
  var str = '';
  response.on('data', function (chunk) {
    str += chunk;
  });
  response.on('end', function () {
    console.log(str);
  });
}

http.get(process.argv[2], callback).end();