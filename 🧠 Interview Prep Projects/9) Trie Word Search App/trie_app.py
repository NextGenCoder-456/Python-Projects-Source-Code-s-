class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_end

    def starts_with(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        results = []
        self._dfs(cur, prefix, results)
        return results

    def _dfs(self, node, path, res):
        if node.is_end:
            res.append(path)
        for ch, nxt in node.children.items():
            self._dfs(nxt, path+ch, res)

if __name__ == "__main__":
    trie = Trie()
    words = ["apple","app","apply","apt","bat","batch","bath"]
    for w in words:
        trie.insert(w)
    print("Search 'app':", trie.search("app"))
    print("Suggestions for 'ap':", trie.starts_with("ap"))
