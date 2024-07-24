//(i) Write a code to generate the Fibonacci sequence until a user-specified limit.
def fibonacci_seq(limit):
    a, b = 0, 1
    fib_sequence = []
    while a <= limit:
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

user_limit = int(input("Enter the limit for the Fibonacci seq: "))
result = fibonacci_seq(user_limit)

print("Fibonacci seq up to", user_limit, ":", result)
