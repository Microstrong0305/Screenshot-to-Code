class Solution:

    def FirstNotRepeatingChar(self, s):
        if s is None or len(s) == 0:
            return -1

        for i in range(len(s)):
            num = s.count(s[i])
            if num == 1:
                return s.index(s[i])
            elif i >= len(s):
                return -1


if __name__ == "__main__":
    str_input = 'abaccdeff'
    sol = Solution()
    print(sol.FirstNotRepeatingChar(str_input))
