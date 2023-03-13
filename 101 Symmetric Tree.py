class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def helper(a, b):
            if bool(a) != bool(b): return False
            if a:
                if a.val != b.val: return False
                if not helper(a.left, b.right): return False
                if not helper(a.right, b.left): return False
            return True
        return helper(root.left, root.right)
