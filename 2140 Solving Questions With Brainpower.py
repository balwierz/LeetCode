class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        best = [0] * len(questions)
        for i, [points, skip] in enumerate(questions):
            # either skip it:
            if i+1 < len(questions):
                best[i+1] = max(best[i], best[i+1])
            # or do it:
            best[i] += points
            if i+1+skip < len(questions):
                best[i+1+skip] = max(best[i+1+skip], best[i])
        return max(best)
