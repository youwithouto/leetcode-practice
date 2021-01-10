# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, result, 0)
        return result

    def helper(self, node: TreeNode, result: List[List[int]], level: int):
        if node is None:
            return
        if level >= len(result):
            result.append([])
        result[level].append(node.val)
        self.helper(node.left, result, level + 1)
        self.helper(node.right, result, level + 1)
