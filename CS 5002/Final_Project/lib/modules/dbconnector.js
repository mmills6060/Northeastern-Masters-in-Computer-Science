const db = require('../core/db');
const { where } = require('../formatters');
const debug = require('debug')('server-connect:db');

module.exports = {

    connect: function(options, name) {
        if (!name) throw new Error('dbconnector.connect has no name.');
        this.setDbConnection(name, options);
    },

    select: async function(options, name, meta) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.select: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.select: sql is required.');
        if (!sql.table) throw new Error('dbconnector.select: sql.table is required.');
        if (typeof sql.sort != 'string') sql.sort = this.parseOptional('{{ $_GET.sort }}', 'string', null);
        if (typeof sql.dir != 'string') sql.dir = this.parseOptional('{{ $_GET.dir }}', 'string', 'asc');

        if (sql.sort && sql.columns) {
            if (!sql.orders) sql.orders = [];

            for (let column of sql.columns) {
                if (column.column == sql.sort || column.alias == sql.sort) {
                    let order = {
                        column: column.alias || column.column,
                        direction: sql.dir.toLowerCase() == 'desc' ? 'desc' : 'asc'
                    };

                    if (column.table) order.table = column.table;

                    sql.orders.unshift(order);

                    break;
                }
            }
        }

        sql.type = 'select';

        if (db.client == 'couchdb') {
            let table = sql.table.table || sql.table;
            let { rows } = await db.list({ include_docs: true, startkey: table + '/', endkey: table + '0' });

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

            if (sql.orders && sql.orders.length) {
                rows.sort((a, b) => {
                    for (let order of sql.orders) {
                        if (a[order.column] == b[order.column]) continue;
                        let desc = order.direction && order.direction.toLowerCase() == 'desc';
                        if (a[order.column] < b[order.column]) {
                            return desc ? 1 : -1;
                        } else {
                            return desc ? -1 : 1;
                        }
                    }

                    return 0;
                });
            }

            if (sql.columns && sql.columns.length) {
                // we can also skip if user want just all columns
                if (!(sql.columns.length == 1 && sql.columns[0].column == '*')) {
                    rows = rows.map(doc => {
                        const row = {};

                        for (let column of sql.columns) {
                            if (column.column == '*') {
                                Object.assign(row, doc);
                            } else {
                                // only support single level for now
                                row[column.alias || column.column || column] = doc[column.column || column];
                            }
                        }

                        return row;
                    });
                }
            }

            if (sql.distinct) {
                rows = [...new Set(rows)];
            }

            let offset = Number(sql.offset || 0);
            let limit = Number(sql.limit || 0);
            return rows.slice(offset, limit ? offset + limit : undefined);
        }

        if (options.test) {
            return {
                options: options,
                query: db.fromJSON(sql, meta).toSQL().toNative()
            };
        }

        if (hasSubs(sql)) {
            prepareColumns(sql);

            const results = await db.fromJSON(sql, meta);

            if (results.length) {
                if (sql.sub) {
                    await _processSubQueries.call(this, db, results, sql.sub, meta);
                }

                if (sql.joins && sql.joins.length) {
                    for (const join of sql.joins) {
                        if (join.sub) {
                            await _processSubQueries.call(this, db, results, join.sub, meta, '_' + (join.alias || join.table));
                        }
                    }
                }

                cleanupResults(results);
            }

            return results;
        }

        return db.fromJSON(sql, meta);
    },

    count: async function(options) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.count: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.count: sql is required.');
        if (!sql.table) throw new Error('dbconnector.count: sql.table is required.');

        sql.type = 'count';

        if (db.client == 'couchdb') {
            let table = sql.table.table || sql.table;
            let { rows } = await db.list({ include_docs: true, startkey: table + '/', endkey: table + '0' });

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

            if (sql.distinct) {
                rows = [...new Set(rows)];
            }

            return rows.length;
        }

        if (options.test) {
            return {
                options: options,
                query: db.fromJSON(sql, meta).toSQL().toNative()
            };
        }

        return (await db.fromJSON(sql)).Total;
    },

    single: async function(options, name, meta) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.single: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.single: sql is required.');
        if (!sql.table) throw new Error('dbconnector.single: sql.table is required.');
        if (typeof sql.sort != 'string') sql.sort = this.parseOptional('{{ $_GET.sort }}', 'string', null);
        if (typeof sql.dir != 'string') sql.dir = this.parseOptional('{{ $_GET.dir }}', 'string', 'asc');

        sql.type = 'first';

        if (db.client == 'couchdb') {
            let table = sql.table.table || sql.table;
            let { rows } = await db.list({ include_docs: true, startkey: table + '/', endkey: table + '0' });

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

            if (sql.orders && sql.orders.length) {
                rows.sort((a, b) => {
                    for (let order of sql.orders) {
                        if (a[order.column] == b[order.column]) continue;
                        let desc = order.direction && order.direction.toLowerCase() == 'desc';
                        if (a[order.column] < b[order.column]) {
                            return desc ? 1 : -1;
                        } else {
                            return desc ? -1 : 1;
                        }
                    }

                    return 0;
                });
            }

            if (sql.columns && sql.columns.length) {
                // we can also skip if user want just all columns
                if (!(sql.columns.length == 1 && sql.columns[0].column == '*')) {
                    rows = rows.map(doc => {
                        const row = {};

                        for (let column of sql.columns) {
                            if (column.column == '*') {
                                Object.assign(row, doc);
                            } else {
                                // only support single level for now
                                row[column.alias || column.column || column] = doc[column.column || column];
                            }
                        }

                        return row;
                    });
                }
            }

            if (sql.distinct) {
                rows = [...new Set(rows)];
            }

            return rows.length ? rows[0] : null;
        }

        if (options.test) {
            return {
                options: options,
                query: db.fromJSON(sql, meta).toSQL().toNative()
            };
        }

        if (hasSubs(sql)) {
            prepareColumns(sql);

            const result = await db.fromJSON(sql, meta);

            if (!result) return null;

            if (sql.sub) {
                await _processSubQueries.call(this, db, [result], sql.sub, meta);
            }

            if (sql.joins && sql.joins.length) {
                for (const join of sql.joins) {
                    if (join.sub) {
                        await _processSubQueries.call(this, db, [result], join.sub, meta, '_' + (join.alias || join.table));
                    }
                }
            }

            cleanupResults([result]);

            return result;
        }

        return db.fromJSON(sql, meta) || null;
    },

    paged: async function(options, name, meta) {
        const connection = this.parseRequired(options.connection, 'string', 'dbconnector.paged: connection is required.');
        const sql = this.parseSQL(options.sql);
        const db = this.getDbConnection(connection);

        if (!db) throw new Error(`Connection "${connection}" doesn't exist.`);
        if (!sql) throw new Error('dbconnector.paged: sql is required.');
        if (!sql.table) throw new Error('dbconnector.paged: sql.table is required.');
        if (typeof sql.offset != 'number') sql.offset = Number(this.parseOptional('{{ $_GET.offset }}', '*', 0));
        if (typeof sql.limit != 'number') sql.limit = Number(this.parseOptional('{{ $_GET.limit }}', '*', 25));
        if (typeof sql.sort != 'string') sql.sort = this.parseOptional('{{ $_GET.sort }}', 'string', null);
        if (typeof sql.dir != 'string') sql.dir = this.parseOptional('{{ $_GET.dir }}', 'string', 'asc');

        if (sql.sort && sql.columns) {
            if (!sql.orders) sql.orders = [];

            for (let column of sql.columns) {
                if (column.column == sql.sort || column.alias == sql.sort) {
                    let order = {
                        column: column.alias || column.column,
                        direction: sql.dir.toLowerCase() == 'desc' ? 'desc' : 'asc'
                    };

                    if (column.table) order.table = column.table;

                    sql.orders.unshift(order);
                    
                    break;
                }
            }
        }

        if (db.client == 'couchdb') {
            let table = sql.table.table || sql.table;
            let { rows } = await db.list({ include_docs: true, startkey: table + '/', endkey: table + '0' });

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

            if (sql.orders && sql.orders.length) {
                rows.sort((a, b) => {
                    for (let order of sql.orders) {
                        if (a[order.column] == b[order.column]) continue;
                        let desc = order.direction && order.direction.toLowerCase() == 'desc';
                        if (a[order.column] < b[order.column]) {
                            return desc ? 1 : -1;
                        } else {
                            return desc ? -1 : 1;
                        }
                    }

                    return 0;
                });
            }

            if (sql.columns && sql.columns.length) {
                // we can also skip if user want just all columns
                if (!(sql.columns.length == 1 && sql.columns[0].column == '*')) {
                    rows = rows.map(doc => {
                        const row = {};

                        for (let column of sql.columns) {
                            if (column.column == '*') {
                                Object.assign(row, doc);
                            } else {
                                // only support single level for now
                                row[column.alias || column.column || column] = doc[column.column || column];
                            }
                        }

                        return row;
                    });
                }
            }

            if (sql.distinct) {
                rows = [...new Set(rows)];
            }

            let offset = Number(sql.offset || 0);
            let limit = Number(sql.limit || 0);
            let total = rows.length;

            return {
                offset,
                limit,
                total,
                page: {
                    offset: {
                        first: 0,
                        prev: offset - limit > 0 ? offset - limit : 0,
                        next: offset + limit < total ? offset + limit : offset,
                        last: (Math.ceil(total / limit) - 1) * limit
                    },
                    current: Math.floor(offset / limit) + 1,
                    total: Math.ceil(total / limit)
                },
                data: rows.slice(offset, limit ? offset + limit : undefined)
            };
        }

        sql.type = 'count';
        let total = +(await db.fromJSON(sql, meta))['Total'];

        sql.type = 'select';
        let data = [];

        if (options.test) {
            return {
                options: options,
                query: db.fromJSON(sql, meta).toSQL().toNative()
            };
        }

        if (hasSubs(sql)) {
            prepareColumns(sql);

            const results = await db.fromJSON(sql, meta);
            
            if (results.length) {
                if (sql.sub) {
                    await _processSubQueries.call(this, db, results, sql.sub, meta);
                }

                if (sql.joins && sql.joins.length) {
                    for (const join of sql.joins) {
                        if (join.sub) {
                            await _processSubQueries.call(this, db, results, join.sub, meta, '_' + (join.alias || join.table));
                        }
                    }
                }

                cleanupResults(results);
            }

            data = results;
        } else {
            data = await db.fromJSON(sql, meta);
        }

        return {
            offset: sql.offset,
            limit: sql.limit,
            total,
            page: {
                offset: {
                    first: 0,
                    prev: sql.offset - sql.limit > 0 ? sql.offset - sql.limit : 0,
                    next: sql.offset + sql.limit < total ? sql.offset + sql.limit : sql.offset,
                    last: (Math.ceil(total / sql.limit) - 1) * sql.limit
                },
                current: Math.floor(sql.offset / sql.limit) + 1,
                total: Math.ceil(total / sql.limit)
            },
            data
        }
    },

};

async function _processSubQueries(db, results, sub, meta, prefix = '') {
    const lookup = new Map();
    const keys = new Set();

    // get keys from results and create lookup table
    // add initial sub field to results (empty array)
    for (const result of results) {
        const key = String(result['__dmxPrimary' + prefix]);
        
        if (lookup.has(key)) {
            lookup.get(key).push(result);
        } else {
            lookup.set(key, [result]);
        }

        keys.add(key);

        for (const field in sub) {
            result[field] = [];
        }
    }

    for (const field in sub) {
        const sql = this.parseSQL(sub[field]);
 
        sql.type = 'select';

        prepareColumns(sql);

        let submeta = meta && meta.find(data => data.name == field);
        if (submeta && submeta.sub) submeta = submeta.sub;

        // get all subresults with a single query
        const subResults = await db.fromJSON(sql, submeta).whereIn(sql.key, Array.from(keys));

        if (subResults.length) {
            if (sql.sub) {
                await _processSubQueries.call(this, db, subResults, sql.sub, submeta);
            }

            if (sql.joins && sql.joins.length) {
                for (const join of sql.joins) {
                    if (join.sub) {
                        await _processSubQueries.call(this, db, subResults, join.sub, submeta, '_' + (join.alias || join.table));
                    }
                }
            }

            // map the sub results to the parent recordset
            for (const subResult of subResults) {
                const results = lookup.get(String(subResult['__dmxForeign']));

                if (results) {
                    for (const result of results) {
                        result[field].push(subResult);
                    }
                }
            }
        }
    }

    // we don't need to return anything since all is updated by reference
}

function hasSubs(sql) {
    if (sql.sub) return true;

    if (sql.joins && sql.joins.length) {
        for (const join of sql.joins) {
            if (join.sub) return true;
        }
    }

    return false;
}

function prepareColumns(sql) {
    const table = sql.table.alias || sql.table.name || sql.table;

    if (!Array.isArray(sql.columns) || !sql.columns.length) {
        sql.columns = [{
            table: table,
            column: '*'
        }];

        if (Array.isArray(sql.joins) && sql.joins.length) {
            for (join of sql.joins) {
                sql.columns.push({
                    table: join.alias || join.table,
                    column: '*'
                });
            }
        }
    }

    if (sql.sub && sql.primary) {
        sql.columns.push({
            table: table,
            column: sql.primary,
            alias: '__dmxPrimary'
        });

        if (sql.groupBy && sql.groupBy.length) {
            sql.groupBy.push({
                table: table,
                column: sql.primary
            });
        }
    }

    if (sql.key) {
        sql.columns.push({
            table: table,
            column: sql.key,
            alias: '__dmxForeign'
        });

        if (sql.groupBy && sql.groupBy.length) {
            sql.groupBy.push({
                table: table,
                column: sql.key
            });
        }
    }

    if (sql.joins && sql.joins.length) {
        for (const join of sql.joins) {
            if (join.sub && join.primary) {
                sql.columns.push({
                    table: join.alias || join.table,
                    column: join.primary,
                    alias: '__dmxPrimary_' + (join.alias || join.table)
                });

                if (sql.groupBy && sql.groupBy.length) {
                    sql.groupBy.push({
                        table: join.alias || join.table,
                        column: join.primary
                    });
                }
            }
        }
    }
}

function cleanupResults(results) {
    for (const result of results) {
        for (const field of Object.keys(result)) {
            if (field.startsWith('__dmx')) {
                delete result[field];
            } else if (Array.isArray(result[field])) {
                cleanupResults(result[field]);
            }
        }
    }
}