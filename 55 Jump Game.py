class Solution:
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        leftMost = n-1
        for i in range(n-2, -1, -1):
            if leftMost <= arr[i]+i:
                leftMost = i
        return leftMost == 0
