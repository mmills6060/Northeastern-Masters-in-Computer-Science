module.exports = {

    provider: async function(options, name) {
        const provider = await this.setAuthProvider(name, options);

        return { identity: provider.identity };
    },

    identify: async function(options) {
        const provider = await this.getAuthProvider(this.parseRequired(options.provider, 'string', 'auth.validate: provider is required.'));

        return provider.identity;
    },

    validate: async function(options) {
        const provider = await this.getAuthProvider(this.parseRequired(options.provider, 'string', 'auth.validate: provider is required.'));
        const { action, username, password, remember } = this.req.body;

        if (action == 'login') {
            return provider.login(username, password, remember);
        }

        if (action == 'logout') {
            return provider.logout();
        }

        if (!provider.identity) {
            return provider.unauthorized();
        }
    },

    login: async function(options) {
        const provider = await this.getAuthProvider(this.parseRequired(options.provider, 'string', 'auth.login: provider is required.'));
        const username = this.parseOptional(options.username, 'string', this.parse('{{$_POST.username}}'));
        const password = this.parseOptional(options.password, 'string', this.parse('{{$_POST.password}}'));
        const remember = this.parseOptional(options.remember, '*', this.parse('{{$_POST.remember}}'));

        return provider.login(username, password, remember);
    },

    logout: async function(options) {
        const provider = await this.getAuthProvider(this.parseRequired(options.provider, 'string', 'auth.logout: provider is required.'));

        return provider.logout();
    },

    restrict: async function(options) {
        const provider = await this.getAuthProvider(this.parseRequired(options.provider, 'string', 'auth.restrict: provider is required.'));

        return provider.restrict(this.parse(options));
    },

};