# 方法一：
# import math
#
# class Solution:
#
#     def Power(self, base, exponent):
#         assert base != 0
#         return math.pow(base, exponent)
#
# sol = Solution()
# print(sol.Power(2, 3))

# # 方法二：
# class Solution:
#
#     def Power(self, base, exponent):
#         return base**exponent
#
# sol = Solution()
# print(sol.Power(2, -3))

# 方法三：
'''
对于这道题目，需要考虑四种情况：
1、底数为0，指数为负数的情况，无意义。
2、指数为0，返回1。
3、指数为负数，返回 1.0/(base**-exponent)
4、指数正数，base**exponent。
'''
# class Solution:
#
#     def Power(self, base, exponent):
#         if (base == 0) and exponent < 0:
#             return 0
#         if exponent == 0:
#             return 1
#         if exponent < 0:
#             result = self.powerWithExponent(1.0/base, -exponent)
#         else:
#             result = self.powerWithExponent(base, exponent)
#
#         return  result
#
#     def powerWithExponent(self, base, exponent):
#         result = 1
#         for i in range(0, exponent):
#             result = result * base
#         return result
#
# sol = Solution()
# print(sol.Power(2, -3))

# 方法四：
class Solution:

    def Power(self, base, exponent):
        '''递归求解'''
        if (base == 0) and exponent < 0:
            return 0
        absExponent = abs(exponent)

        def calPow(base, absExponent):
            if absExponent == 1:
                return base
            if absExponent == 0:
                return 1
            # 递归求次方
            res = calPow(base, absExponent>>1)
            res *= res
            # 判断奇偶性
            if (absExponent & 0x1) == 1:
                res *= base
            return res

        result = calPow(base, absExponent)
        if exponent < 0:
            result = 1.0 / result
        return result

sol = Solution()
print(sol.Power(2, -3))


# reference:https://blog.csdn.net/jsqfengbao/article/details/47164537



