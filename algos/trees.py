"""
TREES.PY

Terminology:
- Internal Node: non-root node
- Leaf Node: no children

- Ancestors: all nodes reachable from current node moving up
- Descendent: all nodes reachable from current node moving down

- Depth of Node: # of edges from N to root
- Height of Tree: depth of deepest node
"""

def in_order_traversal(root):
    if root:
        # process left branch, current node, then right branch
        in_order_traversal(root.left)
        print(root.val) 
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        # process current node, left branch, then right branch
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        # process left branch, right branch, then current node
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)

"""
Binary Trees only have two children.
The following binary tree looks like this:

        5
    1       6
  3   8   2    x
 x x x x x x

Check out the following traversal methods.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    # wow a post_order_traversal, which makes sense since we
    # need to know the left/right children before creating current
    left = make_tree(nodes, f)
    right = make_tree(nodes, f)
    return Node(f(val), left, right)

node = make_tree(iter([5, 1, 3, "x", "x", 8, "x", "x", 6, 2, "x", "x", "x"]), int)

# run traversals here !
# in_order_traversal(node)
# pre_order_traversal(node)
# post_order_traversal(node)

class NonBinaryNode:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children