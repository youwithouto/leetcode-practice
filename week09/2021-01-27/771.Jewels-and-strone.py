class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewel_set = set()
        for c in jewels:
            jewel_set.add(c)
        for c in stones:
            if c in jewel_set:
                result += 1
        return result
