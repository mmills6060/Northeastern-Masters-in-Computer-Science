const { readFileSync } = require('fs');
const { resolve } = require('path');

module.exports = {

    json: function(options) {
        return JSON.parse(this.parse(options.data));
    },

    local: function(options) {
        let path = this.parse(options.path);

        if (typeof path !== 'string') throw new Error('dataset.local: path is required.');

        let data = readFileSync(resolve('public', path));

        return JSON.parse(data);
    },

    remote: function(options) {
        throw new Error('dataset.remote: not implemented, use api instead.');
    },

};