class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counts = [sum(x == 1 for x in row ) for row in mat]
        idx = counts.index(max(counts))
        return (idx, counts[idx])
