"""
TREES.PY

Written by: Austin Pham

Terminology:
- Internal Node: non-root node
- Leaf Node: no children
- Ancestors: all nodes reachable from current node moving up
- Descendent: all nodes reachable from current node moving down
- Level: # of ancestors from node to root
- Height: # of edges on longest path from node to leaf
- Depth: # of edges from node to root
"""

def in_order_traversal(root):
    if root is not None:
        # process left branch, current node, then right branch
        in_order_traversal(root.left)
        print(root.val) 
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root is not None:
        # process current node, left branch, then right branch
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root is not None:
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

class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    # wow a post_order_traversal, which makes sense since we
    # need to know the left/right children before creating current
    left = tree(nodes, f)
    right = tree(nodes, f)
    return BinaryNode(f(val), left, right)

binary = tree(iter([5, 1, 3, "x", "x", 8, "x", "x", 6, 2, "x", "x", "x"]), int)

# in_order_traversal(binary)
# pre_order_traversal(binary)
# post_order_traversal(binary)

class NonBinaryNode:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children