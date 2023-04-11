const { http, https } = require('follow-redirects');
const querystring = require('querystring');
const services = require('./services');
const crypto = require('crypto');

class OAuth2 {

    constructor(app, opts, name) {
        this.app = app;
        this.name = name;
        this.opts = opts;

        if (opts.service) {
            Object.assign(this.opts, services[opts.service]);
        }

        this.access_token = opts.access_token || app.getSession(`${name}_access_token`);
        this.refresh_token = opts.refresh_token || app.getSession(`${name}_refresh_token`);

        if (this.access_token) {
            let expires = app.getSession(`${name}_expires`);

            if (expires && expires < expires_in(-10)) {
                this.access_token = null;

                app.removeSession(`${name}_access_token`);
                app.removeSession(`${name}_expires`);

                if (this.refresh_token) {
                    this.refreshToken(this.refresh_token);
                }
            }
        }
    }

    async init() {
        if (this.opts.jwt_bearer && !this.access_token) {
            const assertion = this.app.getJSONWebToken(this.opts.jwt_bearer);
            let response = await this.grant('urn:ietf:params:oauth:grant-type:jwt-bearer', { assertion });
            this.access_token = response.access_token;
        }

        if (this.opts.client_credentials && !this.access_token) {
            let response = await this.grant('client_credentials');
            this.access_token = response.access_token;
        }
    }

    async authorize(scopes = [], params = {}) {
        let query = this.app.req.query;

        if (query.state && query.state == this.app.getSession(`${this.name}_state`)) {
            this.app.removeSession(`${this.name}_state`);

            if (query.error) {
                throw new Error(query.error_message || query.error);
            }

            if (query.code) {
                let params = {
                    redirect_uri: redirect_uri(this.app.req),
                    code: query.code
                };

                if (this.app.getSession(`${this.name}_code_verifier`)) {
                    params.code_verifier = this.app.getSession(`${this.name}_code_verifier`);
                }

                return this.grant('authorization_code', params);
            }
        }

        if (this.opts.pkce || params.code_verifier) {
            const code_verifier = params.code_verifier || crypto.randomBytes(40).toString('hex');
            this.app.setSession(`${this.name}_code_verifier`, code_verifier);
            params.code_challenge_method = 'S256';
            params.code_challenge = crypto.createHash('sha256').update(code_verifier).digest('base64').replace(/=/g, '').replace(/\+/g, '-').replace(/\//g, '_');
        }

        params = Object.assign({}, {
            response_type: 'code',
            client_id: this.opts.client_id,
            scope: scopes.join(this.opts.scope_separator),
            redirect_uri: redirect_uri(this.app.req),
            state: generate_state()
        }, this.opts.params, params);

        this.app.setSession(`${this.name}_state`, params.state);

        this.app.res.redirect(build_url(this.opts.auth_endpoint, params));
    }

    async refreshToken(refresh_token) {
        return this.grant('refresh_token', { refresh_token });
    }

    async grant(type, params) {
        const endpoint = new URL(this.opts.token_endpoint);

        return new Promise((resolve, reject) => {
            const req = (endpoint.protocol == 'https:' ? https : http).request(endpoint, {
                method: 'POST'
            }, res => {
                let body = '';
                res.setEncoding('utf8');
                res.on('data', chunk => body += chunk);
                res.on('end', () => {
                    if (res.statusCode >= 400) {
                        return reject(new Error(`Http status code ${res.statusCode}. ${body}`));
                    }

                    try {
                        body = JSON.parse(body);
                    } catch (e) { }

                    if (!body.access_token) {
                        return reject(new Error(`Http response has no access_token. ${JSON.stringify(body)}`))
                    }

                    this.app.setSession(`${this.name}_access_token`, body.access_token);
                    this.access_token = body.access_token;

                    if (body.expires_in) {
                        this.app.setSession(`${this.name}_expires`, expires_in(body.expires_in));
                    }

                    if (body.refresh_token) {
                        this.app.setSession(`${this.name}_refresh_token`, body.refresh_token);
                        this.refresh_token = body.refresh_token;
                    }

                    resolve(body);
                });
            });

            const body = querystring.stringify(Object.assign({
                grant_type: type,
                client_id: this.opts.client_id,
                client_secret: this.opts.client_secret
            }, params));

            req.on('error', reject);
            req.setHeader('Content-Type', 'application/x-www-form-urlencoded');
            req.setHeader('Content-Length', body.length); // required by azure endpoint
            req.write(body);
            req.end();
        });
    }

}

function build_url(url, params) {
    return url + (url.indexOf('?') != -1 ? '&' : '?') + querystring.stringify(params);
}

function redirect_uri(req) {
    let hasProxy = !!req.get('x-forwarded-host');
    return `${req.protocol}://${hasProxy ? req.hostname : req.get('host')}${req.path}`;
}

function expires_in(s) {
    return ~~(Date.now() / 1000) + s;
}

function generate_state() {
    const { v4: uuidv4 } = require('uuid');
    return uuidv4();
}

module.exports = OAuth2;