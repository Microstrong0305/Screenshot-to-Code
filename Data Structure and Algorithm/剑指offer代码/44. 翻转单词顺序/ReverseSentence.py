class Solution:

	def ReverseSentence(self, s):
		s_list = s.split(" ")
		s_list.reverse()
		return " ".join(s_list)

if __name__ == '__main__':
	sol = Solution()
	s = "student. a am I"
	print(sol.ReverseSentence(s))
