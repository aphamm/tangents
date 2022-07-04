#################################################
# avg_of_all_contig_subarray (easy)
#################################################
# input: k, arr
# ouput: find average of all subarrays of K contiguous elements
# time: O(N)
# space: O(1)

def avg_of_all_contig_subarray(k, arr):
    result, sum, left = [], 0.0, 0
    for right in range(len(arr)):
        sum += arr[right]
        if right >= k - 1:
            result.append(sum/5)
            sum -= arr[left]
            left += 1
    return result

def test_avg_of_all_contig_subarray():
  print(avg_of_all_contig_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))

#################################################
# max_sum_of_contig_subarray (easy)
#################################################
# input: k, arr
# output: find maximum sum of any subarray of K contiguous elements
# time: O(N)
# space: O(1)

def max_sum_of_contig_subarray(k, arr):
    maxSum, windowSum, left = 0, 0, 0
    for right in range(len(arr)):
        windowSum += arr[right]
        if right >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[left]
            left += 1
    return maxSum

def test_max_sum_of_contig_subarray():
  print(max_sum_of_contig_subarray(3, [2, 1, 5, 1, 7, 2]))

#################################################
# smallest_contig_subarray_min_sum
#################################################
# input: s, arr
# output: length of smallest contiguous subarray with sum >= S
# time: O(N)
# space: O(1)

import math

def smallest_contig_subarray_min_sum(s, arr):
    sum, left = 0, 0
    min_length = math.inf
    for right in range(len(arr)):
        sum += arr[right]
        while sum >= s:
            min_length = min(min_length, right - left + 1)
            sum -= arr[left]
            left += 1
    if min_length == math.inf:
        return 0
    return min_length

def test_smallest_contig_subarray_min_sum():
  print(smallest_contig_subarray_min_sum(7, [2, 1, 5, 2, 3, 2]))
  print(smallest_contig_subarray_min_sum(7, [2, 1, 5, 2, 8]))
  print(smallest_contig_subarray_min_sum(100, [3, 4, 1, 1, 6]))

#################################################
# longest_substring_with_k_distinct (medium)
#################################################
# input: str, k
# output: find longest substring with no more than K distinct characters
# time: O(N)
# space: O(K) for hashmap

def longest_substring_with_k_distinct(str, k):
    max_length, left = 0, 0
    chars = {}
    for right in range(len(str)):
        char = str[right]
        chars[char] = chars.get(char, 0) + 1
        while len(chars) > k:
            char = str[left]
            chars[char] -= 1
            if chars[char] == 0:
                del chars[char]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length
        
def test_longest_substring_with_k_distinct():
  print(longest_substring_with_k_distinct("araaci", 2))
  print(longest_substring_with_k_distinct("araaci", 1))
  print(longest_substring_with_k_distinct("cbbebi", 3))

#################################################
# longest_substring_all_distinct (hard)
#################################################
# input: str
# output: find length of longest substring with all distinct characters
# time: O(N)
# space: O(1) since only 26 letters

def longest_substring_all_distinct(str):
    max_length, left = 0, 0
    chars = {}
    for right in range(len(str)):
        char = str[right]
        chars[char] = chars.get(char, 0) + 1
        while chars[char] > 1:
            chars[str[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

def test_longest_substring_all_distinct():
  print(longest_substring_all_distinct("aabccbb"))
  print(longest_substring_all_distinct("abbbb"))
  print(longest_substring_all_distinct("abccde"))

#################################################
# longest_substring_of_same_letter_after_replacement (hard)
#################################################
# input: str, k
# output: find length of longest substring with same letters after replacement
# time: O(N)
# space: O(1)

def longest_substring_of_same_letter_after_replacement(str, k):
    max_length, left, most_freq_char = 0, 0, 0
    chars = {}
    for right in range(len(str)):
        char = str[right]
        chars[char] = chars.get(char, 0) + 1
        most_freq_char = max(most_freq_char, chars[char])
        if right - left + 1 - most_freq_char > k:
             char = str[left]
             chars[char] -= 1
             left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

def test_longest_substring_of_same_letter_after_replacement():
  print(longest_substring_of_same_letter_after_replacement("aabccbb", 2))
  print(longest_substring_of_same_letter_after_replacement("abbcb", 1))
  print(longest_substring_of_same_letter_after_replacement("abccde", 1))

#################################################
# longest_subarray_of_ones_after_replacement (hard)
#################################################
# input: arr, k
# output: find length of longest subarray of all ones after replacement
# time: O(N)
# space: O(1)

def longest_subarray_of_ones_after_replacement(arr, k):
    left, max_length, max_ones_count = 0, 0, 0
    for right in range(len(arr)):
        if arr[right] == 1:
            max_ones_count += 1
        if right - left + 1 - max_ones_count > k:
            if arr[left] == 1:
                max_ones_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

def test_longest_subarray_of_ones_after_replacement():
  print(longest_subarray_of_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(longest_subarray_of_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

#################################################
# contains_string_permutation (hard)
#################################################
# input: str, pattern
# output: find if string contains any permutation of patter
# time: O(N+M)
# space: O(M)

def find_permutation(str, pattern):
    left, matched, chars = 0, 0, {}
    for char in pattern:
        chars[char] = chars.get(char, 0) + 1
    for right in range(len(str)):
        char = str[right]
        if char in chars:
            chars[char] -= 1
            if chars[char] == 0:
                matched += 1
        if matched == len(chars):
            return True
        if right >= len(pattern) - 1:
            char = str[left]
            left += 1
            if char in chars:
                if chars[char] == 0:
                    matched -= 1
                chars[char] += 1
    return False

def test_find_permutation():
  print(find_permutation("oidbcaf", "abc"))
  print(find_permutation("odicf", "dc"))
  print(find_permutation("bcdxabcdy", "bcdyabcdx"))
  print(find_permutation("aaacb", "abc"))
