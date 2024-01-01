#include "dijkstra.hpp"
#include <queue>
#include <algorithm>

const int INF = 1000000000;

/*
The function below takes a weighted graph and a source vertex
as input and returns a list of shortest distances from the source
vertex to all other vertices of the graph. All the weights are
assummed to be non-negative numbers. The function utilizes
the Dijkstra's algorithm to calculate the distances.
*/

std::vector<Path> dijkstra(
    const std::vector<std::vector<std::pair<int, int>>> &graph,
    int source
) {
    std::vector<int> distances(graph.size(), INF);
    std::vector<int> predecessors(graph.size(), -1);

    // min priority queue
    std::priority_queue<
        std::pair<int, int>,
        std::vector<std::pair<int, int>>,
        std::greater<std::pair<int, int>>
        > queue;

    distances[source] = 0;
    queue.push(std::make_pair(0, source));

    while (!queue.empty()) {
        int currentVtx = queue.top().second;
        int currentVtxDistance = queue.top().first;
        queue.pop();

        if (currentVtxDistance > distances[currentVtx]) {
            continue;
        }

        for (int i = 0; i < graph[currentVtx].size(); i++) {
            int neighbourVtx = graph[currentVtx][i].first;
            int currentToNeighbourDistance = graph[currentVtx][i].second;
            int newDistance = distances[currentVtx] + currentToNeighbourDistance;

            if (newDistance < distances[neighbourVtx]) {
                distances[neighbourVtx] = newDistance;
                predecessors[neighbourVtx] = currentVtx;
                queue.push(std::make_pair(distances[neighbourVtx], neighbourVtx));
            }
        }
    }

    return buildShortestPaths(source, distances, predecessors);
}

std::vector<Path> buildShortestPaths(
    int source,
    const std::vector<int> &distances,
    const std::vector<int> &predecessors
) {
    std::vector<Path> paths;

    std::vector<int> path;
    int vtx = 0;

    for (int target = 0; target < distances.size(); target++) {
        if (target == source) {
            continue;
        }

        path.clear();
        vtx = target;

        while (vtx != -1) {
            path.push_back(vtx);
            vtx = predecessors[vtx];
        }

        std::reverse(path.begin(), path.end());
        paths.push_back(Path(distances[target], path));
    }

    return paths;
}

void Path::print() const {
    for (int i = 0; i < vertices.size() - 1; i++) {
        std::cout << vertices[i] << " -> ";
    }
    std::cout << vertices.back() << " (" << distance << ")" << std::endl;
}
