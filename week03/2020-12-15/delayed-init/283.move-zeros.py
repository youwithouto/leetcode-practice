class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndex = 0
        for i in range(len(nums)):
            current = nums[i]
            if current != 0:
                nums[zeroIndex] = nums[i]
                if i != zeroIndex:
                    nums[i] = 0
                zeroIndex += 1
