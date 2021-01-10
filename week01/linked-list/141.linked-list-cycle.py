# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     try:
    #         slow, fast = head, head.next
    #         while slow is not fast:
    #             slow, fast = slow.next, fast.next.next
    #         return True
    #     except:
    #         return False

    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while (fast and fast.next):
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
