class Temp(object):

	N = 0
	Sum = 0

	def __init__(self):
		Temp.N += 1
		Temp.Sum += Temp.N

	def GetSum():
		return Temp.Sum
		

class Solution:
	def Sum_solution(self, n):
		obj_list = [Temp() for i in range(n)]

		return Temp.GetSum()



if __name__ == "__main__":
	sol = Solution()
	print(sol.Sum_solution(3))