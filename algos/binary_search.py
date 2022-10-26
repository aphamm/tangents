"""
BINARY_SEARCH.PY

Concept: think about binary decisions to shrink search range
Think: "how can i apply a filter to an array & imagine an array of booleans"

704. Binary Search (Easy)
000. First True in Sorted Boolean Array
000. First Element Bigger than Target in Sorted Array
000. First Occurence of Element in Sorted Array
69. Sqrt(x) (Easy)
153. Find Minimum in Rotated Sorted Array
162. Find Peak Element (Medium)
1011. Capacity To Ship Packages Within D Days
000. Minimum Reading Time For Workers
"""

"""
704. Binary Search (Easy)
Leet: https://leetcode.com/problems/binary-search/
Code: https://github.com/onlypham/tangents

Problem: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
Input: nums -> [1, 2, *3*, 4, 8], 3
Output: index -> 2
Other: You must write an algorithm with O(log n) runtime complexity.

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: See if midpoint is our target. If the target is smaller, search the left subarray, else right. Continue until target found.

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # ensure that we allow left == right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # oops, target is smaller, so we want a smaller value
            # throw away right half of array
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

"""
000. First True in Sorted Boolean Array
Code: https://github.com/onlypham/tangents

Input: nums -> [False, False, *True*, True, True]
Output: index -> 2

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {binarySearch} but update index everytime True found

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def firstTrue(self, nums: List[bool]) -> int:
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            # we've found an earlier True !!
            if nums[mid]:
                index = mid 
                # remove current True from search
                right = mid - 1 
            else:
                left = mid + 1
        return index

"""
000. First Element Bigger than Target in Sorted Array
Code: https://github.com/onlypham/tangents

Input: nums
Output: index

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {firstTrue} after applying (nums[mid] >= target) filter

    [2, 3, 4, 5, 6, 8, 9] target == 7
    [F, F, F, F, F, T, T] after applying (nums[mid] >= 7) filter
    reduces to {firstTrue} == value of left after loop

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def firstElement(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # evaluates to True given our filter
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

"""
000. First Occurence of Element in Sorted Array
Code: https://github.com/onlypham/tangents

Input: nums
Output: index

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {firstTrue} but only save index when == target

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def firstOccurrence(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            # only save index if arr[mid] == target
            if nums[mid] == target:
                index = mid
                right = mid - 1
            # oops, target is smaller, so we want a smaller value
            # throw away right half of array
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return index

"""
69. Sqrt(x) (Easy)
Leet: https://leetcode.com/problems/sqrtx/
Code: https://github.com/onlypham/tangents

Input: x
Output: int == floor(squareRoot)

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {lastFalse} after applying (mid * mid > n) filter

    [1, 2, 3, 4, 5, 6, 7, 8] given n == 8, imagine list of size 8
    [F, F, T, T, T, T, T, T] after applying (mid * mid > 8) filter
    reduces to {lastFalse} == right index

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        # after loop, right will point to last False (round down)
        return right

"""
153. Find Minimum in Rotated Sorted Array (Medium)
Leet: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Code: https://github.com/onlypham/tangents

Input: nums
Output: element

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {firstTrue} after applying (arr[mid] <= arr[-1]) filter

    [4, 5, 6, 7, 8, 1, 2, 3] notice arr[-1] == 3
    [F, F, F, F, F, T, T, T] after applying (arr[mid] <= 3) filter
    reduces to {firstTrue} == left index

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        # wish to return element at FirstTrue
        return nums[left]

"""
162. Find Peak Element (Medium)
Leet: https://leetcode.com/problems/find-peak-element/
Code: https://github.com/onlypham/tangents

Input: nums -> [1, 2, 3, *4*, 3, 2, 1] 
    monotonically increase until peak then monotonically decrease
Output: index -> 3

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {firstTrue} after applying (nums[mid] > nums[mid+1]) filter

    *Ensure right = len(nums) - 2 to prevent index out of range* 
    [1, 2, 3, 4, 5, 4, 3, 2, 1] 
    [F, F, F, F, T, T, T, T, T] after applying (nums[mid] > nums[mid+1]) filter
    reduces to {firstTrue} == left index

Complexity:
Time: O(logN) since the search spaces reduces by 2 every recursive call.
Space: O(1)
"""

class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        # wish to return index at FirstTrue == left
        return left

"""
1011. Capacity To Ship Packages Within D Days (Medium)
Leet: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Code: https://github.com/onlypham/tangents

Input: weights, days -> [1, 2, 3, 4, 5], 5
Output: min_capacity -> 3

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {firstTrue} after applying (isFeasible) filter to range of capacities

    weights = [1, 2, 3, 4, 5] where days == 5

    first find min & max of possible capacities
        min ==  max(weights) -> one weight a day
        max == sum(weights) -> all weights in one day

    [5, 6, 7, 8, ..., 12, 13, 14, 15]
    [F, F, F, F, ..., F, T, T, T] after applying (isFeasible) filter
    reduces to {firstTrue} == left index

Complexity:
Time: O(NlogN) == isFeasible is O(N) * binary search is O(logN)
Space: O(1)
"""

class Solution:
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isFeasible(capacity):
            req_days = 1 # will always need at least one day
            cur_weight = 0 # current day weight acculumator
            for weight in weights: # iterate through all weights
                cur_weight += weight # always add next weight
                if cur_weight > capacity: # if over capacity
                    cur_weight = 0 # reset to 0
                    cur_weight += weight # add weight again
                    req_days += 1 # increment req_days
            return req_days <= days # see if at most days

        # O(N), treat left, right as left & right capacity bounds
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if isFeasible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

"""
000. Minimum Reading Time For Workers
Code: https://github.com/onlypham/tangents

Input: times, workers -> [7, 2, 5, 10, 8], 2
    each worker must read contigious subarrays
Output: min_time -> 18 (7+2+5 and 10+8)

Framework: Binary Search
Giveaways: Everytime we make a binary decision to shrink the search space. We will discard the left or right side of the array every iteration.
Idea: reduces to {firstTrue} after applying (isFeasible) filter to range of times

    times = [7, 2, 5, 10, 8] where workers == 2

    first find min & max of possible times
        min == max(times) -> at least longest newspaper 
        max == sum(times) -> one worker reads everything

    [10, 11, 12, 13, ..., 30, 31, 32]
    [F, F, F, F, F, ..., F, T, T, T] after applying (isFeasible) filter
    reduces to {firstTrue} == left index

Complexity:
Time: O(NlogN) == isReadable is O(N) * binary search is O(logN)
Space: O(1)
"""

class Solution:

    def minReadTime(self, times: List[int], workers: int) -> int:
        def isReadable(time_limit):
            # essentially same logic as is_feasible
            workers_needed = 1
            time = 0
            for time in times:
                time += times
                if time > time_limit:
                    time = 0
                    time += times
                    workers_needed += 1
            return workers_needed <= workers

        # O(N), treat left, right as left & right capacity bounds
        left, right  = max(times), sum(times)
        while left <= right:
            mid = (left + right) // 2 
            if isReadable(times, workers, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
