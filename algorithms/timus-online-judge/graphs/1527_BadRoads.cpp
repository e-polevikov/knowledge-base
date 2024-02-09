#include <iostream>
#include <vector>
#include <unordered_set>

struct Edge {
  int vtxFrom, vtxTo, cost, time, height;

  Edge(int vtxFrom, int vtxTo, int cost, int time, int height)
  : vtxFrom(vtxFrom), vtxTo(vtxTo), cost(cost), time(time), height(height)
  { }
};

struct Constraints {
  int totalCost, totalTime, maxCost, maxTime, maxHeight;

  Constraints(int totalCost, int totalTime, int maxCost, int maxTime, int maxHeight)
    : totalCost(totalCost)
    , totalTime(totalTime)
    , maxCost(maxCost)
    , maxTime(maxTime)
    , maxHeight(maxHeight)
  { }
};

const int INF = 1000000000;

std::vector<int> findPath(
  int numVertices,
  int source, int target,
  const std::vector<Edge> &edges,
  const Constraints &constraints
) {
  int times[numVertices][numVertices];
  int paths[numVertices][numVertices];
  std::vector<int> path;

  for (int i = 0; i < numVertices; i++) {
    for (int j = 0; j < numVertices; j++) {
      times[i][j] = INF;
      paths[i][j] = -1;
    }
  }

  times[source][0] = 0;
  for (int currCost = 0; currCost < numVertices; currCost++) {
    while (true) {
      bool updated = false;

      for (int edgeId = 0; edgeId < edges.size(); edgeId++) {
        Edge edge = edges[edgeId];

        if (edge.height > constraints.maxHeight) {
          continue;
        }

        int updatedTime = INF;

        if (edge.cost == 0) {
          updatedTime = times[edge.vtxFrom][currCost] + edge.time;
        } else if (currCost > 0) {
          updatedTime = times[edge.vtxFrom][currCost - 1] + edge.time;
        }
        
        if (updatedTime < times[edge.vtxTo][currCost]) {
          times[edge.vtxTo][currCost] = updatedTime;
          paths[edge.vtxTo][currCost] = edgeId;
          updated = true;
        }

        if (edge.vtxTo == target &&
          currCost <= constraints.maxCost &&
          times[target][currCost] <= constraints.maxTime
        ) {
          while (edgeId != -1) {
            path.push_back(edgeId + 1);
            target = edges[edgeId].vtxFrom;
            currCost -= edges[edgeId].cost;
            edgeId = paths[target][currCost];            
          }

          return path;
        }
      }

      if (!updated) {
        break;
      }
    }
  }

  return path;
}

int main() {
  std::ios_base::sync_with_stdio(false);

  int numVertices, numEdges, source, target, maxCost, maxTime;
  int minHeight = INF;
  int maxHeight = 0;

  std::cin >> numVertices >> numEdges >> source >> target >> maxCost >> maxTime;

  source -= 1;
  target -= 1;
  
  std::vector<Edge> edges;
  int vtxFrom, vtxTo, cost, time, height;
  for (int i = 0; i < numEdges; i++) {
    std::cin >> vtxFrom >> vtxTo >> cost >> time >> height;
    edges.push_back(Edge(
      vtxFrom - 1, vtxTo - 1, cost, time, height
    ));
    minHeight = std::min(minHeight, height);
    maxHeight = std::max(maxHeight, height);
  }

  Constraints constraints(0, 0, maxCost, maxTime, maxHeight);

  std::vector<int> path = findPath(
    numVertices,
    source, target,
    edges, constraints
  );

  if (path.size() == 0) {
    std::cout << -1 << std::endl;
    return 0;
  }

  int left = minHeight;
  int right = maxHeight;
  int optimalHeight = maxHeight;

  while (left <= right) {
    int currHeight = (left + right) / 2;
    Constraints currConstraints(0, 0, maxCost, maxTime, currHeight);

    std::vector<int> currPath = findPath(
      numVertices,
      source, target,
      edges, currConstraints
    );
    
    if (currPath.size() == 0) {
      left = currHeight + 1;
    } else {
      path = std::move(currPath);
      optimalHeight = currHeight;
      right = currHeight - 1;
    }
  }

  std::cout << optimalHeight << std::endl;
  std::cout << path.size() << std::endl;
  for (int i = 0; i < path.size(); i++) {
    std::cout << path[path.size() - i - 1] << " ";
  }

  return 0;
}
