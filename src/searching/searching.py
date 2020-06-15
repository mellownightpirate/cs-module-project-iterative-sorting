def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = low + (high - low) // 2
        middle_value = arr[middle]
        if middle_value == target:
            return middle
        elif target < middle_value:
            high = middle - 1
        else:
            low = middle + 1

    return -1  # not found
