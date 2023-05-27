class Solution:
    def stoneGameIII(self, vals: List[int]) -> str:
        n = len(vals)
        bob = total = sum(vals)
        tail = []
        for i in range(n):
            tail.append(total)
            total -= vals[i]
        tail.append(0)
        tail.append(0)
        tail.append(0)
        @cache
        def strategy(i):
            ret = -9999999999
            if i >= n:
                return 0
            for a in range(i+1, i+4):
                ret = max(ret, tail[i] - strategy(a))
            return ret
        alice = strategy(0)
        bob -= alice
        if alice > bob:
            return "Alice"
        elif bob > alice:
            return "Bob"
        return "Tie"
