'use strict';

var express = require('express');
var http    = require('http');
//var endMw = require('express-end');
var endMw = require('../');
var app = express();

app.use(endMw);

var count = 0;

app.use(function(req, res, next) {
  var current = ++count;
  console.log('[%d] app.use()', current);

  res.once('close',  function() {
    console.log('[%d] app.use(): res.once(close)', current);
  });

  res.once('end',    function() {
    console.log('[%d] app.use(): res.once(end)', current);
  });

  res.once('finish', function() {
    console.log('[%d] app.use(): res.once(finish)', current);
  });

  next();
});


var httpPort = 8080;
var RESPONSE_DELAY = 1000; // Milliseconds

app.get('/test1', function (req, res) {
  var result = { test: 'test' };
  setTimeout(function() {
    res
      .status(200)
      .send(result);
  }, RESPONSE_DELAY);
});


var server = http.createServer(app);

server.listen(httpPort, function () {
  console.log('* Server listening at %s:%d', server.address().address, server.address().port);
});
