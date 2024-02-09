

class Edge:
    def __init__(self, vtx_from, vtx_to, cost, time, height):
        self.vtx_from = vtx_from
        self.vtx_to = vtx_to
        self.cost = cost
        self.time = time
        self.height = height


def find_paths(n, src, dst, edges, max_cost, max_time, max_height):
    times = [[float("inf") for _ in range(n)] for _ in range(n)]
    paths = [[-1 for _ in range(n)] for _ in range(n)]

    times[src][0] = 0
    for curr_cost in range(n):
        while True:
            updated = False

            for edge_id, edge in enumerate(edges):
                if edge.height > max_height:
                    continue

                updated_time = float("inf")

                if edge.cost == 0:
                    updated_time = times[edge.vtx_from][curr_cost] + edge.time
                elif curr_cost > 0:
                    updated_time = times[edge.vtx_from][curr_cost - 1] + edge.time
                
                if updated_time < times[edge.vtx_to][curr_cost]:
                    times[edge.vtx_to][curr_cost] = updated_time
                    paths[edge.vtx_to][curr_cost] = edge_id
                    updated = True

                if edge.vtx_to == dst and \
                   curr_cost <= max_cost and \
                   times[dst][curr_cost] <= max_time:
                    return curr_cost, paths
                
            if not updated:
                break
    
    return -1, []


def build_path(cost, edges, paths, dst):
    curr_vtx, curr_cost, path = dst, cost, []

    edge_id = paths[curr_vtx][curr_cost]
    while edge_id != -1:
        path.append(edge_id + 1)
        curr_vtx = edges[edge_id].vtx_from
        curr_cost -= edges[edge_id].cost
        edge_id = paths[curr_vtx][curr_cost]

    return path[::-1]


def main():
    n, m, src, dst = map(int, input().split())
    max_cost, max_time = map(int, input().split())

    src -= 1
    dst -= 1

    edges = []
    min_height, max_height = float("inf"), 0

    for _ in range(m):
        vtx_from, vtx_to, cost, time, height = map(int, input().split())
        edges.append(Edge(vtx_from - 1, vtx_to - 1, cost, time, height))
        min_height = min(min_height, height)
        max_height = max(max_height, height)
    
    cost, paths = find_paths(
        n, src, dst, edges,
        max_cost, max_time,
        max_height
    )

    if cost == -1:
        print(-1)
        return
    
    optimal_height = max_height
    left, right = min_height, max_height

    while left <= right:
        curr_height = (left + right) // 2

        curr_cost, curr_paths = find_paths(
            n, src, dst, edges,
            max_cost, max_time,
            curr_height
        )

        if curr_cost == -1:
            left = curr_height + 1
        else:
            cost = curr_cost
            paths = curr_paths
            optimal_height = curr_height
            right = curr_height - 1

    path = build_path(cost, edges, paths, dst)

    print(optimal_height)
    print(len(path))
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()
