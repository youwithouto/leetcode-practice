# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     previousNode = None
    #     while head:
    #         currentNode, head = head, head.next
    #         currentNode.next, previousNode = previousNode, currentNode
    #     return previousNode

    def reverseList(self, head: ListNode) -> ListNode:
        return self.doReverseList(None, head)

    def doReverseList(self, reversedListHead: ListNode, remainingListHead: ListNode) -> ListNode:
        if remainingListHead is None:
            return reversedListHead
        currentNode, nextNode = remainingListHead, remainingListHead.next
        currentNode.next = reversedListHead
        return self.doReverseList(currentNode, nextNode)
