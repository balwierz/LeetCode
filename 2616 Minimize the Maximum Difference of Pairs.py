# Problem https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

import numpy as np
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        #arr = np.array([b-a for a, b in pairwise(sorted(nums))])
        if p == 0:
            return 0
        arr = np.array(nums)
        arr.sort()
        diffs = np.diff(arr)
        n = len(nums)-1
        def isPossible(val):
            isGoodPair = diffs <= val
            i = np.append(np.where(np.diff(isGoodPair)), n-1)
            runLen = np.diff(np.append(-1, i))
            return np.sum((runLen[isGoodPair[i]]+1) // 2) >= p
            
        sortedDiffs = np.sort(diffs)
        l, r = -1, n-1 #np.max(diffs)
        while l+1 < r:
            m = (l+r) // 2
            if isPossible(sortedDiffs[m]):
                r = m
            else:
                l = m
        return sortedDiffs[r]
            


class Solution2:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        inf = 9999999999
        memo = [[-1] * (p+1) for _ in range(len(nums)+1)]
        #@lru_cache(maxsize=539999)
        def val(endI, pairN):
            if pairN == 0: return 0
            if endI < 2: return inf
            if endI < pairN * 2:
                return inf
            if memo[endI][pairN] != -1:
                return memo[endI][pairN]
            memo[endI][pairN] = min(val(endI-1, pairN), 
                       max(nums[endI-1]-nums[endI-2], val(endI-2, pairN-1)))
            return memo[endI][pairN]
        return val(len(nums), p)
