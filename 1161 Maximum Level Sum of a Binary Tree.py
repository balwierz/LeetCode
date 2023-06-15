# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = [0] * 10000
        maxLvl = 0
        def dfs(node, level):
            if not node:
                return
            sums[level] += node.val
            nonlocal maxLvl
            maxLvl = max(maxLvl, level)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        ret = float('-inf')
        reti = 0
        for i in range(maxLvl+1):
            if sums[i] > ret:
                ret = sums[i]
                reti = i
        return reti+1
        
