class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        n = len(nums)
        if s == x:
            return n
        if s < x:
            return -1
        left = dict(zip(accumulate(nums), range(1, n+1)))
        left[0] = 0
        ret = inf
        if x in left:
            ret = left[x]
        cumsum = 0

        for i, num in enumerate(nums[::-1]):
            cumsum += num
            if cumsum > x:
                break
            if x - cumsum in left:

                ret = min(ret, i +1 + left[x-cumsum])
        return -1 if ret == inf else ret
