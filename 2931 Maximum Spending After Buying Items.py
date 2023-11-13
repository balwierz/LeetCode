class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        return sum(x * (i+1) for i, x in enumerate(sorted(chain(*values))))
