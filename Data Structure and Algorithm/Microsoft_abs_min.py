import sys


class Solution:

    # 方法一：暴力穷举
    # 时间复杂度为O(n)
    def getMin(self, nums):
        temp_i = -1
        temp_j = -1
        length = len(nums)
        min_ = sys.maxsize
        for i in range(length - 1):
            for j in range(i + 1, length - 1):
                current = abs(nums[i] - nums[j])
                min_ = min(min_, current)
                if min_ == current:
                    temp_i = i
                    temp_j = j
        return (temp_i, temp_j)

    # 方法二：先排序，再求相邻两个数的差值
    # 时间复杂度为0(nlogn)
    def getMin2(self, nums):
        temp_i = -1
        temp_j = -1
        nums.sort()
        min_ = sys.maxsize
        for i in range(1, len(nums)):
            current = abs(nums[i] - nums[i - 1])
            min_ = min(min_, current)
            if min_ == current:
                temp_i = i
                temp_j = i - 1
        return (temp_j, temp_i)

    # 方法三：
    # 设立辅助数组（不排序，直接求相邻两个数的差值）
    def getMin3(self, nums):
        difference = []
        for i in range(1, len(nums)):
            temp = nums[i] - nums[i - 1]
            difference.append(temp)


if __name__ == "__main__":
    nums = [3, 2, 1, 5]
    sol = Solution()
    print(sol.getMin3(nums))
