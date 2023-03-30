module.exports = {

    'google': {
        auth_endpoint: 'https://accounts.google.com/o/oauth2/v2/auth',
        token_endpoint: 'https://www.googleapis.com/oauth2/v4/token',
        params: { access_type: 'offline' }
    },

    'facebook': {
        auth_endpoint: 'https://www.facebook.com/v3.2/dialog/oauth',
        token_endpoint: 'https://graph.facebook.com/v3.2/oauth/access_token'
    },

    'linkedin': {
        auth_endpoint: 'https://www.linkedin.com/oauth/v2/authorization',
        token_endpoint: 'https://www.linkedin.com/oauth/v2/accessToken'
    },

    'github': {
        auth_endpoint: 'https://github.com/login/oauth/authorize',
        token_endpoint: 'https://github.com/login/oauth/access_token'
    },

    'instagram': {
        auth_endpoint: 'https://api.instagram.com/oauth/authorize/',
        token_endpoint: 'https://api.instagram.com/oauth/access_token'
    },

    'amazon': {
        auth_endpoint: 'https://www.amazon.com/ap/oa',
        token_endpoint: 'https://api.amazon.com/auth/o2/token'
    },

    'dropbox': {
        auth_endpoint: 'https://www.dropbox.com/oauth2/authorize',
        token_endpoint: 'https://api.dropbox.com/oauth2/token',
        scope_separator: ','
    },

    'foursquare': {
        auth_endpoint: 'https://foursquare.com/oauth2/authenticate',
        token_endpoint: 'https://foursquare.com/oauth2/access_token'
    },

    'imgur': {
        auth_endpoint: 'https://api.imgur.com/oauth2/authorize',
        token_endpoint: 'https://api.imgur.com/oauth2/token'
    },

    'wordpress': {
        auth_endpoint: 'https://public-api.wordpress.com/oauth2/authorize',
        token_endpoint: 'https://public-api.wordpress.com/oauth2/token'
    },

    'spotify': {
        auth_endpoint: 'https://accounts.spotify.com/authorize',
        token_endpoint: 'https://accounts.spotify.com/api/token'
    },

    'slack': {
        auth_endpoint: 'https://slack.com/oauth/authorize',
        token_endpoint: 'https://slack.com/api/oauth.access'
    },

    'reddit': {
        auth_endpoint: 'https://ssl.reddit.com/api/v1/authorize',
        token_endpoint: 'https://ssl.reddit.com/api/v1/access_token',
        scope_separator: ','
    },

    'twitch': {
        auth_endpoint: 'https://api.twitch.tv/kraken/oauth2/authorize',
        token_endpoint: 'https://api.twitch.tv/kraken/oauth2/token'
    },

    'paypal': {
        auth_endpoint: 'https://identity.x.com/xidentity/resources/authorize',
        token_endpoint: 'https://identity.x.com/xidentity/oauthtokenservice'
    },

    'pinterest': {
        auth_endpoint: 'https://api.pinterest.com/oauth/',
        token_endpoint: 'https://api.pinterest.com/v1/oauth/token',
        scope_separator: ','
    },

    'stripe': {
        auth_endpoint: 'https://connect.stripe.com/oauth/authorize',
        token_endpoint: 'https://connect.stripe.com/oauth/token',
        scope_separator: ','
    },

    'coinbase': {
        auth_endpoint: 'https://www.coinbase.com/oauth/authorize',
        token_endpoint: 'https://www.coinbase.com/oauth/token'
    }

};