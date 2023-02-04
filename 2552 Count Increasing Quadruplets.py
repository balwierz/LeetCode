import numpy as np

class Solution:
    def countQuadruplets(self, A: List[int]) -> int:
        n = len(A)
        dp = [0]*n  # Number of good i->k->j ending at j.
        res = 0
        for j, v in enumerate(A):
            cnt = 0   # cnt_j counts A[i] < A[j] seen so far
            for i in range(j):
                if A[i] > v:
                    dp[i] += cnt  # (we found cnt of {i},j,k = (optimised),i,k)
                else:
                    res += dp[i]  # our i,j = desc j,l ; 
                    cnt += 1      # our i,j = desc i,k
        return res
                    

class Solution2:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        pre  = [[0] * n for _ in range(n)]   #np.zeros((n,n), dtype=int)
        post = [[0] * n for _ in range(n)]   #np.zeros((n,n), dtype=int)
        for k in range(2, n-1):
            cum = int(nums[0] < nums[k])
            for j in range(1, k):
                if nums[j] > nums[k]:
                    pre[k][j] = cum
                cum += int(nums[j] < nums[k])
        for j in range(n-3, 0, -1):
            cum = int(nums[n-1] > nums[j])
            for k in range(n-2, j, -1):
                if nums[j] > nums[k]:
                    post[k][j] = cum
                cum += int(nums[k] > nums[j])
        #print(pre)
        #print(post)
        ret = 0
        for k in range(2, n-1):
            for j in range(n-3, 0, -1):
                ret += pre[k][j] * post[k][j]
        return ret
