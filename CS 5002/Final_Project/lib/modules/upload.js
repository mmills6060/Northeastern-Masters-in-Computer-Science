const fs = require('fs-extra');
const debug = require('debug')('server-connect:upload');
const { join, basename } = require('path');
const { toAppPath, toSystemPath, toSiteUrl, parseTemplate, getUniqFile } = require('../core/path');
const diacritics = require('../core/diacritics');

module.exports = {

    upload: async function(options) {
        let fields = this.parse(options.fields || this.parse('{{$_POST}}'));
        let path = this.parseOptional(options.path, 'string', '/uploads');
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let createPath = this.parseOptional(options.createPath, 'boolean', true);
        let throwErrors = this.parseOptional(options.throwErrors, 'boolean', false);
        let template = this.parseOptional(options.template, 'string', '');
        let replaceSpace = this.parseOptional(options.replaceSpace, 'boolean', false);
        let asciiOnly = this.parseOptional(options.asciiOnly, 'boolean', false);
        let replaceDiacritics = this.parseOptional(options.replaceDiacritics, 'boolean', false);

        if (throwErrors) {
            for (let field in this.req.files) {
                if (Array.isArray(this.req.files[field])) {
                    for (let file of this.req.files[field]) {
                        if (file.truncated) {
                            throw new Error('Some files failed to upload.');
                        }
                    }
                } else {
                    let file = this.req.files[field];
                    if (file.truncated) {
                        throw new Error('Some files failed to upload.');
                    }
                }
            }
        }

        path = toSystemPath(path);

        if (!fs.existsSync(path)) {
            if (createPath) {
                await fs.ensureDir(path);
            } else {
                throw new Error(`Upload path doesn't exist.`);
            }
        }

        let files = this.req.files;
        let uploaded = [];
        
        if (files) {
            await processFields(fields);
        }

        return typeof fields == 'string' ? (uploaded.length ? uploaded[0] : null) : uploaded;

        async function processFields(fields) {
            debug('Process fields: %O', fields);
        
            if (typeof fields == 'object') {
                for (let i in fields) {
                    await processFields(fields[i]);
                }
            } else if (typeof fields == 'string' && files[fields]) {
                let processing = files[fields];

                if (!Array.isArray(processing)) processing = [processing];

                for (let file of processing) {
                    debug('Processing file: %O', file);
                    
                    if (!file.processed) {
                        let name = file.name.replace(/[\x00-\x1f\x7f!%&#@$*()?:,;"'<>^`|+={}\[\]\\\/]/g, '');
                
                        if (replaceSpace) name = name.replace(/\s+/g, '_');
                        if (replaceDiacritics) name = diacritics.replace(name);
                        if (asciiOnly) name = name.replace(/[^\x00-\x7e]/g, '');

                        let filepath = join(path, name);

                        if (template) {
                            filepath = parseTemplate(filepath, template);
                        }

                        if (fs.existsSync(filepath)) {
                            if (overwrite) {
                                await fs.unlink(filepath);
                            } else {
                                filepath = getUniqFile(filepath);
                            }
                        }

                        await file.mv(filepath);

                        uploaded.push({
                            name: basename(filepath),
                            path: toAppPath(filepath),
                            url: toSiteUrl(filepath),
                            type: file.mimetype,
                            size: file.size
                        });
                        
                        file.processed = true;
                    }
                }
            }
        
            return uploaded;
        }
        
    }

};