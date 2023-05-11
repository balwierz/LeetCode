class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        best = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)] # our DP: 
        for i, x in enumerate(nums1):
            ii = i+1
            for j, y in enumerate(nums2):                
                jj = j+1
                best[ii][jj] = max(best[ii-1][jj], best[ii][jj-1], (1 if x==y else 0) + best[ii-1][jj-1])
        return best[len(nums1)][len(nums2)]
