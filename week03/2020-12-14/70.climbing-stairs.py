# Each time you can climt 1 or 2 steps
# -> the last step can be either 1 or 2
class Solution:
    def climbStairs(self, n: int) -> int:
        # when n is [1, 2]
        if n < 3:
            return n
        f1, f2 = 1, 2
        f3 = -1
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3
