var ip   = "0.0.0.0";
var http = require('http');
var util = require('util');
// WHILE_LISTS = ['user-agent']

port = process.argv[2];

http.createServer(function (req, res) {
    url = req.connection.address().address + ':' + req.connection.address().port + req.url;
    console.log(util.format("[%s] - http://%s - [%s]", req.connection.remoteAddress,
                url, req.headers['user-agent']||''));

    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end(url + '\n');
}).listen(port, ip);

console.log("Server running at http://" + ip + ":" + port);
