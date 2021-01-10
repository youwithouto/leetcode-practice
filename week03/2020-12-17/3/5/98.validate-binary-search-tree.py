# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        curr, prev = root, None
        while curr or stack:
            if not curr:
                curr = stack.pop()
                if prev != None and curr.val <= prev:
                    return False
                prev, curr = curr.val, curr.right
            else:
                stack.append(curr)
                curr = curr.left
        return True
