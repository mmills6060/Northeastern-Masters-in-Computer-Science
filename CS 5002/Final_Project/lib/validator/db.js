module.exports = {

    exists: async function(value, options) {
        if (!value) return true;

        const db = this.getDbConnection(options.connection);
        const results = await db.from(options.table).where(options.column, value).limit(1);

        return results.length > 0;
    },

    notexists: async function(value, options) {
        if (!value) return true;

        const db = this.getDbConnection(options.connection);
        const results = await db.from(options.table).where(options.column, value).limit(1);

        return results.length == 0;
    }

};