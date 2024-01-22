

def main():
    n = int(input())
    graph = [[] for _ in range(n)]

    for vtx in range(n):
        neighbours = list(map(lambda x: int(x) - 1, input().split()[:-1]))
        
        for neighbour in neighbours:
            graph[vtx].append(neighbour)
            graph[neighbour].append(vtx)

    colors = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    dfs_stack = [0]

    while len(dfs_stack) > 0:
        vtx = dfs_stack.pop()
        visited[vtx] = True

        for neighbour in graph[vtx]:
            if not visited[neighbour]:
                visited[neighbour] = True
                colors[neighbour] = (colors[vtx] + 1) % 2
                dfs_stack.append(neighbour)
            elif colors[vtx] == colors[neighbour]:
                print(-1)
                return

    print("".join(map(str, colors)))


if __name__ == "__main__":
    main()
