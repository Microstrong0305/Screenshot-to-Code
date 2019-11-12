# 方法一：动态规划解法
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         if not array:
#             return None
#         if len(array) > 0:
#             res = [0 for _ in range(len(array))]
#             res[0] = array[0]
#             for i in range(1, len(array)):
#                 if res[i - 1] < 0:
#                     res[i] = array[i]
#                 else:
#                     res[i] = res[i - 1] + array[i]
#
#         return max(res)


# 方法二：分析数组的规律
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 0 and not array:
            return None
        maxSun = float('-inf')
        currentSum = 0
        for i in array:
            currentSum += i
            if currentSum < i:
                currentSum = i
            if currentSum > maxSun:
                maxSun = currentSum

        return maxSun


if __name__ == "__main__":
    sol = Solution()
    # arr = [6, -3, -2, 7, -15, 1, 2, 2]
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print(sol.FindGreatestSumOfSubArray(arr))
