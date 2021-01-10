# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nodeStack = []
        current, previous = root, None

        while current or nodeStack:
            if current:
                nodeStack.append(current)
                current = current.left
            else:
                node = nodeStack.pop()

                if previous is None or node.val > previous.val:
                    previous = node
                else:
                    return False
                current = node.right

        return True
