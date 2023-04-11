// ArrayList

const { clone } = require('../core/util');

// Create a new ArrayList
exports.create = function(options, name) {
  const value = this.parseOptional(options.value, 'object', []);
  
  if (!name) throw Error('arraylist.create: name is required.');

  if (!this.req.arrays) {
    this.req.arrays = {};
  }

  this.req.arrays[name] = Array.isArray(value) ? clone(value) : [];
};

// Return the ArrayList as array value
exports.value = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.value: ref is required.');

  if (!this.req.arrays) throw Error('arraylist.value: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.value: ArrayList ${ref} not found.`);

  return clone(this.req.arrays[ref]);
};

// Return the size of the ArrayList
exports.size = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.size: ref is required.');

  if (!this.req.arrays) throw Error('arraylist.size: No arraylists are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.size: ArrayList ${ref} not found.`);

  return this.req.arrays[ref].length;
};

// Return the value at a specific index
exports.get = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.get: ref is required.');
  const index = this.parseRequired(options.index, 'number', 'arraylist.get: index is required.');

  if (!this.req.arrays) throw Error('arraylist.get: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.get: ArrayList ${ref} not found.`);

  return clone(this.req.arrays[ref][index]);
};

// Add a value to the ArrayList
exports.add = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.add: ref is required.');
  const value = this.parseRequired(options.value, '*', 'arraylist.add: value is required.');

  if (!this.req.arrays) throw Error('arraylist.add: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.add: ArrayList ${ref} not found.`);

  this.req.arrays[ref].push(clone(value));
};

// Add an array of values to the ArrayList
exports.addAll = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.addAll: ref is required.');
  const value = this.parseRequired(options.value, 'object', 'arraylist.addAll: value is required.');

  if (!this.req.arrays) throw Error('arraylist.addAll: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.addAll: ArrayList ${ref} not found.`);
  if (!Array.isArray(value)) throw Error('arraylist.addAll: Value must be an array.')

  for (let val of value) {
    this.req.arrays[ref].push(clone(val));
  }
};

// Update a value at a specific index
exports.set = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.set: ref is required.');
  const index = this.parseRequired(options.index, 'number', 'arraylist.set: index is required.');
  const value = this.parseRequired(options.value, '*', 'arraylist.set: value is required.');

  if (!this.req.arrays) throw Error('arraylist.set: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.set: ArrayList ${ref} not found.`);

  this.req.arrays[ref][index] = clone(value);
};

// Remove the first occurrence of a specific value
exports.remove = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.remove: ref is required.');
  const value = this.parseRequired(options.value, '*', 'arraylist.remove: value is required.');

  if (!this.req.arrays) throw Error('arraylist.remove: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.remove: ArrayList ${ref} not found.`);

  const index = this.req.arrays[ref].indexOf(value);
  
  if (index == -1) throw Error('arraylist.remove: Value does not exist in the ArrayList.');
  
  this.req.arrays[ref].splice(index, 1);
};

// Remove a value from the ArrayList at a specific index
exports.removeAt = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.removeAt: ref is required.');
  const index = this.parseRequired(options.index, 'number', 'arraylist.removeAt: index is required.');

  if (!this.req.arrays) throw Error('arraylist.removeAt: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.removeAt: ArrayList ${ref} not found.`);

  this.req.arrays[ref].splice(index, 1);
};

// Clear all values from the ArrayList
exports.clear = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.clear: ref is required.');

  if (!this.req.arrays) throw Error('arraylist.clear: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.clear: ArrayList ${ref} not found.`);

  this.req.arrays[ref] = [];
};

// Sort the ArrayList
exports.sort = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.sort: ref is required.');
  const prop = this.parseOptional(options.prop, 'string', null);
  const desc = this.parseOptional(options.desc, 'boolean', false);

  if (!this.req.arrays) throw Error('arraylist.sort: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.sort: ArrayList ${ref} not found.`);

  this.req.arrays[ref].sort((a, b) => {
    if (prop) {
      a = a[prop];
      b = b[prop];
    }

    if (a == b) return 0;
    if (a < b) return desc ? 1 : -1;
    return desc ? -1 : 1;
  });
};

// Return the index of the first occurrence of a specific value
exports.indexOf = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.indexOf: ref is required.');
  const value = this.parseRequired(options.value, '*', 'arraylist.indexOf: value is required.');

  if (!this.req.arrays) throw Error('arraylist.indexOf: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.indexOf: ArrayList ${ref} not found.`);

  return this.req.arrays[ref].indexOf(value);
};

// Return true if the ArrayList contains a specific value
exports.contains = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.contains: ref is required.');
  const value = this.parseRequired(options.value, '*', 'arraylist.contains: value is required.');

  if (!this.req.arrays) throw Error('arraylist.contains: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.contains: ArrayList ${ref} not found.`);

  return this.req.arrays[ref].includes(value);
};

// Return true when ArrayList is empty
exports.isEmpty = function(options) {
  const ref = this.parseRequired(options.ref, 'string', 'arraylist.isEmpty: ref is required.');

  if (!this.req.arrays) throw Error('arraylist.isEmpty: No ArrayList are created.');
  if (!this.req.arrays[ref]) throw Error(`arraylist.isEmpty: ArrayList ${ref} not found.`);

  return !this.req.arrays[ref].length;
};