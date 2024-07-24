# 9 . Using the ‘yield’ keyword in Python, generate “infinitely many” Fibonacci numbers. That is, write a generator function that returns a generator object which yields the fibonacci sequence.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Creating a generator object
fib_gen = fibonacci_generator()

# Printing the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
