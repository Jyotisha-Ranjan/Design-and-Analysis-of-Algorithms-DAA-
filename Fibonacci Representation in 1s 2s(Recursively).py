# Staircase
#5 By the 12th-century Indian mathematician Hemachandra, it is well-known that the Fibonacci sequence represents the number of ways one can express a number as the sum of 1s and 2s.
#(i) Provide a recursive algorithm to enumerate all possible ways of expressing a given number N as a sum of 1s and 2s.
def count_ways_to_sum(N):
    if N == 0:
        return [[]]
    elif N == 1:
        return [[1]]
    elif N == 2:
        return [[1, 1], [2]]
    ways = []

    for way in count_ways_to_sum(N - 1):
        ways.append(way + [1])

    for way in count_ways_to_sum(N - 2):
        ways.append(way + [2])

    return ways

def enumerate_ways_to_sum_input():
    N = int(input("Enter a positive integer (N): "))
    ways = count_ways_to_sum(N)
    print(f"All possible ways to sum {N} using 1s and 2s:")
    for idx, way in enumerate(ways, start=1):
        print(f"Way {idx}: {way}")

enumerate_ways_to_sum_input()
