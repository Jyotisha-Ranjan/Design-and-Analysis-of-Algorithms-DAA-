#4 (ii) Develop an iterative algorithm to achieve the same goal as in (i).
def count_ways_to_sum_iterative(N):
    if N == 0:
        return [[]]
    elif N == 1:
        return [[1]]
    elif N == 2:
        return [[1, 1], [2]]

    ways = [[] for _ in range(N + 1)]
    ways[0] = [[]]
    ways[1] = [[1]]
    ways[2] = [[1, 1], [2]]

    for i in range(3, N + 1):
        for way in ways[i - 1]:
            ways[i].append(way + [1])
        for way in ways[i - 2]:
            ways[i].append(way + [2])

    return ways[N]

def enumerate_ways_to_sum_iterative():
    N = int(input("Enter a positive integer (N): "))
    ways = count_ways_to_sum_iterative(N)
    print(f"All possible ways to sum {N} using 1s and 2s:")
    for idx, way in enumerate(ways, start=1):
        print(f"Way {idx}: {way}")

enumerate_ways_to_sum_iterative()
