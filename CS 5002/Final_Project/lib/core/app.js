const fs = require('fs-extra');
const Scope = require('./scope');
const Parser = require('./parser');
const db = require('./db');
const validator = require('../validator');
const config = require('../setup/config');
const debug = require('debug')('server-connect:app');
const { clone, formatDate, parseDate } = require('../core/util');
const { toSystemPath } = require('../core/path');
const os = require('os');

if (!global.db) {
    global.db = {};
}

function App(req = {}, res = {}) {
    this.error = false;
    this.data = {};
    this.meta = {};
    this.settings = {};
    this.modules = {};

    this.io = global.io;
    this.req = req;
    this.res = res;
    this.global = new Scope();
    this.scope = this.global;

    this.mail = {};
    this.auth = {};
    this.oauth = {};
    this.db = {};
    this.s3 = {};
    this.jwt = {};

    if (config.globals.data) {
        this.set(config.globals.data);
    }

    this.set({
        $_ERROR: null,
        //$_SERVER: process.env,
        $_ENV: process.env,
        $_GET: req.query,
        $_POST: req.method == 'POST' ? req.body : {},
        $_PARAM: req.params,
        $_HEADER: req.headers,
        $_COOKIE: req.cookies,
        $_SESSION: req.session
    });

    let urlParts = req.originalUrl ? req.originalUrl.split('?') : ['', ''];
    let $server = {
        CONTENT_TYPE: req.headers && req.headers['content-type'],
        HTTPS: req.protocol == 'https',
        PATH_INFO: req.path,
        QUERY_STRING: urlParts[1],
        REMOTE_ADDR: req.ip,
        REQUEST_PROTOCOL: req.protocol,
        REQUEST_METHOD: req.method,
        SERVER_NAME: req.hostname,
        BASE_URL: req.headers && req.protocol + '://' + req.headers['host'],
        URL: urlParts[0],
        HOSTNAME: os.hostname()
    };

    if (req.headers) {
        for (let header in req.headers) {
            $server['HTTP_' + header.toUpperCase().replace(/-/, '_')] = req.headers[header];
        }
    }

    // Try to keep same as ASP/PHP
    this.set('$_SERVER', $server);
}

App.prototype = {
    set: function(key, value) {
        this.global.set(key, value);
    },

    get: function(key, def) {
        let value = this.global.get(key);
        return value !== undefined ? value : def;
    },

    remove: function(key) {
        this.global.remove(key);
    },

    setSession: function(key, value) {
        this.req.session[key] = value;
    },

    getSession: function(key) {
        return this.req.session[key];
    },

    removeSession: function(key) {
        delete this.req.session[key];
    },

    setCookie: function(name, value, opts) {
        if (!this.res.headersSent) {
            if (this.res.cookie) {
                this.res.cookie(name, value, opts);
            }
        } else {
            debug(`Trying to set ${name} cookie while headers were already sent.`);
        }
    },

    getCookie: function(name, signed) {
        return signed ? this.req.signedCookies[name] : this.req.cookies[name];
    },

    removeCookie: function(name, opts) {
        if (this.res.clearCookie) {
            this.res.clearCookie(name, {
                domain: opts.domain,
                path: opts.path
            });
        }
    },

    setMailer: function(name, options) {
        let setup = {};

        options = this.parse(options);

        switch (options.server) {
            case 'mail':
                setup.sendmail = true;
                break;

            case 'ses':
                const aws = require('@aws-sdk/client-ses');
                const ses = new AWS.SES({
                    endpoint: options.endpoint,
                    credentials: {
                        accessKeyId: options.accessKeyId,
                        secretAccessKey: options.secretAccessKey
                    }
                });
                setup.SES = { ses, aws };
                break;
            
            default:
                // https://nodemailer.com/smtp/
                setup.host = options.host || 'localhost';
                setup.port = options.port || 25;
                setup.secure = options.useSSL || false;
                setup.auth = {
                    user: options.username,
                    pass: options.password
                };
                setup.tls = {
                    rejectUnauthorized: false
                };
        }

        return this.mail[name] = setup;
    },

    getMailer: function(name) {
        if (this.mail[name]) {
            return this.mail[name];
        }

        if (config.mail[name]) {
            return this.setMailer(name, config.mail[name]);
        }

        if (fs.existsSync(`app/modules/Mailer/${name}.json`)) {
            let action = fs.readJSONSync(`app/modules/Mailer/${name}.json`);
            return this.setMailer(name, action.options);
        }

        throw new Error(`Couldn't find mailer "${name}".`);
    },

    setAuthProvider: async function(name, options) {
        const Provider = require('../auth/' + options.provider.toLowerCase());
        const provider = new Provider(this, options, name);
        if (!provider.identity) await provider.autoLogin();
        this.set('identity', provider.identity);
        return this.auth[name] = provider;
    },

    getAuthProvider: async function(name) {
        if (this.auth[name]) {
            return this.auth[name];
        }

        if (config.auth[name]) {
            return await this.setAuthProvider(name, config.auth[name]);
        }

        if (fs.existsSync(`app/modules/SecurityProviders/${name}.json`)) {
            let action = fs.readJSONSync(`app/modules/SecurityProviders/${name}.json`);
            return await this.setAuthProvider(name, action.options);
        }

        throw new Error(`Couldn't find security provider "${name}".`);
    },

    setOAuthProvider: async function(name, options) {
        const OAuth2 = require('../oauth');
        const services = require('../oauth/services');

        options = this.parse(options);

        let service = this.parseOptional(options.service, 'string', null);
        let opts = service ? services[service] : {};
        opts.client_id = this.parseOptional(options.client_id, 'string', null);
        opts.client_secret = this.parseOptional(options.client_secret, 'string', null);
        opts.token_endpoint = opts.token_endpoint || this.parseRequired(options.token_endpoint, 'string', 'oauth.provider: token_endpoint is required.');
        opts.auth_endpoint = opts.auth_endpoint || this.parseOptional(options.auth_endpoint, 'string', '');
        opts.scope_separator = opts.scope_separator || this.parseOptional(options.scope_separator, 'string', ' ');
        opts.access_token = this.parseOptional(options.access_token, 'string', null);
        opts.refresh_token = this.parseOptional(options.refresh_token, 'string', null);
        opts.jwt_bearer = this.parseOptional(options.jwt_bearer, 'string', false);
        opts.client_credentials = this.parseOptional(options.client_credentials, 'boolean', false);
        opts.params = Object.assign({}, opts.params, this.parseOptional(options.params, 'object', {}));

        this.oauth[name] = new OAuth2(this, this.parse(options), name);
        await this.oauth[name].init();

        return this.oauth[name];
    },

    getOAuthProvider: async function(name) {
        if (this.oauth[name]) {
            return this.oauth[name];
        }

        if (config.oauth[name]) {
            return await this.setOAuthProvider(name, config.oauth[name]);
        }

        if (fs.existsSync(`app/modules/oauth/${name}.json`)) {
            let action = fs.readJSONSync(`app/modules/oauth/${name}.json`);
            return await this.setOAuthProvider(name, action.options);
        }

        throw new Error(`Couldn't find oauth provider "${name}".`);
    },

    setDbConnection: function(name, options) {
        if (global.db[name]) {
            return global.db[name];
        }
        
        options = this.parse(options);

        switch (options.client) {
            case 'couchdb':
                const nano = require('nano');
                global.db[name] = nano(options.connection);
                global.db[name].client = options.client;
                return global.db[name];

            case 'sqlite3':
                if (options.connection.filename) {
                    options.connection.filename = toSystemPath(options.connection.filename);
                }
                break;

            case 'mysql':
            case 'mysql2':
                options.connection = {
                    supportBigNumber: true,
                    dateStrings: !!options.tz,
                    ...options.connection
                };
                break;

            case 'mssql':
                if (options.tz) {
                    // use local timezone to have same behavior as the other drivers
                    // to prevent problems node should have same timezone as database
                    options.connection.options = { useUTC: false, ...options.connection.options };
                }
                break;

            case 'postgres':
                if (options.tz) {
                    const types = require('pg').types;
                    const parseFn = val => val;
                    types.setTypeParser(types.builtins.TIME, parseFn);
                    types.setTypeParser(types.builtins.TIMETZ, parseFn);
                    types.setTypeParser(types.builtins.TIMESTAMP, parseFn);
                    types.setTypeParser(types.builtins.TIMESTAMPTZ, parseFn);
                }
                break;
        }

        if (options.connection && options.connection.ssl) {
            if (options.connection.ssl.key) {
                options.connection.ssl.key = fs.readFileSync(toSystemPath(options.connection.ssl.key));
            }

            if (options.connection.ssl.ca) {
                options.connection.ssl.ca = fs.readFileSync(toSystemPath(options.connection.ssl.ca));
            }

            if (options.connection.ssl.cert) {
                options.connection.ssl.cert = fs.readFileSync(toSystemPath(options.connection.ssl.cert));
            }
        }

        options.useNullAsDefault = true;

        const formatRecord = (record, meta) => {
            for (column in record) {
                if (record[column] != null) {
                    if (meta.has(column)) {
                        const info = meta.get(column);

                        if (['json', 'object', 'array'].includes(info.type)) {
                            if (typeof record[column] == 'string') {
                                try {
                                    // column of type json returned as string, need parse
                                    record[column] = JSON.parse(record[column]);
                                } catch (err) {
                                    console.warn(err);
                                }
                            }
                        }

                        if (info.type == 'date') {
                            record[column] = formatDate(record[column], 'yyyy-MM-dd');
                        }

                        if (info.type == 'time') {
                            if (options.tz == 'local') {
                                record[column] = formatDate(record[column], 'HH:mm:ss.v');
                            } else if (options.tz == 'utc') {
                                record[column] = parseDate(parseDate(formatDate('now', 'yyyy-MM-dd ') + formatDate(record[column], 'HH:mm:ss.v'))).toISOString().slice(11);
                            }
                        }

                        if (['datetime', 'timestamp'].includes(info.type) || Object.prototype.toString.call(record[column]) == '[object Date]') {
                            if (options.tz == 'local') {
                                record[column] = formatDate(record[column], 'yyyy-MM-dd HH:mm:ss.v');
                            } else if (options.tz == 'utc') {
                                record[column] = parseDate(record[column]).toISOString();
                            }
                        }
                    } else {
                        // try to detect datetime
                        if (Object.prototype.toString.call(record[column]) == '[object Date]') {
                            if (options.tz == 'local') {
                                record[column] = formatDate(record[column], 'yyyy-MM-dd HH:mm:ss.v');
                            } else if (options.tz == 'utc') {
                                record[column] = parseDate(record[column]).toISOString();
                            }
                        } else if (typeof record[column] == 'string' && /\d{4}-\d{2}-\d{2}([T\s]\d{2}:\d{2}:\d{2}(\.\d+)?([Zz]|[+-]\d{2}(:\d{2})?)?)?/.test(record[column])) {
                            if (options.tz == 'local') {
                                record[column] = formatDate(record[column], 'yyyy-MM-dd HH:mm:ss.v');
                            } else if (options.tz == 'utc') {
                                record[column] = parseDate(record[column]).toISOString();
                            }
                        }
                    }

                    if (record[column] == undefined) {
                        record[column] = null;
                    } else if (record[column].toJSON) {
                        record[column] = record[column].toJSON();
                    }
                }
            }

            return record;
        };

        options.postProcessResponse = function(result, queryContext) {
            const meta = new Map();

            if (Array.isArray(queryContext)) {
                for (let item of queryContext) {
                    if (item.name && item.type) {
                        meta.set(item.name, item);
                    }
                }
            }

            if (Array.isArray(result)) {
                return result.map(record => formatRecord(record, meta));
            } else {
                return formatRecord(result, meta);
            }
        };

        global.db[name] = db(options);
        //this.res.on('finish', () => global.db[name].destroy());

        return global.db[name];
    },

    getDbConnection: function(name) {
        if (this.__trx) return this.__trx;
        
        if (global.db[name]) {
            return global.db[name];
        }

        if (config.db[name]) {
            return this.setDbConnection(name, config.db[name]);
        }

        if (fs.existsSync(`app/modules/connections/${name}.json`)) {
            let action = fs.readJSONSync(`app/modules/connections/${name}.json`);
            return this.setDbConnection(name, action.options);
        }

        throw new Error(`Couldn't find database connection "${name}".`);
    },

    setS3Provider: function(name, options) {
        options = this.parse(options);

        const { S3 } = require('@aws-sdk/client-s3');
        const endpoint = this.parseRequired(options.endpoint, 'string', 's3.provider: endpoint is required.');
        const accessKeyId = this.parseRequired(options.accessKeyId, 'string', 's3.provider: accessKeyId is required.');
        const secretAccessKey = this.parseRequired(options.secretAccessKey, 'string', 's3.provider: secretAccessKey is required.');

        let region = options.region || 'us-east-1';
        let pos = endpoint.indexOf('.amazonaws');
        if (pos > 3) region = endpoint.substr(3, pos - 3);

        this.s3[name] = new S3({ endpoint: 'https://' + endpoint, credentials: { accessKeyId, secretAccessKey }, region, signatureVersion: 'v4' });

        return this.s3[name];
    },

    getS3Provider: function(name) {
        if (this.s3[name]) {
            return this.s3[name];
        }

        if (config.s3[name]) {
            return this.setS3Provider(name, config.s3[name]);
        }

        if (fs.existsSync(`app/modules/s3/${name}.json`)) {
            let action = fs.readJSONSync(`app/modules/s3/${name}.json`);
            return this.setS3Provider(name, action.options);
        }

        throw new Error(`Couldn't find S3 provider "${name}".`);
    },

    setJSONWebToken: function(name, options) {
        const jwt = require('jsonwebtoken');

        options = this.parse(options);

        let opts = {};

        if (options.alg) opts.algorithm = options.alg;
        if (options.iss) opts.issuer = options.iss;
        if (options.sub) opts.subject = options.sub;
        if (options.aud) opts.audience = options.aud;
        if (options.jti) opts.jwtid = options.jti;
        if (options.expiresIn) opts.expiresIn = options.expiresIn

        return this.jwt[name] = jwt.sign({
            ...options.claims
        }, options.key, {
            expiresIn: 3600, // use as default (required by google)
            ...opts
        });
    },

    getJSONWebToken: function(name) {
        if (config.jwt[name]) {
            return this.setJSONWebToken(name, config.jwt[name]);
        }

        if (fs.existsSync(`app/modules/jwt/${name}.json`)) {
            let action = fs.readJSONSync(`app/modules/jwt/${name}.json`);
            return this.setJSONWebToken(name, action.options);
        }

        throw new Error(`Couldn't find JSON Web Token "${name}".`);
    },

    define: async function(cfg, internal) {
        if (cfg.settings) {
            this.settings = clone(cfg.settings);
        }

        if (cfg.vars) {
            this.set(clone(cfg.vars));
        }

        if (cfg.meta) {
            this.meta = clone(cfg.meta);
            await validator.init(this, this.meta);
        }

        if (fs.existsSync('app/modules/global.json')) {
            await this.exec(await fs.readJSON('app/modules/global.json'), true);
        }

        /*
        debug('body: %o', this.req.body);
        debug('query: %o', this.req.query);
        debug('params: %o', this.req.params);
        debug('headers: %o', this.req.headers);
        debug('cookies: %o', this.req.cookies);
        debug('session: %o', this.req.session);
        */

        await this.exec(cfg.exec || cfg, internal);
    },

    sub: async function(actions, scope) {
        const subApp = new App(this.req, this.res);
        subApp.global = this.global;
        subApp.scope = this.scope.create(scope);
        await subApp.exec(actions, true);
        return subApp.data;
    },

    exec: async function(actions, internal) {
        if (actions.exec) {
            return this.exec(actions.exec, internal);
        }

        actions = clone(actions);

        await this._exec(actions.steps || actions);

        if (this.error !== false) {
            if (actions.catch) {
                this.scope.set('$_ERROR', this.error.message);
                this.error = false;
                await this._exec(actions.catch, true);
            } else {
                throw this.error;
            }
        }

        if (!internal && !this.res.headersSent && !this.noOutput) {
            this.res.json(this.data);
        }
    },

    _exec: async function(steps, ignoreAbort) {
        if (this.res.headersSent) return;
        
        if (typeof steps == 'string') {
            return this.exec(await fs.readJSON(`app/modules/${steps}.json`), true);
        }

        if (this.res.headersSent) {
            // do not execute other steps after headers has been sent
            return;
        }

        if (Array.isArray(steps)) {
            for (let step of steps) {
                await this._exec(step);
                if (this.error) return;
            }
            return;
        }

        if (steps.disabled) {
            return;
        }

        if (steps.action) {
            try {
                let module;

                if (fs.existsSync(`extensions/server_connect/modules/${steps.module}.js`)) {
                    module = require(`../../extensions/server_connect/modules/${steps.module}`);
                } else if (fs.existsSync(`lib/modules/${steps.module}.js`)) {
                    module = require(`../modules/${steps.module}`);
                } else {
                    throw new Error(`Module ${steps.module} doesn't exist`);
                }

                if (typeof module[steps.action] != 'function') {
                    throw new Error(`Action ${steps.action} doesn't exist in ${steps.module || 'core'}`);
                }

                debug(`Executing action step ${steps.action}`);
                debug(`options: %O`, steps.options);

                if (!ignoreAbort && config.abortOnDisconnect && this.req.isDisconnected) {
                    throw new Error('Aborted');
                }

                const data = await module[steps.action].call(this, clone(steps.options), steps.name, steps.meta);

                if (data instanceof Error) {
                    throw data;
                }

                if (steps.name) {
                    this.scope.set(steps.name, data);

                    if (steps.output) {
                        this.data[steps.name] = data;
                    }
                }
            } catch (e) {
                this.error = e;
                return;
            }
        }
    },

    parse: function(value, scope) {
        return Parser.parseValue(value, scope || this.scope);
    },

    parseRequired: function(value, type, err) {
        if (value === undefined) {
            throw new Error(err);
        }

        let val = Parser.parseValue(value, this.scope);

        if (type == '*') {
            if (val === undefined) {
                throw new Error(err);
            }
        } else if (type == 'boolean') {
            val = !!val;
        } else if (typeof val != type) {
            throw new Error(err);
        }

        return val;
    },

    parseOptional: function(value, type, def) {
        if (value === undefined) return def;

        let val = Parser.parseValue(value, this.scope);

        if (type == '*') {
            if (val === undefined) val = def;
        } else if (type == 'boolean') {
            if (val === undefined) {
                val = def;
            } else {
                val = !!val;
            }
        } else if (typeof val != type) {
            val = def;
        }

        return val;
    },

    parseSQL: function(sql) {
        if (!sql) return null;

        ['values', 'orders'].forEach((prop) => {
            if (Array.isArray(sql[prop])) {
                sql[prop] = sql[prop].filter((value) => {
                    if (!value.condition) return true;
                    return !!Parser.parseValue(value.condition, this.scope);
                });
            }
        });

        if (sql.wheres && sql.wheres.rules) {
            if (sql.wheres.conditional && !Parser.parseValue(sql.wheres.conditional, this.scope)) {
                delete sql.wheres;
            } else {
                sql.wheres.rules = sql.wheres.rules.filter(function filterConditional(rule) {
                    if (!rule.rules) return true;
                    if (rule.conditional && !Parser.parseValue(rule.conditional, this.scope)) return false;
                    rule.rules = rule.rules.filter(filterConditional, this);
                    return rule.rules.length;
                }, this);

                if (!sql.wheres.rules.length) {
                    delete sql.wheres;
                }
            }
        }

        if (sql.sub) {
            for (const name in sql.sub) {
                sql.sub[name] = this.parseSQL(sql.sub[name]);
            }
        }

        return Parser.parseValue(sql, this.scope);
    },
};

module.exports = App;