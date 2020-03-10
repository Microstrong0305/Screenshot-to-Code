# -*- coding:utf-8 -*-

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1

        n_list = [i for i in range(n)]
        cursor = 0
        while len(n_list) > 1:
            temp_index = []
            for i in range(0, len(n_list)):
                if cursor == m - 1:
                    temp_index.append(n_list[i])
                    cursor = 0
                else:
                    cursor += 1

            for j in temp_index:
                n_list.remove(j)

        return n_list[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.LastRemaining_Solution(5, 3))
