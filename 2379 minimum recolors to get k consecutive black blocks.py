class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        c = Counter(blocks[:k])
        ret = c['W']
        t = ret
        for i, j in zip(range(n-k), range(k, n)):
            if blocks[i] == 'W':
                t -= 1
            if blocks[j] == 'W':
                t += 1
            ret = min(ret, t)
        return ret
