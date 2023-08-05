class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ret = ''.join([min(x,y) for x, y in zip(s[:len(s)//2], reversed(s[-len(s)//2:]))])
        return ret + (s[len(s)//2] if len(s)%2 else "") + ret[::-1]
