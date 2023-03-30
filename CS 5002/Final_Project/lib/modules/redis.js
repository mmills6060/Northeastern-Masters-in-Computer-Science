const client = global.redisClient;

if (client) {
    const { promisify } = require('util');
    const commands = {};

    [
        'append', 'decr', 'decrby', 'del', 'exists', 'get', 'getset', 'incr', 'incrby',
        'mget', 'set', 'setex', 'setnx', 'strlen', 'lindex', 'linsert', 'llen', 'lpop',
        'lpos', 'lpush', 'lpushx', 'lrange', 'lrem', 'lset', 'ltrim', 'rpop', 'rpush',
        'rpushx', 'copy', 'del', 'expire', 'expireat', 'keys', 'persist', 'pexpire',
        'pexpireat', 'pttl', 'randomkey', 'rename', 'renamenx', 'touch', 'ttl', 'type',
        'unlink'
    ].forEach(command => {
        commands[command] = promisify(client[command]).bind(client);
    });

    exports.append = function(options) {
        options = this.parse(options);
        return commands.append(options.key, options.value);
    };

    exports.decr = function(options) {
        options = this.parse(options);
        return commands.decr(options.key);
    };

    exports.decrby = function(options) {
        options = this.parse(options);
        return commands.decrby(options.key, options.decrement);
    };

    exports.del = function(options) {
        options = this.parse(options);
        return commands.del(options.key);
    };

    exports.exists = function(options) {
        options = this.parse(options);
        return commands.exists(options.key);
    };

    exports.get = function(options) {
        options = this.parse(options);
        return commands.get(options.key);
    };

    exports.getset = function(options) {
        options = this.parse(options);
        return commands.getset(options.key, options.value);
    };

    exports.incr = function(options) {
        options = this.parse(options);
        return commands.incr(options.key);
    };

    exports.incrby = function(options) {
        options = this.parse(options);
        return commands.incrby(options.key, options.increment);
    };

    exports.mget = function(options) {
        options = this.parse(options);
        return commands.mget(options.keys);
    };

    exports.set = function(options) {
        options = this.parse(options);
        return commands.set(options.key, options.value);
    };

    exports.setex = function(options) {
        options = this.parse(options);
        return commands.setex(options.key, options.seconds, options.value);
    };

    exports.setnx = function(options) {
        options = this.parse(options);
        return commands.setnx(options.key, options.value);
    };

    exports.strlen = function(options) {
        options = this.parse(options);
        return commands.strlen(options.key);
    };

    exports.lindex = function(options) {
        options = this.parse(options);
        return commands.lindex(options.key, options.index);
    };

    exports.linsert = function(options) {
        options = this.parse(options); // position: BEFORE|AFTER
        return commands.linsert(options.key, options.position, options.pivot, options.element);
    };

    exports.llen = function(options) {
        options = this.parse(options);
        return commands.llen(options.key);
    };

    exports.lpop = function(options) {
        options = this.parse(options);
        return commands.lpop(options.key, options.count);
    };

    exports.lpos = function(options) {
        options = this.parse(options);
        return commands.lpos(options.key, options.element);
    };

    exports.lpush = function(options) {
        options = this.parse(options);
        return commands.lpush(options.key, options.element);
    };

    exports.lpushx = function(options) {
        options = this.parse(options);
        return commands.lpushx(options.key, options.element);
    };

    exports.lrange = function(options) {
        options = this.parse(options);
        return commands.lrange(options.key, options.start, options.stop);
    };

    exports.lrem = function(options) {
        options = this.parse(options);
        return commands.lrem(options.key, options.count, options.element);
    };

    exports.lset = function(options) {
        options = this.parse(options);
        return commands.lset(options.key, options.index, options.element);
    };

    exports.ltrim = function(options) {
        options = this.parse(options);
        return commands.ltrim(options.key, options.start, options.stop);
    };

    exports.rpop = function(options) {
        options = this.parse(options);
        return commands.rpop(options.key, options.count);
    };

    exports.rpush = function(options) {
        options = this.parse(options);
        return commands.rpush(options.key, options.element);
    };

    exports.rpushx = function(options) {
        options = this.parse(options);
        return commands.rpushx(options.key, options.element);
    };

    exports.copy = function(options) {
        options = this.parse(options);
        return commands.copy(options.source, options.destination);
    };

    exports.del = function(options) {
        options = this.parse(options);
        return commands.del(options.key);
    };

    exports.expire = function(options) {
        options = this.parse(options);
        return commands.expire(options.key, options.seconds);
    };

    exports.expireat = function(options) {
        options = this.parse(options);
        return commands.expireat(options.key, options.timestamp);
    };

    exports.keys = function(options) {
        options = this.parse(options);
        return commands.keys(options.pattern);
    };

    exports.persist = function(options) {
        options = this.parse(options);
        return commands.persist(options.key);
    };

    exports.pexpire = function(options) {
        options = this.parse(options);
        return commands.pexpire(options.key, options.milliseconds);
    };

    exports.pexpireat = function(options) {
        options = this.parse(options);
        return commands.pexpireat(options.key, options.mstimestamp)
    };

    exports.pttl = function(options) {
        options = this.parse(options);
        return commands.pttl(options.key);
    };

    exports.randomkey = function(options) {
        options = this.parse(options);
        return commands.randomkey();
    };

    exports.rename = function(options) {
        options = this.parse(options);
        return commands.rename(options.key, options.newkey);
    };

    exports.renamenx = function(options) {
        options = this.parse(options);
        return commands.renamenx(options.key, options.newkey);
    };

    exports.touch = function(options) {
        options = this.parse(options);
        return commands.touch(options.key);
    };

    exports.ttl = function(options) {
        options = this.parse(options);
        return commands.ttl(options.key);
    };

    exports.type = function(options) {
        options = this.parse(options);
        return commands.type(options.key);
    };

    exports.unlink = function(options) {
        options = this.parse(options);
        return commands.unlink(options.key);
    };
}