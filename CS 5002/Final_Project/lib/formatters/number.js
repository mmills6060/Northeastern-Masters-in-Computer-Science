const { padNumber, formatNumber } = require('../core/util');

module.exports = {

    floor: function(num) {
        return Math.floor(Number(num));
    },

    ceil: function(num) {
        return Math.ceil(Number(num));
    },

    round: function(num) {
        return Math.round(Number(num));
    },

    abs: function(num) {
        return Math.abs(Number(num));
    },

    pow: function(num, exp) {
        return Math.pow(num, exp);
    },

    padNumber: function(num, digids) {
        num = Number(num);
        
        if (isNaN(num) || !isFinite(num)) return 'NaN';
        
        return padNumber(num, digids);
    },

    formatNumber: function(num, decimals, decimalSeparator, groupingSeparator) {
        return formatNumber(num, decimals, decimalSeparator, groupingSeparator);
    },

    hex: function(num) {
        return parseInt(String(num), 16) || NaN;
    },

    currency: function(num, unit, decimalSeparator, groupingSeparator, decimals) {
        unit = typeof unit == 'string' ? unit : '$';
        decimalSeparator = typeof decimalSeparator == 'string' ? decimalSeparator : '.';
        groupingSeparator = typeof groupingSeparator == 'string' ? groupingSeparator : ',';
        decimals = typeof decimals == 'number' ? Math.abs(decimals) : 2;
        
        let formatted = formatNumber(num, decimals, decimalSeparator, groupingSeparator);
        let minus = formatted[0] == '-';

        return (minus ? '-' : '') + unit + formatted.replace(/^\-/, '');
    },

    formatSize: function(num, decimals, binary) {
        num = Number(num);

        if (isNaN(num) || !isFinite(num)) return 'NaN';

        decimals = typeof decimals == 'number' ? Math.abs(decimals) : 2;
        
        let base = binary ? 1024 : 1000;
        let suffix = binary ? ['KiB', 'MiB', 'GiB', 'TiB'] : ['kB', 'MB', 'GB', 'TB'];

        for (let i = 3; i >= 0; i--) {
            let n = Math.pow(base, i + 1);
            if (num >= n) {
                return formatNumber(num / n, decimals) + suffix[i];
            }
        }

        return num + 'B';
    },

};