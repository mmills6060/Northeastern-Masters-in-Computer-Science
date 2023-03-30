const collections = require('./collections');
const conditional = require('./conditional');
const core = require('./core');
const crypto = require('./crypto');
const date = require('./date');
const number = require('./number');
const string = require('./string');

module.exports = {
    ...collections,
    ...conditional,
    ...core,
    ...crypto,
    ...date,
    ...number,
    ...string
};