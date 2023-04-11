const fs = require('fs-extra');
const { clone } = require('../core/util');

module.exports = {

    wait: function(options) {
        let delay = this.parseOptional(options.delay, 'number', 1000);
        return new Promise(resolve => setTimeout(resolve, delay))
    },

    log: function(options) {
        let message = this.parse(options.message);
        console.log(message);
        return message;
    },

    repeat: async function(options) {
        let repeater = this.parseRequired(options.repeat, '*', 'core.repeater: repeat is required.');
        let outputFilter = this.parseOptional(options.outputFilter, 'string', 'include'); // include/exclude
        let outputFields = this.parseOptional(options.outputFields, 'object'/*array[string]*/, []);
        let index = 0, data = [], parentData = this.data;

        switch (typeof repeater) {
            case 'boolean':
                repeater = repeater ? [0] : [];
                break;
            
            case 'string':
                repeater = repeater.split(',');
                break;

            case 'number':
                repeater = (n => {
                    let a = [], i = 0;
                    while (i < n) a.push(i++);
                    return a;
                })(repeater);
                break;
        }

        if (!(Array.isArray(repeater) || repeater instanceof Object)) {
            throw new Error('Repeater data is not an array or object');
        }

        for (let key in repeater) {
            if (repeater.hasOwnProperty(key)) {
                let scope = {};
                this.data = {};

                if (repeater[key] instanceof Object) {
                    for (var prop in repeater[key]) {
                        if (repeater[key].hasOwnProperty(prop)) {
                            scope[prop] = repeater[key][prop];

                            if (outputFilter == 'exclude') {
                                if (!outputFields.includes(prop)) {
                                    this.data[prop] = repeater[key][prop];
                                }
                            } else {
                                if (outputFields.includes(prop)) {
                                    this.data[prop] = repeater[key][prop];
                                }
                            }
                        }
                    }
                }

                scope.$key = key;
                scope.$name = key;
                scope.$value = clone(repeater[key]);
                scope.$index = index;
                scope.$number = index + 1;
                scope.$oddeven = index % 2;

                if (repeater[key] == null) {
                    repeater[key] = {};
                }

                this.scope = this.scope.create(scope, clone(repeater[key]));
                await this.exec(options.exec, true);
                this.scope = this.scope.parent;

                data.push({ ...this.data });

                index++;
            }
        }

        this.data = parentData;

        return data;
    },

    while: async function(options) {
        let max = this.parseOptional(options.max, 'number', Number.MAX_SAFE_INTEGER);
        let i = 0;

        while (this.parse(options.while)) {
            await this.exec(options.exec, true);
            if (++i == max) break;
        }
    },
    
    condition: async function(options) {
        let condition = this.parse(options.if);
        
        if (!!condition) {
            if (options.then) {
                await this.exec(options.then, true);
            }
        } else if (options.else) {
            await this.exec(options.else, true);
        }
    },

    conditions: async function(options) {
        if (Array.isArray(options.conditions)) {
            for (let condition of options.conditions) {
                let when = this.parse(condition.when);
                
                if (!!when) {
                    return this.exec(condition.then, true);
                }
            }
        }
    },

    select: async function(options) {
        let expression = this.parse(options.expression);

        if (Array.isArray(options.cases)) {
            for (let item of options.cases) {
                let value = this.parse(item.value);
                
                if (expression === value) {
                    return this.exec(item.exec, true);
                }
            }
        }
    },

    setvalue: function(options) {
        let key = this.parseOptional(options.key, 'string', '');
        let value = this.parse(options.value);
        if (key) this.set(key, value);
        return value;
    },

    setsession: function(options, name) {
        let value = this.parse(options.value);
        this.req.session[name] = value;
        return value;
    },

    removesession: function(options, name) {
        delete this.req.session[name];
    },

    setcookie: function(options, name) {
        options = this.parse(options);

        let cookieOptions = {
            domain: options.domain || undefined,
            httpOnly: !!options.httpOnly,
            maxAge: options.expires === 0 ? undefined : (options.expires || 30) * 24 * 60 * 60 * 1000, // from days to ms
            path: options.path || '/',
            secure: !!options.secure,
            sameSite: options.sameSite || false
        };

        this.setCookie(name, options.value, cookieOptions);
    },

    removecookie: function(options, name) {
        options = this.parse(options);

        let cookieOptions = {
            domain: options.domain || undefined,
            httpOnly: !!options.httpOnly,
            maxAge: options.expires === 0 ? undefined : (options.expires || 30) * 24 * 60 * 60 * 1000, // from days to ms
            path: options.path || '/',
            secure: !!options.secure,
            sameSite: !!options.sameSite
        };

        this.removeCookie(name, cookieOptions);
    },

    response: function(options) {
        let data = this.parseOptional(options.data, '*', null);
        let status = this.parseOptional(options.status, 'number', 200);
        let contentType = this.parseOptional(options.contentType, 'string', 'application/json');
        if (contentType != 'application/json') {
            this.res.set('Content-Type', contentType);
            this.res.status(status).send(data);
        } else {
            this.res.status(status).json(data);
        }
    },

    error: function(options) {
        let message = this.parseRequired(options.message, 'string', 'core.error: message is required.');
        throw new Error(message);
    },

    redirect: function(options) {
        let url = this.parseRequired(options.url, 'string', 'core.redirect: url is required.');
        let status = this.parseOptional(options.status, 'number', 302);

        this.res.redirect(status == 301 ? 301 : 302, url);
    },

    trycatch: async function(options) {
        try {
            await this.exec(options.try, true);
        } catch (error) {
            this.scope.set('$_ERROR', error.message || error);
            this.error = false;
            if (options.catch) {
                await this.exec(options.catch, true);
            }
        }
    },

    exec: async function(options) {
        var data = {};

        if (options.exec && fs.existsSync(`app/modules/lib/${options.exec}.json`)) {
            let parentData = this.data;
            this.data = {};
            this.scope = this.scope.create({ $_PARAM: this.parse(options.params) });
            await this.exec(await fs.readJSON(`app/modules/lib/${options.exec}.json`), true);
            data = this.data;
            this.scope = this.scope.parent;
            this.data = parentData;
        } else {
            throw new Error(`There is no action called '${options.exec}' found in the library.`);
        }

        return data;
    },

    group: async function(options, name) {
        if (name) {
            return this.sub(options.exec);
        } else {
            return this.exec(options.exec, true);
        }
    },

    parallel: async function(options, name) {
        let actions = options.exec.steps || options.exec;
        if (!Array.isArray(actions)) actions = [actions];
        return await Promise.all(actions.map(exec => {
            if (name) {
                return this.sub(exec);
            } else {
                return this.exec(exec, true);
            }
        }));
    },

    randomUUID: function(options) {
        const { randomUUID } = require('crypto');
        const { v4: uuidv4 } = require('uuid');
        return randomUUID ? randomUUID() : uuidv4();
    },

};