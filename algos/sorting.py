"""
algo: insertion_sort
input: arr
idea: slide first item right until correct place, slide second, slide third...
time: O(N^2) but O(N) if almost sorted
stable: yes
in-place: yes
"""

def insertion_sort(arr):
    for i in range(len(arr)):
        # only look at current i
        cur = i
        # slide it right until in correct place
        while cur > 0 and arr[cur] < arr[cur-1]:
            arr[cur], arr[cur-1] = arr[cur-1], arr[cur]
            cur -= 1
    return arr

def test1():
  assert insertion_sort([1, 9, 2, 6, -1, 4]) == [-1, 1, 2, 4, 6, 9]
  assert insertion_sort([4, 1, 5, 7, 1, 2]) == [1, 1, 2, 4, 5, 7]
  assert insertion_sort([9, 8, 7, 6]) == [6, 7, 8, 9]
  print("Test Cases Passed!")

"""
algo: selection_sort
input: arr
idea: move smallest to front, move 2nd smallest after, move 3rd...
time: O(N^2)
stable: no
in-place: yes
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # set min to i
        min = i
        # find min from i to n
        for j in range(i, n):
            if arr[j] < arr[min]:
                min = j
        # swap position of i and min
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def test2():
  assert selection_sort([1, 9, 2, 6, -1, 4]) == [-1, 1, 2, 4, 6, 9]
  assert selection_sort([4, 1, 5, 7, 1, 2]) == [1, 1, 2, 4, 5, 7]
  assert selection_sort([9, 8, 7, 6]) == [6, 7, 8, 9]
  print("Test Cases Passed!")

"""
algo: selection_sort
input: arr
idea: bubble largest elements to the back iteratively
time: O(N^2) but O(N) if almost sorted
stable: yes
in-place: yes
"""

def bubble_sort(arr):
    n = len(arr)
    # iterate from start to n, start to n-1, start to n-2...
    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            # bubble this ish to the back
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # if no swaps in one iteration :)
        if not swapped:
            return arr
    return arr

def test3():
  assert bubble_sort([1, 9, 2, 6, -1, 4]) == [-1, 1, 2, 4, 6, 9]
  assert bubble_sort([4, 1, 5, 7, 1, 2]) == [1, 1, 2, 4, 5, 7]
  assert bubble_sort([9, 8, 7, 6]) == [6, 7, 8, 9]
  print("Test Cases Passed!")

"""
algo: merge_sort
input: arr
idea: sort left, sort right, merge both
time: always O(NlogN)
stable: yes
in-place: no
"""

def merge_sort(arr):
    n = len(arr)
    # base case: if 0 or 1 elements, return arr
    if n <= 1:
        return arr
    mid = n // 2
    # recursively call merge_sort on left & right halves
    left_sort, right_sort = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    left, right = 0, 0
    merged = []
    while left < mid or right < n - mid:
        # no more elements to add from left_sort
        if left == mid:
            merged.append(right_sort[right])
            right += 1
        # no more elements to add from right_sort
        elif right == n - mid:
            merged.append(left_sort[left])
            left += 1
        # if left_sort has a smaller element than right_sort
        elif left_sort[left] <= right_sort[right]:
            merged.append(left_sort[left])
            left += 1
        else:
            merged.append(right_sort[right])
            right += 1
    return merged

def test4():
  assert merge_sort([1, 9, 2, 6, -1, 4]) == [-1, 1, 2, 4, 6, 9]
  assert merge_sort([4, 1, 5, 7, 1, 2]) == [1, 1, 2, 4, 5, 7]
  assert merge_sort([9, 8, 7, 6]) == [6, 7, 8, 9]
  print("Test Cases Passed!")

"""
algo: quick_sort
input: arr
setup: set pivot as first element
idea: iterate through moving smaller elements to updated pivot location
time: O(NlogN) but O(N^2) if almost sorted
stable: no
in-place: yes
"""

def quick_sort(arr):
    n = len(arr)
    # base case: if 0 or 1 elements, return arr
    if n <= 1:
        return arr
    pivot = 0
    # iterate from 1 to n
    for i in range(1, n):
        # if element smaller than pivot
        if arr[i] <= arr[0]:
            pivot += 1 # move pivot marker up
            arr[pivot], arr[i] = arr[i], arr[pivot] # and swap
    # at this point, pivot will point to last element smaller than pivot 
    arr[pivot], arr[0] = arr[0], arr[pivot]
    # recursively call quick_sort on array left & right of pivot
    return quick_sort(arr[:pivot]) + [arr[pivot]] + quick_sort(arr[pivot+1:])

def test5():
  assert quick_sort([1, 9, 2, 6, -1, 4]) == [-1, 1, 2, 4, 6, 9]
  assert quick_sort([4, 1, 5, 7, 1, 2]) == [1, 1, 2, 4, 5, 7]
  assert quick_sort([9, 8, 7, 6]) == [6, 7, 8, 9]
  print("Test Cases Passed!")

"""
algo: built_in
time: O(NlogN)
stable: yes
in-place: yes
"""

nums = [40, 100, 1, 5, 25, 10]
nums.sort(reverse=True)

tasks = [
    ('Cook dinner', 5),
    ('Buy grocery', 3)
]

# sort tasks by priority in ascending order
sorted_tasks = sorted(tasks, key=lambda task: task[1])

# look into heap sort & BST - O(NlogN)