#include "utils.hpp"

void readGraph(std::vector<std::vector<int>> &graph) {
    int numVertices = 0;
    int numEdges = 0;

    std::cin >> numVertices;
    std::cin >> numEdges;

    graph.resize(numVertices);

    for (int i = 0; i < numEdges; i++) {
        int vtxFrom, vtxTo;

        std::cin >> vtxFrom >> vtxTo;

        graph[vtxFrom].push_back(vtxTo);
        graph[vtxTo].push_back(vtxFrom);
    }
}

void printGraph(const std::vector<std::vector<int>> &graph) {
    for (int i = 0; i < graph.size(); i++) {
        std::cout << i << ": ";
        for (int j = 0; j < graph[i].size(); j++) {
            std::cout << graph[i][j] << " "; 
        }
        std::cout << std::endl;
    }
}
