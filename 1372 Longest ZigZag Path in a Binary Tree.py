def longestZigZag(self, root: Optional[TreeNode], depth = 0, direction = -1) -> int:
    return max(self.longestZigZag(root.left, depth+1 if direction != 0 else 1, 0) if root.left else 0, self.longestZigZag(root.right, depth+1 if direction != 1 else 1, 1) if root.right else 0, depth)
