class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key = lambda x: -x[0])
        cat2count = defaultdict(lambda: 0)
        nCat = 0
        i = 0
        sumProfit = 0
        while k:
            k -= 1
            prof, cat = items[i]
            if cat not in cat2count:
                nCat += 1
            cat2count[cat] += 1
            sumProfit += prof
            i += 1
        ret = sumProfit + nCat**2
        j = i
        while j<len(items):
            prof, cat = items[j]
            if cat2count[cat] == 0:
                sumProfit += prof
                nCat += 1
                cat2count[cat] = 1
                while i>0:
                    i -= 1
                    if cat2count[items[i][1]] >= 2:
                        sumProfit -= items[i][0]
                        cat2count[items[i][1]] -= 1
                        break
                if i == 0:
                    return ret
            j += 1
            ret = max(ret, sumProfit + nCat**2)
        return ret
