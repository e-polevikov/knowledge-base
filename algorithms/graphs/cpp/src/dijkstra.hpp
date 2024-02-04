#include <vector>
#include <iostream>

struct Path {
    int distance;
    std::vector<int> vertices;

    Path(int distance, const std::vector<int> &vertices)
        : distance(distance)
        , vertices(vertices)
    { }

    void print() const;
};

std::vector<Path> dijkstra(
    const std::vector<std::vector<std::pair<int, int>>> &graph,
    int source
);

std::vector<Path> dijkstraModified(
    const std::vector<std::vector<std::pair<int, int>>> &graph,
    int source
);

std::vector<Path> buildShortestPaths(
    int source,
    const std::vector<int> &distances,
    const std::vector<int> &predecessors
);
