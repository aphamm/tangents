"""
BINARY_SEARCH.PY

Concept: think about binary decisions to shrink search range
Think: "how can i apply a filter to an array & imagine an array of booleans"

704. Binary Search (Easy)
first_true
first_element_bigger_than_target
first_occurence
69. Sqrt(x) (Easy)
153. Find Minimum in Rotated Sorted Array
162. Find Peak Element (Medium)
1011. Capacity To Ship Packages Within D Days
min_time_to_read_given_n_workers
"""

"""
704. Binary Search (Easy)
https://leetcode.com/problems/binary-search/

input: arr -> [1, 2, *3*, 4, 8], 3
output: index -> 2
idea: discard half of array based on mid
time: O(logN)
"""

def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    # ensure that we allow left == right
    while left <= right: 
        # no need to check for int overflow
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # oops, target is bigger, so we want a higher value
        # throw away left half of array
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def test1():
  assert binary_search([1, 2, 3, 4, 8, 10], 8) == 4
  assert binary_search([2, 3, 4, 5, 8, 10], 2) == 0
  assert binary_search([2, 3, 4, 5, 8, 10], 11) == -1
  print("Purr-🐱-haps it Passed!")

"""
algo: first_true
input: arr -> [False, False, *True*, True, True]
output: index -> 2
idea: {binary_search} but update index everytime True found
time: O(logN)
"""

def first_true(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            index = mid # we've found an earlier True !!
            right = mid - 1 # remove current True from search
        else:
            left = mid + 1
    return index

def test2():
  assert first_true([False, False, False, True, True, True, True]) == 3
  assert first_true([False, False, True, True, True]) == 2
  assert first_true([False, False, False, False]) == -1
  print("Purr-🐱-haps it Passed!")

"""
algo: first_element_bigger_than_target
input: arr
output: index
idea: {first_true} after applying (arr[mid] >= target) filter

    [2, 3, 4, 5, 6, 8, 9] target == 7
    [F, F, F, F, F, T, T] after applying (arr[mid] >= 7) filter
    reduces {first_true}

time: O(logN)
"""

def first_element_bigger_than_target(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        # evaluates to True given our filter
        if arr[mid] >= target:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index

def test3():
  assert first_element_bigger_than_target([1, 3, 3, 5, 8, 8, 10], 2) == 1
  assert first_element_bigger_than_target([2, 3, 5, 7, 11, 13, 17, 19], 6) == 3
  assert first_element_bigger_than_target([1, 3, 3, 5, 8, 8, 10], 11) == -1
  print("Purr-🐱-haps it Passed!")

"""
algo: first_occurence
input: arr
output: index
idea: modified {first_true} but only save index when == target
time: O(logN)
"""

def first_occurence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr)
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            index = mid # only save index if arr[mid] == target
            right = mid - 1
        # oops, target is smaller, so we want a smaller value
        # throw away right half of array
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return index

def test4():
    assert first_occurence([1, 2, 3, 5, 5, 9], 5) == 3
    assert first_occurence([2, 4, 6, 7, 10], 10) == 4
    assert first_occurence([2, 4, 6, 7, 10], 1) == -1
    print("Purr-🐱-haps it Passed!")

"""
69. Sqrt(x) (Easy)
https://leetcode.com/problems/sqrtx/

input: n
output: int == floor(square_root)
idea: {first_true} after applying (mid * mid > n) filter

    [1, 2, 3, 4, 5, 6, 7, 8] given n == 8, imagine list of size 8
    [F, F, T, T, T, T, T, T] after applying (mid * mid > 8) filter
    reduces to {first_true} BUT return index - 1

time: O(logN)
"""

def square_root(n: int) -> int:
    left, right = 0, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > n:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res - 1

def test5():
    assert square_root(10) == 3
    assert square_root(15) == 3
    assert square_root(8) == 2
    print("Purr-🐱-haps it Passed!")

"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

input: arr
output: index
idea: {first_true}  after applying (arr[mid] <= arr[-1]) filter

    [4, 5, 6, 7, 8, 1, 2, 3] notice arr[-1] == 3
    [F, F, F, F, F, T, T, T] after applying (arr[mid] <= 3) filter
    reduces to {first_true}

time: O(logN)
"""

def minimum_in_rotated_sorted_array(arr: list[int]) -> int:
    left, right = 0, len(arr)
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index

def test6():
    assert minimum_in_rotated_sorted_array([5, 5, 9, 1, 2, 3]) == 3
    assert minimum_in_rotated_sorted_array([4, 6, 7, 10, 2]) == 4
    assert minimum_in_rotated_sorted_array([10, 2, 4, 6, 7]) == 1
    print("Purr-🐱-haps it Passed!")

"""
162. Find Peak Element (Medium)
https://leetcode.com/problems/find-peak-element/

input: arr -> [1, 2, 3, *4*, 3, 2, 1] 
    monotonically increase until peak then monotonically decrease
output: index -> 3
idea: {first_true} after applying (arr[mid] > arr[mid+1]) filter

    *Ensure right = len(arr) - 1 to prevent index out of range* 
    [1, 2, 3, 4, 5, 4, 3, 2, 1] 
    [F, F, F, F, T, T, T, T, T] after applying (arr[mid] > arr[mid+1]) filter
    reduces to {first_true}

time: O(logN)
"""

def find_peak(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index

def test7():
    assert find_peak([1, 2, 4, 7, 4, 3, 2]) == 3
    assert find_peak([4, 6, 7, 10, 2]) == 3
    assert find_peak([1, 2, 7, 5, 4, 1, 1]) == 2
    print("Purr-🐱-haps it Passed!")

"""
1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

input: weights, days -> [1, 2, 3, 4, 5], 5
output: min_capacity -> 3
idea: {first_true} after applying (isFeasible) filter to range of capacities

    weights = [1, 2, 3, 4, 5] where days == 5

    first find min & max of possible capacities
        min ==  max(weights) -> one weight a day
        max == sum(weights) -> all weights in one day

    [5, 6, 7, 8, ..., 12, 13, 14, 15]
    [F, F, F, F, ..., F, T, T, T] after applying (isFeasible) filter
    reduces to {first_true}

time: O(NlogN) == isFeasible is O(N) * binary search is O(logN)
"""

def min_capacity_to_ship_in_d_days(weights: list[int], days: int) -> int:
    # O(N), treat left, right as left & right capacity bounds
    left, right = max(weights), sum(weights)
    index = right # set to right upper bound
    while left <= right:
        mid = (left + right) // 2
        if is_feasible(weights, days, mid):
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index

def is_feasible(weights: list[int], days: int, capacity: int) -> int:
    req_days = 1 # will always need at least one day
    cur_weight = 0 # current day weight acculumator
    for i in range(len(weights)): # iterate through all weights
        cur_weight += weights[i] # always add next weight
        if cur_weight > capacity: # if over capacity
            cur_weight = 0 # reset to 0
            cur_weight += weights[i] # add weight again
            req_days += 1 # increment req_days
    return req_days <= days # see if at most days

def test8():
    assert min_capacity_to_ship_in_d_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert min_capacity_to_ship_in_d_days([1, 2, 3, 4, 5], 3) == 6
    assert min_capacity_to_ship_in_d_days([1, 2, 3, 4, 5], 4) == 5
    assert min_capacity_to_ship_in_d_days([1, 2, 3, 4, 5], 2) == 9
    print("Purr-🐱-haps it Passed!")

"""
algo: min_time_to_read_given_n_workers
input: times, workers -> [7, 2, 5, 10, 8], 2
    each worker must read contigious subarrays
output: min_time -> 18 (7+2+5 and 10+8)
idea: {first_true} after applying (isFeasible) filter to range of times

    times = [7, 2, 5, 10, 8] where workers == 2

    first find min & max of possible times
        min == max(times) -> at least longest newspaper 
        max == sum(times) -> one worker reads everything

    [10, 11, 12, 13, ..., 30, 31, 32]
    [F, F, F, F, F, ..., F, T, T, T] after applying (isFeasible) filter
    reduces to {first_true}

time: O(NlogN) == is_readable is O(N) * binary search is O(logN)
"""

def min_time_to_read_given_n_workers(times: list[int], workers: int) -> int:
    # O(N), treat left, right as left & right capacity bounds
    left, right  = max(times), sum(times)
    index = right
    while left <= right:
        mid = (left + right) // 2 
        if is_readable(times, workers, mid):
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index

def is_readable(times: list[int], workers: int, time_limit: int) -> int:
    # essentially same logic as is_feasible
    workers_needed = 1
    time = 0
    for i in range(len(times)):
        time += times[i]
        if time > time_limit:
            time = 0
            time += times[i]
            workers_needed += 1
    return workers_needed <= workers

def test9():
    assert min_time_to_read_given_n_workers([7, 2, 5, 10, 8], 2) == 18
    assert min_time_to_read_given_n_workers([2, 3, 5, 7], 3) == 7
    assert min_time_to_read_given_n_workers([2, 6, 4, 5, 6, 4], 2) == 15
    print("Purr-🐱-haps it Passed!")
    