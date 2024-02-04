#include "bellman_ford.hpp"

const int INF = 1000000000;

std::vector<int> bellmanFord(
    const std::vector<std::vector<std::pair<int, int>>> &graph,
    int source
) {
    std::vector<int> distances(graph.size(), INF);
    distances[source] = 0;

    for (int i = 0; i < graph.size() - 1; i++) {
        for (int vtx = 0; vtx < graph.size(); vtx++) {
            if (distances[vtx] == INF) {
                continue;
            }

            for (const auto& edges : graph[vtx]) {
                int neighbourVtx = edges.first;
                int vtxToNeighbourDist = edges.second;

                if (distances[vtx] + vtxToNeighbourDist < distances[neighbourVtx]) {
                    distances[neighbourVtx] = distances[vtx] + vtxToNeighbourDist;
                }
            }
        }
    }

    return distances;
}
