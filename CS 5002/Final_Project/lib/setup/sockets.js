const fs = require('fs-extra');
const { basename, extname } = require('path');
const debug = require('debug')('server-connect:sockets');
const { isEmpty } = require('./util');
const config = require('./config');
const cookieParser = require('cookie-parser');
const { promisify } = require('util');

module.exports = function (server, appSession) {
    //if (isEmpty('app/sockets')) return null;

    const io = require('socket.io')();

    if (global.redisClient) {
        /*
        const redisAdapter = require('socket.io-redis');
        io.adapter(redisAdapter({
            pubClient: global.redisClient.duplicate(),
            subClient: global.redisClient.duplicate()
        }));
        */
       const { createAdapter } = require('@socket.io/redis-adapter');
       io.adapter(createAdapter(
        global.redisClient.duplicate(),
        global.redisClient.duplicate()
       ));
    }

    // user hooks
    if (fs.existsSync('extensions/server_connect/sockets')) {
        const entries = fs.readdirSync('extensions/server_connect/sockets', { withFileTypes: true });

        for (let entry of entries) {
            if (entry.isFile() && extname(entry.name) == '.js') {
                const hook = require(`../../extensions/server_connect/sockets/${entry.name}`);
                if (hook.handler) hook.handler(io);
                debug(`Custom sockets hook ${entry.name} loaded`);
            }
        }
    }

    // create socket connections for api endpoints
    if (fs.existsSync('app/api')) {

        io.of('/api').on('connection', async (socket) => {
            socket.onAny(async (event, params, cb) => {
                try {
                    if (typeof cb == 'function' && global.redisClient) {
                        const redisGet = promisify(global.redisClient.get).bind(global.redisClient);
                        const cached = await redisGet('ws:' + event + ':' + JSON.stringify(params));
                        if (cached) return cb(JSON.parse(cached));
                    }

                    const req = Object.assign({}, socket.handshake);
                    const res = {
                        statusCode: 200,
                        getHeader: () => { },
                        setHeader: () => { },
                        sendStatus: (statusCode) => { res.statusCode = statusCode; },
                        write: () => { },
                        end: () => { }
                    };

                    cookieParser(config.secret)(req, res, () => {
                        appSession(req, res, async () => {
                            const App = require('../core/app');
                            const app = new App(req, res);
                            const action = await fs.readJSON(`app/api/${event}.json`);
                            app.set('$_PARAM', params);
                            app.set('$_GET', params); // fake query params
                            app.socket = socket;
                            await app.define(action, true);
                            if (typeof cb == 'function') {
                                cb({
                                    status: res.statusCode,
                                    data: res.statusCode == 200 ? app.data : null
                                });

                                if (global.redisClient) {
                                    let ttl = (action.settings && action.settings.options && action.settings.options.ttl) ? action.settings.options.ttl : null;

                                    if (ttl) {
                                        global.redisClient.setex('ws:' + event + ':' + JSON.stringify(params), ttl, JSON.stringify({
                                            status: res.statusCode,
                                            data: res.statusCode == 200 ? app.data : null
                                        }));
                                    }
                                }
                            }
                        });
                    });
                } catch (e) {
                    debug(`ERROR: ${e.message}`);
                    console.error(e);
                }
            });
        });
    }

    if (fs.existsSync('app/sockets')) {
        parseSockets();
    }

    function parseSockets(namespace = '') {
        const entries = fs.readdirSync('app/sockets' + namespace, { withFileTypes: true });

        io.of(namespace || '/').on('connection', async (socket) => {
            if (fs.existsSync(`app/sockets${namespace}/connect.json`)) {
                try {
                    const req = Object.assign({}, socket.handshake);
                    const res = {
                        statusCode: 200,
                        getHeader: () => { },
                        setHeader: () => { },
                        sendStatus: (statusCode) => { res.statusCode = statusCode; },
                        write: () => { },
                        end: () => { }
                    };

                    cookieParser(config.secret)(req, res, () => {
                        appSession(req, res, async () => {
                            const App = require('../core/app');
                            const app = new App(req, res);
                            const action = await fs.readJSON(`app/sockets${namespace}/connect.json`);
                            app.socket = socket;
                            await app.define(action, true);
                        });
                    });
                } catch (e) {
                    debug(`ERROR: ${e.message}`);
                    console.error(e);
                }
            }

            if (fs.existsSync(`app/sockets${namespace}/disconnect.json`)) {
                socket.on('disconnect', async (event) => {
                    try {
                        const req = Object.assign({}, socket.handshake);
                        const res = {
                            statusCode: 200,
                            getHeader: () => { },
                            setHeader: () => { },
                            sendStatus: (statusCode) => { res.statusCode = statusCode; },
                            write: () => { },
                            end: () => { }
                        };
    
                        cookieParser(config.secret)(req, res, () => {
                            appSession(req, res, async () => {
                                const App = require('../core/app');
                                const app = new App(req, res);
                                const action = await fs.readJSON(`app/sockets${namespace}/disconnect.json`);
                                app.socket = socket;
                                await app.define(action, true);
                            });
                        });
                    } catch (e) {
                        debug(`ERROR: ${e.message}`);
                        console.error(e);
                    }
                });
            }

            socket.onAny(async (event, params, cb) => {
                try {
                    const req = Object.assign({}, socket.handshake);
                    const res = {
                        statusCode: 200,
                        getHeader: () => { },
                        setHeader: () => { },
                        sendStatus: (statusCode) => { res.statusCode = statusCode; },
                        write: () => { },
                        end: () => { }
                    };

                    cookieParser(config.secret)(req, res, () => {
                        appSession(req, res, async () => {
                            const App = require('../core/app');
                            const app = new App(req, res);
                            const action = await fs.readJSON(`app/sockets${namespace}/${event}.json`);
                            app.set('$_PARAM', params);
                            app.socket = socket;
                            await app.define(action, true);
                            if (typeof cb == 'function') cb(app.data);
                        });
                    });
                } catch (e) {
                    debug(`ERROR: ${e.message}`);
                    console.error(e);
                }
            });
        });

        for (let entry of entries) {
            if (entry.isDirectory()) {
                parseSockets(namespace + '/' + entry.name);
            }
        }
    }

    io.attach(server);

    return io;
};