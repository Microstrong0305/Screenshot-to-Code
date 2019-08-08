class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return  0
        dp = [0 for _ in range(0, len(prices))]
        for i in range(1,len(prices)):
            diff_profit = prices[i] - prices[i-1]
            if diff_profit + dp[i-1] <= 0:
                dp[i] = 0
            else:
                dp[i] = diff_profit + dp[i-1]
        return  max(dp)

solution = Solution()
# test 1
#stock = [7, 1, 5, 3, 6, 4]
# test 2
# stock = [7, 6, 4, 3, 1]
# test 3
stock = []
print(solution.maxProfit(stock))





