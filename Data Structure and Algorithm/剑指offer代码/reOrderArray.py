###########最简单的办法就是利用Python的优点，不用排序直接将奇数和偶数拿出来存放，再合并到一起。##########
# 方法一
# class Solution:
#
#     def reOrderArray(self, array):
#         odd = []
#         even = []
#         for i in range(len(array)):
#             if array[i] & 0x1 == 1:
#                 odd.append(array[i])
#             else:
#                 even.append(array[i])
#
#         return odd + even
#
# sol = Solution()
# # array = [1,4,7,2,9,1,4,7,3,5,11]
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sol.reOrderArray(array))


###########如果要求不能使用额外的空间，那么可以借鉴冒泡排序的思想。如果当前数为偶数，后一个数为奇数，则相互交换。##############################
# 方法二
# class Solution:
#     def reOrderArray(self, array):
#         _len = len(array)
#         for i in range(_len-1):
#             if (array[i] & 0x1 == 0)and (array[i+1] & 0x1 == 1):
#                 temp = array[i]
#                 array[i] = array[i+1]
#                 array[i+1] = temp
#                 for j in range(i, 0, -1):
#                     if (array[j] & 0x1 == 1)and (array[j-1] & 0x1 == 0):
#                         temp = array[j]
#                         array[j] = array[j-1]
#                         array[j-1] = temp
#         return array
#
# sol = Solution()
# # array = [0,1,2,3,4,5,6,7,8,9]
# array = [1,4,7,2,9,1,4,7,3,5,11]
# print(sol.reOrderArray(array))

# # 方法三
# class Solution:
#     def reOrderArray(self, array):
#         for i in range(len(array)):
#             for j in range(len(array)-1):
#                 if array[j] % 2 == 0 and array[j+1] % 2 == 1:
#                     temp = array[j+1]
#                     array[j+1] = array[j]
#                     array[j] = temp
#         return array
#
# sol = Solution()
# array = [0,1,2,3,4,5,6,7,8,9]
# print(sol.reOrderArray(array))

# Reference:
#【1】https://www.jianshu.com/p/ed83c477b6a7
#【2】https://suixinblog.cn/2019/03/target-offer-reorder-array.html

