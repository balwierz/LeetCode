class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        thr = max(candies) - extraCandies
        return [x>=thr for x in candies]
