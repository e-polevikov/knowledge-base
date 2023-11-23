#include "dijkstra.hpp"
#include <queue>

#include <iostream>

const int INF = 1000000000;

// The function below takes a weighted graph and a source vertex
// as input and returns a list of shortest distances from the source
// vertex to all other vertices of the graph. All the distances should
// be non-negative numbers. The function utilizes the Dijkstra's
// algorithm to calculate these distances.
//
// Time complexity: O(V * log(V) + E * log(V))
// Memory: O(V)
std::vector<int> dijkstra(
    const std::vector<std::vector<std::pair<int, int>>> &graph,
    int source
) {
    std::vector<int> distances(graph.size(), INF);
    std::vector<bool> visited(graph.size(), false);

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
        queue.pop();

        if (visited[currentVtx]) {
            continue;
        }

        visited[currentVtx] = true;

        for (int i = 0; i < graph[currentVtx].size(); i++) {
            int neighbourVtx = graph[currentVtx][i].first;
            int neighbourVtxDistance = graph[currentVtx][i].second;

            if (distances[currentVtx] + neighbourVtxDistance < distances[neighbourVtx]) {
                distances[neighbourVtx] = distances[currentVtx] + neighbourVtxDistance;
                queue.push(std::make_pair(distances[neighbourVtx], neighbourVtx));
            }
        }
    }

    return distances;
}