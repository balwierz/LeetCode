class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        subtreeSums = set()
        def helper(node):
            nonlocal total, subtreeSums
            if not node:
                return 0
            total += node.val
            ret = helper(node.left) + helper(node.right) + node.val
            subtreeSums.add(ret)
            return ret
        helper(root)
        best = total
        v = 0
        for val in subtreeSums:
            if abs(total / 2 - val) < best:
                best = abs(total / 2 - val)
                v = val
        return v * (total - v) % 1000000007
