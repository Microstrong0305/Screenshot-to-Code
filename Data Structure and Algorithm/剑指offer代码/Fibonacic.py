class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    def Fibonacci2(self, n):
        res = [0 for i in range(n + 1)]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            res[0] = 0
            res[1] = 1
            for i in range(2, n + 1):
                res[i] = res[i - 1] + res[i - 2]

        return res[n]

    def Fibonacci3(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            a = 0
            b = 1
            c = 0
            for i in range(2, n + 1):
                c = a + b
                a = b
                b = c

            return c

    def Fibonacci4(self, n):
        sqrtFive = math.sqrt(5)
        return sqrtFive / 5 * (math.pow(((1 + sqrtFive) / 2), n) - math.pow(((1 - sqrtFive) / 2), n))


import math

so = Solution()
print(so.Fibonacci4(3))
