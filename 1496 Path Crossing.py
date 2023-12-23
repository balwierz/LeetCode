import cmath

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {"N": 1j, "S": -1j, "E": 1, "W": -1}
        pos = complex(0, 0)
        seen = set([pos])
        for x in path:
            pos += direction[x]
            if pos in seen:
                return True
            seen.add(pos)
        return False
