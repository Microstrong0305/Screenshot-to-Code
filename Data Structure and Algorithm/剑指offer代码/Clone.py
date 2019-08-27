'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
解题思路：
1. 遍历链表，复制每个节点，如复制节点A到A1，将节点A1插到节点A后面；
2. 重新遍历链表，复制老节点的随机指针给新节点，如A1.random = A.random.next;
3. 拆分链表，将链表拆分为原链表和复制后的链表
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:

    def Clone(self, pHead):
        self.CloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)

    def CloneNodes(self, pHead):
        return

    def ConnectSiblingNodes(self, pHead):
        return

    def ReconnectNodes(self, pHead):
        return
