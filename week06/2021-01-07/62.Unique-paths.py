class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nums = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                nums[j] += nums[j - 1]
        return nums[-1]
