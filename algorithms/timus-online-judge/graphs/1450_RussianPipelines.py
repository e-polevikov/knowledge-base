

def get_topological_order(graph):
    def visit(vtx):
        visited[vtx] = True

        for neighbour, _ in graph[vtx]:
            if not visited[neighbour]:
                visit(neighbour)
        
        topological_order.append(vtx)

    n = len(graph)
    topological_order = []
    visited = [False for _ in range(n)]
    
    for vtx in range(n):
        if not visited[vtx]:
            visit(vtx)

    return topological_order[::-1]


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        v_from, v_to, distance = map(int, input().split())
        graph[v_from - 1].append((v_to - 1, distance))
    
    source, target = map(int, input().split())

    source -= 1
    target -= 1

    topological_order = get_topological_order(graph)
    distances = [-1 for _ in range(n)]
    distances[source] = 0
    source_id = topological_order.index(source)

    for i in range(source_id, n):
        vtx = topological_order[i]
        
        if distances[vtx] == -1:
            continue

        for neighbour, distance in graph[vtx]:
            distances[neighbour] = max(
                distances[neighbour],
                distances[vtx] + distance
            )

    if distances[target] != -1:
        print(distances[target])
    else:
        print("No solution")

if __name__ == "__main__":
    main()
