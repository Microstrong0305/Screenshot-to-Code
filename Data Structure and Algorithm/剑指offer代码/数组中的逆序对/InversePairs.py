# class Solution:
#
#     def InversePairs(self, data):
#         data_len = len(data)
#         if data is None or data_len == 0:
#             return None
#
#         count = 0
#         for i in range(data_len):
#             for j in range(i + 1, data_len):
#                 if data[i] > data[j]:
#                     count += 1
#         return count
#
#     def InversePairs2(self, data):
#         if data is None or len(data) <= 0:
#             return 0
#
#         new_data = data
#         count = self.InversePairsCore(data, new_data, 0, len(data))
#
#         return count
#
#     def InversePairsCore(self, data, new_data, low, high):
#         if low == high:
#             new_data[low] = data[low]
#             return 0
#
#         len = (high - low) / 2
#         left = self.InversePairsCore(new_data, data, low, low + len) % 1000000007
#         right = self.InversePairsCore(new_data, data, low + len + 1, high) % 1000000007
#
#         # p1 初始化为前半段最后一个数字的下标
#         p1 = low + len
#         # p2 初始化为后半段最后一个数字的下标
#         p2 = high
#         # 开始拷贝的位置
#         p3 = high
#         # 逆序数
#         count = 0
#         while p1 >= low and p2 >= low + len + 1:
#             if data[p1] > data[p2]:
#                 # 对应的逆序数
#                 count += (p2 - low - len)
#                 new_data[p3] = data[p1]
#                 p3 -= 1
#                 p1 -= 1
#                 if count >= 1000000007:
#                     count %= 1000000007
#                 else:
#                     new_data[p3] = data[p2]
#                     p3 -= 1
#                     p2 -= 1
#
#         while p1 >= low:
#             new_data[p3] = data[p1]
#             p3 -= 1
#             p1 -= 1
#
#         while p2 >= low + len + 1:
#             new_data[p3] = data[p2]
#             p3 -= 1
#             p2 -= 1
#
#         return (count + left + right) % 1000000007
#
#
# if __name__ == "__main__":
#     input_data = [7, 5, 6, 4]
#     sol = Solution()
#     print(sol.InversePairs2(input_data))


class Solution:

    def InversePairs(self, data):
        count = 0
        for index, value in enumerate(data):
            for i in range(index + 1, len(data)):
                if value > data[i]:
                    count += 1

        return count % 1000000007


if __name__ == "__main__":
    sol = Solution()
    data_list = [1, 2, 3, 4, 5, 6, 7, 0]
    print(sol.InversePairs(data_list))
