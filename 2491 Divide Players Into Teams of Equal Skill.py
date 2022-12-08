class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        c = Counter(skill)
        s = min(c.keys()) + max(c.keys())
        ret = 0
        for k, v in c.items():
            if v != c[s-k]:
                return -1
            if k + k == s:
                if v % 2 == 1:
                    return -1
                else:
                    ret += v//2 * k * k
            if k < s/2:
                ret += v * k * (s-k)
        return ret
