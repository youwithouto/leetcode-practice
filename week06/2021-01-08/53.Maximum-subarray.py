class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        dp = nums[0]
        for i in range(1, len(nums)):
            dp = max(dp, dp + nums[i - 1])
            result = max(result, dp)
        return result
