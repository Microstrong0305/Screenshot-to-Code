class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :type: int
        """
        if len(prices) <= 1:
            return  0
        hold = [0] * len(prices)
        sold = [0] * len(prices)
        rest = [0] * len(prices)
        hold[0] = -prices[0]
        sold[0] = -float("inf")
        for i in range(1,len(prices)):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
            sold[i] = hold[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sold[i - 1])
        return max(sold[-1], rest[-1])

solution = Solution()
Input = [1, 2, 3, 0, 2]
print(solution.maxProfit(Input))
