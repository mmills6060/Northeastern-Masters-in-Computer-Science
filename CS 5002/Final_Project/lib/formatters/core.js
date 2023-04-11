module.exports = {

    default: function(val, def) {
        return val ? val : def;
    },

    then: function(val, trueVal, falseVal) {
        return val ? trueVal : falseVal;
    },

    toNumber: function(val) {
        return Number(val);
    },

    toString: function(val) {
        return String(val);
    },

    toJSON: function(val) {
        return JSON.stringify(val);
    },

    parseJSON: function(val) {
        return JSON.parse(val);
    },

};