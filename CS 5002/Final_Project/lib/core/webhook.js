// Helper methods for webhooks

const fs = require('fs-extra');
const App = require('./app');

exports.createHandler = function(name, fn = () => 'handler') {
    return async (req, res, next) => {
        const action = await fn(req, res, next);

        if (typeof action == 'string') {
            const path = `app/webhooks/${name}/${action}.json`;

            if (fs.existsSync(path)) {
                const app = new App(req, res);
                let json = await fs.readJSON(path);
                return Promise.resolve(app.define(json)).catch(next);
            } else {
                res.json({error: `No action found for ${action}.`});
                // do not return 404 else stripe will retry
                //next();
            }
        }
    }
};