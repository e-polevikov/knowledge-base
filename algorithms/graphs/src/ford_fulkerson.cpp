#include "ford_fulkerson.hpp"
#include <vector>

const int INF = 1000000000;

int fordFulkerson(
    const std::vector<std::vector<std::pair<int, int>>> &network
) {
    // Build a graph that contains all edges from the initial network
    // and for each edge includes a reverse edge with zero capacity.
    std::vector<std::vector<std::pair<int, int>>> graph(network.size());

    for (int i = 0; i < network.size(); i++) {
        for (int j = 0; j < network[i].size(); j++) {
            int vtxFrom = i;
            int vtxTo = network[i][j].first;
            int capacity = network[i][j].second;

            graph[vtxFrom].push_back(std::make_pair(vtxTo, capacity));
            graph[vtxTo].push_back(std::make_pair(vtxFrom, 0));
        }
    }

    int source = 0;
    int target = graph.size() - 1;
    int maxFlow = 0;
    std::vector<bool> visited(graph.size(), false);
    std::vector<int> path;
    bool targetReachableFromSource = true;

    while (targetReachableFromSource) {
        int currentVtx = source;
        int minCapacity = INF;
        std::fill(visited.begin(), visited.end(), false);
        path.clear();

        // Find any path from source to target
        // and save min capacity of path edges
        visited[currentVtx] = true;
        path.push_back(currentVtx);

        while (currentVtx != target && !path.empty()) {
            bool neighbourVtxFound = false;

            for (int i = 0; i < graph[currentVtx].size(); i++) {
                int neighbourVtx = graph[currentVtx][i].first;
                int edgeCapacity = graph[currentVtx][i].second;

                if (!visited[neighbourVtx] && edgeCapacity > 0) {
                    neighbourVtxFound = true;
                    visited[neighbourVtx] = true;
                    minCapacity = std::min(minCapacity, edgeCapacity);
                    path.push_back(neighbourVtx);
                    currentVtx = neighbourVtx;
                    break;
                }
            }

            if (!neighbourVtxFound) {
                path.pop_back();
                currentVtx = path[path.size() - 1];
            }
        }
        
        // If a target vertext is not reachable
        // on the current iteration, stop the algorithm.

        if (currentVtx != target) {
            targetReachableFromSource = false;
            break;
        }

        // Decrease capacity of path edges by min capacity and
        // increase capacity of path inverse edges by min capacity
        for (int i = 0; i < path.size() - 1; i++) {
            int vtxFrom = path[i];
            int vtxTo = path[i + 1];

            for (int j = 0; j < graph[vtxFrom].size(); j++) {
                if (graph[vtxFrom][j].first == vtxTo) {
                    graph[vtxFrom][j].second -= minCapacity;
                    break;
                }
            }

            for (int j = 0; j < graph[vtxTo].size(); j++) {
                if (graph[vtxTo][j].first == vtxFrom) {
                    graph[vtxTo][j].second += minCapacity;
                    break;
                }
            }
        }

        maxFlow += minCapacity;
    }

    return maxFlow;
}
