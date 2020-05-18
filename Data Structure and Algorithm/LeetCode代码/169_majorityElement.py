from typing import List


class Solution:

    # 方法一： 快排
    def majorityElement(self, nums: List[int]) -> int:
        # 快排
        nums = self.quickSort(nums, 0, len(nums) - 1)
        # 直接返回中位值
        return nums[len(nums) // 2]

    def quickSort(self, nums, low, high):
        if low < high:
            index = self.partition(nums, low, high)
            self.quickSort(nums, low, index - 1)
            self.quickSort(nums, index + 1, high)
        return nums

    def partition(self, nums, low, high):
        key = nums[low]
        while low < high:
            while low < high and nums[high] >= key:
                high -= 1
            nums[low] = nums[high]

            while low < high and nums[low] <= key:
                low += 1
            nums[high] = nums[low]

        nums[high] = key

        return high

    # 方法二：基于Partition函数的时间复杂度为O(n)算法
    def majorityElement2(self, nums: List[int]) -> int:
        middle = len(nums) // 2
        index = self.partition(nums, 0, len(nums) - 1)
        while index != middle:
            if index > middle:
                index = self.partition(nums, 0, index - 1)
            else:
                index = self.partition(nums, index + 1, len(nums) - 1)

        return nums[middle]

    # 方法三：用字典统计
    def majorityElement3(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
                if dic[i] > (len(nums) // 2):
                    return i
            else:
                dic[i] = 1


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majorityElement3(nums))
