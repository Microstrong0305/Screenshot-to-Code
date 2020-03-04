# -*- coding:utf-8 -*-

class Solution:

    def LeftRotateString(self, s, n):
        return s[n:] + s[:n]


if __name__ == "__main__":
    sol = Solution()
    s = 'abcXYZdef'
    n = 0
    print(sol.LeftRotateString(s, n))
