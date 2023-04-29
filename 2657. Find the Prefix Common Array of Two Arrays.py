class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = [0] * (len(A) + 1)
        ret = []
        cnt = 0
        for a, b in zip(A, B):
            seen[a] += 1
            if seen[a] == 2:
                cnt += 1
            seen[b] += 1
            if seen[b] == 2:
                cnt += 1
            ret.append(cnt)
        return ret
