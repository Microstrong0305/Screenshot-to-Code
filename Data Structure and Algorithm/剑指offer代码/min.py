'''
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O(1)）。
'''
class Solution:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minm = float("inf")

    def push(self, node):
        # write code here
        if node < self.minm:
            self.minm = node
            self.minStack.append(self.minm)
        self.minStack.append(node)

    def pop(self):
        # write code here
        if self.stack != []:
            if self.stack[-1] == self.minm:
                self.minStack.pop()
            self.stack.pop(-1)

    def top(self):
        # write code here
        if self.stack != []:
            return self.stack[-1]

    def min(self):
        # write code here
        return self.minStack[-1]