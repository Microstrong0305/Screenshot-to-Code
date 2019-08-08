class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum = 0
        for i in range(len(nums)):
            num_sum += nums[i]

        if num_sum % 2 != 0:
            return False

        n = len(nums)
        C = int(num_sum / 2)
        memo = [False] * (C + 1)

        for i in range(C + 1):
            memo[i] = (nums[0] == i)

        for i in range(1, n):
            for j in range(C, nums[i], -1):
                memo[j] = memo[j] or memo[j - nums[i]]

        return memo[C]

solution = Solution()
# test1
nums = [1, 5, 11, 5]
# test2
# nums = [1, 2, 3, 5]
# test3
# nums = [1, 2, 5]
print(solution.canPartition(nums))
