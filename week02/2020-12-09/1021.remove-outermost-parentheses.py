class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        layer, result = 0, []
        for c in S:
            if c == '(':
                layer += 1
                if layer > 1:
                    result.append(c)
            else:
                if layer > 1:
                    result.append(c)
                layer -= 1
        return "".join(result)
