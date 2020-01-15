# -*- coding:utf-8 -*-

from functools import cmp_to_key


class Solution:

    def PrintMinNumber(self, numbers):
        def cmp(a, b):
            num1 = str(a) + str(b)
            num2 = str(b) + str(a)
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            else:
                return 0

        if numbers is None or len(numbers) == 0:
            return ""

        numbers.sort(key=cmp_to_key(cmp))
        # sorted(numbers, key = cmp_to_key(cmp))
        return "".join(str(num) for num in numbers)

    # 使用冒泡排序
    def PrintMinNumber2(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return ""

        # strNum = [str(num) for num in numbers]
        strNum = list(map(str, numbers))

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                    strNum[i], strNum[j] = strNum[j], strNum[i]

        return ''.join(strNum)


if __name__ == "__main__":
    sol = Solution()
    numbers = [3, 32, 321]
    print(sol.PrintMinNumber2(numbers))

'''
Reference:
[1] 《剑指offer》，何海涛著。
[2] https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.py#L16
[3] https://blog.csdn.net/yurenguowang/article/details/80568996
[4] https://blog.csdn.net/u013129109/article/details/80089387
[5] https://github.com/shenweichen/coding_interviews/blob/master/45.%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0/45.%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.py
'''
