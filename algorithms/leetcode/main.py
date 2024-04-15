
cache = [None for _ in range(1000)]

def minCost(N):
    if cache[N] is not None:
        return cache[N]

    if N <= 1:
        return N
    
    cost = float("Inf")

    for i in range(1, N + 1):
        cost = min(
            cost,
            1 + max(i - 1, minCost(N - i))
        )
    
    cache[N] = cost

    return cost


for i in range(101):
    print(i, minCost(i))
