class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if end not in bankSet:
            return -1
        change = {
            'A': 'CGT',
            'C': 'AGT',
            'G': 'ACT',
            'T': 'ACG'
        }
        queue = [(start, 0)]
        while queue:
            node, step = queue.pop(0)
            if node == end:
                return step
            for i, v in enumerate(node):
                for j in change[v]:
                    newNode = node[:i] + j + node[i + 1:]
                    if newNode in bankSet:
                        queue.append((newNode, step + 1))
                        bankSet.remove(newNode)
        return -1
