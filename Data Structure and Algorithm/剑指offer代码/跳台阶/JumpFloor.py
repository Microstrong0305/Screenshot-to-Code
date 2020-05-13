class Solution:
    # 递归
    def jumpFloor(self, number):
        if number < 0:
            return 0

        def tryJump(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return tryJump(n - 1) + tryJump(n - 2)

        return tryJump(number)

    # 记忆化递归解法
    def jumpFloor2(self, number):
        if number <= 0:
            return 0

        memo = [0] * (number + 1)

        if number >= 1:
            memo[1] = 1

        if number >= 2:
            memo[2] = 2

        def tryJump(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                memo[n] = tryJump(n - 1) + tryJump(n - 2)
            return memo[n]

        if number >= 3:
            tryJump(number)

        return memo[number]

    # 动态规划解法
    def jumpFloor3(self, number):
        if number <= 0:
            return 0

        dp = [0] * (number + 1)
        if number >= 1:
            dp[1] = 1
        if number >= 2:
            dp[2] = 2
        if number >= 3:
            for i in range(3, number + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[number]


if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(5))
