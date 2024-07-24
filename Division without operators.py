#7 (i) Given two positive integers a and b, write an iterative algorithm to determine the quotient and remainder when a is divided by b. You should write a while loop and should not use the division and remainder operators.
def divide_without_division(a, b):
    quotient = 0
    remainder = a  # Initialize remainder to a

    while remainder >= b:
        remainder -= b
        quotient += 1

    return quotient, remainder

a = int(input("Enter a positive integer (a): "))
b = int(input("Enter another positive integer (b): "))

q, r = divide_without_division(a, b)
print(f"The quotient of {a} divided by {b} is: {q}")
print(f"The remainder of {a} divided by {b} is: {r}")
