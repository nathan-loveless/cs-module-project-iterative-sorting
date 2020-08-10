def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    min = 0
    mid = 0
    high = len(arr) - 1

    while min <= high:
        mid = (high + min) // 2
        if arr[mid] < target:
            min = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1  # not found
