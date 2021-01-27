class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        sa = s.split(" ")
        return 0 if len(sa) == 0 else len(sa[-1])
