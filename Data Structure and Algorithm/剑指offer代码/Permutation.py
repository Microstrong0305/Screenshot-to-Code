'''
输入一个字符串，按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则
打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

class Solution:

    def __init__(self):
        self.result = []

    def Permutation(self, str):
       # 判断输入
        if len(str) == 0:
            return
        self.PermutationCore(str, 0)
        sorted(self.result)
        return  self.result

    def PermutationCore(self, str, begin):
        # 递归结束的条件：第一位和最后一位交换完成
        if begin == len(str):
            self.result.append(str)
            return

        for i in range(begin, len(str)):
            # 如果字符串相同，则不交换
            if i != begin and str[i] == str[begin]:
                continue

            # 位置交换，Python中字符串的值是不可以修改的，
            # 可以将字符串转换成列表之后修改值，然后用join组成新字符串。
            newStr = list(str)
            temp = newStr[begin]
            newStr[begin] = newStr[i]
            newStr[i] = temp
            str = ''.join(newStr)

            # 递归调用，前面begin + 1的位置不变，后面的字符串全排列
            self.PermutationCore(str, begin + 1)

if __name__ == "__main__":
    sol = Solution()
    str = 'abc'
    print(sol.Permutation(str))


'''
Reference:
[1] https://cuijiahua.com/blog/2017/12/basis_27.html
'''