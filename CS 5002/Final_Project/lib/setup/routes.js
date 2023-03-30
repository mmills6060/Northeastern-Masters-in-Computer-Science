const fs = require('fs-extra');
const debug = require('debug')('server-connect:setup:routes');
const config = require('./config');
const { map } = require('../core/async');
const { posix, extname } = require('path');
const { serverConnect, templateView } = require('../core/middleware');
const cache = global.redisClient ? require('express-redis-cache')({ client: global.redisClient }) : null;
const database = require('./database');
const webhooks = require('./webhooks');

module.exports = async function (app) {
    app.use((req, res, next) => {
        req.fragment = (req.headers['accept'] || '*/*').includes('fragment');
        next();
    });

    if (fs.existsSync('extensions/server_connect/routes')) {
        const entries = fs.readdirSync('extensions/server_connect/routes', { withFileTypes: true });

        for (let entry of entries) {
            if (entry.isFile() && extname(entry.name) == '.js') {
                let hook = require(`../../extensions/server_connect/routes/${entry.name}`);
                if (hook.before) hook.before(app);
                if (hook.handler) hook.handler(app);
                debug(`Custom router ${entry.name} loaded`);
            }
        }
    }

    if (config.createApiRoutes) {
        fs.ensureDirSync('app/api');
        createApiRoutes('app/api');
    }

    if (fs.existsSync('app/config/routes.json')) {
        const { routes, layouts } = fs.readJSONSync('app/config/routes.json');

        parseRoutes(routes, null);

        function parseRoutes(routes, parent) {
            for (let route of routes) {
                if (!route.path) continue;

                createRoute(route, parent);

                if (Array.isArray(route.routes)) {
                    parseRoutes(route.routes, route);
                }
            }
        }

        function createRoute({ path, method, redirect, url, page, layout, exec, data, ttl, status }, parent) {
            method = method || 'all';
            data = data || {};
            if (page) page = page.replace(/^\//, '');
            if (layout) layout = layout.replace(/^\//, '');
            if (parent && parent.path) path = parent.path + path;

            if (redirect) {
                app.get(path, (req, res) => res.redirect(status == 302 ? 302 : 301, redirect));
            } else if (url) {
                app[method](path, (req, res, next) => {
                    next(parent && !req.fragment ? 'route' : null);
                }, (req, res) => {
                    res.sendFile(url, { root: 'public' })
                });

                if (parent) {
                    createRoute({
                        path,
                        method: parent.method,
                        redirect: parent.redirect,
                        url: parent.url,
                        page: parent.page,
                        layout: parent.layout,
                        exec: parent.exec,
                        data: parent.data
                    });
                }
            } else if (page) {
                if (exec) {
                    if (fs.existsSync(`app/${exec}.json`)) {
                        let json = fs.readJSONSync(`app/${exec}.json`);

                        if (json.exec && json.exec.steps) {
                            json = json.exec.steps;
                        } else if (json.steps) {
                            json = json.steps;
                        }
                        
                        if (!Array.isArray(json)) {
                            json = [json];
                        }


                        if (layout && layouts && layouts[layout]) {
                            if (layouts[layout].data) {
                                data = Object.assign({}, layouts[layout].data, data);
                            }

                            if (layouts[layout].exec) {
                                if (fs.existsSync(`app/${layouts[layout].exec}.json`)) {
                                    let _json = fs.readJSONSync(`app/${layouts[layout].exec}.json`);

                                    if (_json.exec && _json.exec.steps) {
                                        _json = _json.exec.steps;
                                    } else if (_json.steps) {
                                        _json = _json.steps;
                                    }
                                    
                                    if (!Array.isArray(_json)) {
                                        _json = [_json];
                                    }

                                    json = _json.concat(json);
                                } else {
                                    debug(`Route ${path} skipped, "app/${exec}.json" not found`);
                                    return;
                                }
                            }
                        }

                        if (cache && ttl) {
                            app[method](path, (req, res, next) => {
                                res.use_express_redis_cache = !req.query.nocache;
                                res.express_redis_cache_name = req.originalUrl + (req.fragment ? '-fragment' : '');
                                next(parent && !req.fragment ? 'route' : null);
                            }, cache.route({ expire: ttl }), templateView(layout, page, data, json));
                        } else {
                            app[method](path, (req, res, next) => {
                                next(parent && !req.fragment ? 'route' : null);
                            }, templateView(layout, page, data, json));
                        }
                    } else {
                        debug(`Route ${path} skipped, "app/${exec}.json" not found`);
                        return;
                    }
                } else {
                    let json = [];

                    if (layout && layouts && layouts[layout]) {
                        if (layouts[layout].data) {
                            data = Object.assign({}, layouts[layout].data, data);
                        }

                        if (layouts[layout].exec) {
                            if (fs.existsSync(`app/${layouts[layout].exec}.json`)) {
                                let _json = fs.readJSONSync(`app/${layouts[layout].exec}.json`);

                                if (_json.exec && _json.exec.steps) {
                                    _json = _json.exec.steps;
                                } else if (_json.steps) {
                                    _json = _json.steps;
                                }
                                
                                if (!Array.isArray(_json)) {
                                    _json = [_json];
                                }

                                json = _json.concat(json);
                            } else {
                                debug(`Route ${path} skipped, "app/${exec}.json" not found`);
                                return;
                            }
                        }
                    }

                    if (cache && ttl) {
                        app[method](path, (req, res, next) => {
                            res.use_express_redis_cache = !req.query.nocache;
                            res.express_redis_cache_name = req.originalUrl + (req.fragment ? '-fragment' : '');
                            next(parent && !req.fragment ? 'route' : null);
                        }, cache.route({ expire: ttl }), templateView(layout, page, data, json));
                    } else {
                        app[method](path, (req, res, next) => {
                            next(parent && !req.fragment ? 'route' : null);
                        }, templateView(layout, page, data, json));
                    }
                }

                if (parent) {
                    createRoute({
                        path,
                        method: parent.method,
                        redirect: parent.redirect,
                        url: parent.url,
                        page: parent.page,
                        layout: parent.layout,
                        exec: parent.exec,
                        data: parent.data
                    });
                }
            } else if (exec) {
                if (fs.existsSync(`app/${exec}.json`)) {
                    let json = fs.readJSONSync(`app/${exec}.json`);

                    if (cache && ttl) {
                        app[method](path, cache.route({ expire: ttl }), serverConnect(json));
                    } else {
                        app[method](path, serverConnect(json));
                    }

                    return;
                }
            }
        }
    }

    database(app);
    webhooks(app);

    if (fs.existsSync('extensions/server_connect/routes')) {
        const entries = fs.readdirSync('extensions/server_connect/routes', { withFileTypes: true });

        for (let entry of entries) {
            if (entry.isFile() && extname(entry.name) == '.js') {
                let hook = require(`../../extensions/server_connect/routes/${entry.name}`);
                if (hook.after) hook.after(app);
                debug(`Custom router ${entry.name} loaded`);
            }
        }
    }

    function createApiRoutes(dir) {
        const entries = fs.readdirSync(dir, { withFileTypes: true });
    
        return map(entries, async (entry) => {
            let path = posix.join(dir, entry.name);
    
            if (entry.isFile() && extname(path) == '.json') {
                let json = fs.readJSONSync(path);
                let routePath = path.replace(/^app/i, '').replace(/.json$/, '(.json)?');
                let ttl = (json.settings && json.settings.options && json.settings.options.ttl) ? json.settings.options.ttl : 0;
                
                if (cache && ttl) {
                    app.all(routePath, (req, res, next) => {
                        res.use_express_redis_cache = !req.query.nocache;
                        next();
                    }, cache.route({ expire: ttl }), serverConnect(json));
                } else {
                    app.all(routePath, serverConnect(json));
                }

                debug(`Api route ${routePath} created`);
            }
    
            if (entry.isDirectory()) {
                return createApiRoutes(path);
            }
        });
    }
};
