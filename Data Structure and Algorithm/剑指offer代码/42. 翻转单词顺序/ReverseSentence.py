class Solution:

    def ReverseSentence(self, s):
        s_list = s.split(" ")
        s_list.reverse()
        return " ".join(s_list)

    def ReverseSentence2(self, s):
        words = s.split(" ")
        temp_sentence = []
        for i in range(len(words) - 1, -1, -1):
            temp_sentence.append(words[i])
        return " ".join(temp_sentence)


if __name__ == '__main__':
    sol = Solution()
    s = "student. a am I"
    print(sol.ReverseSentence2(s))
