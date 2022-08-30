class Solution:
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        if len(c) == 1 and c['0'] > 0:
            return "0"
        mid = 0
        ret = ""
        for i in range(ord('9'), ord('0')-1, -1):
            n = c[chr(i)] // 2
            if mid == 0 and c[chr(i)] & 1:
                mid = i
            if ret or chr(i) != '0':
                ret += chr(i) * n
        return ret + ['', chr(mid)][mid != 0] + ''.join(reversed(ret))
