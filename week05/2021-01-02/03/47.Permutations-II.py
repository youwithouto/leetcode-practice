class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 0:
            return result
        nums.sort()
        self.findUnique(nums, [False for i in range(len(nums))], [], result)

        return result

    def findUnique(self, nums: List[int], visited: List[bool], trace: List[int], result: List[List[int]]):
        if len(trace) == len(nums):
            result.append(trace[:])
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1]:
                break
            trace.append(nums[i])
            visited[i] = True
            self.findUnique(nums, visited, trace, result)
            trace.pop()
            visited[i] = False
