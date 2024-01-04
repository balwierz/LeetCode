def minOperations(self, nums: List[int]) -> int:
    return -1 if 1 in (c:=Counter(nums).values()) else sum((x+2) // 3 for x in c)
