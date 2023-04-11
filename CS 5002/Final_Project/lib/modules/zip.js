const fs = require('fs-extra');
const debug = require('debug')('server-connect:zip');
const { basename } = require('path');
const { toSystemPath, toAppPath, getFilesArray, getUniqFile } = require('../core/path');
const openZip = (zipfile) => require('unzipper').Open.file(zipfile);

const Zip = function(zipfile, options) {
    this.output = fs.createWriteStream(zipfile);
    this.archive = require('archiver')('zip', options);
    this.archive.on('warning', (err) => {
        if (err.code == 'ENOENT') {
            debug('error: %O', err);
        } else {
            throw err;
        }
    });
    this.archive.on('error', (err) => {
        throw err;
    });
    this.archive.pipe(this.output);
};

Zip.prototype.addFile = function(file) {
    this.archive.file(file, { name: basename(file) });
};

Zip.prototype.addDir = function(dir, recursive) {
    if (recursive) {
        this.archive.directory(dir, false);
    } else {
        this.archive.glob('*', { cwd: dir });
    }
};

Zip.prototype.save = function() {
    return new Promise((resolve, reject) => {
        this.output.on('close', resolve);
        this.archive.on('error', reject);
        this.archive.finalize();
    });
};

module.exports = {

    zip: async function(options) {
        let zipfile = toSystemPath(this.parseRequired(options.zipfile, 'string', 'zip.zip: zipfile is required.'));
        let files = getFilesArray(this.parseRequired(options.files, 'object', 'zip.zip: files is requires.'));
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let comment = this.parseOptional(options.comment, 'string', '');
        
        if (!overwrite) zipfile = getUniqFile(zipfile);

        const zip = new Zip(zipfile, { comment });
        
        for (let file of files) {
            zip.addFile(file);
        }

        await zip.save();

        return toAppPath(zipfile);
    },

    zipdir: async function(options) {
        let zipfile = toSystemPath(this.parseRequired(options.zipfile, 'string', 'zip.zipdir: zipfile is required.'));
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'zip.zipdir: path is required.'));
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let recursive = this.parseOptional(options.recursive, 'boolean', false);
        let comment = this.parseOptional(options.comment, 'string', '');
        
        if (!overwrite) zipfile = getUniqFile(zipfile);

        const zip = new Zip(zipfile, { comment });
        
        zip.addDir(path, recursive);

        await zip.save();

        return toAppPath(zipfile);
    },

    unzip: async function(options) {
        let zipfile = toSystemPath(this.parseRequired(options.zipfile, 'string', 'zip.unzip: zipfile is required.'));
        let dest = toSystemPath(this.parseRequired(options.destination, 'string', 'zip.unzip: destination is required.'));
        let overwrite = this.parseOptional(options.overwrite, 'boolean', true);

        // TODO: overwrite option
        await openZip(zipfile).then(d => d.extract({ path: dest, concurrency: 4 }));

        return true;
    },

    dir: async function(options) {
        let zipfile = toSystemPath(this.parseRequired(options.zipfile, 'string', 'zip.dir: zipfile is required.'));
        
        return openZip(zipfile).then(d => {
            return d.files.map(file => ({
                type: file.type == 'Directory' ? 'dir': 'file',
                path: file.path,
                size: file.uncompressedSize,
                compressedSize: file.compressedSize,
                compressionMethod: file.compressionMethod == 8 ? 'Deflate' : 'None',
                lastModified: file.lastModifiedDateTime
            }));
        });
    },

    comment: async function(options) {
        let zipfile = toSystemPath(this.parseRequired(options.zipfile, 'string', 'zip.comment: zipfile is required.'));
        
        return openZip(zipfile).then(d => d.comment);
    },

};