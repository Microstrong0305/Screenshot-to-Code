class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head1 = l1
        head2 = l2
        while head2:
            a = head2.val
            b = head1.val
            if head2.val < head1.val:
                tempNode1 = head1
                tempNext2 = head2.next
                if head1 == l1:
                    l1 = head2
                while tempNext2 and tempNext2.val < head1.val:
                    if tempNext2.next == None:
                        break
                    tempNext2 = tempNext2.next
                if tempNext2:
                    head2 = tempNext2.next
                    tempNext2.next = tempNode1
                    head1 = tempNode1.next
                else:
                    head2.next = tempNode1
                    head2 = tempNext2
                    head1 = tempNode1.next
            else:
                tempNext1 = head1.next
                while tempNext1.val >= head2.val:
                    if tempNext1.next == None:
                        break
                    tempNext1 = tempNext1.next
                if tempNext1:
                    tempNext2 = head2.next
                    tempNext1.next = head2
                    head1 = tempNext1
                    head2 = tempNext2

        return l1


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
    l1 = sol.mergeTwoLists(l1, l2)

    while l1:
        print(l1.val)
        l1 = l1.next
