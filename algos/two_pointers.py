"""
TWO_POINTERS.PY

Characteristics:

    1. Two moving pointers, moving same/different direction either dependently/indepdently while travering a structure
    2. A function that uses the pointed at elements.
    3. Moving Condition:  decide which pointer moves.
    4. A way to process the array when pointers are moved.

Classifications:

    1. Same direction (remove duplicate)
    2. Opposite direction (two sum sorted)
    3. Sliding Window (longest substring without repeating chars)
    4. Non-Arrays: any iterable structure like linked lists

26. Remove Duplicates from Sorted Array (Easy)
876. Middle of the Linked List (Easy)
167. Two Sum II - Input Array Is Sorted (Medium)
125. Valid Palindrome (Easy)
3. Longest Substring Without Repeating Characters (Medium)
438. Find All Anagrams in a String (Medium)
76. Minimum Window Substring (Hard)
560. Subarray Sum Equals K (Medium)
141. Linked List Cycle (Easy)
1537. Get the Maximum Score (Hard)
42. Trapping Rain Water (Hard)
"""


"""
26. Remove Duplicates from Sorted Array (Easy)
Leet: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Code: https://github.com/onlypham/tangents

Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Input: nums
Output: Return k after placing the final result in the first k slots of nums.
Other: You must do this by modifying the input array in-place with O(1) extra memory.

Framework: Two Pointers (Same Direction)
Giveaways: We need two pointers: 1) to keep the index of where to insert the next non-duplicate value and 2) to find such non-duplicate values.
Big Picture: We will use the "slow" pointer to replace elements in place. Whenever the "fast" pointer visits a new element, we will increment the slow pointer and in-place insert this new element.

Process: 

    1. Start both pointers at the start.
    2. Iterate "fast" pointer to the end.
        a. If "fast" reaches a new element
            i. Increment the "slow" pointer & insert new element
    3. Return slow + 1 as this is the number of distinct elements.

Complexity: 
Time: O(N) since we will iterate through the entire array
Space: O(1) as we do not have to save any additional values
"""

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        # iterate fast until the end
        for fast in range(len(nums)):
            # once fast reaches a new element, increment slow & add element
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1

"""
876. Middle of the Linked List (Easy)
Leet: https://leetcode.com/problems/middle-of-the-linked-list/
Code: https://github.com/onlypham/tangents

Problem: Given the head of a singly linked list, return the middle node of the linked list.
Input: head
Output: Return middle node.
Other: If there are two middle nodes, return the second middle node.

Framework: Two Pointers (Same Direction)
Giveaways: We have two pointers that move in the same direction but one will move twice as fast.
Big Picture: We will have two pointers that iterate through the same linked list where one will travel twice as fast as the other. Once the fast one reaches the end, the slow one will be at the middle.

Process: 

    1. Start both pointers at the start.
    2. Iterate "fast" pointer to the end.
        a. If "fast" reaches a new element
            i. Increment the "slow" pointer & insert new element
    3. Return slow + 1 as this is the number of distinct elements.

Complexity: 
Time: O(N) since we will iterate through the entire array
Space: O(1) as we do not have to save any additional values
"""

class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            # move "fast" pointer twice as fast
            fast = fast.next.next
            slow = slow.next
        return slow

"""
876. Middle of the Linked List (Easy)
Leet: https://leetcode.com/problems/move-zeroes/
Code: https://github.com/onlypham/tangents

Problem: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Input: nums
Output: 
Other: Note that you must do this in-place without making a copy of the array.

Framework: Two Pointers (Same Direction)
Giveaways: We need two pointers: 1) to keep the index of where to insert the next non-zero element 2) to find such non-zero elements.
Big Picture: We will use the "slow" pointer to keep the index of where to place the non-zero element. Whenever the "fast" pointer finds a new non-zero element, we will increment the slow pointer and in-place insert this new element,

Process: 

    1. Start both pointers at the head.
    2. Iterate the fast pointer to the end (ensuring we find all non-zero nums)
        a. Whenever we find a non-zero element. Swap with "slow" pointer
        b. Slow pointer will represent where to insert next non-zero element, so increment after swap.

Complexity: 
Time: O(N) since we will iterate through the entire array.
Space: O(1) as we do not have to save any additional values
"""

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # increment "slow" pointer to be in position to insert 
                # the next non-zero number that "fast" finds
                slow += 1
            
"""
167. Two Sum II - Input Array Is Sorted (Medium)
Leet: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Code: https://github.com/onlypham/tangents

Problem: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Input: numbers, target
Output: [index1 + 1, index2 + 1]
Other: The tests are generated such that there is exactly one solution. You may not use the same element twice. Your solution must use only constant extra space.

Framework: Two Pointers (Opposite Direction)
Giveaways: We need two pointers: 1) to reference the smallest viable element and 2) to reference the biggest viable element
Big Picture: Start with two pointers at both ends of the array (smallest + largest values). If the sum of the two pointers is less than our target, we know that we will not use the left pointer since this value PLUS the max cannot even reach our target. Same logic applies to moving the right pointer. Iterate until we find the target. 

Process: 

    1. Start both pointers at the left/right ends of the array.
    2. If target reached, return indices.
        a. Move left pointer inwards if the sum of the two pointers is less than the target.
        b. Move right pointer inwards if the sum of the two pointers is greater than the target.

Complexity: 
Time: O(N) since we will iterate through the entire array.
Space: O(1) as we do not have to save any additional values
"""

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            # we found the target sum!
            if sum == target:
                return [left, right]
            # if we are less than target, we know we WON'T
            # use left's element to reach the target
            if sum < target:
                left += 1
            else:
                right -= 1

"""
125. Valid Palindrome (Easy)
Leet: https://leetcode.com/problems/valid-palindrome/
Code: https://github.com/onlypham/tangents

Problem: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Input: s
Output: Return True if palindrome, else False

Framework: Two Pointers (Opposite Direction)
Giveaways: We need two pointers: 1) to reference the left end of the string and 2) to reference the right end of ths string
Big Picture: Start with two pointers at both ends of the string. Move the left/right pointers inwards until we reach a valid alphanumeric. Do a case-insensitive comparison and return False if different. 

Process: 

    1. Start both pointers at the left/right ends of the array.
    2. If left/rigth points reach each other, return True.
        a. Move left/right pointers inwards until we reach valid isalnum() character.
        b. Return false if a case-insensitive comparison are not the same.

Complexity: 
Time: O(N) since we will iterate through the entire array.
Space: O(1) as we do not have to save any additional values
"""

class Solution:

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # ensure bother pointers reference valid alphanumeric
            while left < right and not s[left].isalnum(): 
                left += 1
            while left < right and not s[right].isalnum(): 
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

"""
3. Longest Substring Without Repeating Characters (Medium)
Leet: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Code: https://github.com/onlypham/tangents

Problem: Given a string s, find the length of the longest substring without repeating characters.
Input: s
Output: Return longest substring length (int)

Framework: Two Pointers (Sliding Window)
Giveaways: We need two pointers: 1) to reference the left end of our current substring 2) to reference the right end of our current substring
Big Picture: Move the right pointer to increase the range of our substring to include as many characters as possible. Once we see a duplicate, move the left pointer to decrease the range of our substring to remove the duplicated character. Every iteration, calculate the length of the substring and update the new max length if needed.

Process: 

    1. Start both pointers at the start of our array.
    2. Move the right pointer until we POINT AT a duplicate char (add to set)
        a. Calculate new max length if needed. (Max will be right - left)
        b. Once we encouter a duplicate, move left pointer ONE PAST the duplicate (removing from set)

Complexity: 
Time: O(N) since we will iterate through the entire array.
Space: O(N) since we are storing the set of used characters.
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, length, used = 0, 0, 0, set()
        while right < len(s):
            if s[right] not in used:
                used.add(s[right])
                right += 1
            else:
                used.remove(s[left])
                left += 1
            length = max(length, right - left + 1)
        return length

"""
438. Find All Anagrams in a String (Medium)
Leet: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Code: https://github.com/onlypham/tangents

Problem: Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
Input: s, p
Output: Return list of indices

Framework: Two Pointers (Sliding Window)
Giveaways: We need two pointers: 1) to reference the left end of our substring and 2) a right pointer that is always placed len(p) away from our left. If at any time, we are an anagram, we will add the left index to results. 
Big Picture: The right side pointer will 

Process: 

    1. Initilize two hashmaps to create counts for each character.
    2. Add the first len(p) characters of BOTH s and p to hashmaps.
    3. Iterate from len(p) to len(s).
        a. Add right pointer character to current.
        b. Remove left pointer character from current.
            i. Pop left character if fall to 0.
        c. Increment left index & add result if match.

Complexity: 
Time: O(NM) since we iterate through string of size N then check for equality with string of size M
Space: O(1) since there are only 26 english characters
"""

class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        current, target = {}, {}
        # add first len(p) characters to both hashmaps
        for i in range(len(p)):
            current[s[i]] = 1 + current.get(s[i], 0)
            target[p[i]] = 1 + target.get(p[i], 0)
        # if we already have a match, append to results
        res = [0] if current == target else []
        left = 0
        # every iteration, we move right pointer
        for right in range(len(p), len(s)):
            # remove left index AND add right index
            current[s[left]] -= 1
            current[s[right]] = 1 + current.get(s[right], 0)
            # if no more of that character, we pop
            if current[s[left]] == 0:
                current.pop(s[left])
            # increment left pointer
            left += 1
            # append index if anagram
            if current == target:
                res.append(left)
        return res
        
"""
76. Minimum Window Substring (Hard)
Leet: https://leetcode.com/problems/minimum-window-substring/
Code: https://github.com/onlypham/tangents

Problem: Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
Input: s, t
Output: Return substring.
Other: A substring is a contiguous sequence of characters within the string.

Framework: Two Pointers (Sliding Window)
Giveaways: 
Big Picture:

Process: 

    1. Set a left/right pointer, have/need hashmap, have/need count, minLength.
    2. Initilize the hashmap of chars that we NEED & set needCount accordingly.
    3. Iterate the right pointer until the end of the string.
        a. Add the right character to our HAVE hashmap. 
            i. If this character is also in our NEED hashmap, see if we satisfy a condition & increment haveCount accordingly.
        b. While haveCount == needCount, we can remove characters from the left.
            i. If current length < minLength, update result & new minLength.
            ii. Decrement the count of the left char in our HAVE hashmap.
            iii. If left char is in NEED hashmap, see if we unsatisfy a condition & decremenet haveCount accordingly.
            iv. Increment left pointer.
    4. Return resulting substring if minLength != float('inf') 

Complexity: 
Time: O(N) since we at most add & remove each element of the string to our hashmap once. Every update, we only compare a single comparison and update our HAVE count to compare with NEED.
Space: O(# of distinct characters in s) 
"""

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        have, need, left, res = {}, {}, 0, [-1, -1]
        # initilize the hashmap of characters we need
        for char in t:
            need[char] = 1 + need.get(char, 0)
        haveCount, needCount, minLength = 0, len(need), float('inf')
        # iterate until right reaches the end
        for right in range(len(s)):
            char = s[right]
            have[char] = 1 + have.get(char, 0)
            # check if addition of char satisifies a need in hashmap
            if char in need and have[char] == need[char]:
                haveCount += 1
            # while we satisfy the condition, move left pointer
            while haveCount == needCount:
                if right - left + 1 < minLength:
                    res = [left, right]
                    minLength = right - left + 1
                # we can remove left elements until we do not satify condition 
                char = s[left]
                have[char] -= 1
                # check if removal unsatisifies a need in hashamp
                if char in need and have[char] < need[char]:
                    haveCount -= 1
                left += 1
        return s[res[0]:res[1]+1] if minLength != float('inf') else ""

"""
560. Subarray Sum Equals K (Medium)
Leet: https://leetcode.com/problems/subarray-sum-equals-k/
Code: https://github.com/onlypham/tangents

Problem: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
Input: nums, k
Output: Return # of subarrays (int)
Other: A subarray is a contiguous non-empty sequence of elements within an array.

Framework: One Pointer
Giveaways: Use the power of running sums and hashmaps. At a certain point in the array, if we compute the prefix sum MINUS target k and find that value in the hashmap in O(1), we'd be able to create such a subarray.
Big Picture: Keep a hashmap of all prefix sums. We know that if the curSum minus ANY prefix sum that equals our target k, is a valid subarray.

Process: 

    1. Create hashmap of prefix sums starting with {0: 1} 
    2. For num in nums
        a. Add to the current sum
        b. Compute the complement & check hashmap
            i) Increment by the number of prefix sums that equal the complement
        c. Increment the count of curSum in hashmap

Complexity: 
Time: O(N) we will iterate through the nums array once.
Space: O(N) since we only save each running sum
"""

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        # {0: 1} to cover case that curSum == k
        sums, curSum, count = {0: 1}, 0, 0
        for num in nums:
            curSum += num
            complement = curSum - k
            # if we find complement, increment by count
            if complement in sums:
                count += sums[complement]
            # store $ of times, we get particular curSum
            if curSum in sums:
                sums[curSum] += 1
            else:
                sums[curSum] = 1
        return count

"""
141. Linked List Cycle (Easy)
Leet: https://leetcode.com/problems/linked-list-cycle/
Code: https://github.com/onlypham/tangents

Problem: Given head, the head of a linked list, determine if the linked list has a cycle in it.
Input: head
Output: True if cycle else False

Framework: Two Pointer (Same Direction)
Giveaways: Think tortoise and the hare. If there is one clear path to the finish line, the tortoise will get there first and the race will finish. However, if the tortoise is running in circles, it's bound to lap the hare.
Big Picture: Start both pointers at the start and have one move twice as fast. If they ever meet, return True since there is a cycle. End when the fast pointer reaches the end. 

Process: 

    1. Start both the "fast" and "slow" pointer at the head
    2. If the "fast" pointer can move two nodes forward.
        a. Move the "fast" pointer twice.
        b. Move the "slow" pointer once.
        c. If they ever reach each other, return True.
    3. Once the "fast" pointer reaches the end, return False.

Complexity: 
Time: O(N) we will iterate through the entire linked list.
Space: O(1)
"""

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

"""
1537. Get the Maximum Score (Hard)
Leet: https://leetcode.com/problems/get-the-maximum-score/
Code: https://github.com/onlypham/tangents

Problem: You are given two sorted arrays of distinct integers nums1 and nums2. The score is defined as the sum of uniques values in a valid path. A valid path is defined as follows: 1) Choose array nums1 or nums2 to traverse 2) Traverse the current array from left to right2 3) If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path). 
Input: nums1, nums2
Output: Return MAX score in valid path (10 ^ 9 + 7)

Framework: Two Pointer (Same Direction)
Giveaways: The key to this problem is realizing we need to find the sum of the subarrays between two adajcent duplicates. We need two pointers to calculate these sums and so we can store the larger of the two.
Big Picture: First pass through both arrays, we will find the duplicates. Second pass, we will calculate running sums between each duplicate and add the larger of the two to a TOTAL running sum.

Process: 

    1. Iterate through both arrays & find all duplicates.
    2. Keep two running sums for nums1 and nums2.
        a. Calculate the running sum up until the first duplicate.
        b. Add the larger running sum to the TOTAL sum.
        c. Add the duplicate ONCE to the TOTAL sum.
        d. Reset both running sums and continue process until next duplicate.
        c. IF no more duplicate, keep running sum until the end of the array.
    3. Reurn TOTAL sum.

Complexity: 
Time: O(N) we will iterate through the each nums array twice. Once to find the duplicates. Again to find the running sums.
Space: O(1)
"""

class Solution:
    
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        first, second, seen, duplicate = 0, 0, set(), set()
        # create set of all nums in nums1
        for num in nums1:
            seen.add(num)
        # see if any duplicates are in nums2
        for num in nums2:
            if num in seen:
                duplicate.add(num)
        sum1, sum2, total = 0, 0, 0
        # continue until both reach the end of their arrays
        while first < len(nums1) or second < len(nums2):
            # create running sum until duplicate found in nums1
            while first < len(nums1) and nums1[first] not in duplicate:
                sum1 += nums1[first]
                first += 1
            # create running sum until duplciate found in nums2
            while second < len(nums2) and nums2[second] not in duplicate:
                sum2 += nums2[second]
                second += 1
            # add the greater of the two running sums
            total += sum1 if sum1 > sum2 else sum2
            # add the duplicate, make sure we aren't PAST the end
            if first < len(nums1):
                total += nums1[first]
            # move pointers up & reset running sums
            first += 1 ; second += 1
            sum1 = 0 ; sum2 = 0
        # ensure that ONE side didn't have a duplicate at the end of their array
        while first < len(nums1):
            total += nums1[first]
            first += 1
        while second < len(nums2):
            total += nums2[second]
            second += 1
        return total % ( 10 ** 9 + 7 )

"""
42. Trapping Rain Water (Hard)
Leet: https://leetcode.com/problems/trapping-rain-water/
Code: https://github.com/onlypham/tangents

Problem: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height
Output: MAX water (int)

Framework: Two Pointer (Same Direction)
Giveaways: Notice that the water at a particular index in array depends solely on the highest elevation to the left of the current position AND the highest elevation to the right of the current position.
Big Picture: We make two passes through the array. During the first pass, the left pointer will create a list storing LEFT WALL defined as the highest elevation at any position to the left of current position. Right pointer will do the same for RIGHT WALL. On the second pass, we move move the two pointers together and compare the minimum of wallHeights to the elevation.

Process: 

    1. For both left and right, calculate leftWall & rightWall.
        a. Update the leftWall/rightWall starting 0.
        b. Then, update the leftMax/rightMax for future iterations.
    2. Iterate through the array again.
        a. Calculate the lower of the leftWall and rightWall.
        b. If the lower of the two is greater than elevation, add water!

Complexity: 
Time: O(N) as we are iterating through the array three times total.
Space: O(N)
"""

class Solution:

    def trap(self, height: List[int]) -> int:
        leftWall, rightWall = [0] * len(height), [0] * len(height)
        leftMax, rightMax, water = 0, 0, 0
        # update leftMax after we update leftWall since we want the
        # leftWall value for elevations TO THE LEFT of current position
        for i in range(len(height)):
            leftWall[i] = leftMax
            leftMax = max(height[i], leftMax)
        # same exact procedure for rightMax and rightWall
        for i in reversed(range(len(height))):
            rightWall[i] = rightMax
            rightMax = max(height[i], rightMax)
        # if the lower of the two walls is higher than current elevation
        # add to water ( lower - elevation )
        for i in range(len(height)):
            lower = min(leftWall[i], rightWall[i])
            if lower > height[i]:
                water += lower - height[i]
        return water
