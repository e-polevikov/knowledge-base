

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        v_from, v_to, weight = map(int, input().split())
        graph[v_from].append([v_to, weight])
    
    source, target = map(int, input().split())

    distances = [float('inf') for _ in range(n)]
    distances[source] = 0

    for _ in range(n - 1):
        for vtx in range(n):
            if distances[vtx] == float("inf"):
                continue

            for vtx_to, weight in graph[vtx]:
                updated_dist = distances[vtx] + weight
                if updated_dist < distances[vtx_to]:
                    distances[vtx_to] = updated_dist
    
    print(distances)


if __name__ == "__main__":
    main()
