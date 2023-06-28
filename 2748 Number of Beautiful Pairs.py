class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        @cache
        def gcd2(a, b):
            return gcd(a,b)
        first = [int(str(x)[0]) for x in nums]
        last  = [int(str(x)[-1]) for x in nums]
        ret = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd2(first[i], last[j]) == 1:
                    ret += 1
        return ret
