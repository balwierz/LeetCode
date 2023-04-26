class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 51
        n = 0
        for i in range(k):
            if nums[i] < 0:
                n += 1
                cnt[-nums[i]] += 1
        if n < x:
            ret = [0]
        else:
            j = x
            for i in range(50,0,-1):
                j -= cnt[i]
                if j <= 0:
                    ret = [-i]
                    break
        for i in range(k, len(nums)):
            if nums[i-k] < 0:
                cnt[-nums[i-k]] -= 1
                n -= 1
            if nums[i] < 0:
                cnt[-nums[i]] += 1
                n += 1
            if n < x:
                ret.append(0)
            else:
                j = x
                for i in range(50,0,-1):
                    j -= cnt[i]
                    if j <= 0:
                        ret.append(-i)
                        break
        return ret
