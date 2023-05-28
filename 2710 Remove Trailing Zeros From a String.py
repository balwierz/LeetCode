class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ret = ""
        flag = True
        for char in num[::-1]:
            if flag and char == '0':
                pass
            else:
                flag = False
                ret += char
        return ret[::-1]
