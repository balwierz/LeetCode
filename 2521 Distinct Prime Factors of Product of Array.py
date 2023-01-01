class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def erato(n=1000):
            ret = [[] for _ in range(n)]
            i = 2
            while i < n:
                if len(ret[i]) == 0:
                    mul = i
                    while mul < n:
                        ret[mul].append(i)
                        mul += i
                i += 1
            return ret
        factors = erato(max(nums)+1)
        ret = set()
        for num in nums:
            ret = ret.union(factors[num])
        return len(ret)
