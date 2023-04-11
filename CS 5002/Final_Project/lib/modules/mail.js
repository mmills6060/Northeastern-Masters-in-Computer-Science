const fs = require('fs-extra');
const { getFilesArray, toSystemPath } = require('../core/path');
const { basename, posix } = require('path');
const { v4: uuidv4 } = require('uuid');
const IMPORTANCE = { 0: 'low', 1: 'normal', 2: 'high' };

module.exports = {

    setup: function(options, name) {
        if (!name) throw new Error('mail.setup has no name.');
        this.setMailer(name, options);
    },

    send: async function(options) {
        let setup = this.getMailer(this.parseOptional(options.instance, 'string', 'system'));
        let subject = this.parseRequired(options.subject, 'string', 'mail.send: subject is required.');
        let fromEmail = this.parseRequired(options.fromEmail, 'string', 'mail.send: fromEmail is required.');
        let fromName = this.parseOptional(options.fromName, 'string', '');
        let toEmail = this.parseRequired(options.toEmail, 'string', 'mail.send: toEmail is required.');
        let toName = this.parseOptional(options.toName, 'string', '');
        let replyTo = this.parseOptional(options.replyTo, 'string', '');
        let cc = this.parseOptional(options.cc, 'string', '');
        let bcc = this.parseOptional(options.bcc, 'string', '');
        let source = this.parseOptional(options.source, 'string', 'static'); // static, file
        let contentType = this.parseOptional(options.contentType, 'string', 'text'); // text / html
        let body = this.parseOptional(options.body, 'string', '');
        let bodyFile = this.parseOptional(options.bodyFile, 'string', '');
        let embedImages = this.parseOptional(options.embedImages, 'boolean', false);
        let priority = IMPORTANCE[this.parseOptional(options.importance, 'number', 1)];
        let attachments = this.parseOptional(options.attachments, '*', []); // "/file.ext" / ["/file.ext"] / {path:"/file.ext"} / [{path:"/file.ext"}]

        let from = fromName ? `"${fromName}" <${fromEmail}>` : fromEmail;
        let to = toName ? `"${toName}" <${toEmail}>` : toEmail;
        let text = body;
        let html = null;

        if (source == 'file') {
            body = this.parse(await fs.readFile(toSystemPath(bodyFile), 'utf8'));
        }

        if (attachments) {
            attachments = getFilesArray(attachments).map((path) => ({ filename: basename(path), path }));
        }

        if (contentType == 'html') {
            html = body;

            if (embedImages) {
                let cid = {};

                html = html.replace(/(?:"|')([^"']+\.(jpg|png|gif))(?:"|')/gi, (m, url) => {
                    let path = toSystemPath(url);

                    if (fs.existsSync(path)) {
                        if (!cid[path]) {
                            cid[path] = uuidv4();
                            attachments.push({
                                filename: basename(path),
                                path: path,
                                cid: cid[path]
                            });
                        }

                        return `"cid:${cid[path]}"`;
                    } else {
                        console.warn(`${path} not found`);
                    }

                    return `"${url}"`;
                });
            }

            if (this.req.get) { // we can only do this if we have a request to get our hostname
                const hasProxy = !!this.req.get('x-forwarded-host');
                const host = hasProxy ? `${this.req.protocol}://${this.req.hostname}` : this.req.get('host');

                html = html.replace(/(href|src)(?:\s*=\s*)(?:"|')([^"']+)(?:"|')/gi, (m, attr, url) => {
                    if (!url.includes(':')) {
                        url = posix.join(host, url);
                    }

                    return `${attr}="${url}"`;
                });
            }
        }

        const nodemailer = require('nodemailer');
        let transport = nodemailer.createTransport(setup);
        return transport.sendMail({ from, to, cc, bcc, replyTo, subject, html, text, priority, attachments });
    },

};