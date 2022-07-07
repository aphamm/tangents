"""
DEPTH_FIRST.PY

Concept: DFS is the algorithm that implements backtracking (retracing)
Divide & Conquer: split into subproblems of left/right subtree until simple enough to solve directly (null node or found target)
Usage: pre_order tree traversal, combinatorial, graph

Think: "i am just a node, not a tree. i only know my value & my children"
    "how should i proceed with my value. then recurse on my children"

Before Coding: write out STATE, PROCESS, RETURN

contains_target
find_max
104. Maximum Depth of Binary Tree (Easy)
1448. Count Good Nodes in Binary Tree (Medium)
110. Balanced Binary Tree (Easy)
297. Serialize and Deserialize Binary Tree (Hard)
236. Lowest Common Ancestor of a Binary Tree (Medium)
700. Search in a Binary Search Tree (Easy)
98. Validate Binary Search Tree (Medium)
701. Insert into a Binary Search Tree (Medium)
226. Invert Binary Tree (Easy)
"""

def template(node, state):
    if not node:
        return None
    # STATES (func args): pass info from parent to children
        # use to compute return value for current node
    left = template(node.left, state)
    right = template(node.right, state)
    # PROCESS: decide what current node should do with inputs
    value = left + right
    # RETURN: pass info from children to parent
        # after processing current node, what info do we want to share
    return value

from trees import Node, make_tree

"""
tree1:
            2
        1       4         
      x   3   x   6
         x x     x x
"""

tree1 = make_tree(iter([2, 1, "x", 3, "x", "x", 4, "x", 6, "x", "x"]), int)

"""
tree2:
                     7
            4               4         
        2       3        3      6
      2   x   x   8    x   x  x   9
     x x         x x             x x
"""

tree2 = make_tree(iter([7, 4, 2, 2, "x", "x", "x", 3, "x", 8, "x", "x", 4, 3, "x", "x", 6, "x", 9, "x", "x"]), int)

"""
tree3:
                     8
            6               7         
        1      11        3      6
      9   x   x   5    x   4  x   x
     2 x         x x      x x
    x x
"""

tree3 = make_tree(iter([8, 6, 1, 9, 2, "x", "x", "x", "x", 11, "x", 5, "x", "x", 7, 3, "x", 4, "x", "x", 6, "x", "x"]), int)

"""
algo: contains_target
input: node, target
output: True/False
time: O(N) -> visit every node once

states: tell children what target to look for

process: check if target is in left/right subtree

return: tell parent if I found target my subtree (bool)
"""

def contains_target(node: Node, target: int) -> bool:
    if not node:
        return False
    if node.val == target:
        return True
    # check if target is in left/right subtree
    in_left_subtree = contains_target(node.left, target)
    in_right_subtree = contains_target(node.right, target)
    # return True if target in either/both subtree
    return in_left_subtree or in_right_subtree

def test1():
    assert contains_target(tree1, 6) == True
    assert contains_target(tree1, 9) == False
    assert contains_target(tree2, 7) == True
    assert contains_target(tree2, 1) == False
    assert contains_target(tree3, 6) == True
    assert contains_target(tree3, 12) == False
    print("Paw-🐶-some Job!")

"""
algo: find_max
input: node
output: current_max (int)
time: O(N)

state: none

process: get max of left/right subtree & current node's value

return: tell parent current_max of my subtree (int)
"""

def find_max(node: Node) -> int:
  if not node:
    return float('-inf') 
  left_subtree_current_max = find_max(node.left)
  right_subtree_current_max = find_max(node.right)
  return max(node.val, left_subtree_current_max, right_subtree_current_max)

def test2():
    assert find_max(tree1) == 6
    assert find_max(tree2) == 9
    assert find_max(tree3) == 11
    print("Paw-🐶-some Job!")

"""
104. Maximum Depth of Binary Tree (Easy)
https://leetcode.com/problems/maximum-depth-of-binary-tree/

input: node (depth defined by # of NODES not edges)
output: current_depth (int)
time: O(N)

state: none

process: get max of left/right subtree depth & add 1 for current node

return: tell parent current_depth of my subtree (int)
"""

def max_depth(node: Node) -> int:
    if not node:
        return 0
    left_subtree_depth = max_depth(node.left)
    right_subtree_depth = max_depth(node.right)
    # current node adds one to depth
    return max(left_subtree_depth, right_subtree_depth) + 1    

def test3():
    assert max_depth(tree1) == 3
    assert max_depth(tree2) == 4
    assert max_depth(tree3) == 5
    print("Paw-🐶-some Job!")

"""
1448. Count Good Nodes in Binary Tree (Medium)
https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/

input: node 
output: # of good_nodes (int) 
    (good == path from root to X where no node.val > X)
time: O(N)

state: tell children what current_max is

process: count good_nodes in left/right subtree & add 1 if current node == good

return: tell parent how many good_nodes in my subtree (int)
"""

def good_nodes(node: Node) -> int:
    def dfs(node, current_max):
        if not node:
            return 0
        # use state (current_max) to see if current node is good!
        count = 1 if node.val >= current_max else 0
        # update new_current_max (include current node's value)
        new_current_max = max(current_max, node.val)
        # add good nodes from left/right subtree
        good_nodes_in_left_subtree = dfs(node.left, new_current_max)
        good_nodes_in_right_subtree = dfs(node.right, new_current_max)
        count += good_nodes_in_left_subtree + good_nodes_in_right_subtree
        return count 
    return dfs(node, -float('inf'))

def test4():
    assert good_nodes(tree1) == 4
    assert good_nodes(tree2) == 3
    assert good_nodes(tree3) == 3
    print("Paw-🐶-some Job!")

"""
110. Balanced Binary Tree (Easy)
https://leetcode.com/problems/balanced-binary-tree/

input: node 
output: True/False (use wrapped function tree_height(node) -> int)
time: O(N)

state: none

process: get height of left/right subtree. check if height difference > 1.
    add one to current_height

return: tell parent current_height of my subtree OR -1 if unbalanced (int)
"""

def is_balanced(node: Node) -> bool:
    def tree_height(node):
        if not node:
            return 0
        # get height of both subtrees
        left_subtree_height = tree_height(node.left)
        right_subtree_height = tree_height(node.right)
        if left_subtree_height == -1 or right_subtree_height == -1:
            return -1
        if abs(left_subtree_height - right_subtree_height) > 1:
            return -1
        current_height = max(left_subtree_height, right_subtree_height) + 1
        return current_height
    return tree_height(node) != -1

def test5():
    assert is_balanced(tree1) == True
    assert is_balanced(tree2) == True
    assert is_balanced(tree3) == False
    print("Paw-🐶-some Job!")

"""
297. Serialize and Deserialize Binary Tree (Hard)
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

input: node / string
output: string / node
time: O(N)

serialize: pre-order traversal appending each value to a list. append 'x' and return if node is None.

deserialize: iter (next) through list of values. pre-order traversal creating node based on value. return if value == "x".
"""

def seralize(node: Node) -> str:
    res = []
    def dfs(node):
        if not node:
            res.append('x')
            return
        # process current node, then left, then right
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(node)
    return ' '.join(res)

def deserialize(str: str) -> Node:
    def dfs(nodes):
        val = next(nodes)
        if val == "x":
            return
        # create current node, then left, then right
        cur = Node(int(val))
        cur.left = dfs(nodes)
        cur.right = dfs(nodes)
    return dfs(iter(str.split()))

def test6():
    str1 = "2 1 x 3 x x 4 x 6 x x"
    str2 = "7 4 2 2 x x x 3 x 8 x x 4 3 x x 6 x 9 x x"
    str3 = "8 6 1 9 2 x x x x 11 x 5 x x 7 3 x 4 x x 6 x x"
    assert seralize(tree1) == str1
    assert seralize(tree2) == str2
    assert seralize(tree3) == str3
    deserialize(str1)
    deserialize(str2)
    deserialize(str3)
    print("Paw-🐶-some Job!")

"""
236. Lowest Common Ancestor of a Binary Tree (Medium)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

input: node (each node value unique & both targets exist in tree)
output: node
time: O(N)

concept: if val == target, pass information up the tree. two streams of information will trickle up and eventually meet at LCA!

state: tell children what target to look for

process: if both left/right subtree non-null, combine into LCA and return current node, else pass up children's info or null

return: tell parent if LCA/target found otherwise null 
"""

def lowest_common_ancestor(node: Node, target1: int, target2: int) -> Node:
    if not node:
        return None
    # return if either target1/target2 found 
    if node.val == target1 or node.val == target2:
        return node
    # check if LCA/target is in either left/right subtree
    left = lowest_common_ancestor(node.left, target1, target2)
    right = lowest_common_ancestor(node.right, target1, target2)
    # if both targets found, combine into LCA & return
    if left and right:
        return node
    # at this point, either/both left/right are null, return LCA/target
    if left:
        return left
    if right:
        return right
    # no LCA/target found
    return None

def test7():
    assert lowest_common_ancestor(tree1, 3, 4) == tree1
    assert lowest_common_ancestor(tree3, 2, 5) == tree3.left
    assert lowest_common_ancestor(tree3, 7, 4) == tree3.right
    print("Paw-🐶-some Job!")

"""
Binary Search Tree
Define: node greater than left subtree & less than right subtree

Search: O(logN) -> tree height (assuming balanced)
Insertion: O(logN) -> don't need to move other items down like list
Deletion: O(logN) -> find element, if only one subtree, bring to current position. if two subtrees, delete leftmost node on right subtree & put in current position.

Balanced: subtrees with height difference of at max 1
AVL: self-balance via tree rotations

Applications: look up, dynamic insertion
BST > Hash: sorted, look up 1st element greater/smaller than lookup,
    find k-th largest/smallest, efficient memory usage
"""

"""
tree4:
            5
        3       6         
      x   4   x   9
         x x     x x
"""

tree4 = make_tree(iter([5, 3, "x", 4, "x", "x", 6, "x", 9, "x", "x"]), int)

"""
tree5:
                     6
            3               8         
        2       4        7      9
      1   x   x   5    x   x  x   x
     x x         x x
"""

tree5 = make_tree(iter([6, 3, 2, 1, "x", "x", "x", 4, "x", 5, "x", "x", 8, 7, "x", "x", 9, "x", "x"]), int)


"""
700. Search in a Binary Search Tree (Easy)
https://leetcode.com/problems/search-in-a-binary-search-tree/

input: node, target
output: True/False
time: O(logN)

state: tell children what target to look for

process: if target is less than my value, search left subtree

return: tell parent if i'm the target or in subtree (bool)
"""

def search_binary_tree(node: Node, target: int) -> bool:
    if not node:
        return False
    if node.val == target:
        return True
    elif target < node.val:
        return search_binary_tree(node.left, target)
    else:
        return search_binary_tree(node.right, target)

def test8():
    assert search_binary_tree(tree4, 1) == False
    assert search_binary_tree(tree4, 9) == True
    assert search_binary_tree(tree5, 9) == True
    print("Paw-🐶-some Job!")

"""
98. Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

input: node
output: True/False
time: O(N)

state: tell children the range of acceptable values to be in

process: check with state to see if current node has valid number

return: tell parent if I am a valid binary subtree
"""

def valid_binary_tree(node: Node) -> bool:
    def dfs(node, min, max):
        if not node:
            return True
        # if current node value inconsistent, return False
        if node.val <= min or node.val >= max:
            return False
        return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)
    return dfs(node, float('-inf'), float('inf'))

def test9():
    assert valid_binary_tree(tree1) == False
    assert valid_binary_tree(tree2) == False
    assert valid_binary_tree(tree3) == False
    assert valid_binary_tree(tree4) == True
    assert valid_binary_tree(tree5) == True
    print("Paw-🐶-some Job!")

"""
701. Insert into a Binary Search Tree (Medium)
https://leetcode.com/problems/insert-into-a-binary-search-tree/

input: bst, value
output: node
time: O(N)

state: tell children the value to be inserted

process: if value > than current node's value, recursively call insert_bst and set equal to right subtree

return: tell parent the newly inserted Node (or current if already exists)
"""

def insert_bst(node: Node, value: int) -> Node:
    # if null create new node
    if not node:
        return Node(value)
    if value > node.val:
        node.right = insert_bst(node.right, value)
    elif value < node.val:
        node.left = insert_bst(node.left, value)
    # value already exists
    return node

def test10():
    assert seralize(insert_bst(tree4, 10)) == "5 3 x 4 x x 6 x 9 x 10 x x"
    assert seralize(insert_bst(tree5, 10)) == "6 3 2 1 x x x 4 x 5 x x 8 7 x x 9 x 10 x x"
    print("Paw-🐶-some Job!")

"""
226. Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

input: node
output: node
time: O(N)

state: none

process: none

return: pass to the parent the inverted version of the curretn subtree
"""

def invert_binary_tree(node: Node) -> Node:
    if not node:
        return None
    return Node(node.val, invert_binary_tree(node.right), invert_binary_tree(node.left))

def test11():
    assert seralize(invert_binary_tree(tree4)) == "5 6 9 x x x 3 4 x x x"
    assert seralize(invert_binary_tree(tree5)) == "6 8 9 x x 7 x x 3 4 5 x x x 2 x 1 x x"
    print("Paw-🐶-some Job!")