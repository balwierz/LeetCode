class Solution:
    def sumSubarrayMins2(self, arr: List[int], i = 0, j = -1) -> int:
        if j == -1:
            j = len(arr)
        if j == i:
            return 0
        if j == i + 1:
            return arr[i]
        m, mI = 999999, i
        for k in range(i, j):
            if arr[k] < m:
                m = arr[k]
                mI = k
        return ((mI-i+1) * (j-mI) * arr[mI] + self.sumSubarrayMins(arr, i, mI) + self.sumSubarrayMins(arr, mI+1, j)) % 1000000007

    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [(-1, 0, 0)]   # growing stack: (index, value, sumSubarrayMins)
        ret = 0
        for i in range(len(arr)):
            # pop larger values from the stack
            while stack[-1][1] >= arr[i]:
                stack.pop()
            u = (i - stack[-1][0]) * arr[i] + stack[-1][2]
            ret += u
            ret %= 1000000007
            stack.append((i, arr[i], u))
        return ret
