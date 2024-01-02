#include <iostream>
#include <vector>

#include "utils.hpp"
#include "dfs.hpp"
#include "bfs.hpp"
#include "dijkstra.hpp"
#include "bellman_ford.hpp"
#include "ford_fulkerson.hpp"

void runFordFulkerson() {
    std::vector<std::vector<std::pair<int, int>>> graph;
    bool isDirected = true;

    readGraph(graph, isDirected);

    std::cout << "Network:" << std::endl;
    printGraph(graph);

    std::cout << "Max flow from 0 to " << graph.size() - 1;
    std::cout << ": " << fordFulkerson(graph) << std::endl;
}

void runDijkstra() {
    std::vector<std::vector<std::pair<int, int>>> graph;
    bool isDirected = false;

    readGraph(graph, isDirected);

    std::cout << "Graph:" << std::endl;
    printGraph(graph);

    int source = 4;
    std::vector<Path> shortestPaths = dijkstra(graph, source);
    // std::vector<Path> shortestPaths = dijkstraModified(graph, source);

    std::cout << "Shortest paths: " << std::endl;
    for (const auto &path : shortestPaths) {
        path.print();
    }
}

void runBellmanFord() {
    std::vector<std::vector<std::pair<int, int>>> graph;
    bool isDirected = false;

    readGraph(graph, isDirected);

    std::cout << "Graph:" << std::endl;
    printGraph(graph);

    int source = 4;
    std::vector<int> distances = bellmanFord(graph, source);

    for (int i = 0; i < distances.size(); i++) {
        std::cout << i << ": " << distances[i] << std::endl;
    }
}

void runDepthFirstSearch() {
    std::vector<std::vector<int>> graph;
    bool isDirected = false;

    readGraph(graph, isDirected);

    std::cout << "Graph:" << std::endl;
    printGraph(graph);

    std::vector<std::vector<int>> connectedComponents = depthFirstSearch(graph);
    printConnectedComponents(connectedComponents);
}

void runBreadthFirstSearch() {
    std::vector<std::vector<int>> graph;
    bool isDirected = false;

    readGraph(graph, isDirected);

    std::cout << "Graph:" << std::endl;
    printGraph(graph);

    int source = 4;
    std::vector<int> distances = breadthFirstSearch(graph, source);

    for (int i = 0; i < distances.size(); i++) {
        std::cout << i << ": " << distances[i] << std::endl;
    }
}

int main() {
    // cat resources/*.txt | ./bin/main

    // runFordFulkerson();
    // runDijkstra();
    // runBellmanFord();
    // runDepthFirstSearch();
    // runBreadthFirstSearch();

    return 0;
}
