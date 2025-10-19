# lru_cache_flask.py
# Simple Flask app demonstrating an in-memory LRU cache with get/put via HTTP.
from collections import OrderedDict
from flask import Flask, request, jsonify

class LRUCache:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

app = Flask(__name__)
cache = LRUCache(capacity=5)

@app.route("/put", methods=["POST"])
def put():
    key = request.json.get("key")
    value = request.json.get("value")
    cache.put(key, value)
    return jsonify({"status":"ok", "cache": list(cache.cache.items())})

@app.route("/get/<key>", methods=["GET"])
def get_key(key):
    val = cache.get(key)
    return jsonify({"key": key, "value": val, "cache": list(cache.cache.items())})

if __name__ == "__main__":
    app.run(debug=True)
