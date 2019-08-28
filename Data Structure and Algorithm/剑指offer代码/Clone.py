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

    # 复制复杂链表的第一步
    def CloneNodes(self, pHead):
        pNode = pHead
        while(pNode != None):
            pCloned = RandomListNode(None)
            pCloned.label = pNode.label
            pCloned.next = pNode.next
            pCloned.random = None

            pNode.next = pCloned
            pNode = pCloned.next

    # 复制复杂链表的第二步
    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode != None:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 复制复杂链表的第三步
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = None
        pClonedNode = None

        if pNode != None:
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        while pNode != None:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead

class Tool:

    def printList(self, pHead):
        '''
        输出链表信息
        :param pHead:
        :return:
        '''
        while pHead != None:
            print(str(pHead.label) + "->")
            pHead = pHead.next
        print("NULL")

    def isSame(self, pHead1, pHead2):
        '''
        判断两个链表是否是同一个链表，不是值相同
        :param pHead1: 链表头1
        :param pHead2: 链表头2
        :return:
        '''
        while pHead1 != None and pHead2 != None:
            if pHead1 == pHead2:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
            else:
                return False
        return pHead1 == None and pHead2 == None

if __name__ == "__main__":
    #            -----------------
    #          \|/               |
    #  1--------2-------3-------4-------5
    #  |        |     / |\             /|\
    #  ---------+-------                |
    #           ------------------------
    head = RandomListNode(1)
    # head.label = 1
    head.next = RandomListNode(2)
    # head.next.label = 2
    head.next.next = RandomListNode(3)
    # head.next.next.label = 3
    head.next.next.next = RandomListNode(4)
    # head.next.next.next.label = 4
    head.next.next.next.next = RandomListNode(5)
    # head.next.next.next.next.label = 5
    head.random = head.next.next
    head.next.random = head.next.next.next.next.next
    head.next.next.next.random = head.next

    tmp = head
    tool = Tool()
    tool.printList(head)
    print(tool.isSame(head, tmp))

    sol = Solution()
    newHead = sol.Clone(head)
    tool.printList(newHead)
    print(tool.isSame(head, newHead))

# Reference :
# 【1】https://blog.csdn.net/gatieme/article/details/51227939
# 【2】https://wiki.jikexueyuan.com/project/for-offer/question-twenty-six.html

