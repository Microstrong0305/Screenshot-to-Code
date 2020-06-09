import math
from typing import List


class Solution:
    # 定义骰子最大点数
    g_maxValue = 6

    # 方法一：基于递归求骰子点数，时间效率不够高
    def twoSum(self, n: int) -> List[float]:

        if n < 1:
            return []

        # 定义n个骰子的最大点数
        maxSum = n * self.g_maxValue

        # 所有可能的值出现的次数保存在列表中
        pProbabilities = [0] * (maxSum - n + 1)

        # 递归中的第一个骰子有6种情况
        for i in range(1, self.g_maxValue + 1):
            # 递归剩余的（n-1）个骰子
            self.getProbability(n, n, i, pProbabilities)

        # n个骰子的所有点数的排列数为6的n次方
        total = math.pow(self.g_maxValue, n)

        res = list(map(lambda x: x / total, pProbabilities))
        return list(map(lambda x: round(x, 5), res))

    def getProbability(self, original, current, sum, pProbabilities):
        '''
        :param original: 表示n个骰子仍在地上的n
        :param current: 剩余需要递归的骰子数
        :param sum: 骰子点数相加的数
        :param pProbabilities:
        :return:
        '''
        # 递归结束条件
        if current == 1:
            pProbabilities[sum - original] += 1
        else:
            for i in range(1, self.g_maxValue + 1):
                self.getProbability(original, current - 1, i + sum, pProbabilities)

    # 方法二：动态规划解法
    def twoSum2(self, n: int) -> List[float]:
        # 初始化二维数组
        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]

        # 初始化第一行
        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(i, i * 6 + 1):
                for k in range(1, 7):
                    if j >= k + 1:
                        dp[i][j] += dp[i - 1][j - k]

        res = []
        for i in range(n, n * 6 + 1):
            res.append(dp[n][i] * 1.0 / 6 ** n)

        return list(map(lambda x: round(x, 5), res))


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum2(2))
