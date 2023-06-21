class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        data = defaultdict(int)
        for n, c in zip(nums, cost):
            data[n] += c
        k = sorted(data.items())
        @cache
        def y(num):
            ret = 0
            for n, c in k:
                ret += abs(num-n) * c
            return ret
        l, r = -1, len(k)-1
        while l+1 < r:
            mid = (l+r) // 2
            if y(k[mid+1][0]) - y(k[mid][0]) < 0:
                l = mid
            else:
                r = mid
        return y(k[r][0])
