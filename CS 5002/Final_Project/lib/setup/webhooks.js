const fs = require('fs-extra');

module.exports = function(app) {
    app.all('/webhooks/:name', (req, res, next) => {
        if (fs.existsSync(`lib/webhooks/${req.params.name}.js`)) {
            const webhook = require(`../webhooks/${req.params.name}`);
            if (webhook.handler) {
                webhook.handler(req, res, next);
            } else {
                res.json({error: `Webhook ${req.params.name} has no handler.`});
                // do not return error else stripe will retry
                //next(`Webhook ${req.params.name} has no handler.`);
            }
        } else {
            const webhook = require('../core/webhook');
            const handler = webhook.createHandler(req.params.name);
            handler(req, res, next);
        }
    });
};