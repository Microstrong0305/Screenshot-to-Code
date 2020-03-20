from functools import reduce


class Temp(object):
    N = 0
    Sum = 0

    def __init__(self):
        Temp.N += 1
        Temp.Sum += Temp.N


class Solution:
    def Sum_Solution(self, n):
        obj_list = [Temp() for i in range(n)]

        return Temp.Sum

    # 递归
    def Sum_Solution1(self, n):
        # write code here
        if n == 0:
            return 0
        return n + self.Sum_Solution1(n - 1)

    # reduce
    def Sum_Solution2(self, n):
        # write code here
        def add(x, y):
            return x + y

        return reduce(add, range(1, n + 1))


if __name__ == "__main__":
    sol = Solution()
    print(sol.Sum_Solution1(5))
