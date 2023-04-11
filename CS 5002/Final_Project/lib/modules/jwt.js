exports.sign = function(options, name) {
    return this.setJSONWebToken(name, options)
};

exports.decode = function(options) {
    const jwt = require('jsonwebtoken');
    return jwt.decode(this.parse(options.token), { complete: true });
};

exports.verify = function(options) {
    const jwt = require('jsonwebtoken');
    options = this.parse(options);

    try {
        return jwt.verify(options.token, options.key, options);
    } catch (error) {
        const debug = require('debug')('server-connect:jwt');
        debug('jwt verify failed: %o', error);
        if (options.throw) throw error;
        return { error };
    }
};