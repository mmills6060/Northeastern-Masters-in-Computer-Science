// IMPROVE: Improve this with the actual file field being checked, for now we check all uploaded files
function getFiles(app, value) {
    const files = [];

    if (app.req.files) {
        for (let field in app.req.files) {
            if (Array.isArray(app.req.files[field])) {
                for (let file of app.req.files[field]) {
                    if (!file.truncated) {
                        files.push(file);
                    }
                }
            } else {
                let file = app.req.files[field];
                if (!file.truncated) {
                    files.push(file);
                }
            }
        }
    }

    return files;
}

module.exports = {

    accept: function(value, param) {
        const files = getFiles(this, value);
        const allowed = param.replace(/\s/g, '').split(',');

        if (!files.length) {
            return true;
        }

        for (let file of files) {
            if (!allowed.some(allow => {
                if (allow[0] == '.') {
                    const re = new RegExp(`\\${allow}$`, 'i');
                    if (re.test(file.name)) {
                        return true;
                    }
                } else if (/(audio|video|image)\/\*/i.test(allow)) {
                    const re = new RegExp(`^${allow.replace('*', '.*')}$`, 'i');
                    if (re.test(file.mimetype)) {
                        return true;
                    }
                } else if (allow.toLowerCase() == file.mimetype.toLowerCase()) {
                    return true;
                }
            })) {
                return false;
            }
        }

        return true;
    },

    minsize: function(value, param) {
        return !getFiles(this, value).some(file => file.size < param);
    },

    maxsize: function(value, param) {
        return !getFiles(this, value).some(file => file.size > param);
    },

    mintotalsize: function(value, param) {
        return getFiles(this, value).reduce((size, file) => size + file.size, 0) >= param;
    },
    
    maxtotalsize: function(value, param) {
        return getFiles(this, value).reduce((size, file) => size + file.size, 0) <= param;
    },

    minfiles: function(value, param) {
        return getFiles(this, value).length >= param;
    },

    maxfiles: function(value, param) {
        return getFiles(this, value).length <= param;
    },

};