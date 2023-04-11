const AuthProvider = require('./provider');

class DatabaseProvider extends AuthProvider {

    constructor(app, opts, name) {
        super(app, opts, name);
        this.users = opts.users;
        this.perms = opts.permissions;
        this.db = app.getDbConnection(opts.connection);
    }

    async validate(username, password, passwordVerify) {
        if (!username) return false;
        if (!password) password = '';

        let results = await this.db
            .select(this.users.identity, this.users.username, this.users.password)
            .from(this.users.table)
            .where(this.users.username, username);

        for (let result of results) {
            if (result[this.users.username] == username) {
                if (passwordVerify && result[this.users.password].startsWith('$')) {
                    const argon2 = require('argon2');
                    const valid = await argon2.verify(result[this.users.password], password);
                    return valid ? result[this.users.identity] : false;
                } else if (result[this.users.password] == password) {
                    return result[this.users.identity];
                }
            }
        }
        
        return false;
    }

    async permissions(identity, permissions) {
        for (let permission of permissions) {
            if (!this.perms[permission]) return false;

            let perm = this.perms[permission];
            let table = perm.table || this.users.table;
            let ident = perm.identity || this.users.identity;

            let results = await this.db
                .select(ident)
                .from(table)
                .where(ident, identity)
                .where(function() {
                    for (let condition of perm.conditions) {
                        if (condition.operator == 'in') {
                            this.whereIn(condition.column, condition.value);
                        } else if (condition.operator == 'not in') {
                            this.whereNotIn(condition.column, condition.value);
                        } else if (condition.operator == 'is null') {
                            this.whereNull(condition.column);
                        } else if (condition.operator == 'is not null') {
                            this.whereNotNull(condition.column);
                        } else {
                            this.where(condition.column, condition.operator, condition.value);
                        }
                    }
                });

            if (!results.length) return false;
        }

        return true;
    }

}

module.exports = DatabaseProvider;