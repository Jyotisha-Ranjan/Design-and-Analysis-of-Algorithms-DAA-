#4 Using the idea of Binary Search, search for the largest Fibonacci number less than a given positive integer.
def largest_fibo(n):
    if n <= 0:
        return None
    fib1, fib2 = 1, 1
    while fib2 <= n:
        fib1, fib2 = fib2, fib1 + fib2

    return fib1

def largest_fibonacci():
    n = int(input("Enter a positive integer (n): "))
    largest_fib = largest_fibo(n)
    if largest_fib:
        print(f"The largest Fibonacci number less than {n} is {largest_fib}.")
    else:
        print("Invalid input. Please enter a positive integer.")

largest_fibonacci()
