#(ii) Write a code to determine the number of function calls required to build the Fibonacci sequence until the specified limit.
class FibonacciCounter:
    call_count = 0

    def fibonacci(self, n):
        FibonacciCounter.call_count += 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

def count_fibonacci_calls(limit):
    fib_counter = FibonacciCounter()
    fib_sequence = []
    for i in range(limit + 1):
        fib_sequence.append(fib_counter.fibonacci(i))
    return fib_sequence, FibonacciCounter.call_count


limit = 10
fib_sequence, total_calls = count_fibonacci_calls(limit)
print(f"Fibonacci sequence up to {limit}: {fib_sequence}")
print(f"Total function calls: {total_calls}")
