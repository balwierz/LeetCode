class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = root.val
        def bestToLeaf(node) -> int:
            nonlocal ret
            if not node:
                return 0
            l = bestToLeaf(node.left)
            r = bestToLeaf(node.right)
            ret = max(ret, node.val, node.val + l, node.val + r, node.val + l + r)
            return max(0, node.val, node.val + l, node.val + r)
        bestToLeaf(root)
        return ret
