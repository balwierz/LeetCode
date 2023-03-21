def maximizeGreatness(self, nums: List[int]) -> int:
    nums.sort()
    l = 0
    r = 0
    n = len(nums)
    ret = 0
    while True:
        while r < n and nums[r] <= nums[l]:
            r += 1
        if r < n:
            ret += 1
            r += 1
        else:
            break
        l += 1
    return ret
