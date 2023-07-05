class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        best = 0
        curLen = 0
        for num in nums:
            if num > threshold:
                curLen = 0
            elif curLen != 0 and num % 2 != lastMod:
                curLen += 1
            elif num % 2 == 0 : 
                # start the array
                curLen = 1
                lastMod = 0
            else:
                curLen = 0
            best = max(best, curLen)
            lastMod = num % 2
        return best
