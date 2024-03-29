class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        data = [x == m for x in nums]
        l = 0
        s = 0  # sum of good
        ret = 0
        for x in data:
            s += x
            if s > k:
                l += 1
                s -= 1
            if s == k:
                while data[l] == 0:
                    l += 1
                ret += l + 1
        return ret
