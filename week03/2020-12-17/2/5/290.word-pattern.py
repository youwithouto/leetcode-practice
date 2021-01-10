class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char2Word = {}
        word2Char = {}
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        for c, w in zip(pattern, words):
            if c not in char2Word and w not in word2Char:
                char2Word[c] = w
                word2Char[w] = c
            elif c in char2Word and char2Word[c] != w:
                return False
            elif w in word2Char and word2Char[w] != c:
                return False
        other = ' '.join([char2Word[c] for c in pattern])
        print(other)
        return other == s


def main():
    solution = Solution()
    pattern = "abc"
    s = "dog cat dog"
    result = solution.wordPattern(pattern, s)
    print(result)


if __name__ == '__main__':
    main()
