class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all(row[i] == row[(i+k)%len(row)] for row in mat for i in range(len(row)))
