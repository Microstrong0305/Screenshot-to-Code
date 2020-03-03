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


if __name__ == "__main__":
    sol = Solution()
    array = [1, 3, 5, 15, 17]
    tsum = 20
    print(sol.FindNumbersWithSum(array, tsum))

'''
Reference：
【1】https://blog.nowcoder.net/n/0935efd26ade435497dcbe407cfc94ec
'''
