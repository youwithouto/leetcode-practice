class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        ss = self.subsets(nums[1:])
        return ss + [[nums[0]] + s for s in ss]
