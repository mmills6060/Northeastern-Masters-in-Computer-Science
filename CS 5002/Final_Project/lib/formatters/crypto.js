const { createHash, createHmac, createCipheriv, createDecipheriv, randomBytes, scryptSync, randomUUID } = require('crypto');
const { v4: uuidv4 } = require('uuid');

module.exports = {

    randomUUID: function() {
        return randomUUID ? randomUUID() : uuidv4();
    },

    md5: function(data, salt, enc) {
        return hash('md5', data, salt, enc)
    },

    sha1: function(data, salt, enc) {
        return hash('sha1', data, salt, enc)
    },

    sha256: function(data, salt, enc) {
        return hash('sha256', data, salt, enc)
    },

    sha512: function(data, salt, enc) {
        return hash('sha512', data, salt, enc)
    },

    hash: function(data, alg, enc) {
        return hash(alg, data, '', enc);
    },

    hmac: function(data, alg, secret, enc) {
        return hmac(alg, data, secret, enc);
    },

    transform: function(data, from, to) {
        return transform(data, from, to);
    },

    encodeBase64: function(data, enc) {
        enc = typeof enc == 'string' ? enc : 'utf8';
        return transform(data, enc, 'base64');
    },

    decodeBase64: function(data, enc) {
        enc = typeof enc == 'string' ? enc : 'utf8';
        return transform(data, 'base64', enc);
    },

    encodeBase64Url: function(data, enc) {
        enc = typeof enc == 'string' ? enc : 'utf8';
        return transform(data, enc, 'base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
    },

    decodeBase64Url: function(data, enc) {
        enc = typeof enc == 'string' ? enc : 'utf8';
        return transform(data.replace(/-/g, '+').replace(/_/g, '/'), 'base64', enc);
    },

    encrypt: function(data, password, enc) {
        const config = require('../setup/config');
        password = typeof password == 'string' ? password : config.secret;
        enc = typeof enc == 'string' ? enc : 'base64';
        const iv = randomBytes(16);
        const key = scryptSync(password, iv, 32);
        const cipher = createCipheriv('aes-256-cbc', key, iv);
        const encrypted = cipher.update(data, 'utf8', enc);
        return iv.toString(enc) + '.' + encrypted + cipher.final(enc);
    },

    decrypt: function(data, password, enc) {
        const config = require('../setup/config');
        password = typeof password == 'string' ? password : config.secret;
        enc = typeof enc == 'string' ? enc : 'base64';
        const iv = Buffer.from(data.split('.')[0], enc);
        const key = scryptSync(password, iv, 32);
        const decipher = createDecipheriv('aes-256-cbc', key, iv);
        const decrypted = decipher.update(data.split('.')[1], enc, 'utf8');
        return decrypted + decipher.final('utf8');
    },

};

function hash(alg, data, salt, enc) {
    if (data == null) return data;
    salt = typeof salt == 'string' ? salt : '';
    enc = typeof enc == 'string' ? enc : 'hex';
    return createHash(alg).update(data + salt).digest(enc);
}

function hmac(alg, data, secret, enc) {
    if (data == null) return data;
    secret = typeof secret == 'string' ? secret : '';
    enc = typeof enc == 'string' ? enc : 'hex';
    return createHmac(alg, secret).update(data).digest(enc);
}

function transform(data, from, to) {
    if (data == null) return data;
    return Buffer.from(String(data), from).toString(to);
}