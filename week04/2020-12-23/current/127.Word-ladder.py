class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, length + 1))
        return 0
