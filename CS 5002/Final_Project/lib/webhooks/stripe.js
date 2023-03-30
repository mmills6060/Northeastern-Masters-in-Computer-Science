const webhook = require('../core/webhook');
const config = require('../setup/config');
const fs = require('fs-extra')

if (fs.existsSync('app/webhooks/stripe')) {
    const stripe = require('stripe')(config.stripe.secretKey);
    const endpointSecret = config.stripe.endpointSecret;

    exports.handler = webhook.createHandler('stripe', (req, res, next) => {
        const sig = req.headers['stripe-signature'];

        try {
            stripe.webhooks.constructEvent(req.rawBody, sig, endpointSecret);
        } catch (err) {
            res.status(400).send(`Webhook Error: ${err.message}`);
            return false;
        }

        // return the action name to execute
        return req.body.type;
    });
}