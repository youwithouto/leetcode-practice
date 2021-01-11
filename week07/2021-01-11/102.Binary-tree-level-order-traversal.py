# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        level = [root]
        while level:
            values, children = [], []
            for n in level:
                values.append(n.val)
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            result.append(values)
            level = children
        return result
