Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#(iii) Find the largest Fibonacci number less than a given number ‘n’ assuming:
#No such list is available

def largest_fibonacci(n):
    a, b = 0, 1
    largest_fib = None

    while True:
        c = a + b

        if c >= n:
            break

        a = b
        b = c
        largest_fib = c

    return largest_fib

n = 100
largest_fib = largest_fibonacci(n)

if largest_fib is not None:
    print(f"The largest Fibonacci number less than {n} is: {largest_fib}")
else:
    print(f"There is no Fibonacci number less than {n}.")