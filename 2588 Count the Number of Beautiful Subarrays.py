class Solution:
    def beautifulSubarrays4(self, nums: List[int]) -> int:
        c = Counter(accumulate(nums, xor, initial = 0))
        return sum (n*(n-1) for n in c.values()) // 2

    def beautifulSubarrays(self, nums: List[int]) -> int:
        state = defaultdict(int)
        xorant = 0
        ret = 0
        for num in nums:
            state[xorant] += 1
            xorant ^= num
            ret += state[xorant]
        return ret
