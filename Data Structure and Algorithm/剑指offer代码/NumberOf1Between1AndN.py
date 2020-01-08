# -*- coding:utf-8 -*-
class Solution:
    # 方法一：时间复杂度O(nlogn),logn表示n有logn位
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n + 1):
            eachNumCount = 0
            while i:
                if i % 10 == 1:
                    eachNumCount += 1
                i = int(i / 10)
            count += eachNumCount
        return count

    # 方法二
    def NumberOf1Between1AndN_Solution1(self, n):
        # write code here
        if n <= 0:
            return 0
        return self.NumberOf1(str(n))
    
    def NumberOf1(self, n):
        first = int(n[0])
        length = len(n)
        
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1
        
        numFirstDigit = 0
        if first > 1:
            numFirstDigit = self.PowerBase10(length - 1)
        elif first == 1:
            numFirstDigit = int(n[1:]) + 1
        
        numOtherDigits = first * (length - 1) * self.PowerBase10(length - 2)
        
        numRecursive = self.NumberOf1(n[1:])
        
        return numFirstDigit + numOtherDigits + numRecursive
    
    def PowerBase10(self, n):
        result = 1
        for i in range(n):
            result *= 10
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.NumberOf1Between1AndN_Solution1(10000))
