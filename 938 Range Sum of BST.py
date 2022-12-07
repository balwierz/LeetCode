    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ret = 0
        if low < root.val:
            ret += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            ret += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            ret += root.val
        return ret;
