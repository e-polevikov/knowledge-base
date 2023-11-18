#include <iostream>
#include <vector>

#include "utils.hpp"
#include "dfs.hpp"
#include "bfs.hpp"

int main() {
    std::vector<std::vector<int>> graph;

    readGraph(graph);
    printGraph(graph);

    std::vector<std::vector<int>> connectedComponents = depthFirstSearch(graph);
    printConnectedComponents(connectedComponents);

    std::vector<int> distances = breadthFirstSearch(graph, 4);

    for (int i = 0; i < distances.size(); i++) {
        std::cout << i << ": " << distances[i] << std::endl;
    }

    return 0;
}
