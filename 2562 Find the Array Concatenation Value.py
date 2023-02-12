class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        for a, b in zip(nums[:n//2], nums[:n//2-1:-1]):
            ret += int(str(a) + str(b))
        if n % 2:
            ret += nums[n//2]
        return ret
