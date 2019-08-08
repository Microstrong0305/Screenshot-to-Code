class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[1] * col for _ in range(row)]

        for i in range(0, row):
            for j in range(0, col):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

solution = Solution()
obstacleGrid = [[0,0],[1,1],[0,0]]
print(solution.uniquePathsWithObstacles(obstacleGrid))