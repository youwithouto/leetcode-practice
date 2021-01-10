class Solution:
    def isValid(self, s: str) -> bool:
        matching = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in matching:
                stack.append(c)
            elif matching[stack.pop()] != c:
                return False
        return len(stack) == 1
