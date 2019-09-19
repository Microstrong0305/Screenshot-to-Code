'''
输入一个字符串，按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则
打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''


class Solution:

    #方法一：递归解法
    def __init__(self):
        self.result = []

    def Permutation(self, ss):
       # 判断输入
        if len(ss) == 0:
            return []
        self.PermutationCore(ss, 0)
        sorted(self.result)
        return self.result

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

    # 方法二：递归法的第二种写法
    def Permutation2(self, ss):
        if len(ss) <= 0:
            return []
        res = list()
        self.perm(ss, res, '')
        uniq = list(set(res))
        return sorted(uniq)

    def perm(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:], res, path+ss[i])

    # 方法三：递归法的第三种写法
    def Permutation3(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...，然后递归求解
        for i in range(len(ss)):
            for j in self.Permutation3(ss[:i] + ss[i + 1:]):  # 依次固定了元素，其他的全排列（递归求解）
                res.add(ss[i] + j)  # 集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同，如baa,baa）
        return sorted(res)  # sorted()能对可迭代对象进行排序,结果返回一个新的list


if __name__ == "__main__":
    sol = Solution()
    str = 'abc'
    print(sol.Permutation(str))


'''
Reference:
[1] https://cuijiahua.com/blog/2017/12/basis_27.html
[2] https://www.nowcoder.com/questionTerminal/fe6b651b66ae47d7acce78ffdd9a96c7?f=discussion
'''