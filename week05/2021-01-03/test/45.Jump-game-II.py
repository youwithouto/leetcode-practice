class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        reach, largest_reach = nums[0], nums[0]
        times = 1

        for i in range(1, n):
            if i > reach:
                times += 1
                reach = largest_reach
            largest_reach = max(largest_reach, i + nums[i])
        return times
