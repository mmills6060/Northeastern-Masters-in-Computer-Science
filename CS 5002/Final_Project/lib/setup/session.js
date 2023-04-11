const session = require('express-session'); //(Object.assign({ secret: config.secret }, config.session));
const debug = require('debug')('server-connect:setup:session');
const Parser = require('../core/parser');
const Scope = require('../core/scope');
const db = require('../core/db');
const { toSystemPath } = require('../core/path');
const config = require('./config');
const options = config.session;

if (!options.secret) {
    options.secret = config.secret;
}

debug('init session store %o', options.store);

if (options.store.$type == 'redis') { // https://www.npmjs.com/package/connect-redis
    const RedisStore = require('connect-redis')(session);
    options.store = new RedisStore(Object.assign({
        client: global.redisClient
    }, options.store));
} else if (options.store.$type == 'file') { // https://www.npmjs.com/package/session-file-store
    const FileStore = require('session-file-store')(session);
    options.store = new FileStore(options.store);
} else if (options.store.$type == 'database') { // https://www.npmjs.com/package/connect-session-knex
    const KnexStore = require('connect-session-knex')(session);

    if (typeof options.store.knex == 'string') {
        if (!global.db) global.db = {};

        if (!global.db[options.store.knex]) {
            const fs = require('fs-extra');
            const action = fs.readJSONSync(`app/modules/connections/${options.store.knex}.json`);
            const knex_options = Parser.parseValue(action.options, new Scope({ $_ENV: process.env }));

            if (knex_options.connection && knex_options.connection.filename) {
                knex_options.connection.filename = toSystemPath(knex_options.connection.filename);
            }

            if (knex_options.connection && knex_options.connection.ssl) {
                if (knex_options.connection.ssl.key) {
                    knex_options.connection.ssl.key = fs.readFileSync(toSystemPath(knex_options.connection.ssl.key));
                }
    
                if (knex_options.connection.ssl.ca) {
                    knex_options.connection.ssl.ca = fs.readFileSync(toSystemPath(knex_options.connection.ssl.ca));
                }
    
                if (knex_options.connection.ssl.cert) {
                    knex_options.connection.ssl.cert = fs.readFileSync(toSystemPath(knex_options.connection.ssl.cert));
                }
            }
    
            knex_options.useNullAsDefault = true;
    
            knex_options.postProcessResponse = function(result) {
                if (Array.isArray(result)) {
                    return result.map(row => {
                        for (column in row) {
                            if (row[column] && row[column].toJSON) {
                                row[column] = row[column].toJSON();
                            }
                        }
                        return row;
                    });
                } else {
                    for (column in result) {
                        if (result[column] && result[column].toJSON) {
                            result[column] = result[column].toJSON();
                        }
                    }
                    return result;
                }
            };

            global.db[options.store.knex] = db(knex_options);
        }

        options.store.knex = global.db[options.store.knex];
    }

    options.store = new KnexStore(options.store);
} else {
    const MemoryStore = require('../core/memoryStore')(session);
    options.store = new MemoryStore(options.store);
}

module.exports = session(options);