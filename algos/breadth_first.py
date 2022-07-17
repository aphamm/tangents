"""
BREADTH_FIRST.PY

Concept: We visit all nodes in a level before visting the next. BFS uses a queue (First In First Out). We dequeue a node (need at least one element to start the process) & enqueue its children.

Relationship: DFS is better at finding nodes far away from the root, while BFS is better at finding nodes closer.

102. Binary Tree Level Order Traversal (Medium)
103. Binary Tree Zigzag Level Order Traversal (Medium)
199. Binary Tree Right Side View (Medium)
111. Minimum Depth of Binary Tree (Easy)
"""

from collections import deque

def bfs(root):
    # ensure we have at least one element at the start
    queue = deque([root])
    # as long as there is an element in the queue
    while queue:
        node = queue.popleft() # dequeue
        for child in node.children: # enqueue children
            queue.append(child)
    return value

"""
102. Binary Tree Level Order Traversal (Medium)
Leet: https://leetcode.com/problems/binary-tree-level-order-traversal/
Code: https://github.com/onlypham/tangents

Problem: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Input: root
Output: list of lists for each level

Framework: Breadth First Search
Giveaways: Here we must to a level order traversal of the tree. Thus we will first look at the root, then nodes at a depth of 1, then nodes at a depth of 2 and so on.
Concept: At the start of the while loop iteration, the only nodes in the queue will be the nodes in that current level. Count this length. Dequeue this number of nodes every iteration of the while loop.

Process: 

    1. Enqueue the first root node.
    2. While queue not empty.
        a. Count the number of nodes in the queue (which is # in current level)
        b. Dequeue that many nodes in the current level.
            i. For each dequeue'd node, enqueue it's left/right children.
            ii. Append that node to the current level.

Return: none

Complexity: 
Time: O(N) since we visit every node once
Space: O(N)
"""

class Solution:

    def levelOrder(self, root):
        # ensure root is not null
        if not root: 
            return []
        # queue the first root node to start bfs
        queue, res = deque([root]), []
        while queue:
            # number of nodes in current level
            cur_level, size = [], len(queue)
            # dequeue all nodes in current level
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res

"""
103. Binary Tree Zigzag Level Order Traversal (Medium)
Leet: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Code: https://github.com/onlypham/tangents

Problem: Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Input: root
Output: list of lists for each level

Framework: Breadth First Search
Giveaways: Here we must to a level order traversal of the tree. Thus we will first look at the root, then nodes at a depth of 1, then nodes at a depth of 2 and so on. The only twist is that we must reverse the order every other level.
Concept: This is essentially a level order traversal. Follow the same exact steps to get the list of nodes in the current level. Set a boolen that switches every iteration of the while loop. Dependent on this, reverse the list of nodes on the current level before appending to results.

Process: 

    1. Enqueue the first root node.
    2. While queue not empty.
        a. Count the number of nodes in the queue (which is # in current level)
        b. Dequeue that many nodes in the current level.
            i. For each dequeue'd node, enqueue it's left/right children.
            ii. Append that node to the current level.
    3. If not leftToRight, then reverse list of cur_level.
        a. Negate leftToRight before next iteration.

Return: none

Complexity: 
Time: O(N) since we visit every node once
Space: O(N)
"""

class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, res = deque([root]), []
        leftToRight = True
        while queue:
            cur_level, size = [], len(queue)
            for _ in range(size):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not leftToRight:
                cur_level.reverse()
            res.append(cur_level)
            leftToRight = not leftToRight
        return res

"""
199. Binary Tree Right Side View (Medium)
Leet: https://leetcode.com/problems/binary-tree-right-side-view/
Code: https://github.com/onlypham/tangents

Problem: Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Input: root
Output: list of nodes

Framework: Breadth First Search
Giveaways: A level order traversal here makes sense as we only compare nodes within the same level. Given a set of nodes exist in level n, we only need to see which node from 1,2,3...,n is on the right.
Concept: When we enqueue children, we will start by enqueue the right child THEN left child as we want to ensure that the first node in our queue is the right most element. We can think of this exactly as a level order traversal execept instead of reading from left to right, we look from right to left.

Process: 

    1. Enqueue the first root node.
    2. While queue not empty.
        a. Count the number of nodes in the queue (which is # in current level)
        b. Append the first element in the queue to results.
        c. Dequeue the number of nodes in the current level.
            i. For each dequeue'd node, enqueue its RIGHT child then its left.

Return: none

Complexity: 
Time: O(N) since we visit every node once
Space: O(N)
"""

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue, res = deque([root]), []
        while queue:
            size = len(queue)
            res.append(queue[0].val)
            for _ in range(size):
                node = queue.popleft()
                # ensure we enqueue right child first to ensure
                # first element in queue will be right most node
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res

"""
111. Minimum Depth of Binary Tree (Easy)
Leet: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Code: https://github.com/onlypham/tangents

Problem: Given a binary tree, find its minimum depth.
Input: root
Output: depth
Other: The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Framework: Breadth First Search
Giveaways: A level order traversal here makes sense as we know that all nodes in the same level will have the same depth. Thus, when we compare nodes in a particular level, if any of them are terminal/leaf nodes, then this will be the global minimum depth of the entire tree. This is since all further levels will be at a higher depth.
Concept: We star the depth counter at 0 (root node). Every time we iterate through the while loop, we will increase the depth by 1. When we dequeue nodes at a particular level, we will check if it is a root node.

Process: 

    1. Enqueue the first root node. Depth = 0.
    2. While queue not empty.
        a. Depth += 1
        b. Count the number of nodes in the queue (which is # in current level)
        c. Dequeue the number of nodes in the current level.
            i. Check if it is a terminal/leaf node. If so, return depth.
            ii. For each dequeue'd node, enqueue its RIGHT child then its left.

Return: depth

Complexity: 
Time: O(N) since we visit every node once
Space: O(N)
"""

class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth 
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return depth
        