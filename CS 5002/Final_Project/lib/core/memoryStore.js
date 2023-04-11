module.exports = function(session) {
  const Store = session.Store

  const defer = (cb, ...args) => {
    if (typeof cb != 'function') return
    setImmediate(cb, ...args)
  }

  class ExtendedMap extends Map {
    set(key, value, maxAge) {
      const cached = super.get(key)
      if (cached && cached.timer) clearTimeout(cached.timer)
      const timer = maxAge ? setTimeout(super.delete.bind(this, key), maxAge) : null
      return super.set(key, {timer, value})
    }
  
    get(key) {
      const cached = super.get(key)
      return cached && cached.value
    }
  
    delete(key) {
      const cached = super.get(key)
      if (cached && cached.timer) clearTimeout(cached.timer)
      return super.delete(key)
    }
  }

  class MemoryStore extends Store {
    constructor(options = {}) {
      super(options)
      this.sessions = new ExtendedMap()
      this.ttl = options.ttl
    }

    get(sid, callback) {
      let session = this.sessions.get(sid)
      defer(callback, null, session)
    }

    set(sid, session, callback) {
      let ttl = this._getTTL(session)
      if (ttl > 0) {
        this.sessions.set(sid, session, ttl)
      } else {
        this.sessions.delete(sid)
      }
      defer(callback, null)
    }

    touch(sid, session, callback) {
      let ttl = this._getTTL(session)
      let stored = this.sessions.get(sid)
      stored.cookie = session.cookie
      this.sessions.set(sid, stored, ttl)
      defer(callback, null)
    }

    destroy(sid, callback) {
      this.sessions.delete(sid)
      defer(callback, null)
    }

    clear(callback) {
      this.sessions.clear()
      defer(callback, null)
    }

    length(callback) {
      let len = this.sessions.size
      defer(callback, null, len)
    }

    ids(callback) {
      let keys = Array.from(this.sessions.keys())
      defer(callback, null, keys)
    }

    all(callback) {
      let sessions = Array.from(this.sessions.values())
      defer(callback, null, sessions)
    }

    _getTTL(session) {
      if (typeof this.ttl == 'number') return this.ttl
      let maxAge = (session && session.cookie) ? session.cookie.maxAge : null
      return (typeof maxAge == 'number') ? maxAge : 86400000
    }
  }

  return MemoryStore
}