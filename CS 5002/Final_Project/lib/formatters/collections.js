module.exports = {

    join: function(arr, separator, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.map(item => prop ? item[prop] : item).join(separator);
    },

    first: function(arr) {
        if (!Array.isArray(arr)) return arr;
        return arr.length ? arr[0] : null;
    },

    top: function(arr, count) {
        if (!Array.isArray(arr)) return arr;
        return arr.slice(0, count);
    },

    last: function(arr, count) {
        if (!Array.isArray(arr)) return arr;
        if (count) return arr.slice(-count);
        return arr[arr.length - 1];
    },

    where: function(arr, prop, operator, value) {
        if (!Array.isArray(arr)) return arr;
        return arr.filter(item => {
            let val = item[prop];

            switch (operator) {
                case 'startsWith': return String(val).startsWith(value);
                case 'endsWith': return String(val).endsWith(value);
                case 'contains': return String(val).includes(value);
                case '===': return val === value;
                case '!==': return val !== value;
                case '==': return val == value;
                case '!=': return val != value;
                case '<=': return val <= value;
                case '>=': return val >= value;
                case '<': return val < value;
                case '>': return val > value;
            };

            return true;
        });
    },

    unique: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        if (prop) arr = arr.map(item => item[prop]);

        let lookup = [];
        return arr.filter(item => {
            if (lookup.includes(item)) return false;
            lookup.push(item);
            return true;
        });
    },

    groupBy: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.reduce((groups, item) => {
            let group = String(item[prop]);
            if (!groups[group]) groups[group] = [];
            groups[group].push(item);
            return groups;
        }, {});
    },

    sort: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.slice(0).sort((a, b) => {
            a = prop ? a && a[prop] : a;
            b = prop ? b && b[prop] : b;

            if (typeof a == 'string' && typeof b == 'string') {
                return a.localeCompare(b);
            }

            return a < b ? -1 : a > b ? 1 : 0;
        });
    },

    randomize: function(arr) {
        if (!Array.isArray(arr)) return arr;
        arr = arr.slice(0);
        let len = arr.length;
        if (len) {
            while (--len) {
                let rnd = Math.floor(Math.random() * (len + 1));
                let val = arr[len];
                arr[len] = arr[rnd];
                arr[rnd] = val;
            }
        }
        return arr;
    },

    reverse: function(arr) {
        if (!Array.isArray(arr)) return arr;
        return arr.slice(0).reverse();
    },

    count: function(arr) {
        if (!Array.isArray(arr)) return arr;
        return arr.length;
    },

    min: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.reduce((min, num) => {
            num = prop ? num[prop] : num;
            if (num == null) return min;
            num = Number(num);
            if (isNaN(num) || !isFinite(num)) return min;
            return min == null || num < min ? num : min;
        }, null);
    },

    max: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.reduce((max, num) => {
            num = prop ? num[prop] : num;
            if (num == null) return max;
            num = Number(num);
            if (isNaN(num) || !isFinite(num)) return max;
            return max == null || num > max ? num : max;
        }, null);
    },

    sum: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.reduce((sum, num) => {
            num = prop ? num[prop] : num;
            if (num == null) return sum;
            num = Number(num);
            if (isNaN(num) || !isFinite(num)) return sum;
            return sum + num;
        }, 0);
    },

    avg: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        let cnt = 0;
        return arr.reduce((avg, num) => {
            num = prop ? num[prop] : num;
            if (num == null) return avg;
            num = Number(num);
            if (isNaN(num) || !isFinite(num)) return avg;
            cnt++;
            return avg + num;
        }, 0) / cnt;
    },

    flatten: function(arr, prop) {
        if (!Array.isArray(arr)) return arr;
        return arr.map(item => item[prop]);
    },

    keys: function(obj) {
        if (typeof obj != 'object') return obj;
        return Object.keys(obj);
    },

    values: function(obj) {
        if (typeof obj != 'object') return obj;
        return Object.values(obj);
    },

};