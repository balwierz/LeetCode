def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    def allDiffs(L, fences):
        fences.extend((1,L))
        return set(abs(fences[j] - fences[i]) for i in range(len(fences)) for j in range(i+1, len(fences))) 
    side = max(allDiffs(m, hFences).intersection(allDiffs(n, vFences)), default=-1)
    return (side**2 % 1_000_000_007) if side > 0 else -1
