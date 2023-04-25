class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 in nums:
            return n - sum(int(x==1) for x in nums)
        for ret in range(n-1):
            for i in range(n-1-ret):
                nums[i] = gcd(nums[i], nums[i+1])
                if nums[i] == 1:
                    return ret+n
        return -1
