class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        m = set(nums)
        for f, t in zip(moveFrom, moveTo):
            m.remove(f)
            m.add(t)
        return sorted(list(m))
