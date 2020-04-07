from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums) - 1
        if low < high:
            self.QSort(nums, low, high)

        return nums

    def QSort(self, nums, low, high):
        if low < high:
            index = self.Partition(nums, low, high)
            self.QSort(nums, low, index - 1)
            self.QSort(nums, index + 1, high)

    def Partition(self, nums, low, high):
        pivotkey = nums[low]

        while low < high:
            while low < high and nums[high] >= pivotkey:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] < pivotkey:
                low += 1
            nums[high] = nums[low]

        nums[low] = pivotkey
        return high


if __name__ == "__main__":
    # nums = [5, 2, 3, 1]
    nums = [5, 1, 1, 2, 0, 0]
    sol = Solution()
    print(sol.sortArray(nums))
