/* globals describe, before, beforeEach, after, afterEach, it */

'use strict';

var chai = require('chai');
var assert = chai.assert;
var expect = chai.expect;

chai.should();
//http://chaijs.com/plugins/chai-things
chai.use(require('chai-things'));

var EventEmitter = require('events');
var util = require('util');

var endMw = require('../');


describe('express-end', function () {
  var req, res;

  before('before', function () {

  });

  beforeEach('beforeEach', function () {
    req = {};

    var Res = function() {
      EventEmitter.call(this);
    };
    util.inherits(Res, EventEmitter);
    res = new Res();
  });

  it('should replace res.end() & store original res.end() to res._orig_end_handler', function (done) {
    var resEnd = function() {};
    res.end = resEnd;
    expect(res._orig_end_handler).is.undefined;

    endMw(req, res, function() {
      expect(res._orig_end_handler).equals(resEnd);
      expect(res.end).is.not.undefined;
      done();
    });

  });

  it('should avoid to overrride res.end() twice', function (done) {
    var resEnd = function() {};
    res.end = resEnd;
    expect(res._orig_end_handler).is.undefined;

    endMw(req, res, function() {
      expect(res._orig_end_handler).equals(resEnd);
      expect(res.end).is.not.undefined;
      var resEnd2 = res.end;

      endMw(req, res, function() {
        // Originally stored res.end() was not changed
        expect(res._orig_end_handler).equals(resEnd);
        // res.end() points to same MW's handler
        expect(res.end).equals(resEnd2);
        done();
      });

    });

  });

  it('should emit `end` on `res.end()`', function (done) {
    var endArgs = [ 'arg1', 'arg2', 'arg3' ];

    res.end = function() {};

    res.on('end', function() {
      done();
    });

    endMw(req, res, function() {
      res.end.apply(this, endArgs);
    });

  });

  it('should call original res.end() passing correct `this` and `arguments`', function (done) {
    var endArgs = [ 'arg1', 'arg2', 'arg3' ];
    var endThis = { 'end': 'this' };

    var resEnd = function( /* arguments */ ) {
      var args = Array.prototype.slice.call(arguments);
      expect(args).eql(endArgs);
      expect(this).eql(endThis);
      done();
    };
    res.end = resEnd;

    endMw(req, res, function() {
      res.end.apply(endThis, endArgs);
    });

  });

});
