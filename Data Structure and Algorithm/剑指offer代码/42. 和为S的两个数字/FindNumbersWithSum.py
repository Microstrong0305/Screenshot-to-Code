# -*- coding:utf-8 -*-

class Solution:

    def FindNumbersWithSum(self, array, tsum):
        result_list = []
        for index, value in enumerate(array):
            for j in range(index, len(array)):
                if value + array[j] == tsum:
                    result_list.append(value)
                    result_list.append(array[j])
                    break
            if len(result_list) == 2:
                break
        return result_list

    def FindNumbersWithSum2(self, array, tsum):
        if array is None or len(array) < 1:
            return []

        start = 0
        end = len(array) - 1
        result_list = []
        while start <= end:
            if array[start] + array[end] > tsum:
                end -= 1
            elif array[start] + array[end] < tsum:
                start += 1
            elif len(result_list) == 2:
                break
            elif array[start] + array[end] == tsum:
                result_list.append(array[start])
                result_list.append(array[end])
        return result_list


if __name__ == "__main__":
    sol = Solution()
    array = [1, 3, 5, 15, 17]
    tsum = 20
    print(sol.FindNumbersWithSum2(array, tsum))

'''
Reference：
【1】https://blog.nowcoder.net/n/0935efd26ade435497dcbe407cfc94ec
'''
