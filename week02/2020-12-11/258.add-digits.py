class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        while result >= 10:
            result = self.add(result)
        return result

    def add(self, num: int) -> int:
        oldNum, newNum = num, 0
        while oldNum > 0:
            newNum += oldNum % 10
            oldNum = oldNum // 10
        return newNum
