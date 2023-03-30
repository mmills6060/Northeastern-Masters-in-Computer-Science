const fs = require('fs-extra');
const { toSystemPath } = require('../core/path');

module.exports = {

    csv: async function(options) {
        let path = this.parse(options.path);
        let data = this.parse(options.data);
        let header = this.parse(options.header);
        let delimiter = this.parse(options.delimiter);
        let overwrite = this.parse(options.overwrite);
        
        if (typeof path != 'string') throw new Error('export.csv: path is required.');
        if (!Array.isArray(data) || !data.length) throw new Error ('export.csv: data is required.');
        
        delimiter = typeof delimiter == 'string' ? delimiter : ',';

        if (delimiter == '\\t') delimiter = '\t';

        const fd = await fs.open(toSystemPath(path), overwrite ? 'w' : 'wx');

        if (header) {
            await putcsv(fd, Object.keys(data[0]), delimiter);
        }

        for (let row of data) {
            await putcsv(fd, row, delimiter);
        }

        await fs.close(fd);

        return path;
    },

    xml: async function(options) {
        let path = this.parse(options.path);
        let data = this.parse(options.data);
        let root = this.parse(options.root);
        let item = this.parse(options.item);
        let overwrite = this.parse(options.overwrite);

        if (typeof path != 'string') throw new Error('export.xml: path is required.');
        if (!Array.isArray(data) || !data.length) throw new Error('export.xml: data is required.');

        root = typeof root == 'string' ? root : 'export';
        item = typeof item == 'string' ? item : 'item';
        
        const fd = await fs.open(toSystemPath(path), overwrite ? 'w' : 'wx');

        await fs.write(fd, `<?xml version="1.0" encoding="UTF-8" ?><${root}>`);
        for (let row of data) {
            await fs.write(fd, `<${item}>`);
            for (let prop in row) {
                await fs.write(fd, `<${prop}><![CDATA[${row[prop]}]]></${prop}>`);
            }
            await fs.write(fd, `</${item}>`);
        }
        await fs.write(fd, `</${root}>`);
        
        await fs.close(fd);

        return path;
    },

};

async function putcsv(fd, data, delimiter) {
    let str = '';

    if (typeof data != 'object') {
        throw new Error('putcsv: Invalid data.');
    }

    for (let prop in data) {
        if (data.hasOwnProperty(prop)) {
            let value = String(data[prop]);

            if (/["\n\r\t\s]/.test(value) || value.includes(delimiter)) {
                let escaped = false;
                
                str += '"';

                for (let i = 0; i < value.length; i++) {
                    if (value.charAt(i) == '\\') {
                        escaped = true;
                    } else if (!escaped && value.charAt(i) == '"') {
                        str += '"';
                    } else {
                        escaped = false;
                    }

                    str += value.charAt(i);
                }

                str += '"';
            } else {
                str += value;
            }

            str += delimiter;
        }
    }

    if (!str) {
        throw new Error('putcsv: No data.');
    }

    return fs.write(fd, str.substr(0, str.length - delimiter.length) + '\r\n');
}