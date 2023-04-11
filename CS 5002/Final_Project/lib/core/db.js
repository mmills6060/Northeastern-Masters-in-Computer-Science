const knex = require('knex');

knex.QueryBuilder.extend('whereGroup', function(condition, rules) {
    condition = condition.toLowerCase();

    // TODO: Escape likes

    for (let rule of rules) {
        if (!rule.condition) {
            let where = condition == 'or' ? 'orWhere' : 'where';
            let column = rule.data ? rule.data.column : rule.column;

            if (rule.data && rule.data.table) {
                if (rule.data.schema) {
                    column = rule.data.schema + '.' + rule.data.table + '.' + column;
                } else {
                    column = rule.data.table + '.' + column;
                }
            } else if (rule.table) {
                if (rule.schema) {
                    column = rule.schema + '.' + rule.table + '.' + column;
                } else {
                    column = rule.table + '.' + column;
                }
            }

            if (typeof rule.value == 'undefined') {
                rule.value = null;
            }

            if (rule.operator == 'between') {
                this[where + 'Between'](column, rule.value);
            } else if (rule.operator == 'not_between') {
                this[where + 'NotBetween'](column, rule.value);
            } else if (rule.operator == 'is_null') {
                this[where + 'Null'](column);
            } else if (rule.operator == 'is_not_null') {
                this[where + 'NotNull'](column);
            } else if (rule.operator == 'in') {
                this[where + 'In'](column, rule.value);
            } else if (rule.operator == 'not_in') {
                this[where + 'NotIn'](column, rule.value);
            } else if (rule.operator == 'begins_with') {
                this[where](column, 'like', rule.value + '%');
            } else if (rule.operator == 'not_begins_with') {
                this[where + 'Not'](column, 'like', rule.value + '%');
            } else if (rule.operator == 'ends_with') {
                this[where](column, 'like', '%' + rule.value);
            } else if (rule.operator == 'not_ends_with') {
                this[where + 'Not'](column, 'like', '%' + rule.value);
            } else if (rule.operator == 'contains') {
                this[where](column, 'like', '%' + rule.value + '%');
            } else if (rule.operator == 'not_contains') {
                this[where + 'Not'](column, 'like', '%' + rule.value + '%');
            } else {
                this[where](column, rule.operation, rule.value);
            }
        } else {
            this[condition + 'Where'](function() {
                this.whereGroup(rule.condition, rule.rules);
            });
        }
    }

    return this;
});

knex.QueryBuilder.extend('fromJSON', function(ast, meta) {
    if (ast.type == 'count') {
        return this.count('* as Total').from(function() {
            this.fromJSON(Object.assign({}, ast, {
                type: 'select',
                offset: null,
                limit: null,
                orders: null
            })).as('t1');
        }).first();
    } else if (ast.type == 'insert' || ast.type == 'update') {
        let values = {};

        for (let val of ast.values) {
            if (val.type == 'json') {
                // json support
                values[val.column] = JSON.stringify(val.value);
            } else {
                values[val.column] = val.value;
            }
        }

        this[ast.type](values);
    } else {
        this[ast.type]();
    }

    if (ast.returning) {
        // Adding the option includeTriggerModifications allows you
        // to run statements on tables that contain triggers. Only affects MSSQL.
        this.returning(ast.returning, { includeTriggerModifications: true });
    }

    if (ast.table) {
        let table = ast.table.name || ast.table;

        if (ast.table.schema) {
            table = ast.table.schema + '.' + table;
        }

        if (ast.table.alias) {
            table += ' as ' + ast.table.alias;
        }

        this.from(table);
    }

    if ((ast.type == 'select' || ast.type == 'first') && ast.joins && ast.joins.length) {
        for (let join of ast.joins) {
            let table = join.table;

            if (join.schema) {
                table = join.schema + '.' + table;
            }

            if (join.alias) {
                table += ' as ' + join.alias;
            }

            this[(join.type || 'inner').toLowerCase() + 'Join'](table, function() {
                for (let clause of join.clauses.rules) {
                    this.on(
                        (clause.schema ? clause.schema + '.' : '') + clause.table + '.' + clause.column,
                        clause.operation,
                        (clause.value.schema ? clause.value.schema + '.' : '') + clause.value.table + '.' + clause.value.column
                    );
                }
            });
        }
    }

    if ((ast.type == 'select' || ast.type == 'first') && ast.columns) {
        for (let col of ast.columns) {
            let column = col.column || col;

            if (ast.joins && ast.joins.length && col.table) {
                column = col.table + '.' + column;
    
                if (col.schema) {
                    column = col.schema + '.' + column;
                }
            }

            if (col.alias) {
                column += ' as ' + col.alias;
            }

            this[col.aggregate ? col.aggregate.toLowerCase() : 'column'](column);
        }
    }

    if ((ast.type == 'select' || ast.type == 'first') && ast.groupBy && ast.groupBy.length) {
        for (let col of ast.groupBy) {
            if (ast.joins && ast.joins.length && col.table) {
                if (col.schema) {
                    this.groupBy(col.schema + '.' + col.table + '.' + col.column);
                } else {
                    this.groupBy(col.table + '.' + col.column);
                }
            } else {
                this.groupBy(col.column || col);
            }
        }
    }

    if (ast.wheres && ast.wheres.condition) {
        this.whereGroup(ast.wheres.condition, ast.wheres.rules);
    }

    if ((ast.type == 'select' || ast.type == 'first') && ast.orders && ast.orders.length) {
        for (let order of ast.orders) {
            if (ast.joins && ast.joins.length && order.table) {
                if (order.schema) {
                    this.orderBy(order.schema + '.' + order.table + '.' + order.column, order.direction);
                } else {
                    this.orderBy(order.table + '.' + order.column, order.direction);
                }
            } else {
                this.orderBy(order.column, order.direction);
            }
        }
    }

    if (ast.distinct) {
        this.distinct();
    }

    if (ast.type == 'select' && ast.limit) {
        this.limit(ast.limit);
    }

    if (ast.type == 'select' && ast.offset) {
        this.offset(ast.offset);
    }

    if (meta) {
        this.queryContext(meta);
    }
    
	return this;
});

module.exports = knex;