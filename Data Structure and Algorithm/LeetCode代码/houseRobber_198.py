class Solution:

    def __init__(self):
        # memo[i]表示考虑抢劫nums[i:n]所能获得的最大收益
        self.memo = []

    # The third method : dynamic programming
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        self.memo = [-1 for _ in range(nums_len)]
        self.memo[nums_len - 1] = nums[nums_len - 1]
        for i in range(nums_len - 1, -1, -1):
            for j in range(i, nums_len):
                A = self.memo[i]
                if j + 2 < nums_len :
                    B = nums[j] + self.memo[j + 2]
                else:
                    B = nums[j]
                self.memo[i] = max(A, B)
        return  self.memo[0]

solution = Solution()
#test 1
#nums = [1, 2, 3, 1]
#test 2
nums = [1, 2,]
print(solution.rob(nums))
