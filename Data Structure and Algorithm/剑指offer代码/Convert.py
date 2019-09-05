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

    def Convert(self, pRootOfTree):
        '''
        :param pRootOfTree: 二叉树的根节点
        :return: 双向链表的头节点
        '''
        # 用于保存处理过程中的双向链表的尾结点
        self.pLastNodeInList = None
        self.ConvertNode(pRootOfTree)

        # pLastNodeInList指向双向链表的尾节点, 我们需要返回头节点
        pHeadOfList = self.pLastNodeInList
        while pHeadOfList != None and pHeadOfList.left != None:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pNode):
        '''
        :param pNode: 当前的根结点
        :pLastNodeInList: 已经处理好的双向链表的尾结点
        :return:
        '''
        #  结点不为空
        if pNode == None:
            return

        pCurrent = pNode
        # 如果有左子树就先处理左子树
        if pCurrent.left != None:
            self.ConvertNode(pCurrent.left)
        # 将当前结点的前驱指向已经处理好的双向链表（由当前结点的左子树构成）的尾结点
        pCurrent.left = self.pLastNodeInList
        # 如果左子树转换成的双向链表不为空，设置尾结点的后继
        if self.pLastNodeInList != None:
            self.pLastNodeInList.right = pCurrent
        # 记录当前结点为尾结点
        self.pLastNodeInList = pCurrent
        # 处理右子树
        if pCurrent.right != None:
            self.ConvertNode(pCurrent.right)

class Painter:
    def printList(self, head):
        while head != None:
            print(str(head.val) + '->', end='')
            head = head.right

    def printTree(self, root):
        if root != None:
            self.printTree(root.left)
            print(str(root.val) + '->', end='')
            self.printTree(root.right)

if __name__ == "__main__":
    # //            10
    # //         /      \
    # //        6        14
    # //       /\        /\
    # //      4  8     12  16
    node10 = TreeNode(10)
    node6 = TreeNode(6)
    node14 = TreeNode(14)
    node4 = TreeNode(4)
    node8 = TreeNode(8)
    node12 = TreeNode(12)
    node16 = TreeNode(16)
    node10.left = node6
    node10.right = node14
    node6.left = node4
    node6.right = node8
    node14.left = node12
    node14.right = node16
    print("Before convert: ")
    pinter = Painter()
    pinter.printTree(node10)
    print("")
    sol  = Solution()
    head = sol.Convert(node10)
    print("After convert : ")
    pinter.printList(head)
    print()
