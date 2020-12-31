class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        stack = []
        result = 0
        for i, v in enumerate(height):
            while stack and height[stack[-1]] < v:
                bottom = height[stack.pop()]
                if not stack:
                    break
                leftIndex = stack[-1]
                h = min(height[leftIndex], v) - bottom
                w = i - leftIndex - 1
                result += h * w
            stack.append(i)
        return result
