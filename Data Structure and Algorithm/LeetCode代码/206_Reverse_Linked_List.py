# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 空链或只有一个结点，直接返回头指针
        if head is None or head.next is None:
            return head

        # 链表中至少有两个结点
        p1 = head  # 第一个结点
        p2 = p1.next  # 第二个结点
        p3 = p2.next  # 第三个结点

        while p2:
            p3 = p2.next
            p2.next = p1  # 第二个结点指向第一个结点，进行反转
            p1 = p2  # 第一个结点往后移
            p2 = p3  # 第二个结点往后移

        head.next = None  # 第一个结点也就是反转后的最后一个节点指向 NULL
        head = p1  # 头结点指向反转后的第一个节点
        return head

    def reverseList2(self, head: ListNode) -> ListNode:

        # 空链或只有一个结点，直接返回头指针
        if head is None or head.next is None:
            return head

        # 有两个以上结点
        new_head = self.reverseList2(head.next)  # 反转以第二个结点为头的子链表

        # head.next 此时指向子链表的最后一个结点

        # 将之前的头结点放入子链尾
        head.next.next = head
        head.next = None

        return new_head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None

    sol = Solution()
    print(sol.reverseList2(head))
