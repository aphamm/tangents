"""
BACKTRACKNG.PY

Concept: We have a set of choices we wish to explore. At each choice, we are constrained in which choices we can make. We make choices until we reach a goal. If we reach a goal, record. Else, backtrack by undoing the choice that we made to get there.

Combinatorial Search == DFS on State-Space tree
    - Each node: state we can reach in combinatorial search
    - Leaf: solutions to the problem 

Identify State: what we need to have to know we reached a solution
    - State to decide which child node to visit next & which ones to prune
    - ie. letter's already selected, numbers guessed, path taken

257. Binary Tree Paths (Easy)
46. Permutations (Medium)
17. Letter Combinations of a Phone Number (Medium)
509. Fibonacci Number (Easy)
139. Word Break (Medium)
91. Decode Ways (Medium)
131. Palindrome Partitioning (Medium)
39. Combination Sum (Medium)
39. Subsets (Medium)
"""

class Template:

    def backTrack(res, state):
        # state == solution
        if ( GOAL == REACHED ):
            res.append(solution) # report state
            return
        for choice in choices:
            # potential solution 
            if ( choice[i] == valid ):
                make(choice[i]) # state.add(choice)
                backTrack(res, state)
                undo(choice[i]) # backtrack

"""
257. Binary Tree Paths (Easy)
Leet: https://leetcode.com/problems/binary-tree-paths/
Code: https://github.com/onlypham/tangents

Problem: Given the root of a binary tree, return all root-to-leaf paths in any order.
Input: root
Output: List of all paths from root to leaf
Other: Each element should be a string separated by "->"

Framework: Backtracking
Giveaways: We have a set of choices we wish to explore. At each choice, we are constrained by a node's children. Our goal is to reach a leaf.
Big Picture: We wish to explore all paths of the tree. If both children are null, we backtrack since we are at a leaf.

Choice: Traverse down the tree.
Constraints: We can only explore the node's children. 
Goals: We reach a leaf once 

State: Maintain a list to represent current path.
Process: 

    1. If leaf reached, append final path to result & return.
    2. Else, append current node's value & explore left/right children.
        a. Backtrack after exploring by removing current node's value from path.

Return: none

Complexity: 
Time: O(N) since we visit every node once.
Space: O(logN) since for traversing a single path, we only require logN (height of tree) recursive calls.
"""

class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # path defined as a list of node values
        def dfs(root, path, res):   
            # base case: if both children null, we reached a leaf
            if not root.left and not root.right:
                # if root of tree has no children, just append root's value
                if len(path) == 0:
                    res.append(str(root.val))
                    return
                res.append('->'.join(path) + '->' + str(root.val))
                return
            # add current node to our explored path
            path.append(str(root.val))
            if root.left:
                dfs(root.left, path, res)
            if root.right:
                dfs(root.right, path, res)
            # backtrack
            path.pop()
        res = []
        if root:
            dfs(root, [], res)
        return res

    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:  
        # if empty tree, return empty list
        if not root:
            return []
        # if root/leaf node has no children, just return root value
        if not root.left and not root.right:
            return [str(root.val)]
        # add current node's value plus '->' and append ALL paths in left/right subtree
        paths = [(str(root.val) + '->') + path for path in self.binaryTreePaths(root.left)]
        paths += [(str(root.val) + '->') + path for path in self.binaryTreePaths(root.right)]
        return paths

"""
46. Permutations (Medium)
Leet: https://leetcode.com/problems/permutations/
Code: https://github.com/onlypham/tangents

Problem: Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Input: nums
Output: List of all permutations
Other: Return as a List of Lists

Framework: Backtracking
Giveaways: We have a set of choices we wish to explore. At each choice, we are constrained by the letters we have already used. Our goal is to use all the numbers to reach a complete permutation.
Big Picture: We wish to explore all paths given by nums. We choose a number, follow all its paths that reach a complete permutation and then backtrack by unchoosing that number.

Choice: Choose a number in num.
Constraints: We cannot select a number that has already been chosen.
Goals: We want to use up all the numbers in num.

State: Maintain a list to represent current path taken.
Process: 

    1. If all numbers in num used, append final path to result & return.
    2. Else, choose a number. Append to path & explore that choice.
        a. Backtrack after exploring that specific number.

Return: none

Complexity: 
Time: O(N * N!) since there are N! permutations that take N time to traverse
Space: O(N) since for traversing a single permutation, we only require N recursive calls.
"""

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return # backtrack
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)   

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            # if path uses all numbers
            if len(path) == len(nums):
                # make sure to copy list!
                res.append(path[:]) 
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                # add letter to permutation & mark letter used
                path.append(num)
                used[i] = True
                dfs(path, used, res)
                # backtrack
                path.pop()
                used[i] = False
        res = []
        # state: keep track of all used numbers
        dfs([], [False] * len(nums), res)
        return res

"""
17. Letter Combinations of a Phone Number (Medium)
Leet: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Code: https://github.com/onlypham/tangents

Problem: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
Input: digits
Output: List of all permutations
Other: Each permutation represented as a string

Framework: Backtracking
Giveaways: We have a set of choices we wish to explore. At each choice, we are constrained by the number we are given which allows us to choose certain letters. Our goal is to use all the numbers to reach a complete permutation.
Big Picture: We wish to explore all paths given by digits. We get our number and see which letters are possible. We choose a letter and follow all its paths that reach a complete permutation then backtrack.

Choice: Choose a letter in from available letters.
Constraints: Out letter is constraint by the digit in digits.
Goals: We want to use up all the digits in digits.

State: Maintain a list to represent current path taken.
Process: 

    1. If all digits in digits used, append final path to result & return.
    2. Else, get the next number. Choose a letter from available letters.
        a. Append to path & explore that choice.
        b. Backtrack after exploring that specific letter.

Return: none

Complexity: 
Time: O(N * N!) since there are N! permutations that take N time to traverse
Space: O(N) since for traversing a single permutation, we only require N recursive calls.
"""

class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        # if no digits just return empty list
        if len(digits) == 0:
            return res
        self.dfs(digits, dic, '', res)
        return res
    
    def dfs(self, nums, dic, path, res):
        # goal reached when path is length of nums
        if len(path) >= len(nums):
            res.append(path)
            return
        # look at next number & explore all new possible letters
        number = nums[len(path)]
        for letter in dic[number]:
            self.dfs(nums, dic, path + letter, res)

    def letterCombinations2(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(path, res):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            number = digits[len(path)]
            for letter in dic[number]:
                path.append(letter)
                dfs(path, res)
                path.pop()
        res = []
        if len(digits) == 0:
            return res
        dfs([], res)
        return res

"""
509. Fibonacci Number (Easy)
Leet: https://leetcode.com/problems/fibonacci-number/submissions/
Code: https://github.com/onlypham/tangents

Problem: Given n, calculate F(n).
Input: n
Output: Computed Fibonacci sequence
Other: F(0) = 0, F(1) = 1

Framework: Memoization
Giveaways: We have many of the same exact (input-wise) recursive calls. Use this when we have a combinatorial problem with large repeated state-space tree branches.
Big Picture: Save previous function call results to dictionary ("memo"). When we do same exact call again, we simply read from our memo.

Process: 

    1. Handle base case.
    2. See if previous calculation stored in Memo.
    3. Else, perform calculation & store value in memo.

Return: F(n)

Complexity: 
Time: O(N) since we multiply the # of recursive calls by time it takes for each call. We can only reach the code after the "memo check" n times (since we our parameter must be less than initial n). When this happens we call fib two times. We add one for the initial call to fib. The time for each call is constant time. So we get O(2N+1) x O(1) = O(N)
Space: O(N) since we only require N recursive calls.
"""

class Solution:

    memo = {}
    def fib(self, n: int) -> int:
        # if previous calculation stored in memo
        if n in self.memo:
            return self.memo[n]
        # base case
        if n == 0 or n == 1:
            return n
        # otherwise, perform calculation & save value in memo
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
        
"""
139. Word Break (Medium)
Leet: https://leetcode.com/problems/word-break/
Code: https://github.com/onlypham/tangents

Problem: Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Input: s, wordDict
Output: True/False
Other: Words in the dictionary can be used multiple times.

Framework: Memoization
Giveaways: We repeatedly have to find words that come one after another. Once we find a valid first word that is followed by valid second word, no matter what happens in the second recursive call, we should save the fact that we found the first word. 
Big Picture: Save previous function call results to dictionary ("memo"). When we do same exact call again, we simply read from our memo.

Process: 

    1. Return true if we match all letters in s
    2. See if any word was found at index by looking at Memo.
    3. Else, search for word & store in Memo.

Return: True/False

Complexity: 
Time: O(s * w * max(w[i])) where w is length of wordDict and max(w[i])) is maximal possible word length
Space: 
"""

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp represents does a word end at this index
        dp = [True] + [False] * len(s)
        # dp[0] == True since it is the base case before the first word
        for i in range(1, len(s) + 1):
            for word in wordDict:
                # check if current word ends here
                if s[:i].endswith(word):
                    # check if a word ended before the start of current word
                    dp[i] |= dp[i-len(word)]
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(index):
            # return true if we match all letters in s
            if index == len(s):
                return True
            # check if we have the result, if so return True
            if index in memo:
                return memo[index]
            res = False
            for word in wordDict:
                # check if a word starts here
                if s[index:].startswith(word):
                    # find a word that starts after our
                    # current word & save result if we do
                    if dfs(index + len(word)):
                        res = True
                        break
            # save result that a word starts at index
            memo[index] = res
            return res
        return dfs(0)

"""
91. Decode Ways (Medium)
Leet: https://leetcode.com/problems/decode-ways/
Code: https://github.com/onlypham/tangents

Problem: Given a string s containing only digits, return the number of ways to decode it.
Input: s
Output: int
Other: Mappings include: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

Framework: Memoization
Giveaways: We do a DFS of state space tree where we can either "eat" up one OR two digits. However, we see the same subtree occurs multiple times.
Big Picture: Save previous function call results to dictionary ("memo"). When we do same exact call again, we simply read from our memo.

Process: 

    1. Return 1 if we reach the end of the string. Decoding found!
    2. See if any word was found at index by looking at Memo.
    3. Else, recursively call dfs after "eating" 1/2 digits.

Return: # of decodings

Complexity: 
Time: O(N) since we minimize forking potential
Space: O(N) since we use a max call stack depth of N
"""

class Solution:

    def numDecodings(self, s: str) -> int:
        def dfs(index, memo):
            # check memo to see if we already have result
            if index in memo:
                return memo[index]
            # if we reach the end of the string, we found a valid decoding
            if index == len(s):
                return 1
            count = 0
            # add number of valid decodings if we "eat" one digit
            if 0 < int(s[index:index+1]) <= 9:
			    count += dfs(index+1, memo)
            # add number of valid decodings if we "eat" two digits
            if 10 <= int(s[index:index+2]) <= 26:
                count += dfs(index+2, memo)
            memo[index] = count
            return count
        return dfs(0, {})

"""
131. Palindrome Partitioning (Medium)
Leet: https://leetcode.com/problems/palindrome-partitioning/
Code: https://github.com/onlypham/tangents

Problem: Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
Input: s
Output: List of Lists of partitions
Other: A palindrome string is a string that reads the same backward as forward.

Framework: Backtracking
Giveaways: Once we find a palindrome, we will work backwards to find more palindromes and append if valid path.
Big Picture: Do not branch out when subarray is not a palindrome (Prune)

Process: 

    1. Append path to result if we reach the end of the string.
    2. For all subarrays from index + 1 to end, find if valid palindrome.
    3. If valid, recursively call dfs while appending palindrome to path.

Return: none

Complexity: 
Time: O(2^N)
Space: 
"""

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(index, path):
            # if we reach the end of the string
            if index == len(s):
                res.append(path[:])
            for i in range(index + 1, len(s) + 1):
                pal = s[index:i]
                if self.isPalindrome(pal):
                    dfs(i, path + [pal])
        dfs(0, [])
        return res
    
    def isPalindrome(self, word):
        return word == word[::-1]

"""
39. Combination Sum (Medium)
Leet: https://leetcode.com/problems/combination-sum/
Code: https://github.com/onlypham/tangents

Problem: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
Input: candidates, target
Output: List of Lists of unique combinations
Other: We want combinations, not permutations!

Framework: Backtracking
Giveaways: We have a set of choices we wish to explore. At each choice, we are constrained by the the index i. Once we branch in the tree, we cannot use any elements in the array before index i. Our goal is to reach the target.
Big Picture: We wish to explore all paths of canidates to reach the target. If we overshoot the number, we backtrack by unchoosing a canidate.

Choice: Choose a number in candidates.
Constraints: The candidate must be after index i. It also cannot go over target.
Goals: We want to sum the candidates up to reach target.

State: 
    
    i: to limit available canidates to choose from.
    path: record the current path taken
    total: compute the current sum

Process: 

    1. If target achived, append final path to result & return.
    2. Check if we are over target or reached the end of our candidates.
    3. Append candidate[i] to path & recursively call dfs.
        a. Backtrack after exploring by removing candidate[i] from path.

Return: none

Complexity: 
Time: O(N^(Target/min(candidates))) where N is the number of candidates. 
Space: 
"""

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, total):
            # if target reached, append path to result
            if total == target:
                res.append(path[:])
                return
            # return if target > target OR we run out of candidates
            if total > target or i >= len(candidates):
                return
            # first explore path of using candidate[i]
            path.append(candidates[i])
            dfs(i, path, total + candidates[i])
            # backtrack: NO MORE using candidate[i] ever again
            path.pop()
            dfs(i + 1, path, total)
        dfs(0, [], 0)
        return res

"""
39. Subsets (Medium)
Leet: https://leetcode.com/problems/subsets/
Code: https://github.com/onlypham/tangents

Problem: Given an integer array nums of unique elements, return all possible subsets (the power set).
Input: nums
Output: List of Lists of unique subsets
Other: We want combinations, not permutations!

Framework: Backtracking
Giveaways: We have a set of choices we wish to explore. At each choice, we are constrained by index i.Once we branch in the tree, we cannot use any elements in nums before index i. Our goal is to run out of possible numbers to include in our subset.
Big Picture: We wish to explore all paths of numbers so that we run out of possible numbers to use. Once we explore using a number in our subset, we backtrack by unchoosing that number and never using that number again.

Choice: Choose a number in nums.
Constraints: The candidate must be after index i.
Goals: We want to out of numbers in nums.

State: 
    
    i: to limit available canidates to choose from.
    path: record the current path taken

Process: 

    1. If we run out of nums, append final path to result & return.
    2. Append nums[i] to path & recursively call dfs.
        a. Backtrack after exploring by removing nums[i] from path.

Return: none

Complexity: 
Time: O(2^N)
Space: 
"""

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, path):
            # add path to result once we run our of numbers !
            if i >= len(nums):
                res.append(path[:])
                return
            # first explore the path of adding nums[i] to subset
            path.append(nums[i])
            dfs(i + 1, path)
            # backtrack: nums[i] can NEVER be in a subset again
            path.pop()
            dfs(i + 1, path)
        dfs(0, [])
        return res
    