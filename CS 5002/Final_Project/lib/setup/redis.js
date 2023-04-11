const config = require('./config');

if (config.redis) {
    const redis = require('redis');
    global.redisClient = redis.createClient(config.redis === true ? 'redis://redis' : config.redis);
}

module.exports = global.redisClient;