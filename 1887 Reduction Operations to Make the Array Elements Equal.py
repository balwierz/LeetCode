class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        ret = 0
        numDep = 0
        for val in sorted(c.keys(), key = lambda k : -k):
            ret += numDep
            numDep += c[val]
        return ret
