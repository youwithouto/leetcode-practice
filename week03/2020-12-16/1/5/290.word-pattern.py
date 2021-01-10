class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        char2Word = {}
        word2Char = {}
        for c, w in zip(pattern, words):
            if c not in char2Word and w not in word2Char:
                char2Word[c] = w
                word2Char[w] = c
            elif (c not in char2Word and w in word2Char):
                return False
            elif (c in char2Word and char2Word[c] != w):
                return False
        return True
