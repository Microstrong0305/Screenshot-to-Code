# -*- coding:utf-8 -*-

class Solution:

    def LeftRotateString(self, s, n):
        return s[n:] + s[:n]

    def LeftRotateString2(self, s, n):
        if len(s) == 0:
            return s
        s = list(s)

        def Reverse(s, start, end):
            for i in range(start, (start + end) // 2 + 1):
                s[i], s[end - i + start] = s[end - i + start], s[i]
            return s

        n %= len(s)
        # 翻转字符串的前面n个字符
        s = Reverse(s, 0, n - 1)
        # 翻转字符串的后面部分
        s = Reverse(s, n, len(s) - 1)
        # 翻转整个字符串
        s = Reverse(s, 0, len(s) - 1)

        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    s = 'abcXYZdef'
    n = 3
    print(sol.LeftRotateString2(s, n))
