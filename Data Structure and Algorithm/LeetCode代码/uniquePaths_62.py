class Solution:
    def uniquePaths(self, m, n):
        '''
        :param m: int 格子的列数
        :param n: int 格子的行数
        :return:  int  多少条独一无二的路径
        '''
        if not m or not n:
            return 0
        dp = [[1 for i in range(m)] for i in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return  dp[-1][-1]

solution = Solution()
print(solution.uniquePaths(7,3))