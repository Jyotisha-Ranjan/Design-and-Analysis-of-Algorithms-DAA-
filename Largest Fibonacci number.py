#(iii) Find the largest Fibonacci number less than a given number ‘n’ assuming:
#A list of Fibonacci numbers is available
def largest_fibonacci(n, fibonacci_list):
    largest_fib = None

    for fib_num in fibonacci_list:
        if fib_num < n:
            largest_fib = fib_num
        else:
            break

    return largest_fib


fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  # Example list of Fibonacci numbers
n = 50

largest_fib_less_than_n = largest_fibonacci(n, fibonacci_list)

if largest_fib_less_than_n is not None:
    print(f"The largest Fibonacci number less than {n} is: {largest_fib_less_than_n}")
else:
    print(f"There is no Fibonacci number less than {n} in the given list.")
