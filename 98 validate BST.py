# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(this, root):
        if root.left:
            lmin, lmax, lvalid = this.dfs(root.left)
            if not lvalid or lmax >= root.val:
                return (0,0,False)
        else:
            lmin = root.val
        if root.right:
            rmin, rmax, rvalid = this.dfs(root.right)
            if not rvalid or rmin <= root.val:
                return (0,0,False)
        else:
            rmax = root.val
        return (lmin, rmax, True)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[2];
       
