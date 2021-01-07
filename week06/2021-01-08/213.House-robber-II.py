class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.dp(nums[1:]), self.dp(nums[:-1])) if len(nums) != 1 else nums[0]

    def dp(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for n in nums:
            prev, curr = curr, max(curr, prev + n)
        return curr
