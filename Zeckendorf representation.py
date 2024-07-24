#2(i)(Greedy Strategy) Develop an algorithm to find a unique representation of a number using the Fibonacci sequence.
def unique_fibonacci_representation(n):
    fib1, fib2 = 1, 2
    representation = []

    while n > 0:
        while fib2 <= n:
            fib1, fib2 = fib2, fib1 + fib2

        representation.append(fib1)
        n -= fib1
        fib1, fib2 = 1, 2

    return representation

n = 250
representation = unique_fibonacci_representation(n)
print(f"Unique Fibonacci representation of {n}: {representation}")

#ii) Determine the time complexity of the developed algorithm.
# The TC of the above code is O(n)
