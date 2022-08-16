class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return (k[0] for k in Counter(nums).most_common(k))
