
def find_connected_components(graph):
    connected_components = []
    visited = [False for _ in range(len(graph))]
    
    for vtx in range(len(graph)):
        if visited[vtx]:
            continue
        
        visited[vtx] = True
        connected_components.append([vtx])
        dfs_stack = [vtx]
        
        while len(dfs_stack) > 0:
            curr_vtx = dfs_stack.pop()

            for neighbour in graph[curr_vtx]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    connected_components[-1].append(neighbour)
                    dfs_stack.append(neighbour)
    
    return connected_components


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def connected(component1, component2, segments, points):
    return False


def main():
    n, m = map(int, input().split())

    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    
    segments = set()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        point_from, point_to = map(lambda x: int(x) - 1, input().split())
        segments.add((point_from, point_to))
        graph[point_from].append(point_to)
        graph[point_to].append(point_from)
    
    connected_components = find_connected_components(graph)
    num_components = len(connected_components)

    components_graph = [[] for _ in range(num_components)]

    for i in range(num_components):
        for j in range(i + 1, num_components):
            if connected(
                connected_components[i],
                connected_components[j],
                segments, points
            ):
                components_graph[i].append(j)
                components_graph[j].append[i]
    
    connected_components = find_connected_components(components_graph)

    if connected_components == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
