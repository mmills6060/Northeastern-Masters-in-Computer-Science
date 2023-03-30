function defered() {
    let resolve, reject;
    let promise = new Promise((_resolve, _reject) => {
        resolve = _resolve;
        reject = _reject;
    });

    return {
        promise,
        resolve,
        reject
    };
}

function limit(concurrency) {
    let running = 0;
    let queue = [];

    function init() {
        if (running < concurrency) {
            running++;
            return Promise.resolve();
        }

        let defer = defered();
        queue.push(defer);
        return defer.promise;
    }

    function complete(a) {
        let next = queue.shift();

        if (next) {
            next.resolve();
        } else {
            running--;
        }

        return a;
    }

    return function(fn) {
        return function() {
            let args = Array.prototype.slice.apply(arguments);

            return init().then(() => {
                return fn.apply(null, args);
            }).finally(complete);
        }
    }
}

module.exports = {

    map: function(arr, fn, concurrency) {
        arr = Array.isArray(arr) ? arr : [arr];

        if (concurrency) {
            const limiter = limit(concurrency)
            return Promise.all(arr.map(limiter(fn)));
        }

        return Promise.all(arr.map(fn));
    },

    mapSeries: function(arr, fn) {
        arr = Array.isArray(arr) ? arr : [arr];

        return arr.reduce((promise, curr, index, arr) => {
            return promise.then(prev => {
                return fn(curr, index, arr).then(val => {
                    prev.push(val);
                    return prev;
                });
            })
        }, Promise.resolve([]));
    },

    reduce: function(arr, fn, start) {
        arr = Array.isArray(arr) ? arr : [arr];

        if (!arr.length) {
            return Promise.resolve(start);
        }

        return arr.reduce((promise, curr, index, arr) => {
            return promise.then(prev => {
                if (prev === undefined && arr.length === 1) {
                    return curr;
                }

                return fn(prev, curr, index, arr);
            });
        }, Promise.resolve(start));
    },

};