# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node: TreeNode, minValue: int, maxValue: int) -> bool:
        if node == None:
            return True
        if minValue != None and node.val <= minValue:
            return False
        if maxValue != None and node.val >= maxValue:
            return False
        return self.helper(node.left, minValue, node.val) and self.helper(node.right, node.val, maxValue)

    def helperInner(self, node: TreeNode, parentValue: int) -> bool:
        if node == None:
            return True
