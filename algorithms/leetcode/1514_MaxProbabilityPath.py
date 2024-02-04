import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """

        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        
        probabilities = [0.0 for _ in range(n)]
        probabilities[start_node] = 1.0
        pqueue = [(-1.0, start_node)]

        while len(pqueue) > 0:
            p, vtx = heapq.heappop(pqueue)
            p *= -1

            if p > probabilities[vtx]:
                continue

            for neighbour, neighbour_p in graph[vtx]:
                updated_p = p * neighbour_p
                if updated_p > probabilities[neighbour]:
                    probabilities[neighbour] = updated_p
                    heapq.heappush(pqueue, (-updated_p, neighbour))

        return probabilities[end_node]
