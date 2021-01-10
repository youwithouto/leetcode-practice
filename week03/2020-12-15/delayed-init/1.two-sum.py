class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2Id = {}
        for i in range(len(nums)):
            currentNum = nums[i]
            theOtherNum = target - currentNum
            if theOtherNum in num2Id:
                return [i, num2Id[theOtherNum]]
            else:
                num2Id[currentNum] = i
