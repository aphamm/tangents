#################################################
# insertion_sort
#################################################
# input: arr
# idea: move first item to correct place, move second item, move third...
# time: O(N^2) but O(N) if almost sorted
# stable: yes
# in-place: yes

def insertion_sort(arr):
    for i in range(len(arr)):
        cur = i
        while cur > 0 and arr[cur] < arr[cur-1]:
            arr[cur], arr[cur-1] = arr[cur-1], arr[cur]
            cur -= 1
    return arr

def test_insertion_sort():
  print(insertion_sort([1, 9, 2, 6, -1, 4, 4, 8, 2]))

#################################################
# selection_sort
#################################################
# input: arr
# idea: move smallest to front, move second smallest after, move third...
# time: O(N^2)
# stable: no
# in-place: yes

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def test_selection_sort():
  print(selection_sort([1, 9, 2, 6, -1, 4, 4, 8, 2]))

#################################################
# bubble_sort
#################################################
# input: arr
# idea: bubble largest elements to the back iteratively
# time: O(N^2) but O(N) if almost sorted
# stable: yes
# in-place: yes

def bubble_sort(arr):
    n = len(arr)
    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

def test_bubble_sort():
  print(bubble_sort([1, 9, 2, 6, -1, 4, 4, 8, 2]))

#################################################
# merge_sort
#################################################
# input: arr
# idea: sort left, sort right, merge both
# time: always O(NlogN)
# stable: yes
# in-place: no

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left_sorted, right_sorted = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    left_index, right_index = 0, 0
    merged = []
    while left_index < mid or right_index < n - mid:
        if left_index == mid:
            merged.append(right_sorted[right_index])
            right_index += 1
        elif right_index == n - mid:
            merged.append(left_sorted[left_index])
            left_index += 1
        elif left_sorted[left_index] <= right_sorted[right_index]:
            merged.append(left_sorted[left_index])
            left_index += 1
        else:
            merged.append(right_sorted[right_index])
            right_index += 1
    return merged

def test_merge_sort():
  print(merge_sort([1, 9, 2, 6, -1, 4, 4, 8, 2]))

#################################################
# quick_sort
#################################################
# input: arr
# setup: set pivot as first element
# idea: iterate through moving smaller elements to updated pivot location
# time: O(NlogN) but O(N^2) if almost sorted
# stable: no
# in-place: yes

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = 0
    for i in range(1, n):
         if arr[i] <= arr[0]:
              pivot += 1
              arr[pivot], arr[i] = arr[i], arr[pivot]
    arr[pivot], arr[0] = arr[0], arr[pivot]
    return quick_sort(arr[:pivot]) + [arr[pivot]] + quick_sort(arr[pivot+1:])

def test_quick_sort():
  print(quick_sort([1, 9, 2, 6, -1, 4, 4, 8, 2]))

#################################################
# built_in
#################################################
# time: O(NlogN)
# stable: yes
# in-place: yes

nums = [40, 100, 1, 5, 25, 10]
nums.sort(reverse=True)

tasks = [
    ('Cook dinner', 5),
    ('Buy grocery', 3)
]

# sort tasks by priority in ascending order
sorted_tasks = sorted(tasks, key=lambda task: task[1])

# look into heap sort & BST - O(NlogN)