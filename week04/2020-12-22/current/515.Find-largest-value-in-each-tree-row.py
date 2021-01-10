# Definition for a binary tree node.
from abc import abstractproperty


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result, q = [], [root]
        while q:
            current, next = [], []
            for item in q:
                current.append(item)
                if item.left:
                    next.append(item.left)
                if item.right:
                    next.append(item.right)
            currentMax = max([node.val for node in current])
            result.append(currentMax)
            q = next
        return result
