class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        prices = [[float("inf") for _ in range(n)] for _ in range(n)]
        distances = [[float("inf") for _ in range(n)] for _ in range(n)]

        for flight in flights:
            prices[flight[0]][flight[1]] = flight[2]

        for i in range(n):
            distances[i][0] = prices[src][i]
        
        for j in range(1, n):
            for i in range(n):
                for t in range(n):
                    distances[i][j] = min(
                        distances[i][j],
                        distances[t][j - 1] + prices[t][i]
                    )

        min_distance = distances[dst][0]
        for i in range(1, min(k + 1, n)):
            min_distance = min(min_distance, distances[dst][i])

        return min_distance if min_distance != float("inf") else -1
