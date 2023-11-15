class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        lastElem = 1
        for x in arr[1:]:
            if x > lastElem:
                lastElem += 1
        return lastElem
