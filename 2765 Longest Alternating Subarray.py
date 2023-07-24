class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        maxLen = -1
        lastNum = nums[0]
        lastLen = 0
        for num in nums[1:]:
            if lastLen == 0:
                if num == lastNum + 1:
                    lastLen = 2
                    maxLen = max(maxLen, 2)
            else:
                if num == lastNum + (1 if lastLen % 2 == 1 else -1):
                    lastLen += 1
                    maxLen = max(maxLen, lastLen)
                else:
                    if num == lastNum + 1:
                        lastLen = 2
                    else:
                        lastLen = 0
            lastNum = num
        return maxLen
