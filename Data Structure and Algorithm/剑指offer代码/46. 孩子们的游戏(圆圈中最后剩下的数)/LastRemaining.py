# -*- coding:utf-8 -*-

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        n_list = [i for i in range(n)]
        cursor = 0
        while True:
            temp_index = []
            for i in range(0, len(n_list)):
                if cursor == m - 1:
                    temp_index.append(n_list[i])
                    cursor = 0
                else:
                    cursor += 1

            for j in temp_index:
                n_list.remove(j)

            if len(n_list) == 1:
                return n_list[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.LastRemaining_Solution(11, 3))
