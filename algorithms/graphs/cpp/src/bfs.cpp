#include "bfs.hpp"
#include <queue>

/*
A function takes an unweighted graph and a source vertex as
input and returns a list of shortest distances
from the source vertex to all other vertices of
the graph. If some vertex is not reachable from
the source, its distance is set to -1. The function
utilizes the breadth-first search algorithm to find
the shortest distances.

Time complexity: O(V + E)
Memory: O(V)
*/

std::vector<int> breadthFirstSearch(
    const std::vector<std::vector<int>> &graph,
    int source
) {
    std::vector<int> distances(graph.size(), -1);
    std::vector<bool> visited(graph.size(), false);
    std::queue<int> bfsQueue;

    visited[source] = true;
    distances[source] = 0;
    bfsQueue.push(source);

    while (!bfsQueue.empty()) {
        int currentVtx = bfsQueue.front();
        bfsQueue.pop();

        for (int i = 0; i < graph[currentVtx].size(); i++) {
            int neighbourVtx = graph[currentVtx][i];

            if (!visited[neighbourVtx]) {
                visited[neighbourVtx] = true;
                distances[neighbourVtx] = distances[currentVtx] + 1;
                bfsQueue.push(neighbourVtx);
            }
        }
    }

    return distances;
}
