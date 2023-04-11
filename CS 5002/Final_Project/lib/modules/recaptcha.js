const querystring = require('querystring');
const https = require('https');

exports.validate = function(options) {
    const secret = this.parseRequired(options.secret, 'string', 'recaptcha.validate: secret is required.');
    const msg = this.parseOptional(options.msg, 'string', 'Recaptcha check failed.');

    const response = this.req.body['g-recaptcha-response'];
    const remoteip = this.req.ip;
    const data = querystring.stringify({ secret, response, remoteip });

    return new Promise((resolve, reject) => {
        const req = https.request('https://www.google.com/recaptcha/api/siteverify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': data.length
            }
        }, (res) => {
            let body = '';

            res.setEncoding('utf8');
            res.on('data', (chunk) => body += chunk);
            res.on('end', () => {
                if (res.statusCode >= 400) return reject(body);
                
                if (body.charCodeAt(0) === 0xFEFF) {
                    body = body.slice(1);
                }

                body = JSON.parse(body);

                if (!body.success) {
                    this.res.status(400).json({
                        form: { 'g-recaptcha-response': msg }
                    });
                }

                resolve(body);
            });
        });

        req.on('error', reject);
        req.write(data);
        req.end();
    });
};