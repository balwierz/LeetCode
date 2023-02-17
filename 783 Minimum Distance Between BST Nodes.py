class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ret = 1000000
        def minmax(node):
            nonlocal ret
            if not node: return [None, None]
            lMin, lMax = minmax(node.left)
            rMin, rMax = minmax(node.right)
            if lMax:
                ret = min(ret, node.val - lMax)
            if rMin:
                ret = min(ret, rMin - node.val)
            rMax = rMax if rMax else node.val
            lMin = lMin if lMin else node.val
            return [lMin, rMax]
        minmax(root)
        return ret
