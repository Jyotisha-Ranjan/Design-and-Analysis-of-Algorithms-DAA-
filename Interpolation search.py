# 8 (i) (Interpolation Search) Assuming that the given list of numbers are growing linearly, perform an efficient “jump-based” search (similar to the binary search except that the choice of m is based on the linear growth of the data).
def linear_jump_search(arr, x):
    n = len(arr)
    jump = 1
    while jump < n and arr[jump] < x:
        jump += 1

    start = jump - 1
    end = min(jump, n - 1)

    while start <= end:
        if arr[start] == x:
            return start
        start += 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

index = linear_jump_search(arr, x)
if index != -1:
    print(f"Element {x} found at index {index}.")
else:
    print(f"Element {x} not found in the list.")
