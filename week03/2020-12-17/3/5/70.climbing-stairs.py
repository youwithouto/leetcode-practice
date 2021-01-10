# the last step: 1 or 2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        s1, s2 = 1, 2
        s3 = 0
        for i in range(3, n + 1):
            s3 = s1 + s2
            s1, s2 = s2, s3
        return s3
