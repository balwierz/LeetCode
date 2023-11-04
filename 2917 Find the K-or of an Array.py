class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(32):
            A = 1 << i
            count = 0
            for num in nums:
                #count += int(bool(num & A))
                if num & A:
                    count += 1
            if count >= k:
                ret |= A
        return ret
