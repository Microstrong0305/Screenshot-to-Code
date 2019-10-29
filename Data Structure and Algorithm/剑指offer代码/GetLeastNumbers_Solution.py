# -*- coding:utf-8 -*-

# 方法一：快排
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         if len(tinput) < k or len(tinput) == 0:
#             return []
#         list = self.Sort(tinput, 0, len(tinput) - 1)
#         return list[0:k]
#
#     def Sort(self, array, low, high):
#         if low < high:
#             index = self.partition(array, low, high)
#             self.Sort(array, low, index - 1)
#             self.Sort(array, index + 1, high)
#         return array
#
#     def partition(self, array, low, high):
#         key = array[low]
#         while low < high:
#             while low < high and array[high] >= key:
#                 high = high - 1
#             array[low] = array[high]
#             while low < high and array[low] <= key:
#                 low = low + 1
#             array[high] = array[low]
#         array[high] = key
#         return high

# 方法二：基于Partition函数O(n)的算法
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         # write code here
#         # 空列表
#         if tinput == None or len(tinput) == 0 or len(tinput) < k:
#             return []
#
#         index = self.partition(tinput, 0, len(tinput) - 1)
#         while index != k - 1:
#             if index > k - 1:
#                 index = self.partition(tinput, 0, index - 1)
#             else:
#                 index = self.partition(tinput, index + 1, len(tinput) - 1)
#
#         return sorted(tinput[:k])
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


import heapq

"""
Python中的heapq模块用来建立“堆”这种数据结构。
heapq.heappush(res, -i) 意为：向堆res中添加一个元素-i
heapq.heappushpop(res, -i)意为：将元素-i与堆顶的元素比较。如果该元素值大于堆顶元素，则将该元素与堆顶元素替换。否则不改变堆元素。
"""


# 方法三：最大堆，O(nlogk)
class Solution:
    # def GetLeastNumbers_Solution(self, tinput, k):
    #     if len(tinput) < k:
    #         return []
    #     res = []
    #     for i in tinput:
    #         heapq.heappush(res, -i) if len(res) < k else heapq.heappushpop(res, -i)
    #     return sorted(list(map(lambda x: -x, res)))
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        return heapq.nsmallest(k, tinput)


'''
Reference:
[1] https://blog.csdn.net/u010005281/article/details/80084994
[2] https://blog.csdn.net/fuxuemingzhu/article/details/79637795
'''

if __name__ == '__main__':
    tinput = [4, 5, 1, 6, 2, 7, 3, 8]
    solution = Solution()
    print(solution.GetLeastNumbers_Solution(tinput, 4))
