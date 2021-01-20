class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            tmp = result[i & (i - 1)] + 1
            result.append(tmp)
        return result
