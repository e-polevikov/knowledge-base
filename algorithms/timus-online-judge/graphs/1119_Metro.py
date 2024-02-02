import math


def main():
    n, m = map(int, input().split())
    k = int(input())
    diagonals = set()

    for _ in range(k):
        v1, v2 = map(int, input().split())
        diagonals.add((v2, v1))

    distances = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        distances[i][0] = i
    
    for i in range(n + 1):
        distances[0][i] = i
    
    sqrt2 = math.sqrt(2)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (i, j) in diagonals:
                distances[i][j] = distances[i - 1][j - 1] + sqrt2
            else:
                distances[i][j] = min(
                    distances[i - 1][j] + 1,
                    distances[i][j - 1] + 1
                )

    print(round(distances[-1][-1] * 100))


if __name__ == "__main__":
    main()
