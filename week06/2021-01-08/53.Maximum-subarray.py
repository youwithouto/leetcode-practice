class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = dp = nums[0]
        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            result = max(result, dp)
        return result