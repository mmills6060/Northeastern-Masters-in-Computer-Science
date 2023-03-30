/**
 * emits an event to all clients filtered by the given options
 * @param {string} namespace - only to the specified namespace
 * @param {string} room - emit only to the specified room (can be combined with namespace)
 * @param {string} eventName - the name of the event
 * @param {object} params - any parameters/data to send with the event
 */
exports.emit = function(options) {
    if (this.io) {
        options = this.parse(options);

        if (options.namespace) {
            if (options.room) {
                this.io.of(options.namespace).to(options.room).emit(options.eventName, options.params);
            } else {
                this.io.of(options.namespace).emit(options.eventName, options.params);
            }
        } else {
            if (options.room) {
                this.io.in(options.room).emit(options.eventName, options.params);
            } else {
                this.io.emit(options.eventName, options.params);
            }
        }
    }
};

/**
 * emit an event to all clients except the sender
 * @param {string} room - broadcast in a specific room
 * @param {string} eventName - the name of the event
 * @param {object} params - the parameters/data to send with the event
 */
exports.broadcast = function(options) {
    if (this.socket) {
        options = this.parse(options);

        if (options.room) {
            this.socket.to(options.room).emit(options.eventName, options.params);
        } else {
            this.socket.broadcast.emit(options.eventName, options.params);
        }
    }
};

/**
 * emit an event to client and wait for an answer
 * @param {string} room - broadcast in a specific room
 * @param {string} eventName - the name of the event
 * @param {object} params - the parameters/data to send with the event
 */
exports.request = function(options) {
    if (this.socket) {
        options = this.parse(options);

        return new Promise((resolve) => {
            this.socket.emit(options.eventName, options.params, resolve);
        });
    }

    return null;
};

/**
 * send a private meessage to a socket
 * @param {string} socketId - the socket id to send the message to
 * @param {string} eventName - the name of the event
 * @param {object} params - the parameters/data to send with the event
 */
exports.message = function(options) {
    if (this.io) {
        options = this.parse(options);

        this.io.to(options.socketId).emit(options.eventName, options.params);
    }
};

/**
 * special serverconnect refresh broadcast
 * @param {string} action - the action that require refresh
 */
exports.refresh = async function(options) {
    if (this.io) {
        options = this.parse(options);

        // Do we have a global redis client?
        if (global.redisClient) {
            try { // ignore any errors here
                const { promisify } = require('util');
                const redisKeys = promisify(global.redisClient.keys).bind(global.redisClient);
                const redisDel = promisify(global.redisClient.del).bind(global.redisClient);
                let wsKeys = await redisKeys('ws:' + options.action + ':*');
                if (wsKeys.length) await redisDel(wsKeys);
                let scKeys = await redisKeys('erc:' + '/api/' + options.action + '*');
                if (scKeys.length) await redisDel(scKeys);
            } catch (e) {
                console.error(e);
            }
        }

        this.io.of('/api').emit(options.action, options.params);
    }
};

/**
 * let current client join a room
 * @param {string} room - the room to join
 */
exports.join = function(options) {
    if (this.socket) {
        this.socket.join(this.parse(options.room));
    }
};

/**
 * let current client leave a room
 * @param {string} room - the room to leave
 */
exports.leave = function(options) {
    if (this.socket) {
        this.socket.leave(this.parse(options.room));
    }
};

/**
 * get the socket id of the current client
 */
exports.identify = function(options) {
    return this.socket ? this.socket.id : null;
};

/**
 * get the rooms the current client has joined
 */
exports.rooms = function(options) {
    return this.socket ? Array.from(this.socket.rooms) : [];
};

/**
 * get all the rooms
 * @param {string} namespace - the namespace
 */
exports.allRooms = async function(options) {
    if (this.io) {
        let adapter = io.of(options.namespace || '/').adapter;

        if (typeof adapter.allRooms == 'function') {
            return Array.from(await adapter.allRooms());
        } else if (adapter.rooms) {
            return Array.from(adapter.rooms.keys());
        }
    }

    return [];
};

/**
 * get all the connected sockets
 * @param {string} namespace - the namespace
 * @param {string} room - return only clients in a specific room
 */
exports.allSockets = async function(options) {
    if (this.io) {
        options = this.parse(options);

        if (options.room) {
            return Array.from(await this.io.of(options.namespace || '/').in(options.room).allSockets());
        } else {
            return Array.from(await this.io.of(options.namespace || '/').allSockets());
        }
    }

    return [];
};

