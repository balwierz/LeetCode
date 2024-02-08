def returnToBoundaryCount(self, nums: List[int]) -> int:
    return sum(x==0 for x in accumulate(nums))
