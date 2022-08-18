class Solution:
    def minSetSize2(self, arr: List[int]) -> int:
        nRemove = len(arr)/2
        c = Counter(arr).items()
        c = sorted(c, key=lambda x:x[1])
        m = 0
        ret = 0
        while(m<nRemove):
            ret += 1
            m += c.pop()[1]
        return ret
    
    def minSetSize(self, arr: List[int]) -> int:
        nRemove = len(arr)/2
        c = Counter(arr).values()
        h = [-v for v in c]
        heapify(h)
        ret = 0
        m = 0
        while(m<nRemove):
            ret += 1
            m -= heappop(h)
        return ret
