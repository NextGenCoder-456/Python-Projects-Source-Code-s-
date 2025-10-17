class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    update_height(node)
    bf = balance_factor(node)
    # LL
    if bf > 1 and key < node.left.key:
        return rotate_right(node)
    # RR
    if bf < -1 and key > node.right.key:
        return rotate_left(node)
    # LR
    if bf > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    # RL
    if bf < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)
    return node

def inorder(node):
    return inorder(node.left) + [node.key] + inorder(node.right) if node else []

def print_levels(root):
    if not root: 
        print("Empty")
        return
    q = [(root, 0)]
    curr_level = 0
    line = []
    while q:
        node, lvl = q.pop(0)
        if lvl != curr_level:
            print(f"Level {curr_level}: {line}")
            line = []
            curr_level = lvl
        line.append(f"{node.key}(h={node.height},bf={balance_factor(node)})")
        if node.left: q.append((node.left, lvl+1))
        if node.right: q.append((node.right, lvl+1))
    print(f"Level {curr_level}: {line}")

if __name__ == "__main__":
    keys = [10,20,30,40,50,25]
    root = None
    for k in keys:
        root = insert(root, k)
        print("\nAfter inserting", k)
        print_levels(root)
    print("\nInorder:", inorder(root))
