'''
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为
该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹
出序列。(注意：这两个序列的长度是相等的)
'''
class Solution:

    def isPopOrder(self, pushV, popV):
        stack = []
        while popV:
            # 如果pushV不空，且与popV头元素都相同，则出栈
            if pushV and pushV[0] == popV[0]:
                pushV.pop(0)
                popV.pop(0)
            # 如果不满足前面的条件，判断stack是否为空，不为空则判断stack[-1]与popV[0]是否相等，相等则出栈。
            elif stack and stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop(-1)
            # 如果pushV不空则，stack入栈
            elif pushV:
                stack.append(pushV.pop(0))
            # 最后说明pushV为空，且stack[-1]与popV[0]不相同，则出栈序列有误，返回False
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    pushV = [1, 2, 3, 4, 5]
    # popV = [4, 5, 3, 2, 1]
    popV = [4, 3, 5 ,1, 2]
    print(sol.isPopOrder(pushV, popV))

'''
Reference: 
[1] https://blog.csdn.net/qq_34364995/article/details/81477676
'''



