module.exports = {

    startsWith: function(val, str) {
        if (val == null) return false;
        return String(val).startsWith(str);
    },

    endsWith: function(val, str) {
        if (val == null) return false;
        return String(val).endsWith(str);
    },

    contains: function(val, str) {
        if (val == null) return false;
        return String(val).includes(str);
    },

    between: function(val, min, max) {
        return val >= min && val <= max;
    },

    inRange: function(val, min, max) {
        val = Number(val);
        min = Number(min);
        max = Number(max);

        return val >= min && val <= max;
    },

};