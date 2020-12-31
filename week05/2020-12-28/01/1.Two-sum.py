class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement2Id = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current
            if complement in complement2Id:
                return [i, complement2Id[complement]]
            else:
                complement2Id[current] = i
