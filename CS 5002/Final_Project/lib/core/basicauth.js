// Code taken from https://github.com/jshttp/basic-auth/blob/master/index.js
// Copyright(c) 2013 TJ Holowaychuk
// Copyright(c) 2014 Jonathan Ong
// Copyright(c) 2015-2016 Douglas Christopher Wilson

module.exports = auth;
module.exports.parse = parse;

const CREDENTIALS_REGEXP = /^ *(?:[Bb][Aa][Ss][Ii][Cc]) +([A-Za-z0-9._~+/-]+=*) *$/;
const USER_PASS_REGEXP = /^([^:]*):(.*)$/;

function auth(req) {
    if (!req) throw new Error('argument req is required.');
    if (typeof req != 'object') throw new Error('argument req needs to be an object.');

    return parse(getAuthorization(req));
}

function decodeBase64(str) {
    return Buffer.from(str, 'base64').toString();
}

function getAuthorization(req) {
    if (!req.headers || typeof req.headers != 'object') {
        throw new Error('argument req needs to have headers.');
    }

    return req.headers.authorization;
}

function parse(str) {
    if (typeof str != 'string') {
        return undefined;
    }

    const match = CREDENTIALS_REGEXP.exec(str);
    if (!match) return undefined;

    const userPass = USER_PASS_REGEXP.exec(decodeBase64(match[1]));
    if (!userPass) return undefined;

    return { username: userPass[1], password: userPass[2] };
}