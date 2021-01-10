from typing import Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        l = self.permute(nums[1:])

        for i in l:
            for j in range(len(i) + 1):
                k = i[:]
                k.insert(j, nums[0])
                result.append(k)

        return result
