# btree_to_dll.py
# Convert binary tree to doubly linked list in-place (inorder sequence).

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None  # or prev in DLL
        self.right = None # or next in DLL

# helper returns (head, tail)
def btree_to_dll(root):
    if not root:
        return (None, None)
    lh, lt = btree_to_dll(root.left)
    rh, rt = btree_to_dll(root.right)
    # connect left tail to root
    if lt:
        lt.right = root
        root.left = lt
    else:
        lh = root
    # connect root to right head
    if rh:
        root.right = rh
        rh.left = root
    else:
        rt = root
    return (lh, rt)

def print_dll(head):
    res=[]
    cur=head
    while cur:
        res.append(str(cur.val))
        cur = cur.right
    print(" <-> ".join(res))

if __name__ == "__main__":
    # build sample tree
    #       4
    #     /   \
    #    2     6
    #   / \   / \
    #  1  3  5  7
    nodes = [Node(i) for i in range(8)]
    root = nodes[4]
    root.left = nodes[2]; root.right = nodes[6]
    nodes[2].left = nodes[1]; nodes[2].right = nodes[3]
    nodes[6].left = nodes[5]; nodes[6].right = nodes[7]
    head, tail = btree_to_dll(root)
    print_dll(head)
