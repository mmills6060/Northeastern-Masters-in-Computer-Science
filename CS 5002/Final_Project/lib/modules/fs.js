const fs = require('fs-extra');
const { join, dirname, basename, extname } = require('path');
const { toSystemPath, toAppPath, toSiteUrl, getUniqFile, parseTemplate } = require('../core/path');
const { map } = require('../core/async');

module.exports = {

    download: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.download: path is required.'));
        let filename = this.parseOptional(options.filename, 'string', basename(path));

        if (fs.existsSync(path)) {
            this.res.download(path, filename);
            this.noOutput = true;
        } else {
            this.res.sendStatus(404);
        }
    },

    exists: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.exists: path is required.'));

        if (await isFile(path)) {
            if (options.then) {
                await this.exec(options.then, true);
            }
            return true;
        } else {
            if (options.else) {
                await this.exec(options.else, true);
            }
            return false;
        }
    },

    direxists: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.direxists: path is required.'));

        if (await isDirectory(path)) {
            if (options.then) {
                await this.exec(options.then, true);
            }
            return true;
        } else {
            if (options.else) {
                await this.exec(options.else, true);
            }
            return false;
        }
    },

    createdir: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.createdir: path is required.'));

        await fs.ensureDir(path);

        return toAppPath(path);
    },

    removedir: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.removedir: path is required.'));

        await fs.remove(path);

        return toAppPath(path);
    },

    emptydir: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.emptydir: path is required.'));

        await fs.emptyDir(path)

        return toAppPath(path);
    },

    move: async function(options) {
        let from = toSystemPath(this.parseRequired(options.from, 'string', 'fs.move: from is required.'));
        let to = toSystemPath(this.parseRequired(options.to, 'string', 'fs.move: to is required.'));
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let createdir = this.parseOptional(options.createdir, 'boolean', true);

        if (!fs.existsSync(to)) {
            if (createdir) {
                await fs.ensureDir(to);
            } else {
                throw new Error(`Destination path doesn't exists.`);
            }
        }

        to = join(to, basename(from));

        if (!overwrite) {
            to = getUniqFile(to);
        }

        await fs.move(from, to, { overwrite: true });

        return toAppPath(to);
    },

    rename: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.rename: path is required.'));
        let template = this.parseRequired(options.template, 'string', 'fs.rename: template is required.');
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let to = parseTemplate(path, template);

        if (!overwrite && fs.existsSync(to)) {
            throw new Error(`fs.rename: file "${to}" already exists.`);
        }

        await fs.rename(path, to);

        return toAppPath(to);
    },

    copy: async function(options) {
        let from = toSystemPath(this.parseRequired(options.from, 'string', 'fs.copy: from is required.'));
        let to = toSystemPath(this.parseRequired(options.to, 'string', 'fs.copy: to is required.'));
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let createdir = this.parseOptional(options.createdir, 'boolean', true);

        if (!fs.existsSync(to)) {
            if (createdir) {
                await fs.ensureDir(to);
            } else {
                throw new Error(`Destination path doesn't exist.`);
            }
        }

        to = join(to, basename(from));

        if (!overwrite && fs.existsSync(to)) {
            to = getUniqFile(to);
        }

        await fs.copy(from, to);

        return toAppPath(to);
    },

    remove: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.remove: path is required.'));

        await fs.unlink(path);

        return true;
    },

    dir: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.dir: path is required.'));
        let allowedExtensions = this.parseOptional(options.allowedExtensions, 'string', '');
        let showHidden = this.parseOptional(options.showHidden, 'boolean', false);
        let includeFolders = this.parseOptional(options.includeFolders, 'boolean', false);
        let folderSize = this.parseOptional(options.folderSize, 'string', 'none');
        let concurrency = this.parseOptional(options.concurrency, 'number', 4);

        folderSize = ['none', 'files', 'recursive'].includes(folderSize) ? folderSize : 'none';
        allowedExtensions = allowedExtensions ? allowedExtensions.split(/\s*,\s*/).map(ext => lowercase(ext[0] == '.' ? ext : '.' + ext)) : [];

        let files = await fs.readdir(path, { withFileTypes: true });

        files = files.filter(entry => {
            if (!includeFolders && entry.isDirectory()) return false;
            if (!showHidden && entry.name[0] == '.') return false;
            if (allowedExtensions.length && entry.isFile() && !allowedExtensions.includes(lowercase(extname(entry.name)))) return false;
            return entry.isFile() || entry.isDirectory();
        });

        // Fast parallel map
        return map(files, async (entry) => {
            let curr = join(path, entry.name);
            let stat = await fs.stat(curr);

            if (folderSize != 'none' && entry.isDirectory()) {
                stat.size = await calcSize(curr, folderSize == 'recursive', concurrency);
            }

            return {
                type: entry.isFile() ? 'file' : 'dir',
                name: entry.name,
                folder: toAppPath(dirname(curr)),
                basename: basename(curr, extname(curr)),
                extension: extname(curr),
                path: toAppPath(curr),
                url: toSiteUrl(curr),
                size: stat.size,
                created: stat.ctime,
                accessed: stat.atime,
                modified: stat.mtime
            };
        }, concurrency);
    },

    stat: async function(options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'fs.stat: path is required.'));
        let folderSize = this.parseOptional(options.folderSize, 'string', 'none');
        let concurrency = this.parseOptional(options.concurrency, 'number', 4);

        folderSize = ['none', 'files', 'recursive'].includes(folderSize) ? folderSize : 'none';

        let stat = await fs.stat(path);

        if (folderSize != 'none' && stat.isDirectory()) {
            stat.size = await calcSize(path, folderSize == 'recursive', concurrency);
        }

        return {
            type: stat.isFile() ? 'file' : 'dir',
            name: basename(path),
            folder: toAppPath(dirname(path)),
            basename: basename(path, extname(path)),
            extension: extname(path),
            path: toAppPath(path),
            url: toSiteUrl(path),
            size: stat.size,
            created: stat.ctime,
            accessed: stat.atime,
            modified: stat.mtime
        };
    },

};

function lowercase(str) {
    return str.toLowerCase();
}

async function calcSize(folder, recursive, concurrency) {
    let entries = await fs.readdir(folder);

    return map(entries, async (entry) => {
        let stat = await fs.stat(join(folder, entry));

        if (stat.isDirectory() && recursive) {
            return calcSize(join(folder, entry), recursive, concurrency);
        }

        return stat.size;
    }, concurrency).then(arr => arr.reduce((size, curr) => size + curr, 0));
};

async function isFile(path) {
    try {
        let stats = await fs.stat(path);
        return stats.isFile();
    } catch (err) {
        return false;
    }
}

async function isDirectory(path) {
    try {
        let stats = await fs.stat(path);
        return stats.isDirectory();
    } catch (err) {
        return false;
    }
}