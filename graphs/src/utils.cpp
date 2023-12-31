#include "utils.hpp"

// For unweighted graphs
void readGraph(std::vector<std::vector<int>> &graph, bool isDirected) {
    int numVertices = 0;
    int numEdges = 0;

    std::cin >> numVertices;
    std::cin >> numEdges;

    graph.resize(numVertices);

    for (int i = 0; i < numEdges; i++) {
        int vtxFrom, vtxTo;

        std::cin >> vtxFrom >> vtxTo;

        graph[vtxFrom].push_back(vtxTo);

        if (!isDirected) {
            graph[vtxTo].push_back(vtxFrom);
        }
    }
}

// For unweighted graphs
void printGraph(const std::vector<std::vector<int>> &graph) {
    for (int i = 0; i < graph.size(); i++) {
        std::cout << i << ": ";
        for (int j = 0; j < graph[i].size(); j++) {
            std::cout << graph[i][j] << " "; 
        }
        std::cout << std::endl;
    }
}

// For weighted graphs
void readGraph(
    std::vector<std::vector<std::pair<int, int>>> &graph,
    bool isDirected
) {
    int numVertices = 0;
    int numEdges = 0;

    std::cin >> numVertices;
    std::cin >> numEdges;

    graph.resize(numVertices);

    for (int i = 0; i < numEdges; i++) {
        int vtxFrom, vtxTo, weight;

        std::cin >> vtxFrom >> vtxTo >> weight;

        graph[vtxFrom].push_back(std::make_pair(vtxTo, weight));

        if (!isDirected) {
            graph[vtxTo].push_back(std::make_pair(vtxFrom, weight));
        }
    }
}

// For weighted graphs
void printGraph(const std::vector<std::vector<std::pair<int, int>>> &graph) {
    for (int i = 0; i < graph.size(); i++) {
        std::cout << i << ": ";
        for (int j = 0; j < graph[i].size(); j++) {
            std::cout << "(" << graph[i][j].first << ", " << graph[i][j].second << ") "; 
        }
        std::cout << std::endl;
    }
}
