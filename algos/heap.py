"""
HEAP.PY

Priority Queue: an abstract data type implented with a heap

    1. Insert: item with key (keys == used to sort nodes)
    2. Delete_Min/Max (values == data we wish to store)

Max/Min Heap:

    1. an almost complete tree (traverse level order)
    2. (Min Heap) children's key is greater than parent

Useful: height guaranteed to be O(logN) & insert/delete O(logN)
Implemented: usually as an array. for node i, its children are (2i+1, 2i+2) and its parent is at floor((i-1)/2)

973. K Closest Points to Origin (Medium)
23. Merge k Sorted Lists (Hard)
378. Kth Smallest Element in a Sorted Matrix (Medium)
767. Reorganize String (Medium)
215. Kth Largest Element in an Array (Medium)
263. Ugly Number (Easy)
295. Find Median from Data Stream (Hard)
"""

class MinHeap:
    # insert operation
    def bubbleUp(node):
        while node.parent exist and node.parent.key > node.key:
            swap node and node.parent
            node = node.parent
    # delete operation: after moving last element to the top
    def bubbleDown(node):
        while node is not a leaf:
            if smallestChild < node:
                swap node and smallestChild
                node = smallestChild
            else:
                break

# python's default: min heap
import heapq
h = [] # heap == array/list
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (3, 'write code'))
heapq.heappop(h)

# max heap: reverse sign before pushing & reverse again when popping
h = []
heapq.heappush(h, -1 * 10)
heapq.heappush(h, -1 * 30)
-1 * heapq.heappop(h)

# create heap out of list: O(N)
arr = [3, 1, 2]
heapq.heapify(arr)

"""
973. K Closest Points to Origin (Medium)
Leet: https://leetcode.com/problems/k-closest-points-to-origin/
Code: https://github.com/onlypham/tangents

Problem: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
Input: points
Output: Return the k closest points.
Other: The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).

Framework: Heap
Giveaways: We need to order points based on a sorting criteria (key)
Big Picture: We will insert points into a heap based on their Euclidean distance from the origin.

Process: 

    1. Push points into a minHeap using distance as a key.
    2. Return the first k elements.

Complexity: 
Time: O(NlogN) since we insert into a heap N times
Space: O(N) since we store all N points
"""

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # push onto heap based on distance
        # no need to sqrt()
        for x, y in points:
            heapq.heappush(heap, (x ** 2 + y ** 2, x, y))
        # return the first k points of the heap
        return [(x,y) for (dist, x, y) in heap[0:k]]

"""
23. Merge k Sorted Lists (Hard)
Leet: https://leetcode.com/problems/merge-k-sorted-lists/
Code: https://github.com/onlypham/tangents

Problem: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Input: lists
Output: Return sorted linked-list

Framework: Heap
Giveaways: We need to keep track of sorted values.
Big Picture: We essentially iterate through all the linked lists storing the values in a minHeap. Then we pop the heap and construct the new linked list.

Process: 

    1. For all nodes in each list, push onto heap.
    2. For entire minHeap, pop and insert into node structure.

Complexity: 
Time: O(KNlogN) since we insert into a heap KN times
Space: O(KN) since each list may have N elements
"""

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode(-1)
        min_heap = []
        for list in lists:
            while list:
                heappush(min_heap, list.val)
                list = list.next
        while min_heap:
            node.next = ListNode(heappop(min_heap))
            node = node.next
        return dummy.next

"""
378. Kth Smallest Element in a Sorted Matrix (Medium)
Leet: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Code: https://github.com/onlypham/tangents

Problem: Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Input: matrix, k
Output: Return kth smallest
Other: You must find a solution with a memory complexity better than O(n2).

Framework: Heap
Giveaways: Just think of Merge Sort. We've already sorted M arrays and now need to merge them. We keep a heap of the smallest current element in each M arrays and thus will know exactly what to insert next sorted list. In this case, we wish to simply iterate to the next element to find the k+1 smallest element.
Big Picture: Create an initial heap with all elements in the first column. This essentially acts as a storing pointers for each row to determine the next lowest value in that row. We can then pop the value, i, j from the heap and then push the next element in the row (stop if we reach the end of the row).

Process:

    1. Heapify (value, i, j) the first element in each row (first column)
    2. For up to range k
        a. Pop from the heap
        b. Push the next element onto the heap, if exists
    3. Return res

Complexity: 
Time: O(N^2logN) since we might need to visit N*N elements and each time, we are inserting a new element into the heap.
Space: O(N) since we only store N elements at a time (one column)
"""

class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        cols = len(matrix[0])
        # create array consisting of first element in each row
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapify(heap)
        res = 0
        for _ in range(k):
            res, i, j = heappop(heap)
            # if we can, push the next element of the matrix in array
            if j + 1 < cols:
                heappush(heap, (matrix[i][j+1], i, j+1))
        return res

"""
767. Reorganize String (Medium)
Leet: https://leetcode.com/problems/reorganize-string/
Code: https://github.com/onlypham/tangents

Problem: Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Input: s
Output: Return any possible rearrangement of s or return "" if not possible.

Framework: Heap
Giveaways: We need to keep an updated tally of the two most frequent characters as we continually use them to create our string
Big Picture: Once we have the character frequencies, we will want to use the characters in pairs. This is 1) so we use up the high frequency characters first and 2) a character will not touch itself given the two characters in the pair are distinct. We will need a heap to keep a updating tally of the two most frequent characters

Process: 

    1. Create a maxHeap of (frequency, character)
    2. Pop from the heap in pairs
        a) Add the characters to the string
        b) If the frequency is >2, push back onto stack
    3. Check for any single elements left in the heap
        a) Ensure the frequency is NOT >2

Complexity: 
Time: O(N + KlogN) since heapify is O(N) and we need to pop K elements 
Space: O(N) since we store n elements. 
"""

class Solution:

    def reorganizeString(self, s: str) -> str:
        if not s: return ""
        heap = [(-freq, char) for char, freq in Counter(s).items()]
        heapify(heap)
        res = ""
        while len(heap) > 1:
            f1, c1 = heappop(heap)
            f2, c2 = heappop(heap)
            res += c1
            res += c2
            if -f1 > 1: heappush(heap, (f1+1, c1))
            if -f2 > 1: heappush(heap, (f2+1, c2))
        if heap:
            f, c = heap[0]
            if -f > 1: return ""
            else: res += c
        return res

"""
215. Kth Largest Element in an Array (Medium)
Leet: https://leetcode.com/problems/kth-largest-element-in-an-array/
Code: https://github.com/onlypham/tangents

Problem: Given an integer array nums and an integer k, return the kth largest element in the array.
Input: nums, k
Output: kth largest element
Other: You must solve it in O(n) time complexity.

Framework: Heap
Giveaways: Notice that once we heapify an array, we only need to pop k-1 times to return the Kth largest element. (We can also use Quick Sort but prone to more mistakes) 
Big Picture: Heapify the array & pop k-1 times.

Process: 

    1. Heapify nums into a minHeap.
    2. Pop k-1 times.
    3. Return -nums[0].

Complexity: 
Time: O(N + KlogN) since heapify is O(N) and we need to pop K elements 
Space: O(N) since we store n elements. 
"""

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapify(nums)
        for _ in range(k - 1):
            heappop(nums)
        return -nums[0]

"""
263. Ugly Number (Easy)
Leet: https://leetcode.com/problems/ugly-number/
Code: https://github.com/onlypham/tangents

Problem: Given an integer n, return true if n is an ugly number.
Input: n
Output: True if ugly else false
Other: An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Framework: Heap
Giveaways: For isUgly, simply keep dividing by 2, 3, 5 until n hopefully reaches 1. If it equals 1, it is ugly. For nthUgly, we start with 1 and then repeatedly multiply by all the factors to get more ugly numbers. However, we need to keep track of the lowest next ugly number to multiple 2, 3, 5 by. In this case, we use a heap.
Big Picture: For nthUgly, start with 1 in a minHeap. Pop the value, multiply it by all our factors, check if it was previously used, if not, push onto the heap. Repeat this process n times to get the nth ugly.

Process: (nthUgly)

    1. Start with a minHeap of just 1.
    2. For range (n-1)
        a. Pop the heap & multiply by every factor (2, 3, 5)
        b. If new ugly not used, add to used set & push to heap
    3. Return the next value in the heap.

Complexity: 
Time: O(N + KlogN) since heapify is O(N) and we need to pop K elements 
Space: O(N) since we store n elements. 
"""

class Solution:
    
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            # n is divisible by p AND n > 0 (comparison chain)
            while n % p == 0 < n:
                n /= p
        return n == 1

    def nthUgly(self, n: int) -> bool:
        uglies, heap, used = (2, 3, 5), [1], {1}
        for _ in range(n - 1):
            val = heappop(heap)
            for ugly in uglies:
                if val * ugly not in used:
                    used.add(val * ugly)
                    heappush(heap, val * ugly)
        return heap[0]

"""
295. Find Median from Data Stream (Hard)
Leet: https://leetcode.com/problems/find-median-from-data-stream/
Code: https://github.com/onlypham/tangents

Problem: Implement the MedianFinder class: 1) MedianFinder() initializes the MedianFinder object. 2) void addNum(int num) adds the integer num from the data stream to the data structure. 3) double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
Other: The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

Framework: Heap
Giveaways: We want to keep two piles of numbers. We will designate a small and big pile as the first/second pile. At all times, we want to know the biggest element of the first pile and the smallest element of the second pile. We will use a maxHeap and minHeap for the first/second pile respectively.
Big Picture: At all times, we will have at least N elements in the first pile and N OR N+1 in the second pile. If there are N elements in the second, we will just return the the average of the two piles (heap[0]). If there are N+1 elements in the second, we will return the second pile (heap[0]).

    1. Init two heaps.
    2. AddNum
        a) If heaps same length, we want to push to second pile.
            i) Including the newest element, find the biggest element in the first pile and push to second pile.
        b) If second has one more than first, we want to push to first pile.
            i) Including the newest element, find the smallest element in the second pile and push to first pile.
    3. FindMedian
        a) If both piles same length, return average
        b) If second is bigger by 1 element, return first element of second pile

Process: 

Complexity: 
Time: addNum O(logN) & findMedian O(1)
Space: O(N)
"""

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        first, second = self.heaps
        # heaps same length -> want to push to second
        if len(first) == len(second):
            max = -heappushpop(first, -num)
            heappush(second, max)
        else: # second has one more element -> want to push to first
            min = heappushpop(second, num)
            heappush(first, -min)

    def findMedian(self) -> float:
        first, second = self.heaps
        # if same length just return average
        if len(first) == len(second):
            return (-first[0] + second[0]) / 2
        return second[0]
        