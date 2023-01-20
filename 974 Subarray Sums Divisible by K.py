class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        tab = [0] * k
        shift = 0
        ret = 0
        for w in nums:
            tab[shift%k] += 1
            shift -= w
            ret += tab[shift%k]
        return ret
