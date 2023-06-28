class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        used = [False] * len(words)
        data = defaultdict(list)
        for i, w in enumerate(words):
            data[w[::-1]].append(i)
        ret = 0
        for i, w in enumerate(words):
            if used[i]:
                next
            for j in data[w]:
                if not used[j] and j != i:
                    used[i] = True
                    used[j] = True
                    ret += 1
                    break
        return ret
