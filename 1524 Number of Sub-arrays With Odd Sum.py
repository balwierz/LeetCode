class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ret = 0
        nOdd = 0
        nEven = 0
        for num in arr:
            if num & 1:  # num is odd, changing parity
                nOdd, nEven = nEven, nOdd
                nOdd += 1
            else:
                nEven += 1
            ret += nOdd
        return ret % 1_000_000_007
