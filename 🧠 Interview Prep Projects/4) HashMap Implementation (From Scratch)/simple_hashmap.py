class SimpleHashMap:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return default

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __repr__(self):
        return "{" + ", ".join(str(bucket) for bucket in self.table if bucket) + "}"

if __name__ == "__main__":
    m = SimpleHashMap()
    m.put("apple", 5)
    m.put("banana", 7)
    print("apple:", m.get("apple"))
    m.put("apple", 9)
    print("after update:", m.get("apple"))
    m.delete("banana")
    print("map:", m)
