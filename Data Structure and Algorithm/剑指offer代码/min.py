'''
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O(1)）。
'''
class Solution:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min_num = None

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min_num is None:
            self.min_num = node
            self.minStack.append(self.min_num)
        elif self.min_num < node:
            self.minStack.append(self.min_num)
        else:
            self.min_num = node
            self.minStack.append(node)

    def pop(self):
        # write code here
        if len(self.stack) > 0 and len(self.minStack):
            self.minStack.pop()
            self.stack.pop()

    def top(self):
        # write code here
        return

    def min(self):
        # write code here
        return self.minStack[-1]

if __name__ == '__main__':
    stack = Solution()
    current_stack = [11, 7, 8, 9, 5, 12, 15]
    for num in (current_stack):
        stack.push(num)
    print(stack.min(), stack.stack)
    print(stack.minStack)
    # 测试用例
    # 输入一个比最小值大的
    stack.push(7)
    print(stack.min(), stack.stack)

    # 输入一个比最小值小的
    stack.push(4)
    print(stack.min(), stack.stack)

    # 弹出最小值
    stack.pop()
    print(stack.min(), stack.stack)

    # 弹出非最小值
    stack.pop()
    print(stack.min(), stack.stack)