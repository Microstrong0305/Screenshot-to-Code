# -*- coding:utf-8 -*-

from functools import cmp_to_key


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers == None or len(numbers) <= 0:
            return ''

        str_list = []
        for i in numbers:
            str_list.append(str(i))

        # key是一种比较规则
        # 比较 x+y 和 x-y 的大小，因为是str型，需要先转换成int型
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        str_list.sort(key=key)
        return ''.join(str_list)


if __name__ == "__main__":
    sol = Solution()
    numbers = [3, 32, 321]
    print(sol.PrintMinNumber(numbers))


'''
Reference:
[1] https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%8A%8A%E6%95%B0%E7%BB%84%E6%8E%92%E6%88%90%E6%9C%80%E5%B0%8F%E7%9A%84%E6%95%B0.py#L16
[2] https://blog.csdn.net/yurenguowang/article/details/80568996
[3] https://blog.csdn.net/u013129109/article/details/80089387
'''


