def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
    def gcd(a, b):
        while a != 0:
            a, b = b%a, a
        return b
            
    g = gcd(k, len(arr))
    sets = (arr[i::g] for i in range(g))
    ret = 0
    for s in sets:
        mid = int(statistics.median(s))
        ret += sum([abs(a-mid) for a in s])
    return ret
