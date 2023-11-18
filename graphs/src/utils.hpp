#include <vector>
#include <iostream>

// For unweighted graphs
void readGraph(std::vector<std::vector<int>> &graph);
void printGraph(const std::vector<std::vector<int>> &graph);

// For weighted graphs
void readGraph(std::vector<std::vector<std::pair<int, int>>> &graph);
void printGraph(const std::vector<std::vector<std::pair<int, int>>> &graph);
