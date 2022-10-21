class Solution:
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        seen = Counter()
        for i, v in enumerate(nums):
            if seen[v]:
                return True
            if i >= k:
                seen[nums[i-k]] -= 1
            seen[v] += 1
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False
