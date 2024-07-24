# 10 Given a sorted list A in ascending order and an element x, efficiently find the leftmost occurrence of x in A.
def leftmost_occurrence(A, x):
    left = 0
    right = len(A) - 1
    result = -1  # Initialize result to -1 (not found)

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == x:
            result = mid  # Update result to current index
            right = mid - 1  # Continue searching in the left half
        elif A[mid] < x:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return result

# Example usage:
A = [1, 2, 2, 2, 3, 3, 4, 5, 5, 6]
x = 2

leftmost_index = leftmost_occurrence(A, x)
if leftmost_index != -1:
    print(f"The leftmost occurrence of {x} in A is at index {leftmost_index}.")
else:
    print(f"{x} is not found in A.")
