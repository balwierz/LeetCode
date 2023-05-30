class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum2count = defaultdict(int)
        sum2count[0] = 1
        runSum = 0
        ret = 0
        for a in nums:
            runSum += a
            ret += sum2count[runSum - k]
            sum2count[runSum] += 1
        return ret
