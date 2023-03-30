const fs = require('fs-extra');

exports.isEmpty = (path) => {
    try {
        let stat = fs.statSync(path);
        if (!stat.isDirectory()) return true;
        let items = fs.readdirSync(path);
        return !items || !items.length;
    } catch (e) {
        return true;
    }
}