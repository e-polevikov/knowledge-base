import heapq


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        v_from, v_to, weight = map(int, input().split())
        graph[v_from - 1].append([v_to - 1, weight])
    
    source, target = map(lambda x: int(x) - 1, input().split())

    distances = [float('inf') for _ in range(n)]
    distances[source] = 0
    pqueue = [(0, source)]

    while len(pqueue) > 0:
        dist, vtx = heapq.heappop(pqueue)

        if distances[vtx] < dist:
            continue
        
        for neighbour, neighbour_dist in graph[vtx]:
            updated_dist = distances[vtx] + neighbour_dist
            if updated_dist < distances[neighbour]:
                distances[neighbour] = updated_dist
                heapq.heappush(pqueue, (updated_dist, neighbour))
    
    print(distances[target])


if __name__ == "__main__":
    main()
