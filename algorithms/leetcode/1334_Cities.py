import heapq


class Solution(object):
    def dijkstra(self, graph, source, distanceThreshold):
        distances = [float("Inf")] * len(graph)
        
        distances[source] = 0
        queue = [(0, source)]

        while len(queue) > 0:
            distance, vtx = heapq.heappop(queue)

            if distance > distances[vtx]:
                continue
            
            for neighbour, weight in graph[vtx]:
                updatedDistance = distance + weight

                if updatedDistance > distanceThreshold:
                    continue
                
                if updatedDistance < distances[neighbour]:
                    distances[neighbour] = updatedDistance
                    heapq.heappush(queue, (updatedDistance, neighbour))
        
        return distances


    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """

        graph = [[] for _ in range(n)]
        vtxMin, minCities = 0, float("Inf")

        for edge in edges:
            vtxFrom, vtxTo, weight = edge
            graph[vtxFrom].append((vtxTo, weight))
            graph[vtxTo].append((vtxFrom, weight))
        
        for vtx in range(n):
            distances = self.dijkstra(graph, vtx, distanceThreshold)
            print(distances)
            numReachableCities = len(list(filter(lambda dist: dist > 0 and dist != float("Inf"), distances)))
            print(numReachableCities)

            if numReachableCities <= minCities:
                vtxMin = vtx
                minCities = numReachableCities

        return vtxMin
        

def main():
    n = 5
    edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    distanceThreshold = 2

    solution = Solution()
    print(solution.findTheCity(n, edges, distanceThreshold))


if __name__ == "__main__":
    main()
