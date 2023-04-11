const fs = require('fs-extra');
const { isEmpty } = require('./util');
const config = require('./config');
const debug = require('debug')('server-connect:cron');

exports.start = () => {
    if (!config.cron || isEmpty('app/schedule')) return;

    debug('Start schedule');

    processEntries('app/schedule');
};

function processEntries(path) {
    const schedule = require('node-schedule');
    const entries = fs.readdirSync(path, { withFileTypes: true });

    for (let entry of entries) {
        if (entry.isFile() && entry.name.endsWith('.json')) {
            try {
                const job = fs.readJSONSync(`${path}/${entry.name}`);
                const rule = job.settings.options.rule;

                debug(`Adding schedule ${entry.name}`);

                if (rule == '@reboot') {
                    setImmediate(exec(job.exec));
                } else {
                    schedule.scheduleJob(rule, exec(job.exec))
                }
            } catch (e) {
                console.error(e);
            }
        } else if (entry.isDirectory()) {
            processEntries(`${path}/${entry.name}`);
        }
    }
}

function exec(action) {
    return async () => {
        const App = require('../core/app');
        const app = new App({ params: {}, session: {}, cookies: {}, signedCookies: {}, query: {}, headers: {} });
        return app.define(action, true);
    }
}