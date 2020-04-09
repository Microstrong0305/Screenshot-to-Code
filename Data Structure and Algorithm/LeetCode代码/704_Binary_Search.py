from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums is None or len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    sol = Solution()
    print(sol.search(nums, 9))
