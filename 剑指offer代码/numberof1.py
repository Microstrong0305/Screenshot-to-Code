class solution:

    def numberof1(self, n):
        count = 0
        if n < 0:
            n = n & 0x7FFFFFFF
            count += 1
        while n >0 :
            count += n & 1
            n = n >> 1
        return count

sol = solution()
print(sol.numberof1(-5))














