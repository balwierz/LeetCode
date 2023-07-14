class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num-difference] + 1
        return max(dp.values())
    def longestSubsequence2(self, arr: List[int], difference: int) -> int:
        ret = 1
        mn = min(arr)
        mx = max(arr)
        state = [0] * (mx-mn+1)
        for x in arr:
            x -= mn
            y = state[x] + 1
            if 0 <= x + difference <= mx - mn:
                state[x+difference] = y
            ret = max(ret, y)
        return ret
            
            
