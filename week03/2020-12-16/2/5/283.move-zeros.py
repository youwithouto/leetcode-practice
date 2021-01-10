class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        targetIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[targetIndex], nums[i] = nums[i], nums[targetIndex]
                targetIndex += 1
