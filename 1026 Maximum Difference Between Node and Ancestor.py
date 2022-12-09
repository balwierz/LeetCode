class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def helper(node, a, b):
            nonlocal ret
            if node == None:
                return
            ret = max(abs(a - node.val), abs(b - node.val), ret)
            helper(node.left, min(a, node.val), max(b, node.val))
            helper(node.right, min(a, node.val), max(b, node.val))
        helper(root, root.val, root.val)
        return ret
