const AuthProvider = require('./provider');
const debug = require('debug')('server-connect:auth');

class SingleProvider extends AuthProvider {

    constructor(app, opts, name) {
        super(app, opts, name);
        this.username = opts.username;
        this.password = opts.password;
    }

    validate(username, password) {
        if (username == this.username && password == this.password) {
            return username;
        }

        return false;
    }

    permissions() {
        return true;
    }

}

module.exports = SingleProvider;