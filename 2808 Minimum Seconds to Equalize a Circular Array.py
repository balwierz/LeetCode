class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        last_gap = defaultdict(lambda: (0,0))
        for i in range(len(nums)*2):
            num = nums[i%len(nums)]
            last_gap[num] = (i, max(last_gap[num][1], i-last_gap[num][0]))
        return min(g for l, g in last_gap.values()) // 2
