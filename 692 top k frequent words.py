class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        upTo = cnt.most_common(k)[-1][1]
        easyPart = [e    for e in cnt.items() if e[1]  > upTo]
        hardPart = [e[0] for e in cnt.items() if e[1] == upTo]
        easyPart = [e[0] for e in sorted(sorted(easyPart, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)]
        hardPart = sorted(hardPart)[0:(k-len(easyPart))]
        return easyPart + hardPart
