class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 暴力解法
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        if not l1:
            prev.next = l2
        else:
            prev.next = l1

        return dummy.next

    # 递归解法
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2


if __name__ == "__main__":
    l1_node1 = ListNode(1)
    l1 = l1_node1
    l1_node2 = ListNode(2)
    l1_node1.next = l1_node2
    l1_node3 = ListNode(4)
    l1_node2.next = l1_node3

    l2_node1 = ListNode(1)
    l2 = l2_node1
    l2_node2 = ListNode(3)
    l2_node1.next = l2_node2
    l2_node3 = ListNode(4)
    l2_node2.next = l2_node3

    sol = Solution()
    l1 = sol.mergeTwoLists2(l1, l2)

    while l1:
        print(l1.val)
        l1 = l1.next
