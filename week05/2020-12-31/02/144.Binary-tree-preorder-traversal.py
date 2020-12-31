# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node: TreeNode, result: List[int]):
        if node is None:
            return
        result.append(node.val)
        self.helper(node.left, result)
        self.helper(node.right, result)
