class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(n, 0, '', result)
        return result

    def helper(self, left: int, right: int, current: str, result: List[str]):
        if left == 0 and right == 0:
            result.append(current)
            return
        if left > 0:
            self.helper(left - 1, right + 1, current + "(", result)
        if right > 0:
            self.helper(left, right - 1, current + ")", result)
