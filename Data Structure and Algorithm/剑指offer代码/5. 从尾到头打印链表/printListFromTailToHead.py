class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 正着遍历链表，逆序输出遍历结果
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        res = []
        index = listNode
        while index:
            res.append(index.val)
            index = index.next

        return res[::-1]

    # 递归
    def printListFromTailToHead2(self, listNode):
        if listNode is None:
            return []
        ans = self.printListFromTailToHead2(listNode.next)
        ans.append(listNode.val)
        return ans

    # 借助栈结构
    def printListFromTailToHead3(self, listNode):
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]

    # 链表原地反转
    def printListFromTailToHead4(self, listNode):
        if not listNode:
            return []

        p1 = listNode
        p2 = listNode.next
        p3 = listNode.next.next
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        listNode.next = None
        listNode = p1

        res = []
        while listNode:
            res.append(listNode.val)
            listNode = listNode.next

        return res


if __name__ == "__main__":
    node0 = ListNode(0)
    head = node0
    node1 = ListNode(1)
    node0.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node4.next = None

    sol = Solution()
    print(sol.printListFromTailToHead4(head))
