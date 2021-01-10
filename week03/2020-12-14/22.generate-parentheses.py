class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.doGenerate(n, 0, "", result)
        return result

    def doGenerate(self, left: int, right: int, sequence: str, sequences: List[str]):
        if left == 0 and right == 0:
            sequences.append(sequence)
            return sequences
        if left > 0:
            self.doGenerate(left - 1, right + 1,
                            sequence + "(", sequences)
        if right > 0:
            self.doGenerate(left, right - 1, sequence + ")", sequences)
