# last step: 1 or 2
# the current step needs the previous two steps

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        s1, s2, total = 1, 2, 0
        for i in range(3, n + 1):
            total = s1 + s2
            s1, s2 = s2, total
        return total
