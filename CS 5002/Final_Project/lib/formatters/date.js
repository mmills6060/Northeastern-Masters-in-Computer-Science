const { padNumber, parseDate, formatDate } = require('../core/util');

module.exports = {

    formatDate: function(date, format) {
        date = parseDate(date);
        if (date == null) return date;
        
        return formatDate(date, format);
    },

    dateAdd: function(date, interval, num) {
        date = parseDate(date);
        if (date == null) return date;

        switch (interval) {
            case 'years': date.setFullYear(date.getFullYear() + num); break;
            case 'months': date.setMonth(date.getMonth() + num); break;
            case 'weeks': date.setDate(date.getDate() + (num * 7)); break;
            case 'days': date.setDate(date.getDate() + num); break;
            case 'hours': date.setHours(date.getHours() + num); break;
            case 'minutes': date.setMinutes(date.getMinutes() + num); break;
            case 'seconds': date.setSeconds(date.getSeconds() + num); break;
        }

        return date.toISOString();
    },

    dateDiff: function(date, interval, date2) {
        date = parseDate(date);
        date2 = parseDate(date2);

        let diff = Math.abs(date2 - date);

        if (isNaN(diff) || date == null || date2 == null) return undefined;

        let s = 1000, m = s * 60, h = m * 60, d = h * 24, w = d * 7;

        switch (interval) {
            case 'years': return Math.abs(date2.getFullYear() - date.getFullYear());
            case 'months': return Math.abs((date2.getFullYear() * 12 + date2.getMonth()) - (date.getFullYear() * 12 + date.getMonth()));
            case 'weeks': return Math.floor(diff / w);
            case 'days': return Math.floor(diff / d);
            case 'hours': return Math.floor(diff/ h);
            case 'minutes': return Math.floor(diff / m);
            case 'seconds': return Math.floor(diff / s);
            case 'hours:minutes':
                h = Math.floor(diff / h);
                m = Math.floor(diff / m);
                return padNumber(h, 2) + ':' + padNumber(m - (h * 60), 2);
            case 'minutes:seconds':
                m = Math.floor(diff / m);
                s = Math.floor(diff / s);
                return padNumber(m, 2) + ':' + padNumber(s - (m * 60), 2);
            case 'hours:minutes:seconds':
                h = Math.floor(diff / h);
                m = Math.floor(diff / m);
                s = Math.floor(diff / s);
                return padNumber(h, 2) + ':' + padNumber(m - (h * 60), 2) + ':' + padNumber(s - m * 60, 2);
        }

        return undefined;
    },

    toTimestamp: function(date) {
        date = parseDate(date);
        if (date == null) return date;
        return Math.floor(date.getTime() / 1000);
    },

    toLocalTime: function(date) {
        date = parseDate(date);
        if (date == null) return date;
        return formatDate(date, 'yyyy-MM-dd HH:mm:ss.v');
    },

    toUTCTime: function(date) {
        date = parseDate(date);
        if (date == null) return date;
        return date.toISOString();
    },

};