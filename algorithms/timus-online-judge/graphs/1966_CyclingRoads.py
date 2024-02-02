import itertools


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(point1, point2, point3):
    slopes_relation = \
          (point2.y - point1.y) * (point3.x - point2.x) \
        - (point3.y - point2.y) * (point2.x - point1.x)

    # collinear
    if slopes_relation == 0:
        return 0
    
    # clockwise / counterclockwise
    if slopes_relation > 0:
        return 1
    else:
        return 2


def inside_segment(point, segment):
    point1, point2 = segment

    min_x, max_x = min(point1.x, point2.x), max(point1.x, point2.x)
    min_y, max_y = min(point1.y, point2.y), max(point1.y, point2.y)

    return min_x < point.x < max_x and min_y < point.y < max_y


def intersect(point1, point2, point3, point4):
    orientation1 = orientation(point1, point2, point3)
    orientation2 = orientation(point1, point2, point4)
    orientation3 = orientation(point3, point4, point1)
    orientation4 = orientation(point3, point4, point2)

    if orientation1 != orientation2 and orientation3 != orientation4:
        return True
    
    if orientation1 == 0 and inside_segment(point3, (point1, point2)):
        return True

    if orientation2 == 0 and inside_segment(point4, (point1, point2)):
        return True

    if orientation3 == 0 and inside_segment(point1, (point3, point4)):
        return True

    if orientation4 == 0 and inside_segment(point2, (point3, point4)):
        return True

    return False


def connected(component1, component2, segments, points):
    if len(component1) == 1 and len(component2) == 1:
        return False
    
    if len(component1) == 1 or len(component2) == 1:
        point = None
        edges = None

        if len(component1) == 1:
            point = points[component1[0]]
            edges = itertools.permutations(component2, 2)
        else:
            point = points[component2[0]]
            edges = itertools.permutations(component1, 2)

        for edge in edges:
            if edge in segments:
                point1 = points[edge[0]]
                point2 = points[edge[1]]

                if orientation(point, point1, point2) == 0 \
                  and inside_segment(point, (point1, point2)):
                    return True
        
        return False

    edges1 = itertools.permutations(component1, 2)
    edges2 = itertools.permutations(component2, 2)

    for edge1 in edges1:
        for edge2 in edges2:
            if edge1 in segments and edge2 in segments:
              point1 = points[edge1[0]]
              point2 = points[edge1[1]]
              point3 = points[edge2[0]]
              point4 = points[edge2[1]]

              if intersect(point1, point2, point3, point4):
                  return True

    return False


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
                components_graph[j].append(i)

    connected_components = find_connected_components(components_graph)

    if len(connected_components) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
