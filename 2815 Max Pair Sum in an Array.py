class Solution:
    def maxSum(self, nums: List[int]) -> int:
        data = [[0, 0] for _ in range(10)]
        cnt = [0] * 10
        for num in nums:
            m = max([int(x) for x in str(num)])
            if num > min(data[m]):
                data[m] = (num, max(data[m]))
                cnt[m] += 1
        return max(sum(pair) * (c >= 2) for pair, c in zip(data, cnt)) if max(cnt) >= 2 else -1
