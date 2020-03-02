class Solution:
	def maxSubArray(self, nums):
		nums_len = len(nums)
		result = [0 for i in range(nums_len)]
		maxSum = result[0] = nums[0]
		for i in range(1, nums_len):
			if nums[i] >= result[i-1] + nums[i]:
				result[i] = nums[i]
			else:
				result[i] = result[i-1] + nums[i]

			if maxSum <= result[i]:
				maxSum = result[i]
		return maxSum


if __name__ == '__main__':
	nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	sol = Solution()
	print(sol.maxSubArray(nums))