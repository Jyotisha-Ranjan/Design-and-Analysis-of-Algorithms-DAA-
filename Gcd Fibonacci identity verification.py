#(ii) Verify that GCD(Fm ,Fn)=FGCD(m,n),` where Fn is the (n+1)th Fibonacci number. What is the minimum number of cases to verify in order to build confidence? Can this confidence be quantified with probability?
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def verify_identity(m, n):
    Fm = fibonacci(m)
    Fn = fibonacci(n)
    gcd_mn = gcd(m, n)
    Fgcd_mn = fibonacci(gcd_mn)
    gcd_Fm_Fn = gcd(Fm, Fn)

    if gcd_Fm_Fn == Fgcd_mn:
        print(f"Verification passed for m = {m}, n = {n}.")
    else:
        print(f"Verification failed for m = {m}, n = {n}.")

verify_identity(5, 3)
verify_identity(8, 5)
