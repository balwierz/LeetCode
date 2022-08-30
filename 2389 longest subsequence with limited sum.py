import numpy as np
import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = np.array(sorted(nums))
        cs = np.cumsum(nums)
        ret = []
        for q in queries:
            ret.append(bisect.bisect_right(cs, q))
        return ret
