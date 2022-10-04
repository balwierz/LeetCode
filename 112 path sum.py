class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if targetSum == root.val and root.left is None and root.right is None:
            return True
        if root.left:
            if self.hasPathSum(root.left, targetSum-root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, targetSum-root.val):
                return True
        return False
