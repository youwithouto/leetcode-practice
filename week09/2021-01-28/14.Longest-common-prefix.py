class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if strs is None or len(strs) == 0:
            return result
        gold = strs[0]
        for i in range(len(gold)):
            c = gold[i]
            for w in strs:
                if i >= len(w) or c != w[i]:
                    return result
            result += c
        return result
