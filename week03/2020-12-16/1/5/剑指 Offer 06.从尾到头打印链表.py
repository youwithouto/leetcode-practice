# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result = []
        self.helper(result, head)
        return result

    def helper(self, result: List[int], node: ListNode):
        if node == None:
            return []
        elif node.next == None:
            result.append(node.val)
        else:
            self.helper(result, node.next)
            result.append(node.val)
