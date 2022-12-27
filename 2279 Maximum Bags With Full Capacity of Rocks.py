import numpy as np
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        cap = sorted([c-r for c, r in zip(capacity, rocks)])
        i = 0
        while i<len(cap) and additionalRocks >= cap[i]:
            additionalRocks -= cap[i]
            i += 1
        return i
