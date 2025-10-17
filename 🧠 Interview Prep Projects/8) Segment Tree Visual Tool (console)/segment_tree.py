class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
        # build
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def range_sum(self, l, r):
        # sum on interval [l, r]
        l += self.size
        r += self.size
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.tree[l]
                l += 1
            if r % 2 == 0:
                s += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return s

    def update(self, idx, value):
        pos = self.size + idx
        self.tree[pos] = value
        pos //= 2
        while pos:
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos + 1]
            pos //= 2

    def visualize(self):
        print("Segment tree array representation:")
        print(self.tree)

if __name__ == "__main__":
    data = [2,1,5,3,4]
    st = SegmentTree(data)
    st.visualize()
    print("sum(1,3) =", st.range_sum(1,3))
    st.update(2,10)
    print("After update:")
    st.visualize()
    print("sum(1,3) =", st.range_sum(1,3))
