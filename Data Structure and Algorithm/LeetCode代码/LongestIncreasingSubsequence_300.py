class Solution:

    def lengthOfLIS(self, nums):
        '''
        :param nums: List[int]
        :return:
        '''
        if len(nums) == 0 :
            return 0
        memo = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
        res = 1
        for i in range(len(nums)):
            res = max(res, memo[i])
        return res

solution = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.lengthOfLIS(nums))