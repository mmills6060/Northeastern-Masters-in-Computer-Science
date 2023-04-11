// Perhaps use hashy as reference to implement bcrypt and needRehash action
// https://github.com/JsCommunity/hashy

// supports argon2i, argon2d and argon2id
exports.passwordHash = async function(options) {
  const password = this.parseRequired(options.password, 'string', 'crypto.passwordHash: password is required.')
  const algo = this.parseOptional(options.algo, 'string', 'argon2i')
  const argon2 = require('argon2')
  const type = argon2[algo]
  return argon2.hash(password, { type })
}

exports.passwordVerify = async function(options) {
  const password = this.parseRequired(options.password, 'string', 'crypto.passwordVerify: password is required.')
  const hash = this.parseRequired(options.hash, 'string', 'crypto.passwordVerify: hash is required.')
  const argon2 = require('argon2')
  return argon2.verify(hash, password)
}

exports.passwordNeedsRehash = async function(options) {
  const hash = this.parseRequired(options.hash, 'string', 'crypto.passwordNeedsRehash: hash is required.')
  const algo = this.parseOptional(options.algo, 'string', 'argon2i')
  const argon2 = require('argon2')
  return argon2.needsRehash(hash, {})
}

exports.uuid = async function(options) {
  const { randomUUID } = require('crypto')
  const { v4: uuidv4 } = require('uuid')
  return randomUUID ? randomUUID() : uuidv4()
}