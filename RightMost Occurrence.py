#3 (ii) If x does belong to A, determine the rightmost occurrence of x in A. Make sure to use ONLY a WHILE loop and NO recursion.
def right_element(array, x):
    left, right = 0, len(array) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == x:
            result = mid
            left = mid + 1
        elif array[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

def right_ele():
    input_str = input("Enter the sorted array elements separated by spaces: ")
    array = list(map(int, input_str.split()))

    x = int(input("Enter the value to search (x): "))

    index = right_element(array, x)

    if index != -1:
        print(f"The rightmost element of {x} in the array is at index {index}.")
    else:
        print(f"{x} does not belong to the array.")

right_ele()
