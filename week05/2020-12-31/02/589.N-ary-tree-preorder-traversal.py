"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node: 'Node', result: List[int]):
        if node is None:
            return
        result.append(node.val)
        for child in node.children:
            self.helper(child, result)
