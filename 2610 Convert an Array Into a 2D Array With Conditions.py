def findMatrix(self, nums: List[int]) -> List[List[int]]:
    c = Counter(nums)
    ret = []
    while(c):
        ret.append([k for k in c.keys()])
        c = {k: v-1 for k, v in c.items() if v > 1}
    return ret
