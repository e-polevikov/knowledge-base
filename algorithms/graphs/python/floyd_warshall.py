

def main():
    n, m = map(int, input().split())
    distances = [[float("inf") for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        vtx_from, vtx_to, distance = map(int, input().split())
        distances[vtx_from][vtx_to] = distance

    for i in range(n):
        distances[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(
                    distances[i][j],
                    distances[i][k] + distances[k][j]
                )
    
    for i in range(n):
       for j in range(n):
            if i == j:
                continue

            print(i, j, distances[i][j])


if __name__ == "__main__":
    main()
