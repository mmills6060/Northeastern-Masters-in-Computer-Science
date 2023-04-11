'use strict';

var debug = require('debug')('end');


var endMw = function(req, res, next) {

  if (!res._orig_end_handler) {

    res._orig_end_handler = res.end;

    res.end = function () {
      res.end = res._orig_end_handler;
      res.emit('end');
      res.end.apply(this, arguments);
    };

  } else {
    debug('Warning: res.end() function is already overridden');
  }

  next();

};


module.exports = endMw;

