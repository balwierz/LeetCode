class Solution:

    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        @cache 
        def helper(i, t):
            if i<0 or t<0:  #impossible
                return None
            if t == 0:
                return [[]]
            ret = []
            if (a := helper(i-1, t) is not None:
                ret.extend(a)
            if (b := helper(i, t-can[i])) is not None:
                for x in b:
                    bb = x.copy()
                    bb.append(can[i])
                    ret.append(bb)
            if len(ret): return ret
            else: return None
        return helper(len(can)-1, target)
