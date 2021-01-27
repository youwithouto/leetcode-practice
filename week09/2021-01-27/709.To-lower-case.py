class Solution:
    def toLowerCase(self, str: str) -> str:
        def cvt(c):
            i = ord(c)
            return chr(i + 32) if i >= 65 and i <= 90 else c
        return "".join(map(cvt, str))
