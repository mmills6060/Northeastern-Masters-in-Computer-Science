const config = require('./config');
const debug = require('debug')('server-connect:setup:upload');
const fs = require('fs-extra');
const qs = require('qs');

module.exports = function(app) {
    const fileupload = require('express-fileupload');
    const isEligibleRequest = require('express-fileupload/lib/isEligibleRequest');

    // Make sure tmp folder exists and make it empty
    fs.ensureDirSync(config.tmpFolder);
    fs.emptyDirSync(config.tmpFolder);

    // Always use tmp folder
    app.use(fileupload(Object.assign({}, config.fileupload, {
        useTempFiles: true,
        tempFileDir: config.tmpFolder
    })));
    
    app.use((req, res, next) => {
        if (!isEligibleRequest(req)) {
            return next();
        }

        let encoded = qs.stringify(req.body);
        if (req.files) {
            for (let field in req.files) {
                encoded += '&' + field + '=' + field;
            }
        }

        req.body = qs.parse(encoded, {
            arrayLimit: 1000
        });

        // Cleanup
        res.once('close', () => {
            if (req.files) {
                for (let field in req.files) {
                    let file = req.files[field];
                    
                    if (Array.isArray(file)) {
                        file.forEach((file) => {
                            if (file.tempFilePath && fs.existsSync(file.tempFilePath)) {
                                debug('delete %s', file.tempFilePath);
                                fs.unlink(file.tempFilePath);
                            }
                        });
                    } else if (file.tempFilePath && fs.existsSync(file.tempFilePath)) {
                        debug('delete %s', file.tempFilePath);
                        fs.unlink(file.tempFilePath);
                    }
                }
            }
        });

        next();
    });

    debug('Upload middleware configured.');
}