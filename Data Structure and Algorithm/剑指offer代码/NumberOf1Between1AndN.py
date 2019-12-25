# -*- coding:utf-8 -*-
class Solution:
    # 方法一：时间复杂度O(nlogn),logn表示n有logn位
    # def NumberOf1Between1AndN_Solution(self, n):
    #     # write code here
    #     count = 0
    #     for i in range(1, n + 1):
    #         eachNumCount = 0
    #         while i:
    #             if i % 10 == 1:
    #                 eachNumCount += 1
    #             i = int(i / 10)
    #         count += eachNumCount
    #     return count

    # 方法二
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here


if __name__ == "__main__":
    sol = Solution()
    print(sol.NumberOf1Between1AndN_Solution(13))
