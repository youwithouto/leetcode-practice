class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if len(nums) < k:
            return result
        deq = deque()

        for i in range(k):
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            if deq[0] < i - k + 1:
                deq.popleft()

            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        result.append(nums[deq[0]])

        return result
