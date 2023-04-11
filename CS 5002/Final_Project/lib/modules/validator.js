const validator = require('../validator');

module.exports = {

    validate: function(options) {
        const data = this.parse(options.data);
        const noError = this.parseOptional(options.noError, 'boolean', false);

        return validator.validateData(this, data, noError);
    },

    error: function(options, name) {
        const message = this.parseRequired(options.message, 'string', 'validator.error: message is required.');
        const error = { [options.fieldName ? 'form' : 'data']: {[options.fieldName || name]: message  }};
        this.res.status(400).json(error);
    },

};