class Solution:

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        self.arr = [0 for _ in range(len(nums))]
        return max(self.getRob(nums, self.arr, 0, len(nums)-2),
                   self.getRob(nums, self.arr, 1, len(nums)-1))

    def getRob(self, nums, arr, start, end):
        """
        :param nums: list[int]
        :param arr:  list[int]
        :param start: int
        :param end: int
        :return:
        """
        arr[start] = nums[start]
        arr[start + 1] =max(nums[start], nums[start + 1])
        for i in range(start+2,end + 1):
            arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
        return  arr[end]

solution = Solution()
# test 1
# nums = []
# test 2
# nums = [2, 3]
# test 3
nums = [2, 3, 2]
print(solution.rob(nums))