const fs = require('fs-extra');
const path = require('path');
const { randomUUID } = require('crypto');
const { v4: uuidv4 } = require('uuid');

const NOOP = function() {};

const OPERATORS = {
    '{'  : 'L_CURLY',
    '}'  : 'R_CURLY',
    '('  : 'L_PAREN',
    ')'  : 'R_PAREN',
    '['  : 'L_BRACKET',
    ']'  : 'R_BRACKET',
    '.'  : 'PERIOD',
    ','  : 'COMMA',
    ':'  : 'COLON',
    '?'  : 'QUESTION',
    // Arithmetic operators
    '+'  : 'ADDICTIVE',
    '-'  : 'ADDICTIVE',
    '*'  : 'MULTIPLICATIVE',
    '/'  : 'MULTIPLICATIVE',
    '%'  : 'MULTIPLICATIVE',
    // Comparison operators
    '===': 'EQUALITY',
    '!==': 'EQUALITY',
    '==' : 'EQUALITY',
    '!=' : 'EQUALITY',
    '<'  : 'RELATIONAL',
    '>'  : 'RELATIONAL',
    '<=' : 'RELATIONAL',
    '>=' : 'RELATIONAL',
    'in' : 'RELATIONAL',
    // Logical operators
    '&&' : 'LOGICAL_AND',
    '||' : 'LOGICAL_OR',
    '!'  : 'LOGICAL_NOT',
    // Bitwise operators
    '&'  : 'BITWISE_AND',
    '|'  : 'BITWISE_OR',
    '^'  : 'BITWISE_XOR',
    '~'  : 'BITWISE_NOT',
    '<<' : 'BITWISE_SHIFT',
    '>>' : 'BITWISE_SHIFT',
    '>>>': 'BITWISE_SHIFT'
};

const EXPRESSIONS = {
    'in' : function(a, b)    { return a() in b(); },
    '?'  : function(a, b, c) { return a() ? b() : c(); },
    '+'  : function(a, b)    { a = a(); b = b(); return a == null ? b : b == null ? a : a + b; },
    '-'  : function(a, b)    { return a() - b(); },
    '*'  : function(a, b)    { return a() * b(); },
    '/'  : function(a, b)    { return a() / b(); },
    '%'  : function(a, b)    { return a() % b(); },
    '===': function(a, b)    { return a() === b(); },
    '!==': function(a, b)    { return a() !== b(); },
    '==' : function(a, b)    { return a() == b(); },
    '!=' : function(a, b)    { return a() != b(); },
    '<'  : function(a, b)    { return a() < b(); },
    '>'  : function(a, b)    { return a() > b(); },
    '<=' : function(a, b)    { return a() <= b(); },
    '>=' : function(a, b)    { return a() >= b(); },
    '&&' : function(a, b)    { return a() && b(); },
    '||' : function(a, b)    { return a() || b(); },
    '&'  : function(a, b)    { return a() & b(); },
    '|'  : function(a, b)    { return a() | b(); },
    '^'  : function(a, b)    { return a() ^ b(); },
    '<<' : function(a, b)    { return a() << b(); },
    '>>' : function(a, b)    { return a() >> b(); },
    '>>>': function(a, b)    { return a() >>> b(); },
    '~'  : function(a)       { return ~a(); },
    '!'  : function(a)       { return !a(); }
};

const ESCAPE = {
    'n': '\n',
    'f': '\f',
    'r': '\r',
    't': '\t',
    'v': '\v',
    "'": "'",
    '"': '"',
    '`': '`'
};

const formatters = require('../formatters');

// User formatters
if (fs.existsSync('extensions/server_connect/formatters')) {
    const files = fs.readdirSync('extensions/server_connect/formatters');
    for (let file of files) {
        if (path.extname(file) == '.js') {
            Object.assign(formatters, require(`../../extensions/server_connect/formatters/${file}`));
        }
    }
}

function lexer(expr) {
    let tokens = [],
        token,
        name,
        start,
        index = 0,
        op = true,
        ch,
        ch2,
        ch3;
    
    while (index < expr.length) {
        start = index;

        ch = read();

        if (isQuote(ch) && op) {
            name = 'STRING';
            token = readString(ch);
            op = false;
        } else if ((isDigid(ch) || (is('.') && peek() && isDigid(peek()))) && op) {
            name = 'NUMBER';
            token = readNumber();
            op = false;
        } else if (isAlpha(ch) && op) {
            name = 'IDENT';
            token = readIdent();
            if (is('(')) {
                name = 'METHOD';
            }
            op = false;
        } else if (is('/') && op && (token == '(' || token == ',' || token == '?' || token == ':') && testRegexp()) {
            name = 'REGEXP';
            token = readRegexp();
            op = false;
        } else if (isWhitespace(ch)) {
            index++;
            continue;
        } else if ((ch3 = read(3)) && OPERATORS[ch3]) {
            name = OPERATORS[ch3];
            token = ch3;
            op = true;
            index += 3;
        } else if ((ch2 = read(2)) && OPERATORS[ch2]) {
            name = OPERATORS[ch2];
            token = ch2;
            op = true;
            index += 2;
        } else if (OPERATORS[ch]) {
            name = OPERATORS[ch];
            token = ch;
            op = true;
            index++;
        } else {
            throw new Error('Lexer Error: Unexpected token "' + ch + '" at column ' + index + ' in expression {{' + expr + '}}');
        }

        tokens.push({
            name: name,
            index: start,
            value: token
        });
    }

    return tokens;

    function read(n) {
        if (!n) n = 1;
        return expr.substr(index, n);
    }

    function peek(n) {
        n = n || 1;
        return index + n < expr.length ? expr[index + n] : false;
    }

    function is(chars) {
        return chars.indexOf(ch) != -1;
    }

    function isQuote(ch) {
        return ch == '"' || ch == "'";
    }

    function isDigid(ch) {
        return ch >= '0' && ch <= '9';
    }

    function isAlpha(ch) {
        return (ch >= 'a' && ch <= 'z') ||
               (ch >= 'A' && ch <= 'Z') ||
                ch == '_' || ch == '$';
    }

    function isAlphaNum(ch) {
        return isAlpha(ch) || isDigid(ch);
    }

    function isWhitespace(ch) {
        return ch == ' ' || ch == '\r' || ch == '\t' || ch == '\n' || ch == '\v' || ch == '\u00A0';
    }

    function isExpOperator(ch) {
        return ch == '-' || ch == '+' || isDigid(ch);
    }

    function readString(quote) {
        let str = '', esc = false;

        index++;
        
        while (index < expr.length) {
            ch = read();

            if (esc) {
                if (ch == 'u') {
                    // unicode escape
                    index++;
                    let hex = read(4);
                    if (!hex.match(/[\da-f]{4}/i)) {
                        throw new Error('Lexer Error: Invalid unicode escape at column ' + index + ' in expression {{' + expr + '}}');
                    }
                    str += String.fromCharCode(parseInt(hex, 16));
                    index += 3;
                } else {
                    str += ESCAPE[ch] ? ESCAPE[ch] : ch;
                }

                esc = false;
            } else if (ch == '\\') {
                // escape character
                esc = true;
            } else if (ch == quote) {
                // end of string
                index ++;
                return str;
            } else {
                str += ch;
            }

            index++;
        }

        throw new Error('Lexer Error: Unterminated string at column ' + index + ' in expression {{' + expr + '}}');
    }

    function readNumber() {
        let num = '', exp = false;

        while (index < expr.length) {
            ch = read();

            if (isDigid(ch) || (is('.') && peek() && isDigid(peek()))) {
                num += ch;
            } else {
                let next = peek();

                if (is('eE') && isExpOperator(next)) {
                    num += 'e';
                    exp = true;
                } else if (isExpOperator(ch) && next && isDigid(next) && exp) {
                    num += ch;
                    exp = false;
                } else if (isExpOperator(ch) && (!next || !isDigid(next)) && exp) {
                    throw new Error('Lexer Error: Invalid exponent at column ' + index + ' in expression {{' + expr + '}}');
                } else {
                    break;
                }
            }

            index++;
        }

        return +num;
    }

    function readIdent() {
        let ident = '';

        while (index < expr.length) {
            ch = read();

            if (isAlphaNum(ch)) {
                ident += ch;
            } else {
                break;
            }

            index++;
        }

        return ident;
    }

    function readRegexp() {
        let re = '', mod = '', esc = false;

        index ++;

        while (index < expr.length) {
            ch = read();

            if (esc) {
                esc = false;
            } else if (ch == '\\') {
                esc = true;
            } else if (ch == '/') {
                index++;

                while ('ign'.indexOf(ch = read()) != -1) {
                    mod += ch;
                    index++;
                }

                return re + '%%%' + mod;
            }

            re += ch;
            index++;
        }

        throw new Error('Lexer Error: Unterminated regexp at column ' + index + ' in expression {{' + expr + '}}');
    }

    function testRegexp() {
        var idx = index, ok = true;

        try {
            readRegexp();
        } catch (e) {
            ok = false;
        }

        // reset our index and ch
        index = idx;
        ch = '/';

        return ok;
    }
}

function parser(expr, scope) {
    let tokens = lexer(expr),
        context = undefined,
        RESERVED = {
            'PI'       : function() { return Math.PI; },
            'UUID'     : function() { return randomUUID ? randomUUID() : uuidv4(); },
            'NOW'      : function() { return date(); },
            'NOW_UTC'  : function() { return utc_date(); },
            'TIMESTAMP': function() { return timestamp(); },
            '$this'    : function() { return scope.data; },
            '$global'  : function() { return globalScope.data; },
            '$parent'  : function() { return scope.parent && scope.parent.data; },
            'null'     : function() { return null; },
            'true'     : function() { return true; },
            'false'    : function() { return false; },
            '_'        : function() { return { __dmxScope__: true } }
        };

    return start()();

    function pad(s, n) {
        return ('000' + s).substr(-n);
    }

    function date(dt) {
        dt = dt || new Date();
        return pad(dt.getFullYear(), 4) + '-' + pad(dt.getMonth() + 1, 2) + '-' + pad(dt.getDate(), 2) + ' ' +
               pad(dt.getHours(), 2) + ':' + pad(dt.getMinutes(), 2) + ':' + pad(dt.getSeconds(), 2);
    }

    function utc_date(dt) {
        dt = dt || new Date();
        return pad(dt.getUTCFullYear(), 4) + '-' + pad(dt.getUTCMonth() + 1, 2) + '-' + pad(dt.getUTCDate(), 2) + 'T' +
               pad(dt.getUTCHours(), 2) + ':' + pad(dt.getUTCMinutes(), 2) + ':' + pad(dt.getUTCSeconds(), 2) + 'Z';
    }

    function timestamp(dt) {
        dt = dt || new Date();
        return ~~(dt / 1000);
    }

    function read() {
        if (tokens.length === 0) {
            throw new Error('Parser Error: Unexpected end of expression {{' + expr + '}}');
        }

        return tokens[0];
    }

    function peek(e) {
        if (tokens.length > 0) {
            let token = tokens[0];

            if (!e || token.name == e) {
                return token;
            }
        }

        return false;
    }

    function expect(e) {
        let token = peek(e);

        if (token) {
            tokens.shift();
            return token;
        }

        return false;
    }

    function consume(e) {
        if (!expect(e)) {
            throw new Error('Parser Error: Unexpected token, expecting ' + e + ' in expression {{' + expr + '}}');
        }
    }

    function fn(expr) {
        let args = [].slice.call(arguments, 1);

        return function() {
            if (EXPRESSIONS[expr]) {
                return EXPRESSIONS[expr].apply(context, args);
            } else {
                return expr;
            }
        }
    }

    function start() {
        return conditional();
    }

    function conditional() {
        let left = logicalOr(), middle, token;

        if ((token = expect('QUESTION'))) {
            middle = conditional();

            if ((token = expect('COLON'))) {
                return fn('?', left, middle, conditional());
            } else {
                throw new Error('Parse Error: Expecting : in expression {{' + expr + '}}');
            }
        } else {
            return left;
        }
    }

    function logicalOr() {
        let left = logicalAnd(), token;

        while (true) {
            if ((token = expect('LOGICAL_OR'))) {
                left = fn(token.value, left, logicalAnd());
            } else {
                return left;
            }
        }
    }

    function logicalAnd() {
        let left = bitwiseOr(), token;

        if ((token = expect('LOGICAL_AND'))) {
            left = fn(token.value, left, logicalAnd());
        }

        return left;
    }

    function bitwiseOr() {
        let left = bitwiseXor(), token;

        if ((token = expect('BITWISE_OR'))) {
            left = fn(token.value, left, bitwiseXor());
        }

        return left;
    }

    function bitwiseXor() {
        let left = bitwiseAnd(), token;

        if ((token = expect('BITWISE_XOR'))) {
            left = fn(token.value, left, bitwiseAnd());
        }

        return left;
    }

    function bitwiseAnd() {
        let left = equality(), token;

        if ((token = expect('BITWISE_AND'))) {
            left = fn(token.value, left, bitwiseAnd());
        }

        return left;
    }

    function equality() {
        let left = relational(), token;

        if ((token = expect('EQUALITY'))) {
            left = fn(token.value, left, equality());
        }

        return left;
    }

    function relational() {
        let left = bitwiseShift(), token;

        if ((token = expect('RELATIONAL'))) {
            left = fn(token.value, left, relational());
        }

        return left;
    }

    function bitwiseShift() {
        let left = addictive(), token;

        if ((token = expect('BITWISE_SHIFT'))) {
            left = fn(token.value, left, addictive());
        }

        return left;
    }

    function addictive() {
        let left = multiplicative(), token;

        while ((token = expect('ADDICTIVE'))) {
            left = fn(token.value, left, multiplicative());
        }

        return left;
    }

    function multiplicative() {
        let left = unary(), token;

        while ((token = expect('MULTIPLICATIVE'))) {
            left = fn(token.value, left, unary());
        }

        return left;
    }

    function unary() {
        let token;

        if ((token = expect('ADDICTIVE'))) {
            if (token.value == '+') {
                return primary();
            } else {
                return fn(token.value, function() { return 0; }, unary());
            }
        } else if ((token = expect('LOGICAL_NOT'))) {
            return fn(token.value, unary());
        }

        return primary();
    }

    function primary() {
        let value, next;

        if (expect('L_PAREN')) {
            value = start();
            consume('R_PAREN');
        } else if (expect('L_CURLY')) {
            let obj = {};

            if (read().name != 'R_CURLY') {
                do {
                    let key = expect().value;
                    consume('COLON');
                    obj[key] = start()();
                } while (expect('COMMA'));
            }

            value = fn(obj);

            consume('R_CURLY');
        } else if (expect('L_BRACKET')) {
            let arr = [];

            if (read().name != 'R_BRACKET') {
                do {
                    arr.push(start()());
                } while (expect('COMMA'));
            }

            value = fn(arr);

            consume('R_BRACKET');
        } else if (expect('PERIOD')) {
            value = peek() ? objectMember(fn(scope.data)) : fn(scope.data);
        } else {
            let token = expect();

            if (token === false) {
                throw new Error('Parser Error: Not a primary expression {{' + expr + '}}');
            }

            if (token.name == 'IDENT') {
                value = RESERVED.hasOwnProperty(token.value)
                      ? RESERVED[token.value]
                      : function() { return scope.get(token.value) };
            } else if (token.name == 'METHOD') {
                if (!formatters[token.value]) {
                    throw new Error('Parser Error: Formatter "' + token.value + '" does not exist, expression {{' + expression + '}}');
                }

                value = fn(formatters[token.value]);
            } else if (token.name == 'REGEXP') {
                value = function() {
                    let re = token.value.split('%%%');
                    return new RegExp(re[0], re[1]);
                };
            } else {
                value = function() { return token.value };
            }
        }

        while ((next = expect('L_PAREN') || expect('L_BRACKET') || expect('PERIOD'))) {
            if (next.value == '(') {
                value = functionCall(value, context);
            } else if (next.value == '[') {
                value = objectIndex(value);
            } else if (next.value == '.') {
                context = value;
                value = objectMember(value);
            } else {
                throw new Error('Parser Error: Parse error in expression {{' + expr + '}}');
            }
        }

        context = undefined;

        return value;
    }

    function functionCall(func, ctx) {
        let argsFn = [];

        if (read().name != 'R_PAREN') {
            do {
                argsFn.push(start());
            } while (expect('COMMA'));
        }

        consume('R_PAREN');

        return function() {
            let args = [];

            if (ctx) args.push(ctx());

            for (let argFn of argsFn) {
                args.push(argFn());
            }

            let fnPtr = func() || NOOP;

            return fnPtr.apply(null, args);
        }
    }

    function objectIndex(obj) {
        let indexFn = start();

        consume('R_BRACKET');

        return function() {
            let o = obj(),
                i = indexFn();
            
            if (typeof o != 'object') return undefined;

            if (o.__dmxScope__) {
                return scope.get(i);
            }

            return o[i];
        }
    }

    function objectMember(obj) {
        let token = expect();

        return function() {
            let o = obj();

            if (token.name == 'METHOD') {
                if (!formatters[token.value]) {
                    throw new Error('Parser Error: Formatter "' + token.value + '" does not exist, expression {{' + expr + '}}');
                }

                return formatters[token.value];
            }

            if (o && o.__dmxScope) {
                return scope.get(token.value);
            }

            return o && o[token.value];
        }
    }
}

function parseValue(value, scope) {
    if (value == null) return value;

    value = value.valueOf();

    if (typeof value == 'object') {
        for (let key in value) {
            value[key] = parseValue(value[key], scope);
        }
    }

    if (typeof value == 'string') {
        if (value.substr(0, 2) == '{{' && value.substr(-2) == '}}') {
            let expr = value.replace(/^\{\{|\}\}$/g, '');

            if (expr.indexOf('{{') == -1) {
                return parser(expr, scope);
            }
        }

        return parseTemplate(value, scope);
    }

    return value;
}

function parseTemplate(template, scope) {
    return template.replace(/\{\{(.*?)\}\}/g, function(a, m) {
        var value = parser(m, scope);
        return value != null ? String(value) : '';
    });
}

exports.lexer = lexer;
exports.parse = parser;
exports.parseValue = parseValue;
exports.parseTemplate = parseTemplate;