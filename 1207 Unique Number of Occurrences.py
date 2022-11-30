class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return set(Counter(Counter(arr).values()).values()) == set([1])
