# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(float("-inf"), float('inf'), root)

    def helper(self, minVal: int, maxVal: int, node: TreeNode) -> bool:
        if not node:
            return True
        if node.val <= minVal or node.val >= maxVal:
            return False
        return self.helper(minVal, node.val, node.left) and self.helper(node.val, maxVal, node.right)
