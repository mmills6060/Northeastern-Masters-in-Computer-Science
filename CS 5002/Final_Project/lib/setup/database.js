// allow Wappler to run queries on the server

const crypto = require('crypto');
const App = require("../core/app");
const config = require('./config');

module.exports = function (app) {
    app.post('/_db_', async (req, res) => {
        const time = req.get('auth-time');
        const hash = req.get('auth-hash');
        if (!time || !hash || isNaN(time)) return res.status(400).json({ error: 'Auth headers missing' });

        const diff = Math.abs(Date.now() - time) / 1000;
        if (diff > 60) return res.status(400).json({ error: 'Auth time diff to high' });
        if (hash !== crypto.createHmac('sha256', config.secret).update(req.rawBody).digest('hex')) return res.status(400).json({ error: 'Auth hash invalid' });

        const sc = new App(req, res);
        const db = sc.getDbConnection(req.body.name);

        let results = [];

        try {
            results = await db.raw(req.body.query);
        } catch (error) {
            return res.json({ error: error.sqlMessage });
        }

        if (db.client.config.client == 'mysql' || db.client.config.client == 'mysql2') {
            results = results[0];
        } else if (db.client.config.client == 'postgres' || db.client.config.client == 'redshift') {
            results = results.rows;
        }

        res.json({ results });
    });
}
