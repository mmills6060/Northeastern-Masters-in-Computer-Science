const config = require('../setup/config');
const crypto = require('crypto');
const debug = require('debug')('server-connect:auth');

class AuthProvider {

    constructor(app, opts, name) {
        this.app = app;
        this.name = name;
        this.identity = this.app.getSession(this.name + 'Id') || false;
        this.secret = opts.secret || config.secret;
        this.basicAuth = opts.basicAuth;
        this.basicRealm = opts.basicRealm;
        this.passwordVerify = opts.passwordVerify || false;

        this.cookieOpts = {
            domain: opts.domain || undefined,
            httpOnly: true,
            maxAge: (opts.expires || 30) * 24 * 60 * 60 * 1000, // from days to ms
            path: opts.path || '/',
            secure: !!opts.secure,
            sameSite: opts.sameSite || 'Strict',
            signed: true
        };
    }

    async autoLogin() {
        if (this.basicAuth) {
            const auth = require('../core/basicauth')(this.app.req);
            debug(`Basic auth credentials received: %o`, auth);
            if (auth) await this.login(auth.username, auth.password, false, true);
        }

        const cookie = this.app.getCookie(this.name + '.auth', true);
        if (cookie) {
            const auth = this.decrypt(cookie);
            debug(`Login with cookie: %o`, auth);
            if (auth) await this.login(auth.username, auth.password, true, true);
        } else {
            debug(`No login cookie found`);
        }
    }

    async login(username, password, remember, autoLogin) {
        const identity = await this.validate(username, password, this.passwordVerify);

        if (!identity) {
            await this.logout();

            if (!autoLogin) {
                this.unauthorized();
                return false;
            }
        } else {
            this.app.setSession(this.name + 'Id', identity);
            this.app.set('identity', identity);

            if (remember) {
                debug('setCookie', identity, username, password);
                this.app.setCookie(this.name + '.auth', this.encrypt({ username, password }), this.cookieOpts);
            }

            this.identity = identity;
        }

        return identity;
    }

    async logout() {
        this.app.removeSession(this.name + 'Id');
        this.app.removeCookie(this.name + '.auth', this.cookieOpts);
        this.app.remove('identity');
        this.identity = false;
    }

    async restrict(opts) {
        if (this.identity === false) {
            if (opts.loginUrl) {
                if (this.app.req.fragment) {
                    this.app.res.status(222).send(opts.loginUrl);
                } else {
                    this.app.res.redirect(opts.loginUrl);
                }
            } else {
                this.unauthorized();
            }

            return;
        }

        if (opts.permissions) {
            const allowed = await this.permissions(this.identity, opts.permissions);
            if (!allowed) {
                if (opts.forbiddenUrl) {
                    if (this.app.req.fragment) {
                        this.app.res.status(222).send(opts.forbiddenUrl);
                    } else {
                        this.app.res.redirect(opts.forbiddenUrl);
                    }
                } else {
                    this.forbidden();
                }
            }
        }
    }

    encrypt(data) {
        const iv = crypto.randomBytes(16);
        const key = crypto.scryptSync(this.secret, iv, 32);
        const cipher = crypto.createCipheriv('aes-256-cbc', key, iv);
        const encrypted = cipher.update(JSON.stringify(data), 'utf8', 'base64');
        return iv.toString('base64') + '.' + encrypted + cipher.final('base64');
    }

    decrypt(data) {
        // try/catch to prevent errors on currupt cookies
        try {
            const iv = Buffer.from(data.split('.')[0], 'base64');
            const key = crypto.scryptSync(this.secret, iv, 32);
            const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
            const decrypted = decipher.update(data.split('.')[1], 'base64', 'utf8');
            return JSON.parse(decrypted + decipher.final('utf8'));
        } catch (err) {
            return undefined;
        }
    }

    unauthorized() {
        if (this.basicAuth) {
            this.app.res.set('WWW-Authenticate', `Basic Realm="${this.basicRealm}"`);
        }
        this.app.res.sendStatus(401);
    }

    forbidden() {
        this.app.res.sendStatus(403);
    }

    async validate(username, password) {
        throw new Error('auth.validate needs to be extended.');
    }

    async permissions(identity, permissions) {
        throw new Error('auth.permissions needs to be extended.');
    }

}

module.exports = AuthProvider;