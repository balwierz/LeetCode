class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mem = defaultdict(lambda: defaultdict(int))  # target index, words[i] index; number of ways
        tLen = len(target)
        wLen = len(words[0])
        countM = [[0] * 26 for _ in range(wLen)]
        for w in words:
            for i, c in enumerate(w):
                countM[i][ord(c)-ord('a')] += 1
        
        def helper(targI, wordI):
            if targI == tLen:
                return 1
            if tLen - targI > wLen - wordI:
                return 0
            nonlocal mem
            if targI in mem and wordI in mem[targI]:
                return mem[targI][wordI]
            nonlocal countM
            nonlocal target
            ret = helper(targI, wordI+1)
            if countM[wordI][ord(target[targI])-ord('a')]:
                ret += countM[wordI][ord(target[targI])-ord('a')] * helper(targI+1, wordI+1)
            ret %= 1000000007
            mem[targI][wordI] = ret
            return ret
        
        return helper(0, 0)

class Solution2:
    def numWays(self, words: List[str], target: str) -> int:
        counters = [Counter(x) for x in zip(*words)]
        
        @cache
        def dp(i, t):
            if t == len(target):
                return 1
            elif len(counters) - i < len(target) - t:
                return 0
            res = dp(i + 1, t)
            x = counters[i][target[t]]
            if x > 0:
                res += x * dp(i + 1, t + 1)
            return res % 1_000_000_007
        return dp(0, 0)
