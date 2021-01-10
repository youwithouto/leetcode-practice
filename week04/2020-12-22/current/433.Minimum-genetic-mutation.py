class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if end not in bankSet:
            return -1
        q = [(start, 0)]
        change = {
            'A': 'TCG',
            'T': 'ACG',
            'C': 'ATG',
            'G': 'ATC'
        }

        while q:
            node, step = q.pop(0)
            if node == end:
                return step
            for i, v in enumerate(node):
                for j in change[v]:
                    new = node[:i] + j + node[i + 1:]
                    if new in bankSet:
                        q.append((new, step + 1))
                        bankSet.remove(new)
        return -1
