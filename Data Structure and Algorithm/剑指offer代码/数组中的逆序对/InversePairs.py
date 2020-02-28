class Solution:

    def InversePairs(self, data):
        if data is None or len(data) <= 0:
            return 0

        copy = [i for i in data]

        count = self.InversePairsCore(data, copy, 0, len(data) - 1)

        return count % 1000000007

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0

        length = (end - start) // 2
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        # p1 初始化为前半段最后一个数字的下标
        p1 = start + length
        # p2 初始化为后半段最后一个数字的下标
        p2 = end
        # 开始拷贝的位置
        p3 = end
        # 逆序数
        count = 0

        # 对两个数组进行对比取值的过程
        while p1 >= start and p2 >= start + length + 1:
            if data[p1] > data[p2]:
                copy[p3] = data[p1]
                p3 -= 1
                p1 -= 1
                # 对应的逆序数
                count += p2 - start - length
            else:
                copy[p3] = data[p2]
                p3 -= 1
                p2 -= 1

        # 剩下的一个数组未取完的操作
        while p1 >= start:
            copy[p3] = data[p1]
            p3 -= 1
            p1 -= 1

        while p2 >= start + length + 1:
            copy[p3] = data[p2]
            p3 -= 1
            p2 -= 1

        return count + left + right


if __name__ == "__main__":
    # input_data = [7, 5, 6, 4]
    input_data = [1, 2, 3, 4, 5, 6, 7, 0]
    sol = Solution()
    print(sol.InversePairs(input_data))

# class Solution:
#
#     def InversePairs(self, data):
#         count = 0
#         for index, value in enumerate(data):
#             for i in range(index + 1, len(data)):
#                 if value > data[i]:
#                     count += 1
#
#         return count % 1000000007
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     data_list = [1, 2, 3, 4, 5, 6, 7, 0]
#     print(sol.InversePairs(data_list))


'''
Reference：
【1】https://github.com/leeguandong/Interview-code-practice-python/blob/master/%E5%89%91%E6%8C%87offer/%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%80%86%E5%BA%8F%E5%AF%B9.py
'''
