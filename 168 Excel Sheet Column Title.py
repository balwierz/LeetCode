class Solution:
    def convertToTitle(self, num: int) -> str:
        ret = ""
        base = ord('A')
        while num:
            num -= 1 #wtf numbering from one
            ret += chr(num%26 + base)
            num //= 26
        return ret[::-1]
