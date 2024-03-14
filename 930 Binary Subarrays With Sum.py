class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ret = 0
        if goal == 0:
            for a, b in groupby(nums):
                if a == 0:
                    nz = len(list(b))
                    ret += (nz+1) * nz // 2
            return ret
        windowSum = 0
        l, r = 0, 0
        while r<n and windowSum < goal:
            windowSum += nums[r]
            r += 1
        if windowSum < goal:
            return 0
        while r<n+1:
            num0l, num0r = 1, 1
            while r<n and nums[r] == 0:
                num0r += 1
                r += 1
            while l<r and nums[l] == 0:
                num0l += 1
                l += 1
            ret += num0l * num0r
            l += 1
            r += 1
        return ret
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSum = 0
        cnt  = 0
        mpp = defaultdict(int)
        mpp[0] = 1
        for i in range(len(nums)):
            preSum += nums[i]
            remove = preSum - goal
            if remove in mpp:
                cnt += mpp[remove]
            mpp[preSum] += 1
        return cnt       
