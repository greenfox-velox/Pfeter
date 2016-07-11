// Create a webserver that can receive any request to any path. It should respond the path name, the request methos and the current time.

var http = require('http');

var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Path: ' + req.url + ' Request method: ' + req.method + ' Time: ' + Date());
});

server.listen(3000, '127.0.0.1');
console.log('Server running');
