const { existsSync: exists } = require('fs');
const { dirname, basename, extname, join, resolve, relative, posix } = require('path');
const { v4: uuidv4 } = require('uuid');
const debug = require('debug')('server-connect:path');

module.exports = {

    getFilesArray: function(paths) {
        let files = [];

        if (!Array.isArray(paths)) {
            paths = [paths];
        }

        for (let path of paths) {
            if (Array.isArray(path)) {
                files = files.concat(module.exports.getFilesArray(path));
            } else if (path && path.path) {
                files.push(module.exports.toSystemPath(path.path));
            } else if (path) {
                files.push(module.exports.toSystemPath(path));
            }
        }

        return files;
    },

    toSystemPath: function(path) {
        if (path[0] != '/' || path.includes('../')) {
            throw new Error(`path.toSystemPath: Invalid path "${path}".`);
        }

        return resolve('.' + path);
    },

    toAppPath: function(path) {
        let root = resolve('.');
        let rel = relative(root, path).replace(/\\/g, '/');

        debug('toAppPath: %O', { root, path, rel });

        if (rel.includes('../')) {
            throw new Error(`path.toAppPath: Invalid path "${rel}".`);
        }

        return '/' + rel;
    },

    toSiteUrl: function(path) {
        let root = resolve('public');
        let rel = relative(root, path).replace(/\\/g, '/');

        debug('toSiteUrl: %O', { root, path, rel });

        if (rel.includes('../')) {
            return '';
        }

        return '/' + rel;
    },

    getUniqFile: function(path) {
        let n = 1;

        while (exists(path)) {
            path = path.replace(/(_(\d+))?(\.\w+)$/, (a, b, c, d) => '_' + (n++) + (d || a));
            if (n > 999) throw new Error(`path.getUniqFile: Couldn't create a unique filename for ${path}`);
        }

        return path;
    },

    parseTemplate: function(path, template) {
        let n = 1, dir = dirname(path), file = template.replace(/\{([^\}]+)\}/g, (a, b) => {
            switch (b) {
                case 'name': return basename(path, extname(path));
                case 'ext' : return extname(path);
                case 'guid': return uuidv4();
            }

            return a;
        });

        if (file.includes('{_n}')) {
            template = file;
            file = template.replace('{_n}', '');

            while (exists(join(dir, file))) {
                file = template.replace('{_n}', n++);
                if (n > 999) throw new Error(`path.parseTemplate: Couldn't create a unique filename for ${path}`);
            }
        }

        return join(dir, file);
    }

};