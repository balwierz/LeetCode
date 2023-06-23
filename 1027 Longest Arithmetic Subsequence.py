class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        pred = defaultdict(set)
        ret = 2
        for i, x in enumerate(nums):
            p = pred[x]
            pred[x] = set()
            for step, length in p:
                pred[x+step].add((step, length+1))
                ret = max(ret, length+1)
            for j in range(i):
                step = x-nums[j]
                pred[x+step].add((step, 2))
        return ret
