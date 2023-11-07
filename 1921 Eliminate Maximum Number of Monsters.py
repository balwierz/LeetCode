def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
    for i, x in enumerate(sorted(b/v for b, v in zip(dist, speed))):
        if i >= x:
            return i
    return i+1
