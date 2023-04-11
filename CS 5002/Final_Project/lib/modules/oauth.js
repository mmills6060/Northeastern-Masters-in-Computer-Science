module.exports = {

    provider: async function(options, name) {
        const oauth = await this.setOAuthProvider(name, options)
       
        return {
            access_token: oauth.access_token,
            refresh_token: oauth.refresh_token
        };
    },

    authorize: async function(options) {
        const oauth = await this.getOAuthProvider(options.provider);

        return oauth.authorize(this.parse(options.scopes), this.parse(options.params));
    },

    refresh: async function(options) {
        const oauth = await this.getOAuthProvider(options.provider);

        return oauth.refreshToken(this.parse(options.refresh_token));
    },

};