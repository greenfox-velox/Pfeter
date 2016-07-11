// Create a webserver with express, that can receive any request to any path. It should respond the path name, the request methos and the current time.

var express = require('express');

var app = express();

app.get('/', function(req, res) {
  res.send('Path: ' + req.url + ' Request method: ' + req.method + ' Time: ' + Date());
});

app.listen(3000);
console.log('Server running');
