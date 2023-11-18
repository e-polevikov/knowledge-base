#include <iostream>
#include <vector>

#include "utils.hpp"

int main() {
    std::vector<std::vector<int>> graph;

    readGraph(graph);
    printGraph(graph);

    return 0;
}
