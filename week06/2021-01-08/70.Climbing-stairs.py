class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a, b = 1, 2
        result = 0
        for i in range(3, n + 1):
            result = a + b
            a, b = b, result
        return result
