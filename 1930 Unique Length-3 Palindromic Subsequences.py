class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        masks = [0] * 26
        s = [ord(x)-ord('a') for x in s]
        s2 = [1 << x for x in s]
        left = accumulate(s2, operator.__or__, initial=0)
        right = list(accumulate(s2[::-1], operator.__or__, initial=0))[-2::-1]
        for l, x, r in zip(left, s, right):
            masks[x] |= l & r
        return sum(x.bit_count() for x in masks)
