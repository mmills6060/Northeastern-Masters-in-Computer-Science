const fs = require('fs-extra');
const { toSystemPath } = require('../core/path');
const { keysToLowerCase } = require('../core/util');

// simple inital implementation
// better implementation at:
// https://github.com/adaltas/node-csv-parse
// https://github.com/mafintosh/csv-parser
function parseCSV(csv, options) {
    if (!csv) return [];

    if (csv.charCodeAt(0) === 0xFEFF) {
        csv = csv.slice(1);
    }

    let delimiter = options.delimiter.replace('\\t', '\t');
    let keys = options.fields;
    let line = 1;
    let data = [];

    if (options.header) {
        keys = getcsv();

        options.fields.forEach(field => {
            if (keys.indexOf(field) == -1) {
                throw new Error('parseCSV: ' + field + ' is missing in ' + options.path);
            }
        });

        line++;
    }

    let size = keys.length;

    while (csv.length) {
        let values = getcsv();
        let o = {};

        if (values.length != size) {
            throw new Error('parseCSV: colomns do not match. keys: ' + size + ', values: ' + values.length + ' at line ' + line);
        }

        for (let i = 0; i < size; i++) {
            o[keys[i]] = values[i];
        }

        data.push(o);

        line++;
    }

    return data;

    function getcsv() {
        let data = [''], l = csv.length,
            esc = false, escesc = false,
            n = 0, i = 0;

        while (i < l) {
            let s = csv.charAt(i);

            if (s == '\n') {
                if (esc) {
                    data[n] += s;
                } else {
                    i++;
                    break;
                }
            } else if (s == '\r') {
                if (esc) {
                    data[n] += s;
                }
            } else if (s == delimiter) {
                if (esc) {
                    data[n] += s;
                } else {
                    data[++n] = '';
                    esc = false;
                    escesc = false;
                }
            } else if (s == '"') {
                if (escesc) {
                    data[n] += s;
                    escesc = false;
                }

                if (esc) {
                    esc = false;
                    escesc = true;
                } else {
                    esc = true;
                    escesc = false;
                }
            } else {
                if (escesc) {
                    data[n] += '"';
                    escesc = false;
                }

                data[n] += s;
            }

            i++;
        }

        csv = csv.substr(i);

        return data;
    }
}

module.exports = {

    csv: async function(options) {
        let path = this.parseRequired(options.path, 'string', 'export.csv: path is required.');
        let fields = this.parseOptional(options.fields, 'object', []);
        let header = this.parseOptional(options.header, 'boolean', false);
        let delimiter = this.parseOptional(options.delimiter, 'string', ',');
        let csv = await fs.readFile(toSystemPath(path), 'utf8');

        return parseCSV(csv, { fields, header, delimiter });
    },

    xml: async function(options) {
        // TODO: import.xml
        throw new Error('import.xml: not implemented.');
    },

};