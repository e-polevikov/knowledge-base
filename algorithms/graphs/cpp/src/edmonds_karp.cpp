#include "edmonds_karp.hpp"
#include <vector>
#include <queue>
#include <algorithm>

namespace {

struct Edge {
    int vtxTo;
    int capacity;
    int initialCapacity;

    Edge(int vtxTo, int capacity, int initialCapacity) 
        : vtxTo(vtxTo)
        , capacity(capacity)
        , initialCapacity(initialCapacity)
    { }
};

const int INF = 1000000000;

std::vector<std::vector<Edge>> buildResidualNetwork(
    const std::vector<std::vector<std::pair<int, int>>> &network
) {
    std::vector<std::vector<Edge>> residualNetwork(network.size());

    for (int i = 0; i < network.size(); i++) {
        for (int j = 0; j < network[i].size(); j++) {
            int vtxFrom = i;
            int vtxTo = network[i][j].first;
            int capacity = network[i][j].second;

            residualNetwork[vtxFrom].push_back(Edge(vtxTo, capacity, capacity));
            residualNetwork[vtxTo].push_back(Edge(vtxFrom, 0, 0));
        }
    }

    return residualNetwork;
}

bool augmentingPathExists(
    const std::vector<std::vector<Edge>> &residualNetwork,
    std::vector<int> &predecessors,
    int &pathFlow
) {
    std::vector<bool> visited(residualNetwork.size(), false);
    std::queue<int> bfsQueue;

    int source = 0;
    int target = residualNetwork.size() - 1;

    visited[source] = true;
    bfsQueue.push(source);

    std::fill(predecessors.begin(), predecessors.end(), -1);
    pathFlow = INF;

    while (!bfsQueue.empty()) {
        int currentVtx = bfsQueue.front();
        bfsQueue.pop();

        for (int i = 0; i < residualNetwork[currentVtx].size(); i++) {
            int neighbourVtx = residualNetwork[currentVtx][i].vtxTo;
            int capacity = residualNetwork[currentVtx][i].capacity;

            if (!visited[neighbourVtx] && capacity > 0) {
                visited[neighbourVtx] = true;
                predecessors[neighbourVtx] = currentVtx;
                bfsQueue.push(neighbourVtx);
                pathFlow = std::min(pathFlow, capacity);
            }
        }
    }

    return visited[target];
}

std::vector<int> reconstructPath(std::vector<int> &predecessors) {
    std::vector<int> path;
    int source = 0;
    int target = predecessors.size() - 1;
    int predecessor = predecessors[target];

    path.push_back(target);
    while (predecessor != -1) {
        path.push_back(predecessor);
        predecessor = predecessors[predecessor];
    }
    
    std::reverse(path.begin(), path.end());

    return path;
}

void sendFlow(
    std::vector<std::vector<Edge>> &residualNetwork,
    const std::vector<int> &augmentingPath,
    int pathFlow
) {
    for (int i = 0; i < augmentingPath.size() - 1; i++) {
        int vtxFrom = augmentingPath[i];
        int vtxTo = augmentingPath[i + 1];

        for (int j = 0; j < residualNetwork[vtxFrom].size(); j++) {
            if (residualNetwork[vtxFrom][j].vtxTo == vtxTo) {
                residualNetwork[vtxFrom][j].capacity -= pathFlow;
                break;
            }
        }

        for (int j = 0; j < residualNetwork[vtxTo].size(); j++) {
            if (residualNetwork[vtxTo][j].vtxTo == vtxFrom) {
                residualNetwork[vtxTo][j].capacity += pathFlow;
                break;
            }
        }
    }
}

Flow reconstructFlow(
    std::vector<std::vector<Edge>> &residualNetwork,
    int maxFlow
) {
    Flow flow = Flow(maxFlow);

    for (int i = 0; i < residualNetwork.size(); i++) {
        for (int j = 0; j < residualNetwork[i].size(); j++) {
            Edge edge = residualNetwork[i][j];

            if (edge.initialCapacity > 0) {
                flow.edges.push_back(EdgeFlow(
                    i, edge.vtxTo,
                    edge.initialCapacity - edge.capacity
                ));
            }
        }
    }

    return flow;
}

}

Flow edmondsKarp(
    const std::vector<std::vector<std::pair<int, int>>> &network
) {
    std::vector<std::vector<Edge>> residualNetwork = buildResidualNetwork(network);
    std::vector<int> predecessors(residualNetwork.size(), -1);
    int maxFlow = 0;
    int pathFlow = INF;

    while (augmentingPathExists(residualNetwork, predecessors, pathFlow)) {
        std::vector<int> augmentingPath = reconstructPath(predecessors);
        sendFlow(residualNetwork, augmentingPath, pathFlow);
        maxFlow += pathFlow;
    }

    Flow flow = reconstructFlow(residualNetwork, maxFlow);

    return flow;
}
