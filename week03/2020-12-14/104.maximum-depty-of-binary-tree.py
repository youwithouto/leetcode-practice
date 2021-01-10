# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root)

    def helper(self, node: TreeNode) -> int:
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 1
        return max(self.helper(node.left), self.helper(node.right)) + 1
