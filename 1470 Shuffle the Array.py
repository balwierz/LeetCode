class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [c for a, b in zip(nums[:n], nums[n:]) for c in (a,b)]
