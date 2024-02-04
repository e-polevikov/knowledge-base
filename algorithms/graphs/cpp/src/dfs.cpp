#include "dfs.hpp"
#include <stack>
#include <iostream>

/*
A function takes an unweighted graph as input
and returns a list of connected components of this graph.
The function applies the depth-first search algorithm
to find the components in the graph.

Time complexity: O(V + E)
Memory: O(V)
*/

std::vector<std::vector<int>> depthFirstSearch(
    const std::vector<std::vector<int>> &graph
) {
    std::vector<std::vector<int>> connectedComponents;
    std::stack<int> dfsStack;
    std::vector<bool> visited(graph.size(), false);

    for (int i = 0; i < visited.size(); i++) {
        if (visited[i]) {
            continue;
        }
        
        int currentVtx = i;
        visited[currentVtx] = true;
        dfsStack.push(currentVtx);
        connectedComponents.push_back(std::vector<int>());

        while (!dfsStack.empty()) {
            currentVtx = dfsStack.top();
            dfsStack.pop();
            
            connectedComponents.back().push_back(currentVtx);

            for (int j = 0; j < graph[currentVtx].size(); j++) {
                int neighbourVtx = graph[currentVtx][j];
                if (!visited[neighbourVtx]) {
                    visited[neighbourVtx] = true;
                    dfsStack.push(neighbourVtx);
                }
            }
        }
    }

    return connectedComponents;
}

void printConnectedComponents(
    const std::vector<std::vector<int>> &connectedComponents
) {
    for (const auto& component : connectedComponents) {
        for (auto vtx : component) {
            std::cout << vtx << ' ';
        }
        std::cout << std::endl;
    }
}
