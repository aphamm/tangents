"""
GRAPHS.PY

Concept: A tree is a connected acyclic graph with n nodes and n-1 edges while having only 1 path between 2 nodes in a tree. Graphs may have cycles and be disconnected. Most interview graph problems are connected undirected graphs.

BFS: shortest distance from A to B (unweight), graph of unknown size (word ladder), graph of infinite size (knight shortest path), shortest path in weighted graph (Dijkstra)  

DFS: uses less memory than BFS for wide graphs (no queue needed), finding nodes far from root (maze)

733. Flood Fill (Easy)
200. Number of Islands (Medium)
1197. Minimum Knight Moves (Medium)
286. Walls and Gates (Medium)
752. Open the Lock (Medium)
127. Word Ladder (Hard)
773. Sliding Puzzle (Hard)
444. Sequence Reconstruction (Medium)
269. Alien Dictionary (Hard)
207. Course Schedule (Medium)
"""

from collections import deque
from curses import resetty
from re import S

class Template:

    # O(|V| + |E|) -> number of vertices/edges
    def bfs(root):
        queue = deque([root])
        visited = set([root])
        level = 0
        while queue:
            # get number of nodes in current level
            n = len(queue)
            for _ in range(n):
                # dequeue node + process it
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    # check if neighbor has been previously visited
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            # increment level after processing current level
            level += 1
    
    # O(n+m) -> number of vertices/edges
    def dfs(root, visited):
        for neighbor in get_neighbors(root):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            # recursively call on unvisited neighbors
            dfs(neighbor, visited)

    # getting neighbors from matrix graph
    def get_neighbors(coordinate):
        row, col = coordinate
        # starting north, clockwise
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        res = []
        for i in range(length(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                res.append((neighbor_row, neighbor_col))
        return res

"""
733. Flood Fill (Easy)
Leet: https://leetcode.com/problems/flood-fill/
Code: https://github.com/onlypham/tangents

Problem: An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
Input: sr, sc, color
Output: Modified image after flood fill
Other: To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Framework: Depth First Search
Giveaways: We  need to traverse all connected 4D pixels to the starting point. We can use DFS by using the changed pixel color as a marker for if the pixel has been previously visited.
Concept: Change the color for a given pixel. Then recursively call on all adjacent pixels that are NOT the new color.

Process: 

    1. Get the original color. Return if new color == original.
    2. Change the color of the pixel.
        a. For all "in-bound" pixels that are the OLD color.
            i. Recursively call dfs.

Complexity: 
Time: O(MxN) since we at most have to change all pixels of the grid
Space: 
"""

class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            image[i][j] = color
            # find neighbors that are within bounds & are the old oclor
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        # save the original color
        old, m, n = image[sr][sc], len(image), len(image[0])
        # if old color == new color, just return
        if image[sr][sc] != color:
            dfs(sr, sc)
        return image

"""
200. Number of Islands (Medium)
Leet: https://leetcode.com/problems/number-of-islands/
Code: https://github.com/onlypham/tangents

Problem: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
Input: grid
Output: # of islands (int)
Other: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Framework: Depth First Search
Giveaways: We need to traverse all connected 4D pixels to a certain point. We can use DFS starting at this particular point and demarking all its connected neighbors. 
Concept: Look through the entire mxn grid of points. If we find a "1", increase the count and mark that particular point and all of its connected neighbors as a "0" to denote that it was already counted in a single island. 

Process: 

    1. Iterate through the entire range MxN of the grid.
        a. Mark that particular point with a '0'.
        b. For all "in-bound" points that == "1", recursively call dfs.
        c. Increase count by 1 to signify we found one entire island.

Complexity: 
Time: O(MxN) since we must traverse the entire grid
Space: 
"""

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:       
        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)
        count, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

"""
1197. Minimum Knight Moves (Medium)
Leet: https://leetcode.com/problems/minimum-knight-moves/
Code: https://github.com/onlypham/tangents

Problem: In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0]. Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists
Input: x, y
Output: minimum moves (int)

Framework: Breadth First Search
Giveaways: Shortest path means BFS. We want to analyze all possible paths 1 move from the start, 2 moves from the start, 3 moves from the start...
Concept: Starting at (0,0) we find all possible neighbors that we add to a queue. We want to search all unvisited neighbors in a single level (single step). If it was already previously visited, it would essentially be a duplicate search (all points we can reach via moving here can be achieved in this previously visited state)

Process: 

    1. Enqueue the starting coordinate (0,0)
        a. Iterate through the length of the queue (one level == one move)
            i. If it is our desired target, return steps.
            ii. Find all unvisited "in-bound" neighbors & add to queue. 
        b. Increase count by 1 to signify we exhausted all moves in one level.

Complexity: 
Time: 
Space: 
"""

from collections import deque

class Solution:

    def minKnightMoves(self, x: int, y: int) -> int:
        # given a coordinate, return a list of possible moves
        def viableMoves(coord):
            res, x, y = [], coord
            rowMoves = [-2, -2, -1, 1, 2, 2, 1, -1]
            colMoves = [-1, 1, 2, 2, 1, -1, -2, -2]
            for i in range(len(rowMoves)):
                r = x + rowMoves[i]
                c = y + colMoves[i]
                res.append((r, c))
            return res
        def bfs(coord):
            visited, steps, queue = set(), 0, deque([coord])
            while queue:
                n = len(queue)
                # ensure we only dequeue one level at a time 
                for _ in range(n):
                    position = queue.popleft()
                    # if we find point, return steps
                    if position[0] == x and position[1] == y:
                        return steps
                    # add neighbors to queue if not visited before
                    for neighbor in viableMoves(position):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                steps += 1
        # return BFS starting at (0,0)
        return bfs((0, 0))

"""
286. Walls and Gates (Medium)
Leet: https://leetcode.com/problems/walls-and-gates/
Code: https://github.com/onlypham/tangents

Problem: In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0]. Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists
Input: x, y
Output: minimum moves (int)

Framework: Breadth First Search
Giveaways: Shortest path means BFS. We want to analyze all possible paths 1 move from the gate, 2 moves from the gate, 3 gate...
Concept: We basically do a simultaneous BFS from all gates. We will update the distance integer of all reachable empty spaces. We do not touch walls (-1) or previously visited spaces (1,2,3...). 

Process: 

    1. Enqueue all the gates in the dungeon
        a. Iterate through the length of the queue (one level == one step)
            i. Demark the space as visited by changing it's value to current distance.
            ii. Find all unvisited "in-bound" neighbors & add to queue. 
        b. Increase count by 1 to signify we exhausted all moves in one level.

Complexity: 
Time: O(MxN) since we visit all the grid positions
Space: O(1)
"""

class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        nRows, nCols = len(rooms), len(rooms[0])
        queue, distance = deque(), 0
        # iterate through entire grid & enqueue the gates
        for i in range(nRows):
            for j in range(nCols):
                if rooms[i][j] == 0:
                    queue.append((r, c))
        while queue:
            # iterate through one level of BFS (one additional step)
            for _ in range(len(queue)):
                x, y = queue.popleft()
                rooms[x][y] = distance
                for r, c in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                    if 0 <= r < nRows and 0 <= c < nCols:
                        # ensure we are only appending unvisited grids
                        if rooms[r][c] == float('inf'):
                            queue.append((r, c))
            dist += 1

"""
752. Open the Lock (Medium)
Leet: https://leetcode.com/problems/open-the-lock/
Code: https://github.com/onlypham/tangents

Problem: You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
Input: deadends, target
Output: minimum moves (int) OR -1 if impossible
Other: The lock initially starts at '0000', a string representing the state of the 4 wheels.

Framework: Breadth First Search
Giveaways: Shortest path means BFS. We want to analyze all possible paths 1 move from 0000, 2 moves from 0000, 3 moves from 0000...
Concept: Do a BFS starting from 0000. For one level of the queue (representing one turn), we will return if combination reached OR deadend reached. Track all previously visited combinations to ensure we do not explore duplicates.

Process: 

    1. Enqueue the first combination "0000".
    2. Create a visit set of deadends (don't want to be able to visit these)
    3. Iterate through the length of the queue (one level == one combination)
        a. If combination == target, return turns
        b. For every valid unvisited combination, add to queue.
        c. Add one to turns counter. 
    4. Return -1 if we do not find any valid paths to target.

Complexity: 
Time: O(1000) which is the # of combinations or 10^4 = 1000
Space: O(1000) for the same reasons since we have a visited set
"""

class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def combinations(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        queue, turns, visit = deque(["0000"]), 0, set(deadends)
        while queue:
            for _ in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return turns
                for combo in combinations(lock):
                    if combo in visit:
                        continue
                    visit.add(combo)
                    queue.append(combo)
            turns += 1
        return -1

"""
127. Word Ladder (Hard)
Leet: https://leetcode.com/problems/word-ladder/
Code: https://github.com/onlypham/tangents

Problem: A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that: 1) Every adjacent pair of words differs by a single letter. 2) Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList. 3) sk == endWord. 
Input: beginWord, endWord, dictionary wordList
Output: minimum number of transformation words (int) OR 0 if none exist

Framework: Breadth First Search
Giveaways: Shortest path means BFS. We want to analyze all possible words 1 transformation from beginWord, 2 transformations from beginWord...
Concept: Do a BFS starting from beginWord. For one level of the queue (representing one transformation), we will return if endWord is reached. Track all previously visited words to ensure we do not explore duplicates.

Process: 

    1. Enqueue the first beginWord.
    2. Create a visit set of words (don't want to be able to visit again)
    3. Iterate through the length of the queue (one level == one transformation)
        a. If word == endWord, return count
        b. For every valid unvisited word in wordList, add to queue.
        c. Add one to turns counter. 
    4. Return 0 if we do not find any valid paths to target.

Complexity: 
Time: 
Space: 
"""

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue, wordList = deque([[beginWord, 1]]), set(wordList)
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # find all one letter transformations to get next_word
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        # remove from wordList b/c we don't want to visit again
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
        
"""
773. Sliding Puzzle (Hard)
Leet: https://leetcode.com/problems/sliding-puzzle/
Code: https://github.com/onlypham/tangents

Problem: On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
Input: board
Output: return least number of moves to solve board (int) OR -1 if impossible
Other: The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Framework: Breadth First Search
Giveaways: We want to find the minimum amount of moves, so DFS is a suitable choice. We want to find all board positions 1 move from the beginning, 2 moves from the beginning, 3 moves from the beginning...
Concept: Do a BFS from the beginning board position. The only possible moves are switches with the "0". Thus, we find where the "0" can move and then swap the positions of "0" and the other element. 

Process: 

    1. Serialize the board into a string.
    2. Create a dictionary for given an index i, where can I move.
    3. Enqueue the first board position WITH index of "0".
        a. Iterate through the length of the queue (one level == one move of "0")
        b. If we reach the solved state, return moves.
        c. For all swap of "0" and its neighbors.
            i. Append to queue if not visited.

Complexity: 
Time: O(N!) where n is the size of the matrix (permutations of board)
Space: O(N!) for the same reasons since we have a visited set
"""

class Solution:

    def slidingPuzzle(self, board):
        # seralize board to row-major string
        s = "".join(str(c) for row in board for c in row)
        # [0, 1, 2] let board look at such where
        # [3, 4, 5] moves represents possibles moves from certain position
        moves = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}
        visit, moves = set(s), 0
        # queue represents string + index of "0"
        queue = deque([(s, s.index("0"))])
        while queue:
            for _ in range(len(queue)):
                s, i = queue.popleft()
                if s == "123450":
                    return moves
                current = [c for c in s]
                # represents the moves that 0 can take from current position
                for move in moves[i]:
                    nextMove = current[:]
                    # swap 0 with element in its end destination (== move)
                    nextMove[i], nextMove[move] = nextMove[move], nextMove[i]
                    nextS = "".join(nextMove)
                    if nextS in visit:
                        continue
                    visit.add(nextS)
                    queue.append((nextS, move))
            moves += 1
        return -1

"""
Kahn's Algorithm: systematically remove one node at a time, each time removing a node such that no other nodes point to that node

If cyclic -> no valid solution -> otherwise we'd find a node that doesn't depend on any other nodes

STEPS:

    1. Iterate thru nodes & count # of parents node has {node: # of parents}
    2. Enqueue nodes with 0 parents.
    3. Deque node & subtract 1 from parent count of all its children.
    4. Enqueue any nodes where parent count drops to 0.
    5. Repeat until queue empty. Else, cycle.

BFS: In topo sort, we only enqueue nodes with 0 parents, where in BFS we enqueue all neighboring nodes into queue.

EXAMPLE: Task Scheduling

Problem: Given a list of tasks, compute a sequence of tasks that can be performed such that we complete every task once while satisfying all the requirements.
Input: tasks, requirements [a, b] where a needs to be completed before b
Output: task ordering
"""

class Solution:

    def countParents(graph):
        counts = { node: 0 for node in graph }
        for parent in graph:
            for node in graph[parent]:
                counts[node] += 1
        return counts

    def topoSort(graph):
        res, queue = [], deque()
        # create hashmap {node: # of parents}
        counts = countParents(graph)
        # enqueue nodes with 0 parents
        for node in counts:
            if counts[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            res.append(node)
            # for all node's children, subtract 1 from parent count
            for child in graph[node]:
                counts[child] -= 1
                # enqueue parent counts that drop to 0
                if counts[child] == 0:
                    queue.append(child)
        # return topo sort list if we include all nodes, else invalid
        return res if len(graph) == len(res) else None

    def scheduleTasks(tasks: List[str], requirements: List[List[str]]) -> List[str]:
        # create { task: children }
        graph = {t: [] for t in tasks}
        # a needs to be completed befoer b
        for a, b in requirements:
            graph[a].append(b)
        return ttopoSortopo(graph)

"""
444. Sequence Reconstruction (Medium)
Leet: https://leetcode.com/problems/sequence-reconstruction/
Code: https://github.com/onlypham/tangents

Problem: Determine whether original is the only sequence that can be reconstructed from seqs. Reconstruction means building the shortest sequence so that all sequences in seqs are subsequences of it. 
Input: org (N), seqs (M)
Output: True if only one sequence reconstructed from seqs and == org

Framework: Topological Sort
Giveaways: We see that we must find an ordering of nodes ("numbers") such that every node appears before all the nodes it points to. Parent comes before its children. The seqs give us a graph such that: [1, 2, 3] implies we have edges 1->2 and 2->3
Concept: Kahn's Algorithm == BFS. We keep nodes with no parents in a queue, pop top of queue, subtract 1 from parent count for all its children, then push any new nodes with 0 parent count. The KEY is we do not want the queue to have more than two options at any one time (since this implies we do not have one unique decision to make org)

Process: 

    1. Create a graph of { parent: set(children) }
    2. Create hashmap of { node: # of parents }
    3. Enqueue all nodes with 0 parents. Iterate through queue.
        a. Ensure queue only has one item at a time -> unique ordering
        b. Pop node & decrement count of node's children's parent count.
        c. Append all nodes with parent count 0 to queue.
    4. Return if seq == org

Complexity: 
Time: O(M+N) since this is the number of edges & nodes we must traverse
Space: 
"""

class Solution:

    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        def countParents(graph):
            counts = { node: 0 for node in graph }
            for parent in graph:
                for node in graph[parent]:
                    counts[node] += 1
            return counts
        def topoSort(graph):
            seq = []
            queue = deque()
            # create hashmap {node: # of parents}
            counts = countParents(graph)
            # enqueue nodes with 0 parents
            for node in counts:
                if counts[node] == 0:
                    queue.append(node)
            while queue:
                # ENSURE queue only has one item
                if len(queue) > 1:
                    return False
                node = queue.popleft()
                seq.append(node)
                for child in graph[node]:
                    counts[child] -= 1
                    if counts[child] == 0:
                        queue.append(child)
            return seq == org
        # create graph with N nodes
        graph = { node: set() for node in range(len(org)) }
        for seq in seqs:
            parent, child = seq[0], seq[1]
            graph[parent].add(child)
        return topoSort(graph)

"""
269. Alien Dictionary (Hard)
Leet: https://leetcode.com/problems/alien-dictionary/
Code: https://github.com/onlypham/tangents

Problem: There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language. Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. 
Input: words
Output: string (empty "" if no solution), may be multiple solutions

Framework: Topological Sort
Giveaways: We see the notion of lexicographical ordering lends well to node orderings such that if c1 < c2 then we must have c1 -> c2 in the graph. Once we create a graph representation, we can use a topological sort to find a valid ordering. 
Concept: Only consider adjacent words. For each pair, find the first different character c1 != c2. In the graph, create c1 -> c2. Ensure we don't have the same starting prefix but len(w1) > len(w2), ie. [abc, ab]. Then perform a topological sort. We keep nodes with no parents in a queue, pop top of queue, subtract 1 from parent count for all its children, then push any new nodes with 0 parent count. If we have any non-zero parent counts after the sort, there must be a cycle, which results in an invalid ordering.

Process: 

    1. Create a graph of { parent char : set(children) }
    2. For adjacent words, add the first differing character to the graph.
    3. Topological Sort
        a. Create parent counts for all the nodes.
        b. Enqueue all nodes with 0 parents.
        c. Iterate through the queue.
            i. Pop character & decrement count of all children's parent count.
            ii. Append all nodes with parent count 0 to queue.
        d. If any more non-zero parent counts, return None.
    4. Return appropriate string.

Complexity: 
Time: O(distinct chars in words) since that will dictate the size of our graph
Space: 
"""

class Solution:

    def alienOrder(self, words: List[str]) -> str:
        def countParents(graph):
            counts = { node: 0 for node in graph }
            for parent in graph:
                for node in graph[parent]:
                    counts[node] += 1
            return counts
        def topoSort(graph):
            res, queue = [], deque()
            # create hashmap { node: # of parents} 
            counts = countParents(graph)
            # enqueue nodes with 0 parents
            for node in counts:
                if counts[node] == 0:
                    queue.append(node)
            while queue:
                node = queue.popleft()
                res.append(node)
                for child in graph[node]:
                    counts[child] -= 1
                    if counts[child] == 0:
                        queue.append(child)
            # ensure we do not have any non-zero parent counts
            for count in counts.values():
                if count != 0:
                    return None
            return res
        # hashmap for { parent char : children }
        graph = { c : set() for w in words for c in w }
        # only consider adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            # same starting prefix but w1 > w2 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                # find first differing character
                if w1[j] != w2[j]:
                    # letter in word1 is the parent to letter in word2
                    graph[w1[j].add(w2[j])]
                    break
        s = topoSort(graph)
        if s is None:
            return ""
        return "".join(s)

"""
207. Course Schedule (Medium)
Leet: https://leetcode.com/problems/course-schedule/
Code: https://github.com/onlypham/tangents

Problem: There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
Input: numCourses, prerequisites
Output: True if can finish all course, else false

Framework: DFS
Giveaways: Though the cycles can be detected using BFS, we can also use DFS. 
Concept: This dependency relationship can be thought of as a directed graph where course -> prereq. Any impossible course schedules will have a cycle. To detect cycles via DFS, we mark each node in our DFS path as visiting. It becomes visited if it has no children or we've visited all its children. If we come back to a node that is in a visiting state, we have a cycle.

Process: 

    1. Create a graph of { course : set(prereq) }
    2. Create a states list for all courese & set to TO_VISIT.
    3. Starting from every node, ensure DFS does not return False.
        a. In DFS recurisve call...
            i. Set node's state to VISITING.
            ii. For each neighbor, if we visit
                A. a VISITED node, continue
                B. a VISITING node, cycle detected, return False
                C. recursively DFS on each neighbor -> ensure no cycles
            iii. Mark node as VISITED & return True.

Complexity: 
Time: O(N+M) or the number of nodes + edges in our graph
Space: 
"""

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(start, states):
            # let 1 == VISTING
            states[start] = 1
            for node in graph[start]:
                # let 2 == VISITED
                if states[node] == 2:
                    continue
                # if revisiting a VISITING node -> cycle
                if states[node] == 1:
                    return False
                # if neighbors found a cycle -> cycle
                if not dfs(node, states):
                    return False
            # mark as visited
            states[start] = 2
            return True
        # build graph
        graph = defaultdict(set)
        for course, prereq in prerequisites:
            graph[course].add(prereq)
        # let 0 == TO_VISIT
        states = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not dfs(i, states):
                return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = { i:[] for i in range(numCourses) }
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # all course along current DFS path
        visit = set()
        def dfs(course):
            # if we visit a visited set
            if course in visit:
                return False
            # if course has no prereq, it can be completed
            if graph[course] == []:
                return True
            # currently visiting course
            visit.add(course)
            for prereq in graph[course]:
                # if it returns False (course can't be completed), we return False
                if not dfs(prereq):
                    return False
            visit.remove(course)
            graph[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

"""
Shortest-Path Faster Algorithm (SPFA)

A BFS variant where instead of checking if neighbor has been visited, we see if we can improve our distance by checking neighbors & pushing nodes into queue if it does. We get a complexity of O(N*M) where n is # of nodes & m is # of edges

Dijkstra's Algorithm

Uses priority queue to store nodes by distance from root node. Popping from the queue, we know this has the current shortest distance from root to node. We get a complexity of O(NlogE). Optimizations: skip elements in priority queue with greater distance than what currently in array OR terminate once we reach destination node.

function Dijkstra(Graph, source):
    dist[source] ← 0
    create vertex priority queue Q
    for each vertex v in Graph:
        if v ≠ source
            dist[v] ← INFINITY
            prev[v] ← UNDEFINED
        Q.add_with_priority(v, dist[v])
    while Q is not empty:
        u ← Q.extract_min()   // remove best vertex
        for each neighbor v of u:
            alt ← dist[u] + weight(u, v)
            if alt < dist[v]
                dist[v] ← alt
                prev[v] ← u
                Q.decrease_priority(v, alt)
    return dist, prev

Uniform Cost Search

Instead of adding all vertices to priority queue at beginning, we can add new vertices as we check the neighbors. This is better when we have a large graph that doesn't fit in memory. 
"""

from heapq import heappush, heappop

class Solution:

    def shortestPath(graph: List[List[Tuple[int, int]]], a: int, b: int) -> int:
        def bfs(root: int, target: int):
            queue = deque([root])
            distance = [float('inf')] * len(graph)
            distance[root] = 0
            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    # only update distance to neighbor if we find a shorter distance
                    if distance[neighbor] <= distance[node] + weight:
                        continue
                    # append neighbor to the graph & update distance
                    queue.append(neighbor)
                    distance[neighbor] = distance[node] + weight
            return distance[target]
        return -1 if bfs(a, b) == float('inf') else bfs(a, b)

    def dijkstra(graph: List[List[Tuple[int, int]]], a: int, b: int) -> int:
        def bfs(root: int, target: int):
            # HEAP = ( distance, node index )
            queue = [(0, root)]
            distances = []
            for i in range(len(graph)):
                if i == root:
                    distances.append(0)
                    heappush(queue, (0, i))
                else:
                    distances.append(float('inf'))
                    heappush(queue, (float('inf'), i))
            while queue:
                _, node = heappop(queue)
                for neighbor, weight in graph[node]:
                    d = distances[node] + weight
                    if distances[neighbor] <= d:
                        continue
                    heappush(queue, (d, neighbor))
                    distances[neighbor] = d
            return distances[target]
        return -1 if bfs(a, b) == float('inf') else bfs(a, b)

    def uniformCostSearch(graph: List[List[Tuple[int, int]]], a: int, b: int) -> int:
        def bfs(root: int, target: int):
            # HEAP = ( distance, node index )
            queue = [(0, root)]
            distances = [float('inf')] * len(graph)
            distances[root] = 0
            while queue:
                distance, node = heappop(queue)
                # terminate once we reach target
                if node == target:
                    return distance
                # skip if distance greater than current optimum
                if distance > distances[node]:
                    continue
                for neighbor, weight in graph[node]:
                    d = distances[node] + weight
                    if distances[neighbor] <= d:
                        continue
                    heappush(queue, (d, neighbor))
                    distances[neighbor] = d
            return distances[target]
        return -1 if bfs(a, b) == float('inf') else bfs(a, b)

"""
Minimum Spanning Tree

Generating the tree with smallest total weight by selecting edges from a graph to include every node. Greedy solution of choosing smallest weighted edge.

Kruskal's Algorithm

Choose smallest weigthed edge in the graph, consistently growing the tree by one edge. We get a complexity of O(MlogM) where M denotes the number of edges. This is since we must sort the graph initially then we iterate through and do either a union/find operation at every edge (logM).


    1. Sort the edges from lowest to highest using any method
    2. Try every edge, as long as the 2 nodes that the edge connects are not currently connected, we add new edge.
    3. Repeat step 2, until we have n - 1 edges.

Prim's Algorithm

    1. Start at any node
    2. Push all neighbor edges of the node into Priority Queue
    3. If edge leads to unvisited node, add edge to tree & push new neighbor edges. 
    4. Repeat step 3, until we have n - 1 edges.
"""
