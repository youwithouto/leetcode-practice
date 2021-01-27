class Solution:
    def myAtoi(self, s: str) -> int:
        MAX, MIN = pow(2, 31) - 1, 0 - pow(2, 31)
        result = 0
        tmp = ""
        s = s.strip()
        if len(s) == 0:
            return result
        isNegative = s[0] == "-"
        if isNegative or s[0] == "+":
            s = s[1:]

        if len(s) == 0 or not s[0].isdigit():
            return result

        for c in s:
            if c.isdigit():
                tmp += c
            else:
                break
        result = int(tmp)
        if isNegative:
            result = 0 - MIN if 0 - result < MIN else result
        else:
            result = MAX if result > MAX else result
        return 0 - result if isNegative else result
