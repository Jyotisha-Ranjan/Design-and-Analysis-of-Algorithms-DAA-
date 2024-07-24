#6 (i) Give two positive integers m and n, determine the GCD(m,n).
def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

# Example usage:
m = int(input("Enter a positive integer (m): "))
n = int(input("Enter another positive integer (n): "))

result = gcd(m, n)
print(f"The GCD of {m} and {n} is: {result}")
