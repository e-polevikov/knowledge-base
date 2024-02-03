#include <iostream>
#include <vector>
#include <unordered_set>

struct Edge {
  int id, vtxTo, cost, time, height;

  Edge(int id, int vtxTo, int cost, int time, int height)
  : id(id), vtxTo(vtxTo), cost(cost), time(time), height(height)
  { }
};

struct Vertex {
  int id, key;

  Vertex(int id, int key) : id(id), key(key) {} 
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

void buildPath(
  const std::vector<std::vector<Edge>> &graph,
  int target,
  std::vector<Vertex> &orderedPath,
  std::unordered_set<int> &pathVertices,
  Constraints &constraints
) {
  if (orderedPath.back().key == target) {
    return;
  }

  for (const auto& edge : graph[orderedPath.back().key]) {
    if (pathVertices.find(edge.vtxTo) != pathVertices.end()) {
      continue;
    }

    if (constraints.totalCost + edge.cost > constraints.maxCost) {
      continue;
    }

    if (constraints.totalTime + edge.time > constraints.maxTime) {
      continue;
    }

    if (edge.height > constraints.maxHeight) {
      continue;
    }

    orderedPath.push_back(Vertex(edge.id, edge.vtxTo));
    pathVertices.insert(edge.vtxTo);
    constraints.totalCost += edge.cost;
    constraints.totalTime += edge.time;

    buildPath(graph, target, orderedPath, pathVertices, constraints);

    if (orderedPath.back().key == target) {
      return;
    }

    orderedPath.pop_back();
    pathVertices.erase(edge.vtxTo);
    constraints.totalCost -= edge.cost;
    constraints.totalTime -= edge.time;
  }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  int numVertices, numEdges, source, target, maxCost, maxTime;
  int minHeight = 1000000000;
  int maxHeight = 0;

  std::cin >> numVertices >> numEdges >> source >> target >> maxCost >> maxTime;

  source -= 1;
  target -= 1;
  
  std::vector<std::vector<Edge>> graph(numVertices, std::vector<Edge>());
  int vtxFrom, vtxTo, cost, time, height;
  for (int i = 0; i < numEdges; i++) {
    std::cin >> vtxFrom >> vtxTo >> cost >> time >> height;
    graph[vtxFrom - 1].push_back(Edge(
      i + 1, vtxTo - 1, cost, time, height
    ));
    minHeight = std::min(minHeight, height);
    maxHeight = std::max(maxHeight, height);
  }

  std::vector<Vertex> orderedPath;
  std::unordered_set<int> pathVertices;
  Constraints constraints(0, 0, maxCost, maxTime, maxHeight);

  orderedPath.push_back(Vertex(-1, source));
  pathVertices.insert(source);

  buildPath(graph, target, orderedPath, pathVertices, constraints);

  if (orderedPath.back().key != target) {
    std::cout << -1 << std::endl;
    return 0;
  }

  int left = minHeight;
  int right = maxHeight;
  int optimalHeight = maxHeight;

  while (left <= right) {
    int currHeight = (left + right) / 2;
    std::vector<Vertex> currOrderedPath;
    std::unordered_set<int> currPathVertices;
    Constraints currConstraints(0, 0, maxCost, maxTime, currHeight);

    currOrderedPath.push_back(Vertex(-1, source));
    currPathVertices.insert(source);

    buildPath(graph, target, currOrderedPath, currPathVertices, currConstraints);

    if (currOrderedPath.back().key != target) {
      left = currHeight + 1;
    } else {
      orderedPath = std::move(currOrderedPath);
      optimalHeight = currHeight;
      right = currHeight - 1;
    }
  }

  std::cout << optimalHeight << std::endl;
  std::cout << orderedPath.size() - 1 << std::endl;
  for (int i = 1; i < orderedPath.size(); i++) {
    std::cout << orderedPath[i].id << " ";
  }

  return 0;
}
