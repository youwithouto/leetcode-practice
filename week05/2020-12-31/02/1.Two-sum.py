class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value2Index = {}
        for i in range(len(nums)):
            current = nums[i]
            other = target - current
            if other in value2Index:
                return [value2Index[other], i]
            else:
                value2Index[current] = i
