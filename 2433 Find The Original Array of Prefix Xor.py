class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        last = 0
        ret = []
        for x in pref:
            ret.append(last ^ x)
            last = x
        return ret
