# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def go(node):  # returns (sum, numNodes)
            if not node: return (0, 0)
            sL, nL = go(node.left)
            sR, nR = go(node.right)
            s = sL + sR + node.val
            n = nL + 1 + nR
            if s//n == node.val:
                nonlocal ret
                ret += 1
            return (s, n)
        
        go(root)
        return ret


        
