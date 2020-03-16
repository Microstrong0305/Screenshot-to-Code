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

    def FindContinuousSequence1(self, tsum):
        if tsum == 0 or tsum == 1 or tsum == 2:
            return []

        result_list = []

        mid = int((tsum + 1) // 2)
        array = [i for i in range(0, mid + 1)]
        small = 1
        big = 2
        temp_sum = array[small] + array[big]
        temp = [array[small], array[big]]
        while True:
            if temp_sum == tsum:
                temp_list = [t for t in temp]
                result_list.append(temp_list)
                if big < len(array) - 1:
                    big += 1
                    temp_sum = temp_sum + array[big]
                    temp.append(array[big])
                else:
                    return result_list
            if temp_sum > tsum:
                temp_sum = temp_sum - array[small]
                temp.remove(array[small])
                small += 1
            if temp_sum < tsum:
                if big < len(array) - 1:
                    big += 1
                    temp_sum = temp_sum + array[big]
                    temp.append(array[big])
                else:
                    return result_list

        return result_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.FindContinuousSequence1(15))
