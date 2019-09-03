'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的节点，只能
调整树中结点指针的指向。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, root):
        pLastNodeInList = None
        self.ConvertNode(root, pLastNodeInList)

        # pLastNodeInList指向双向链表的尾节点, 我们需要返回头节点
        pHeadOfList = pLastNodeInList
        while pHeadOfList != None and pHeadOfList.left != null:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pNode, pLastNodeInList):
        if pNode == None:
            return

        pCurrent = pNode

        if pCurrent.left != None:
            self.ConvertNode(pCurrent.left, pLastNodeInList)

        pCurrent.left = pLastNodeInList
        if pLastNodeInList != None:
            pLastNodeInList.right = pCurrent

        pLastNodeInList = pCurrent

        if pCurrent.right != None:
            self.ConvertNode(pCurrent.right, pLastNodeInList)
