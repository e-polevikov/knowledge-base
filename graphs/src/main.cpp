#include <iostream>
#include <vector>

#include "utils.hpp"
#include "dfs.hpp"
#include "bfs.hpp"
#include "dijkstra.hpp"
#include "bellman_ford.hpp"

int main() {
    std::vector<std::vector<std::pair<int, int>>> graph;

    readGraph(graph);
    printGraph(graph);

    // std::vector<int> distances = dijkstra(graph, 4);
    std::vector<int> distances = bellman_ford(graph, 4);

    /*
    std::vector<std::vector<int>> connectedComponents = depthFirstSearch(graph);
    printConnectedComponents(connectedComponents);

    std::vector<int> distances = breadthFirstSearch(graph, 4);
    */

    for (int i = 0; i < distances.size(); i++) {
        std::cout << i << ": " << distances[i] << std::endl;
    }

    return 0;
}
