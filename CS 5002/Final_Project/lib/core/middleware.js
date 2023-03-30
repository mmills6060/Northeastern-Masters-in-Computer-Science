const config = require('../setup/config');
const debug = require('debug')('server-connect:router');
const { clone } = require('./util');
const App = require('./app');

module.exports = {
    serverConnect: function(json) {
        return async function(req, res, next) {
            const app = new App(req, res);

            debug(`Serving serverConnect ${req.path}`);

            return Promise.resolve(app.define(json)).catch(next);
        };
    },

    templateView: function(layout, page, data, exec) {
        return async function(req, res, next) {
            const app = new App(req, res);
            
            debug(`Serving templateView ${req.path}`);

            const routeData = clone(data);
            const methods = {
                _: (expr, data = {}) => {
                    return app.parse(`{{${expr}}}`, app.scope.create(data));
                },

                _exec: async (name, steps, data = {}) => {
                    let context = {};
                    app.scope = app.scope.create(data, context);
                    await app.exec(steps, true);
                    app.scope = app.scope.parent;
                    app.set(name, context);
                    return context;
                },

                _repeat: (expr, cb) => {
                    let data = app.parse(`{{${expr}}}`);
                    if (Array.isArray(data)) return data.forEach(cb);
                    return '';
                },

                _route: req.route.path
            };

            let template = page;
            if (layout && !req.fragment) {
                routeData.content = '/' + page;
                template = 'layouts/' + layout;
            }

            if (exec) {
                return Promise.resolve(app.define(exec, true)).then(() => {
                    if (!res.headersSent) {
                        app.set(app.parse(routeData));
                        debug(`Render template ${template}`);
                        debug(`Template data: %O`, Object.assign({}, app.global.data, app.data));
                        res.render(template, Object.assign({}, app.global.data, app.data, methods), async (err, html) => {
                            // callback is needed when using ejs with aync, html is a promise
                            if (err) return next(err);
                            html.then(html => res.send(html)).catch(err => next(err));
                        });
                    }
                }).catch(next)
            } else {
                app.set(app.parse(routeData));
                debug(`Render template ${template}`);
                debug(`Template data: %O`, app.global.data);
                res.render(template, Object.assign({}, app.global.data, methods), async (err, html) => {
                    // callback is needed when using ejs with aync, html is a promise
                    if (err) return next(err);
                    html.then(html => res.send(html)).catch(err => next(err));
                });
            }
        };
    }
};