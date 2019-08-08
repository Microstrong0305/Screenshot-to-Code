# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#
#         l1 = len(word1)
#         l2 = len(word2)
#
#         def tryMinDistance(i, j):
#             if i == -1:
#                 return j + 1
#             elif j == -1:
#                 return i + 1
#
#             elif (word1[i] == word2[j]):
#                 return tryMinDistance(i - 1, j - 1)
#             else:
#                 return (1 + min(tryMinDistance(i - 1, j - 1),  # replace i
#                                    tryMinDistance(i - 1, j),  # delete i
#                                    tryMinDistance(i, j - 1)  # add i+1 index
#                                    ))
#
#         return tryMinDistance(l1 - 1, l2 - 1)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        # print(dp)

        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j

        for i in range(l1+1):
            for j in range(l2+1):
                if word1[i - 1] == word2[j - 1]:
                    c  = 0
                else:
                    c = 1
                dp[i][j] = min(dp[i-1][j-1]+c, min(dp[i][j-1], dp[i-1][j])+1)

        return dp[l1][l2]

so = Solution()
# test 1
word1 = "horse"
word2 = "ros"

# test 2
# word1 = "intention"
# word2 = "execution"

# test 3
# word1 = "dinitrophenylhydrazine"
# word2 = "benzalphenylhydrazone"

# test 4
# word1 = ""
# word2 =""
print(so.minDistance(word1, word2))