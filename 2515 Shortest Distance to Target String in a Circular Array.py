class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        words = [word == target for word in words]
        indDist = [min([abs(i - j*len(words) - startIndex) for j in [-1,0,1]]) for i, val in enumerate(words) if val]
        return min(indDist) if len(indDist) else -1
