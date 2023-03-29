import numpy as np
class Solution:
    def maxSatisfaction2(self, s: List[int]) -> int:
        s.sort(reverse=True)
        total = 0
        cur_sum = 0
        for val in s:
            cur_sum += val
            if (cur_sum < 0):
                break
            total += cur_sum
        return total
    
    def maxSatisfaction2(self, s: List[int]) -> int:
        s.sort(reverse=True)
        s = np.array(s)
        ret = 0
        for i in range(1, len(s)+1):
            ret = max(ret, np.inner(s[:i], np.arange(i, 0, -1)))
        return ret
    
