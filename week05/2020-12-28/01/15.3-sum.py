class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low, high = i + 1, len(nums) - 1
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append((nums[i], nums[low], nums[high]))
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
        return result
