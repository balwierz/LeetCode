class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join(map(lambda w: w[0], words))
