class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        for i in range(0, len(s), k):
            ret.append(s[i : i+k])
        if len(s) % k:
            ret[-1] += fill * (k - len(s) % k)
        return ret
