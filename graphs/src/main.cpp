#include <iostream>
#include <vector>

#include "utils.hpp"
#include "dfs.hpp"

int main() {
    std::vector<std::vector<int>> graph;

    readGraph(graph);
    printGraph(graph);

    std::vector<std::vector<int>> connectedComponents = depthFirstSearch(graph);
    printConnectedComponents(connectedComponents);

    return 0;
}
