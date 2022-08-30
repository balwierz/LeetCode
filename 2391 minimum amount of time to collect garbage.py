class Solution:
    def garbageCollection(self, rubbish: List[str], travel: List[int]) -> int:
        n = len(rubbish)
        last = [0] * 128
        last[ord("G")] = last[ord("P")] = last[ord("M")] = 0
        collectTime = 0
        for i in range(n):
            c = Counter(rubbish[i])
            for k, v in c.items():
                collectTime += v
                last[ord(k)] = i
        travelTime = sum(travel[:last[ord("G")]]) + \
                     sum(travel[:last[ord("P")]]) + \
                     sum(travel[:last[ord("M")]])
        return travelTime + collectTime
