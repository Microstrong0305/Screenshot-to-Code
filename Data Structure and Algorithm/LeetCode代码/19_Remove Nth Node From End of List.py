class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head

        count = 0
        tempHead = head
        while tempHead:
            count += 1
            tempHead = tempHead.next

        if count == 1 and n == 1:
            return None

        node = head
        temp = 0
        while node:
            temp += 1
            if count - n == 0:
                head = head.next
                return head
            if temp == (count - n):
                removeNode = node.next
                lastNode = removeNode.next
                node.next = lastNode
                break
            node = node.next
        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        if n == 1 and head.next == None:
            return head.next

        fast = head
        slow = head
        while n:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        node = slow.next.next
        slow.next = node

        return head


if __name__ == "__main__":

    node1 = ListNode(1)
    head = node1
    # node1.next = None
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = None
    # head.next = node2
    # node2.next = node3
    # node4 = ListNode(4)
    # node3.next = node4
    # node5 = ListNode(5)
    # node4.next = node5
    # node6 = ListNode(6)
    # node5.next = node6
    # node6.next = None

    sol = Solution()
    new_head = sol.removeNthFromEnd2(head, 3)

    while new_head:
        print(new_head.val)
        new_head = new_head.next
