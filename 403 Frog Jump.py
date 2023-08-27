class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1: return False
        seen = {(1, 1)}
        target = stones[-1]
        pos = set(stones)
        def jump(start, velocity):
            if start == target:
                return True
            z = start+velocity
            if velocity == 1:
                newState = ((z+1, 2), (z, 1))
            else:
                newState = ((z+1, velocity+1), (z, velocity), (z-1, velocity-1))
            for ns in newState:
                if ns[0] in pos and ns not in seen:
                    seen.add(ns)
                    if jump(*ns):
                        return True
            return False
        return jump(1, 1)
