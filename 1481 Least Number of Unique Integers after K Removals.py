def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    c = sorted(Counter(arr).values())
    for i, count in enumerate(c):
        k -= count
        if k <= 0:
            return len(c) -i -int(k==0)
