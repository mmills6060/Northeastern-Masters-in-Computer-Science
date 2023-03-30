function Scope(data, parent, context) {
    if (typeof data != 'object') {
        data = { $value: data };
    }

    this.data = data;
    this.parent = parent;
    this.context = context;
};

Scope.prototype = {
    create: function(data, context) {
        return new Scope(data, this, context);
    },

    get: function(name) {
        if (this.data[name] !== undefined) {
            return this.data[name];
        }

        if (this.parent) {
            return this.parent.get(name);
        }

        return undefined;
    },

    set: function(name, value) {
        if (typeof name == 'object') {
            for (let prop in name) {
                this.set(prop, name[prop]);
            }
        } else {
            this.data[name] = value;

            if (this.context) {
                this.context[name] = value;
            }
        }
    },

    has: function(name) {
        if (this.data[name] !== undefined) {
            return true;
        }

        if (this.parent) {
            return this.parent.has(name);
        }

        return false;
    },

    remove: function(name) {
        delete this.data[name];

        if (this.context) {
            delete this.context[name];
        }
    },
}

module.exports = Scope;