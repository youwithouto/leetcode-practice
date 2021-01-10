class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = -n
        return self.helper(x, n)

    def helper(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.helper(x, n//2)
        return half * half if n % 2 == 0 else half * half * x
