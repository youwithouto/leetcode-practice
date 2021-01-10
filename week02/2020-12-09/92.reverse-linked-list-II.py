# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(0, head)
        pre = dummy

        for i in range(m - 1):
            pre = pre.next

        cur, reverse = pre.next, None
        for i in range(n - m + 1):
            next = cur.next
            cur.next, reverse = reverse, cur
            cur = next
        pre.next.next = cur
        pre.next = reverse

        return dummy.next
