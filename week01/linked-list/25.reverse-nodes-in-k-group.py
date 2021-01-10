# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                previousNode, currentNode = r, l
                for _ in range(k):
                    # current.next -> previous
                    # previous -> current
                    # current -> current.next
                    currentNode.next, previousNode, currentNode = previousNode, currentNode, currentNode.next

                # connect the previous k-group and the just-reversed k-group
                # tail.next -> current head
                # tail -> current tail
                # l -> r
                jump.next, jump, l = previousNode, l, r
            else:
                return dummy.next
