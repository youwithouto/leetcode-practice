class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        s1, s2 = 1, 2
        total = 0
        for i in range(3, n + 1):
            total = s1 + s2
            s1, s2 = s2, total
        return total
