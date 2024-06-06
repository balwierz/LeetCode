class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def processChain(krotnosci):
            if len(krotnosci) == 0:
                return 1
            dp = [1] * (len(krotnosci) + 2)
            for i, kr in enumerate(krotnosci):
                dp[i] = (2**kr-1) * dp[i-2] + dp[i-1]
            print(krotnosci, dp)
            return dp[-3]
        
        bins = defaultdict(Counter)
        for num in nums:
            bins[num%k][num] += 1
        
        numBad = 1
        for b in bins.values():
            data = list(sorted(b.keys()))
            krotnosci = [b[data[0]]]
            prevKey = data[0]
            for key in data[1:]:
                if key == prevKey + k:
                    krotnosci.append(b[key])
                else:
                    numBad *= processChain(krotnosci)
                    krotnosci = [b[key]]
                prevKey = key
            numBad *= processChain(krotnosci)

        return numBad - 1


