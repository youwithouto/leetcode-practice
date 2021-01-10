class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None:
            return False
        steps = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= steps:
                steps = i
        return steps == 0
