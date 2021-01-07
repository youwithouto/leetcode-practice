class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = dp_max = dp_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dp_max, dp_min = dp_min, dp_max
            dp_max = max(nums[i], nums[i] * dp_max)
            dp_min = min(nums[i], nums[i] * dp_min)
            result = max(dp_max, result)
        return result
