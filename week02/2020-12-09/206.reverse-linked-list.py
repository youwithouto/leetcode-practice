# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, curr = None, head
        while curr:
            next = curr.next
            curr.next = pre
            pre, curr = curr, next
        return pre
