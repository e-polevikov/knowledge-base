class Solution(object):
    def visit(self, x, y, matrix, visited, length):
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nextX = x + dx
            nextY = y + dy

            if not (0 <= nextX < len(matrix)):
                continue

            if not (0 <= nextY < len(matrix[0])):
                continue
            
            if matrix[nextX][nextY] <= matrix[x][y]:
                continue

            if not visited[nextX][nextY]:
                self.visit(nextX, nextY, matrix, visited, length + 1)
            
            visited[x][y] = max(visited[x][y], visited[nextX][nextY] + 1)


    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        nRows = len(matrix)
        nCols = len(matrix[0])

        visited = [[0 for _ in range(nCols)] for _ in range(nRows)]

        for i in range(nRows):
            for j in range(nCols):
                if not visited[i][j]:
                    self.visit(i, j, matrix, visited, 0)
        
        maxLen = max(map(max, visited))

        return maxLen + 1

def main():
    matrix = [
        [1, 1, 4],
        [2, 1, 3],
        [3, 1, 2],
        [4, 1, 1]
    ]

    solution = Solution()
    print(solution.longestIncreasingPath(matrix))


if __name__ == "__main__":
    main()
