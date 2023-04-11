module.exports = {

    insert: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.insert: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.insert: sql is required.');
        if (!sql.table) throw new Error('dbconnector.insert: sql.table is required.');

        sql.type = 'insert';

        if (db.client == 'couchdb') {
            const doc = {};

            for (const value of sql.values) {
                doc[value.column] = value.value;
            }

            const result = await db.insert(doc, sql.table + '/' + Date.now());
            
            if (result.ok) {
                return { affected: 1, identity: result.id };
            } else {
                //throw new Error('dbconnector.insert: error inserting document into couchdb.');
                return { affected: 0 };
            }
        }

        if (options.test) {
            return {
                options: options,
                query: sql.toString()
            };
        }

        if (sql.sub) {
            return db.transaction(async trx => {
                // TODO: test how identity is returned for each database
                // main insert, returns inserted id
                const [identity] = (await trx.fromJSON(sql)).map(value => value[sql.returning] || value);

                // loop sub (relation table)
                for (let { table, key, value, values } of Object.values(sql.sub)) {
                    if (!Array.isArray(value)) break;

                    for (const current of value) {
                        if (typeof current == 'object') {
                            current[key] = identity;
                            await trx(table).insert(current);
                        } else {
                            if (values.length != 1) throw new Error('Invalid value mapping');
                            await trx(table).insert({
                                [key]: identity,
                                [values[0].column]: current
                            });
                        }
                    }
                }

                return { affected: 1, identity };
            });
        }

        let identity = await db.fromJSON(sql);

        if (identity) {
            if (Array.isArray(identity)) {
                identity = identity[0];
            }
    
            if (typeof identity == 'object') {
                identity = identity[Object.keys(identity)[0]];
            }
        }

        return { affected: 1, identity };
    },

    update: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.update: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.update: sql is required.');
        if (!sql.table) throw new Error('dbconnector.update: sql.table is required.');

        sql.type = 'update';

        if (db.client == 'couchdb') {
            let { rows } = await db.list({ include_docs: true, startkey: sql.table + '/', endkey: sql.table + '0' });

            rows = rows.map(row => row.doc);

            if (sql.wheres) {
                const validate = (row, rule) => {
                    if (rule.operator) {
                        let a = row[rule.data.column];
                        let b = rule.value;

                        switch (rule.operator) {
                            case 'equal': return a == b;
                            case 'not_equal': return a != b;
                            case 'in': return b.includes(a);
                            case 'not_in': return !b.includes(a);
                            case 'less': return a < b;
                            case 'less_or_equal': return a <= b;
                            case 'greater': return a > b;
                            case 'greater_or_equal': return a >= b;
                            case 'between': return b[0] <= a <= b[1];
                            case 'not_between': return !(b[0] <= a <= b[1]);
                            case 'begins_with': return String(a).startsWith(String(b));
                            case 'not_begins_with': return !String(a).startsWith(String(b));
                            case 'contains': return String(a).includes(String(b));
                            case 'not_contains': return !String(a).includes(String(b));
                            case 'ends_with': return String(a).endsWith(String(b));
                            case 'not_ends_with': return !String(a).endsWith(String(b));
                            case 'is_empty': return a == null || a == '';
                            case 'is_not_empty': return a != null && a != '';
                            case 'is_null': return a == null;
                            case 'is_not_null': return a != null;
                        }
                    }

                    if (rule.condition && rule.rules.length) {
                        for (const _rule of rule.rules) {
                            const valid = validate(row, _rule);
                            if (!valid && rule.condition == 'AND') return false;
                            if (valid && rule.condition == 'OR') return true;
                        }

                        return rule.condition == 'OR' ? false : true;
                    }

                    return true;
                };

                rows = rows.filter(row => {
                    return validate(row, sql.wheres);
                });
            }

            const result = await db.bulk(rows.map(doc => {
                for (const value of sql.values) {
                    doc[value.column] = value.value;
                }

                return doc;
            }));

            return { affected: Array.isArray(result) ? result.filter(result => result.ok).length : rows.length };
        }

        if (options.test) {
            return {
                options: options,
                query: sql.toString()
            };
        }

        if (sql.sub) {
            return db.transaction(async trx => {
                let updated = await trx.fromJSON(sql);

                if (!Array.isArray(updated)) {
                    // check if is single update
                    const single = (
                        sql.wheres &&
                        sql.wheres.rules &&
                        sql.wheres.rules.length == 1 &&
                        sql.wheres.rules[0].field == sql.returning &&
                        sql.wheres.rules[0].operation == '='
                    );

                    if (single) {
                        // get id from where condition
                        updated = [sql.wheres.rules[0].value];
                    } else {
                        // create a select with same where conditions
                        updated = await trx.fromJSON({
                            ...sql,
                            type: 'select',
                            columns: [sql.returning]
                        });

                        updated = updated.map(value => value[sql.returning]);
                    }
                } else {
                    updated = updated.map(value => value[sql.returning]);
                }

                // loop sub
                for (let { table, key, value, values } of Object.values(sql.sub)) {
                    if (!Array.isArray(value)) break;

                    // delete old related data first
                    await trx(table).whereIn(key, updated).del();

                    // for each updated item
                    for (const identity of updated) {
                        // insert value
                        for (const current of value) {
                            if (typeof current == 'object') {
                                current[key] = identity;
                                await trx(table).insert(current);
                            } else {
                                if (values.length != 1) throw new Error('Invalid value mapping');
                                await trx(table).insert({
                                    [key]: identity,
                                    [values[0].column]: current
                                });
                            }
                        }
                    }
                }

                return { affected: updated.length };
            });
        }

        let affected = await db.fromJSON(sql);

        return { affected };
    },

    delete: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.delete: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.delete: sql is required.');
        if (!sql.table) throw new Error('dbconnector.delete: sql.table is required.');

        sql.type = 'del';

        if (db.client == 'couchdb') {
            let { rows } = await db.list({ include_docs: true, startkey: sql.table + '/', endkey: sql.table + '0' });

            rows = rows.map(row => row.doc);

            if (sql.wheres) {
                const validate = (row, rule) => {
                    if (rule.operator) {
                        let a = row[rule.data.column];
                        let b = rule.value;

                        switch (rule.operator) {
                            case 'equal': return a == b;
                            case 'not_equal': return a != b;
                            case 'in': return b.includes(a);
                            case 'not_in': return !b.includes(a);
                            case 'less': return a < b;
                            case 'less_or_equal': return a <= b;
                            case 'greater': return a > b;
                            case 'greater_or_equal': return a >= b;
                            case 'between': return b[0] <= a <= b[1];
                            case 'not_between': return !(b[0] <= a <= b[1]);
                            case 'begins_with': return String(a).startsWith(String(b));
                            case 'not_begins_with': return !String(a).startsWith(String(b));
                            case 'contains': return String(a).includes(String(b));
                            case 'not_contains': return !String(a).includes(String(b));
                            case 'ends_with': return String(a).endsWith(String(b));
                            case 'not_ends_with': return !String(a).endsWith(String(b));
                            case 'is_empty': return a == null || a == '';
                            case 'is_not_empty': return a != null && a != '';
                            case 'is_null': return a == null;
                            case 'is_not_null': return a != null;
                        }
                    }

                    if (rule.condition && rule.rules.length) {
                        for (const _rule of rule.rules) {
                            const valid = validate(row, _rule);
                            if (!valid && rule.condition == 'AND') return false;
                            if (valid && rule.condition == 'OR') return true;
                        }

                        return rule.condition == 'OR' ? false : true;
                    }

                    return true;
                };

                rows = rows.filter(row => {
                    return validate(row, sql.wheres);
                });
            }

            const result = await db.bulk(rows.map(doc => {
                doc._deleted = true;
                return doc;
            }));

            return { affected: Array.isArray(result) ? result.filter(result => result.ok).length : rows.length };
        }

        if (options.test) {
            return {
                options: options,
                query: sql.toString()
            };
        }

        if (sql.sub) {
            return db.transaction(async trx => {
                const deleted = (await trx.fromJSON(sql)).map(value => value[sql.returning] || value);

                // loop sub
                for (let { table, key } of Object.values(sql.sub)) {
                    // delete related data
                    await trx(table).whereIn(key, deleted).del();
                }

                return { affected: deleted.length };
            });
        }

        let affected = await db.fromJSON(sql);

        return { affected };
    },

    custom: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbupdater.custom: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.custom: sql is required.');
        if (typeof sql.query != 'string') throw new Error('dbupdater.custom: sql.query is required.');
        if (!Array.isArray(sql.params)) throw new Error('dbupdater.custom: sql.params is required.');

        if (db.client == 'couchdb') {
            throw new Error('dbupdater.custom: couchdb is not supported.');
        }

        const params = [];
        const query = sql.query.replace(/([:@][a-zA-Z_]\w*|\?)/g, param => {
            if (param == '?') {
                params.push(sql.params[params.length].value);
                return '?';
            }

            let p = sql.params.find(p => p.name == param);
            if (p) {
                params.push(p.value);
                return '?';
            }

            return param;
        });

        let results = await db.raw(query, params);

        if (db.client.config.client == 'mysql' || db.client.config.client == 'mysql2') {
            results = results[0];
        } else if (db.client.config.client == 'postgres' || db.client.config.client == 'redshift') {
            results = results.rows;
        }

        return results;
    },

    execute: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbupdater.execute: connection is required.');
        const query = this.parseRequired(options.query, 'string', 'dbupdater.execute: query is required.');
        const params = this.parseOptional(options.params, 'object', []);
        const db = this.getDbConnection(connection);
        
        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);

        if (db.client == 'couchdb') {
            throw new Error('dbupdater.execute: couchdb is not supported.');
        }

        let results = await db.raw(query, params);

        if (db.client.config.client == 'mysql' || db.client.config.client == 'mysql2') {
            results = results[0];
        } else if (db.client.config.client == 'postgres' || db.client.config.client == 'redshift') {
            results = results.rows;
        }

        return results;
    },

    // bulk insert
    // values is array of objects with column(key) and value
    // batchSize is number of inserts per query (multi insert statement)
    bulkinsert: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbupdater.bulkinsert: connection is required.');
        const table = this.parseRequired(options.table, 'string', 'dbupdater.bulkinsert: table is required.');
        const values = this.parseRequired(options.values, 'object', 'dbupdater.bulkinsert: values is required.');
        const batchSize = this.parseOptional(options.batchSize, 'number', 100);
        const db = this.getDbConnection(connection);

        if (db.client == 'couchdb') {
            throw new Error('dbupdater.bulkinsert: couchdb is not supported.');
        }

        await db.transaction(async transaction => {
            for (let i = 0; i < values.length; i += batchSize) {
                let batch = values.slice(i, i + batchSize);
                await transaction(table).insert(batch);
            }
        });
    },

};