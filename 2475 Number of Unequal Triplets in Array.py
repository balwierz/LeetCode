class Solution:
    def unequalTriplets2(self, nums: List[int]) -> int:
        c = list(Counter(nums).values())
        ret = 0
        for i in range(0, len(c)):
            for j in range(i+1, len(c)):
                for k in range(j+1, len(c)):
                    ret += c[i] * c[j] * c[k]
        return ret
    
    def unequalTriplets(self, nums: List[int]) -> int:
        s = list(accumulate(Counter(nums).values()))
        return sum(s[i - 1] * (s[i] - s[i - 1]) * (s[-1] - s[i]) for i in range(1, len(s)-1))
