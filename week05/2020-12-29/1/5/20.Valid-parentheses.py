class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        open = []
        for c in s:
            if c not in pair:
                open.append(c)
            elif len(open) <= 0 or pair[c] != open.pop():
                return False
        return len(open) == 0
