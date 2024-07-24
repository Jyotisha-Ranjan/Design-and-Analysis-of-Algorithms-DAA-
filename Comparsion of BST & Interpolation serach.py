#(ii) Compare the working of Interpolation Search and Binary Search by running them over a dataset of 1 million points or more.
import time
import numpy as np

# Generate a sorted array of 10,000,000 points
data = np.arange(10000000)

# Define the target value to search for
target = 9999999

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Time Binary Search
start_time = time.time()
binary_result = binary_search(data, target)
binary_time = time.time() - start_time

# Time Interpolation Search
start_time = time.time()
interpolation_result = interpolation_search(data, target)
interpolation_time = time.time() - start_time

# Output results
print(f"Binary Search: Found at index {binary_result} in {binary_time:.10f} seconds")
print(f"Interpolation Search: Found at index {interpolation_result} in {interpolation_time:.10f} seconds")
