from collections import deque


def find_shortest_distances(graph, source):
    distances = [float("inf") for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    queue = deque()

    queue.append(source)
    visited[source] = True
    distances[source] = 0

    while len(queue) > 0:
        vtx = queue.popleft()

        for neighbour in graph[vtx]:
            if visited[neighbour]:
                continue
            
            visited[neighbour] = True
            distances[neighbour] = distances[vtx] + 1
            queue.append(neighbour)
    
    return distances


def main():
    n_lines = int(input())
    stations = set()
    edges = set()

    for _ in range(n_lines):
        line = list(map(int, input().split()))
        for i in range(1, len(line) - 1):
            station_from = min(line[i], line[i + 1])
            station_to = max(line[i], line[i + 1])

            stations.add(station_from)
            stations.add(station_to)
            edges.add((station_from, station_to))
    
    path = list(map(int, input().split()))
    
    stations = list(sorted(list(stations)))
    stations_ids = {stations[i]: i for i in range(len(stations))}

    metro_graph = [[] for _ in range(len(stations))]
    for edge in edges:
        vtx_from = stations_ids[edge[0]]
        vtx_to = stations_ids[edge[1]]
        metro_graph[vtx_from].append(vtx_to)
        metro_graph[vtx_to].append(vtx_from)
    
    source = stations_ids[path[1]]
    distances = find_shortest_distances(metro_graph, source)

    source = stations_ids[path[-1]]
    visited = [False for _ in range(len(metro_graph))]

    for station in path[1:]:
        visited[stations_ids[station]] = True
    
    queue = deque()
    queue.append(source)
    candidates = [stations[source]]

    while len(queue) > 0:
        vtx = queue.popleft()

        for neighbour in metro_graph[vtx]:
            if visited[neighbour]:
                continue

            if distances[neighbour] == distances[vtx] + 1:
                visited[neighbour] = True
                queue.append(neighbour)
                candidates.append(stations[neighbour])
    
    candidates = "\n".join(list(map(str, sorted(candidates))))
    print(candidates)
    

if __name__ == "__main__":
    main()
