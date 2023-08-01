class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [[i for i in range(1, n+1)]]
        return [elem + [j] for j in range(k, n+1) for elem in self.combine(j-1, k-1)]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [elem + [j] for j in range(k, n+1) for elem in self.combine(j-1, k-1)]
