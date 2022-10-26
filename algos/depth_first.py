"""
DEPTH_FIRST.PY

Concept: DFS is the algorithm that implements backtracking (retracing)

Divide & Conquer: split into subproblems of left/right subtree until simple enough to solve directly (null node or found target)

Usage: pre_order tree traversal, combinatorial, graph

Think: "i am just a node, not a tree. i only know my value & my children"
    "how should i proceed with my value. then recurse on my children"

Before Coding: write out STATE, PROCESS, RETURN

000. Find Value in Binary Tree
000. Find Max of Binary Tree
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

def dfs(node, state):
    if not node:
        return None
    # STATES (func args): pass info from parent to children
        # use to compute return value for current node
    left = dfs(node.left, state)
    right = dfs(node.right, state)
    # PROCESS: decide what current node should do with inputs
    value = left + right
    # RETURN: pass info from children to parent
        # after processing current node, what info do we want to share
    return value

"""
000. Find Value in Binary Tree
code: https://github.com/onlypham/tangents

input: node, target
output: True/False (bool)
time: O(N) -> visit every node once

state: tell children what target to look for
process: check if target is in left/right subtree
return: tell parent if I found target my subtree
"""

class Solution:
    def containsTarget(self, root: Optional[TreeNode], val) -> bool:
        if not root:
            return False
        # return True if we find target
        if root.val == val:
            return True
        # check if target is in left/right subtree
        in_left = containsTarget(root.left, val)
        in_right = containsTarget(root.right, val)
        # return True if target in either/both subtree
        return in_left or in_right

"""
000. Find Max of Binary Tree
code: https://github.com/onlypham/tangents

input: node
output: current_max (int)
time: O(N) -> visit every node once

state: none
process: get max of left/right subtree & current node's value
return: tell parent current_max of my subtree
"""

class Solution:
    def findMax(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('-inf')
        # find max of left/right subtree
        left_max = findMax(node.left)
        right_max = findMax(node.right)
        # return max of left/right subtree & current node's value
        return max(node.val, left_max, right_max)

"""
104. Maximum Depth of Binary Tree (Easy)
leet: https://leetcode.com/problems/maximum-depth-of-binary-tree/
code: https://github.com/onlypham/tangents

input: node (depth defined by # of NODES not edges)
output: current_depth (int)
time: O(N) -> visit every node once
space: O(N) -> recursive stack

state: none
process: get max of left/right subtree depth & add 1 for current node
return: tell parent current_depth of my subtree
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # null node adds 0 to depth
        if not root:
            return 0
        # find maxDepth of both left/right subtree
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # current node adds one to depth
        return max(left_depth, right_depth) + 1

"""
1448. Count Good Nodes in Binary Tree (Medium)
leet: https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/
code: https://github.com/onlypham/tangents

input: node 
output: # of good_nodes (int) where good == path from root to X where no node.val > X
time: O(N) -> visit every node once
space: O(H) -> height of tree

state: tell children what current_max is
process: count good_nodes in left/right subtree & add 1 if current node == good
return: tell parent how many good_nodes in my subtree (int)
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, current_max):
            if not root:
                return 0
            # use state (current_max) to see if current node is good!
            count = 1 if root.val >= current_max else 0
            # update new_current_max (include current node's value)
            new_max = max(current_max, root.val)
            # add good nodes from left/right subtree
            count += dfs(root.left, new_max)
            count += dfs(root.right, new_max)
            return count
        return dfs(root, float('-inf'))

"""
110. Balanced Binary Tree (Easy)
leet: https://leetcode.com/problems/balanced-binary-tree/
code: https://github.com/onlypham/tangents

input: node 
output: True/False (use wrapped function tree_height(node) -> int)
time: O(N) -> visit every node once

state: none
process: get height of left/right subtree. check if height difference > 1. add one to current_height
return: tell parent current_height of my subtree OR -1 if unbalanced (int)
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def treeHeight(root):
            if not root:
                return 0
            # get height of both subtrees
            left_height = treeHeight(root.left)
            right_height = treeHeight(root.right)
            # if either subtree is unbalanced return -1
            if left_height == -1 or right_height == -1:
                return -1
            # calculate if height difference is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            # return max height of subtree + 1 for current node
            return max(left_height, right_height) + 1
        return treeHeight(root) != -1

"""
297. Serialize & Deserialize Binary Tree (Hard)
leet: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
code: https://github.com/onlypham/tangents

input: node / string
output: string / node
time: O(N) -> visit every node once

serialize: pre-order traversal appending each value to a string separated by a space. append 'x' and return if node is None.
deserialize: pre-order traversal creating node based on value. return None if value == "x".
"""

class Codec:

    def serialize(self, root):
        # if null, demark as special character
        if not root:
            return 'x'
        # return string of current node's value, left child & right child
        return ' '.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])
        
    def deserialize(self, data):
        # use self.data since data stream consumed as we build left subtree
        self.data = data
        # base case: no tree
        if self.data[0] == 'x':
            return None
        # recreate tree in pre-order traversal: current, left, right
        node = TreeNode(self.data[:self.data.find(' ')]) 
        node.left = self.deserialize(self.data[self.data.find(' ')+1:])
        node.right = self.deserialize(self.data[self.data.find(' ')+1:])
        return node

"""
236. Lowest Common Ancestor of a Binary Tree (Medium)
leet: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
code: https://github.com/onlypham/tangents

input: node (each node value unique & both targets exist in tree)
output: node
time: O(N) -> visit every node once

concept: if val == p/q, pass information up the tree. two streams of information will trickle up and eventually meet at LCA!

state: tell children what target to look for
process: if both left/right subtree non-null, combine into LCA and return current node, else pass up children's info or null
return: tell parent if LCA/target found otherwise null 
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # return if either p/q found 
        if root == p or root == q:
            return root
        # see if LCA/p/q found in either subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if both targets found, combine into LCA & return
        if left and right:
            return root
        # either left/right OR both subtrees are null, so just pass either
        # if LCA/p/q not found in current node & left/right subtree, return None
        return left or right

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
700. Search in a Binary Search Tree (Easy)
leet: https://leetcode.com/problems/search-in-a-binary-search-tree/
code: https://github.com/onlypham/tangents

input: node, target
output: node
time: O(logN) -> height of tree

state: tell children what target to look for
process: if target is less than my value, search left subtree
return: tell parent if i'm the target node or if its in my left/right subtree
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        # if value is smaller than node's current value, search left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

"""
98. Validate Binary Search Tree (Medium)
leet: https://leetcode.com/problems/validate-binary-search-tree/
code: https://github.com/onlypham/tangents

input: node
output: True/False
time: O(N) -> visit every node once

state: tell children the range of acceptable values to be in
process: check with state to see if current node has valid number
return: tell parent if I am a valid binary subtree
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min, max):
            if not root:
                return True
            # ensure current node is strictly within bounds
            if root.val <= min or root.val >= max:
                return False
            # check if both left/right subtrees are valid
            left = dfs(root.left, min, root.val)
            right = dfs(root.right, root.val, max)
            # return True only if both subtrees are valid
            return left and right
        return dfs(root, float('-inf'), float('inf'))

"""
701. Insert into a Binary Search Tree (Medium)
leet: https://leetcode.com/problems/insert-into-a-binary-search-tree/
code: https://github.com/onlypham/tangents

input: node, value
output: node
time: O(logN) -> height of the tree

state: tell children the value to be inserted
process: if val less then current node's value, insert into left subtree
return: tell parent the newly inserted Node (or current if already created)
"""

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # we can insert Node here
        if not root:
            return TreeNode(val)
        # if value less then current node's value, insert into left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

"""
226. Invert Binary Tree (Easy)
leet: https://leetcode.com/problems/invert-binary-tree/
code: https://github.com/onlypham/tangents

input: node
output: node
time: O(N)

state: none
process: none
return: pass to the parent the inverted version of the current subtree
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # simply create new TreeNode with swapped & inverted left/right subtree
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
