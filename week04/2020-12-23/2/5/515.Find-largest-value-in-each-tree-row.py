# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        self.helper(root, result)
        return result

    def helper(self, node: TreeNode, result: List[int]):
        queue = [node]
        while queue:
            currentMax, next = float('-inf'), []
            for i in range(len(queue)):
                n = queue[i]
                if n.val > currentMax:
                    currentMax = n.val
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            result.append(currentMax)
            queue = next
