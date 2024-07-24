# 3 (i) Given a sorted array A in ascending order and an element x, determine whether x belongs to A.
def binary_search(array, x):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == x:
            return True
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

def element_in_array():
    input_str = input("Enter the sorted array elements separated by spaces: ")
    array = list(map(int, input_str.split()))

    x = int(input("Enter the value to search (x): "))
    if binary_search(array, x):
        print(f"{x} belongs to the array.")
    else:
        print(f"{x} does not belong to the array.")


element_in_array()
