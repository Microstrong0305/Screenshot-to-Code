from typing import List


class Solution:
    # 方法一： 双指针，时间复杂度为O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 0:
            return None
        low = 0
        high = len(numbers) - 1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low + 1, high + 1]
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                low += 1

    # 方法二：暴力解法（双重循环）,时间复杂度为O(n方)
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 0:
            return None

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

    # 方法三：二分搜索法，时间复杂度为O(n log n)
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            difference = target - numbers[i]
            index = self.search_Bin(numbers, difference, i + 1)
            if index != -1:
                return [i + 1, index + 1]

    def search_Bin(self, numbers, target, start):
        if len(numbers) <= 0:
            return -1
        low = start
        high = len(numbers) - 1
        while low <= high:
            middle = (low + high) // 2
            if numbers[middle] == target:
                return middle
            elif numbers[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
        return -1


if __name__ == "__main__":
    numbers = [2, 3, 4]
    target = 6
    sol = Solution()
    print(sol.twoSum3(numbers, target))
