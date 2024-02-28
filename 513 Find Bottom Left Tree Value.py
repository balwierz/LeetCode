def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    def helper(node):
        # returns (depth, leftmostbottomvalue)
        if not node:
            return [0, None]
        if not node.left and not node.right:
            return [1, node.val]
        dl, vl = helper(node.left)
        dr, vr = helper(node.right)
        if dr > dl:
            return [dr+1, vr]
        return [dl+1, vl]
    return helper(root)[1]
