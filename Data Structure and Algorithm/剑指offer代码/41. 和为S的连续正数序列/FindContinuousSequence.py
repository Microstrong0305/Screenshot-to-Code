# -*- coding:utf-8 -*-

import math


class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum == 0 or tsum == 1:
            return []
        mid_ceil = int(math.ceil(float(tsum) / 2))
        result_list = []
        for i in range(1, mid_ceil + 1, 1):
            temp_sum = 0
            for j in range(i, 0, -1):
                temp_sum += j
                if temp_sum == tsum:
                    temp_list = [k for k in range(j, i + 1, 1)]
                    result_list.append(temp_list)
        return result_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.FindContinuousSequence(3))
