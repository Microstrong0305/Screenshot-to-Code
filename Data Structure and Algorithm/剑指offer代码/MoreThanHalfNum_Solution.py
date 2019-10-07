# -*- coding:utf-8 -*-

# 方法一：快排+查找
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         sortedList = self.QuickSort(numbers, 0, len(numbers) - 1)
#         for i in sortedList:
#             if sortedList.count(i) > len(sortedList) / 2:
#                 return i
#
#         return 0
#
#     def QuickSort(self, numList, low, high):
#         if low >= high:
#             return numList
#         index = self.partition(numList, low, high)
#         self.QuickSort(numList, low, index - 1)
#         self.QuickSort(numList, index + 1, high)
#
#         return numList
#
#     def partition(self, numList, low, high):
#         key = numList[low]
#         while low < high:
#             while low < high and numList[high] >= key:
#                 high -= 1
#             numList[low] = numList[high]
#
#             while low < high and numList[low] <= key:
#                 low += 1
#             numList[high] = numList[low]
#
#         numList[high] = key
#         return high

# 方法二：
class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        return

if __name__ == "__main__":
    sol = Solution()
    # list = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    list = [1]
    print(sol.MoreThanHalfNum_Solution(list))
