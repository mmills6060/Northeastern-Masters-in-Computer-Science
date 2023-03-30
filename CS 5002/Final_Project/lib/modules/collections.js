const { clone } = require('../core/util');

module.exports = {

    addColumns: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.addColumns: collection is required.');
        let add = this.parseRequired(options.add, 'object', 'collections.addColumns: add is required.');
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let output = [];

        for (let row of collection) {
            let newRow = clone(row);

            for (let column in add) {
                if (overwrite || newRow[column] == null) {
                    newRow[column] = add[column];
                }
            }

            output.push(newRow);
        }

        return output;
    },
    
    filterColumns: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.filterColumns: collection is required.');
        let columns = this.parseRequired(options.columns, 'object'/*array[string]*/, 'collections.filterColumns: columns is required.');
        let keep = this.parseOptional(options.keep, 'boolean', false);
        let output = [];

        for (let row of collection) {
            let newRow = {};

            for (let column in row) {
                if (columns.includes(column)) {
                    if (keep) {
                        newRow[column] = clone(row[column]);
                    }
                } else if (!keep) {
                    newRow[column] = clone(row[column]);
                }
            }

            output.push(newRow);
        }

        return output;
    },
    
    renameColumns: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.renamecolumns: collection is required.');
        let rename = this.parseRequired(options.rename, 'object', 'collections.renamecolumns: rename is required.');
        let output = [];

        for (let row of collection) {
            let newRow = {};

            for (let column in row) {
                newRow[rename[column] || column] = clone(row[column]);
            }

            output.push(newRow);
        }

        return output;
    },
    
    fillDown: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.fillDown: collection is required.');
        let columns = this.parseRequired(options.columns, 'object'/*array[string]*/, 'collections.fillDown: columns is required.');
        let output = [];
        let values = {};

        for (let column of columns) {
            values[column] = null;
        }

        for (let row of collection) {
            let newRow = clone(row);

            for (let column in values) {
                if (newRow[column] == null) {
                    newRow[column] = values[column];
                } else {
                    values[column] = newRow[column];
                }
            }

            output.push(newRow);
        }

        return output;
    },
    
    addRows: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.addRows: collection is required.');
        let rows = this.parseRequired(options.rows, 'object'/*array[object]*/, 'collections.addRows: rows is required.');

        return clone(collection).concat(clone(rows));
    },
    
    addRownumbers: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.addRownumbers: collection is required.');
        let column = this.parseOptional(options.column, 'string', 'nr');
        let startAt = this.parseOptional(options.startAt, 'number', 1);
        let desc = this.parseOptional(options.desc, 'boolean', false);
        let output = [];
        let nr = desc ? collection.length + startAt - 1 : startAt;

        for (let row of collection) {
            let newRow = clone(row);
            
            newRow[column] = desc ? nr-- : nr++;
            
            output.push(newRow);
        }

        return output;
    },
    
    join: function(options) {
        let collection1 = this.parseRequired(options.collection1, 'object'/*array[object]*/, 'collections.join: collection1 is required.');
        let collection2 = this.parseRequired(options.collection2, 'object'/*array[object]*/, 'collections.join: collection2 is required.');
        let matches = this.parseRequired(options.matches, 'object', 'collections.join: matches is required.');
        let matchAll = this.parseOptional(options.matchAll, 'boolean', false);
        let output = [];

        for (let row1 of collection1) {
            let newRow = clone(row1);

            for (let row2 of collection2) {
                let join = false;

                for (let match in matches) {
                    if (row1[match] == row2[matches[match]]) {
                        join = true;
                        if (!matchAll) break;
                    } else if (matchAll) {
                        join = false;
                        break;
                    }
                }

                if (join) {
                    for (let column in row2) {
                        newRow[column] = clone(row2[column]);
                    }
                    break;
                }
            }

            output.push(newRow);
        }

        return output;
    },
    
    normalize: function(options) {
        let collection = this.parseRequired(options.collection, 'object'/*array[object]*/, 'collections.normalize: collection is required.');
        let columns = [];
        let output = [];

        for (let row of collection) {
            for (let column in row) {
                if (!columns.includes(column)) {
                    columns.push(column);
                }
            }
        }

        for (let row of collection) {
            let newRow = {};

            for (let column of columns) {
                newRow[column] = row[column] == null ? null : clone(row[column]);
            }

            output.push(newRow);
        }

        return output;
    },
    
};